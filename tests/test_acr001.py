"""ACR-001 deterministic/mocked tests; never claim mock verdicts prove live safety."""
import copy
import hashlib
import json
from pathlib import Path
import pytest
from test_consensus import harness, cloud, assess, MockDisagree, SNAPSHOT, URLS
from test_contract_readiness import configure_synthetic, SYNTHETIC

TRUE2 = '{"relevance_validations":[true,true],"relation_validations":[true]}'
TRUE4 = {"relevance_validations":[True]*4,"relation_validations":[True]*6}


def fixed_candidate(eim, h):
    configure_synthetic(h)
    return eim.candidate_from_model_output(list(h.urls), ["READABLE"]*4,
        [s["content_digest"] for s in SYNTHETIC["sources"]], json.dumps(SYNTHETIC["expected_model_output"]))


def test_positive_repeated_fixed_candidate_control_flow(eim,harness):
    h = harness
    proposed = fixed_candidate(eim,h)
    before = copy.deepcopy(proposed)
    h.model_output["Validator"] = json.dumps(TRUE4)
    h.participant = "Validator"
    _,validator = eim.consensus_callbacks((SYNTHETIC["claim"],SYNTHETIC["context"],h.urls))
    h.vm._in_nondet = True
    try:
        for _ in range(5):
            assert validator(eim.gl.vm.Return(proposed)) is True
    finally:
        h.vm._in_nondet = False
    assert len(h.http)==20 and len(h.models)==5 and h.writes==[]
    assert proposed==before
    assert all('"relations":["DEPENDENT","INDEPENDENT","UNKNOWN","INDEPENDENT","UNKNOWN","UNKNOWN"]' in prompt for _,prompt in h.models)


@pytest.mark.parametrize("key,index", [("relevance_validations",i) for i in range(4)]+[("relation_validations",i) for i in range(6)])
def test_every_single_field_false_disagrees_atomic(eim,harness,key,index):
    h = harness
    fixed_candidate(eim,h)
    verdict=copy.deepcopy(TRUE4)
    verdict[key][index]=False
    h.model_output["Validator"]=json.dumps(verdict)
    with pytest.raises(MockDisagree):
        h.contract.assess("negative",SYNTHETIC["claim"],SYNTHETIC["context"],list(h.urls))
    assert h.writes==[] and len(h.models)==2


@pytest.mark.parametrize("raw", [
    "not JSON", "```json\n"+TRUE2+"\n```", TRUE2+" trailing", "null", "[]",
    '{"relevance_validations":[true,true],"relation_validations":[true],"score":1}',
    '{"relevance_validations":[true,true],"relevance_validations":[true,true],"relation_validations":[true]}',
    '{"relevance_validations":[true,true]}',
    '{"relevance_validations":[true],"relation_validations":[true]}',
    '{"relevance_validations":[true,true],"relation_validations":[]}',
    '{"relevance_validations":[true,true],"relation_validations":[true,true]}',
    '{"relevance_validations":[1,true],"relation_validations":[true]}',
    '{"relevance_validations":["true",true],"relation_validations":[true]}',
    '{"relevance_validations":[null,true],"relation_validations":[true]}',
    '{"relevance_validations":[NaN,true],"relation_validations":[true]}',
    '{"relevance_validations":true,"relation_validations":[true]}',
])
def test_strict_validation_parser_rejects(eim,raw):
    with pytest.raises(eim.ProtocolError) as exc:
        eim.parse_validation_output(raw,2)
    assert exc.value.code=="INVALID_MODEL_OUTPUT"


@pytest.mark.parametrize("raw", ["", " ",None,RuntimeError("provider")])
def test_validator_model_failure_disagrees_no_write(eim,harness,raw):
    harness.model_output["Validator"]=raw
    with pytest.raises(MockDisagree):
        assess(harness)
    assert harness.writes==[]


def test_validator_does_not_call_classification_and_has_no_reasoning(eim,harness,monkeypatch):
    h=harness
    candidate=eim.candidate_from_model_output(list(URLS),["READABLE"]*2,
       [hashlib.sha256(b"Visible observation acquisition path").hexdigest()]*2,
       '{"relevance":["RELEVANT","RELEVANT"],"relations":["UNKNOWN"]}')
    def forbidden(*args):
        raise AssertionError("Validator must not regenerate a candidate")
    monkeypatch.setattr(eim,"classify_snapshot",forbidden)
    h.participant="Validator"; h.model_output["Validator"]=TRUE2; h.vm._in_nondet=True
    try:
        assert eim.consensus_callbacks(SNAPSHOT)[1](eim.gl.vm.Return(candidate)) is True
    finally:
        h.vm._in_nondet=False
    prompt=h.models[0][1]
    labels=json.loads(prompt.split("PROPOSED LABELS\n",1)[1].split("\n\nEND OF UNTRUSTED DATA",1)[0])
    assert labels=={"relevance":["RELEVANT","RELEVANT"],"relations":["UNKNOWN"]}
    assert "different first-choice label alone" in prompt
    assert "DEPENDENT is not transitive" in prompt
    assert h.writes==[]


@pytest.mark.parametrize("fault", ["digest","missing-pair","illegal-enum"])
def test_bad_evidence_or_schema_rejected_before_model(eim,harness,fault):
    c=eim.candidate_from_model_output(list(URLS),["READABLE"]*2,[hashlib.sha256(b"Visible observation acquisition path").hexdigest()]*2,
      '{"relevance":["RELEVANT","RELEVANT"],"relations":["UNKNOWN"]}')
    if fault=="digest": c["sources"][0]["content_digest"]="f"*64
    elif fault=="missing-pair": c["pairs"].clear()
    else: c["pairs"][0]["relation"]="FAKE"
    harness.participant="Validator"; harness.vm._in_nondet=True
    try:
        assert eim.consensus_callbacks(SNAPSHOT)[1](eim.gl.vm.Return(c)) is False
    finally:
        harness.vm._in_nondet=False
    assert harness.models==[] and harness.writes==[]


def test_validator_injection_boundary_and_definitions_verbatim(eim,harness):
    attack=(Path(__file__).parents[1]/"fixtures/injection/source.txt").read_text()
    blocks=[{"index":i,"url":url,"read_status":"READABLE","content":attack} for i,url in enumerate(URLS)]
    c=eim.candidate_from_model_output(list(URLS),["READABLE"]*2,["a"*64]*2,
      '{"relevance":["RELEVANT","RELEVANT"],"relations":["UNKNOWN"]}')
    prompt=eim.validation_prompt((attack,attack,URLS),blocks,c)
    assert json.loads(prompt.split("SOURCE BLOCKS\n",1)[1].split("\n\nPROPOSED LABELS",1)[0])==blocks
    definitions=eim.CLASSIFICATION_PROMPT_V1.split("RELEVANCE DEFINITIONS\n",1)[1].split("OUTPUT SCHEMA AND ORDERING\n",1)[0]
    assert definitions in prompt and "{{SOURCE_BLOCKS_JSON}}" in prompt
    assert "No Leader reasoning is provided" in prompt


@pytest.mark.parametrize("fault", ["dependent-to-independent", "independent-to-dependent", "relevant-to-not-relevant"])
def test_negative_frozen_candidate_semantic_mutations_scripted_boundary(eim,harness,fault):
    # These are scripted field rejections, not a claim that a real model rejects them.
    h=harness
    fixed_candidate(eim,h)
    def mutate(c):
        if fault=="dependent-to-independent": c["pairs"][0]["relation"]="INDEPENDENT"
        elif fault=="independent-to-dependent": c["pairs"][1]["relation"]="DEPENDENT"
        else:
            c["sources"][0]["relevance"]="NOT_RELEVANT"
            for p in c["pairs"]:
                if p["i"]==0 or p["j"]==0: p["relation"]="UNKNOWN"
    h.mutation=mutate
    with pytest.raises(MockDisagree):
        h.contract.assess("mutation",SYNTHETIC["claim"],SYNTHETIC["context"],list(h.urls))
    assert len(h.models)==2 and h.writes==[]


def test_unrelated_relevance_flip_scripted_rejection(eim,harness):
    h=harness
    body=b"Office stationery inventory: 14 staplers; no temperatures or weather observations."
    for actor in ("Leader","Validator"):
        h.responses[(actor,URLS[1])]={"status":200,"headers":{},"body":body}
        h.model_output[actor]='{"relevance":["RELEVANT","NOT_RELEVANT"],"relations":["UNKNOWN"]}'
    h.mutation=lambda c:c["sources"][1].update(relevance="RELEVANT")
    with pytest.raises(MockDisagree): assess(h)
    assert len(h.models)==2 and h.writes==[]
