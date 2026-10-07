import ast
import copy
import itertools
import json
import subprocess
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
CREATOR = "0x" + "ab" * 20
URLS = ["https://raw.githubusercontent.com/a/r/main/" + chr(97+i) + ".txt" for i in range(4)]


def candidate(e, n=4, relations=None, relevant=None, statuses=None):
    relevant = relevant or ["RELEVANT"] * n
    statuses = statuses or ["READABLE"] * n
    return {"schema_version": e.SCHEMA_VERSION,
            "sources": [{"index": i, "url": URLS[i], "read_status": statuses[i],
                         "content_digest": "a" * 64 if statuses[i] == "READABLE" else None,
                         "relevance": relevant[i]} for i in range(n)],
            "pairs": [{"i": i, "j": j, "relation": relation}
                      for (i, j), relation in zip(e.ordered_pairs(n), relations or ["UNKNOWN"] * (n*(n-1)//2))]}


def rejected(e, code, function, *args):
    with pytest.raises(e.ProtocolError) as exc:
        function(*args)
    assert exc.value.code == code


@pytest.mark.parametrize("key", ["", "a" * 65, "a b", "é", "x.y", "\nkey", None, 5])
def test_key_rejection(eim, key):
    rejected(eim, "INVALID_INPUT", eim.validate_key, key)


def test_input_boundaries(eim):
    for key in ("a", "X_9-" * 16):
        for n in (2, 4):
            data = eim.normalize_inputs(key, "😀" * 600, "中" * 400, URLS[:n])
            assert len(data["claim"]) == 600
    for claim, context, urls in [(" ", "", URLS[:2]), ("x"*601, "", URLS[:2]),
                                 ("x", "y"*401, URLS[:2]), (None, "", URLS[:2]),
                                 ("x", None, URLS[:2]), ("x", "", URLS[:1]),
                                 ("x", "", URLS + [URLS[0]]), ("x", "", tuple(URLS[:2]))]:
        rejected(eim, "INVALID_INPUT", eim.normalize_inputs, "k", claim, context, urls)


def test_text_normalization(eim):
    assert eim.normalize_text("\ufeff \r\n中 😀\rA  B\n ") == "中 😀\nA  B"
    assert eim.normalize_text("X\\Y\"!") == "X\\Y\"!"
    assert eim.content_digest("\ufeff x\r\ny ") == eim.content_digest("x\ny")
    assert eim.content_digest("x  y") != eim.content_digest("x y")
    assert eim.normalize_text("\u0085x\u001c") == "x"
    rejected(eim, "INVALID_INPUT", eim.normalize_text, "\ud800")


@pytest.mark.parametrize("url", [
    "http://alice.github.io/a.txt", "https://alice.github.io/a.txt?", "https://alice.github.io/a.txt#",
    "https://user@alice.github.io/a.txt", "https://alice.github.io:444/a.txt", "https://alice.github.io:/a.txt",
    "https://alice.github.io/a\\b.txt", "https://alice.github.io/\na.txt", "https://alice.github.io/\ta.txt",
    "https://alice.github.io/a\x7f.txt", "https://alice.github.io/中文.txt", "https://alice.github.io/a b.txt",
    "https://127.0.0.1/a.txt", "https://[::1]/a.txt", "https://alice.github.io/./a.txt",
    "https://alice.github.io/x/../a.txt", "https://alice.github.io/%2e/a.txt",
    "https://alice.github.io/.%2E/a.txt", "https://alice.github.io/%2E%2e/a.txt",
    "https://nested.alice.github.io/a.txt", "https://alice.github.io.evil.com/a.txt",
    "https://evilgithub.io/a.txt", "https://alice.github.io./a.txt", "https://-alice.github.io/a.txt",
    "https://alice-.github.io/a.txt", "https://al--ice.github.io/a.txt",
    "https://"+"a"*40+".github.io/a.txt", "https://alice.github.io/a.TXT",
    "https://alice.github.io/a.html", "https://alice.github.io", "https://alice.github.io/%zz.txt",
])
def test_url_restrictions(eim, url):
    rejected(eim, "UNSUPPORTED_URL", eim.normalize_url, url)


def test_url_normalization_duplicates_and_boundary(eim):
    assert eim.normalize_url("HTTPS://Alice.GITHUB.IO:443/A%2fb.md") == "https://alice.github.io/A%2fb.md"
    assert eim.normalize_url("https://"+"a"*39+".github.io/a.sol").endswith("a.sol")
    prefix = "https://alice.github.io/"
    assert len(eim.normalize_url(prefix + "x"*(512-len(prefix)-4) + ".txt")) == 512
    rejected(eim, "INVALID_INPUT", eim.normalize_url, prefix + "x"*(513-len(prefix)-4)+".txt")
    rejected(eim, "DUPLICATE_URL", eim.normalize_inputs, "k", "x", "",
             ["HTTPS://ALICE.GITHUB.IO:443/a.txt", "https://alice.github.io/a.txt"])
    assert eim.normalize_inputs("k", "x", "", list(reversed(URLS)))["urls"] == URLS


def test_creator_and_hash_vectors(eim):
    vectors = json.loads((ROOT / "tests/vectors/canonical-v1.json").read_text())
    for vector in vectors:
        inputs = eim.normalize_inputs(**vector["raw_inputs"])
        assert inputs == vector["normalized_inputs"]
        assert eim.normalize_creator(vector["creator"]) == vector["normalized_creator"]
        assert eim.canonical_json([eim.PROTOCOL_VERSION, vector["normalized_creator"], inputs["client_key"]]) == vector["request_canonical_json"]
        assert eim.canonical_json([eim.PROTOCOL_VERSION, inputs["claim"], inputs["context"], inputs["urls"]]) == vector["payload_canonical_json"]
        assert eim.request_id(vector["creator"], inputs["client_key"]) == vector["request_id"]
        assert eim.payload_digest(inputs["claim"], inputs["context"], inputs["urls"]) == vector["payload_digest"]
    for address in ("0x123", " " + CREATOR, CREATOR + "0", None):
        rejected(eim, "INVALID_INPUT", eim.normalize_creator, address)
    result = subprocess.run(["node", str(ROOT / "tests/vectors/verify_vectors.mjs")], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert "vectors verified" in result.stdout


@pytest.mark.parametrize("raw", [
    "", "```json\n{}\n```", "explanation {}", "{} trailing", "[]", "null",
    '{"relevance":[],"relevance":[],"relations":[]}',
    '{"relevance":[],"relations":[],"x":1}', '{"relevance":[]}',
    '{"relevance":[NaN],"relations":[]}', '{"relevance":[Infinity],"relations":[]}',
    '{"relevance":[{"x":1,"x":2}],"relations":[]}',
    '{"relevance":["RELEVANT","RELEVANT"],"relations":["SELF"]}',
    '{"relevance":["RELEVANT"],"relations":["UNKNOWN"]}',
    '{"relevance":[true,"RELEVANT"],"relations":["UNKNOWN"]}',
])
def test_strict_model_parser_rejects(eim, raw):
    rejected(eim, "INVALID_MODEL_OUTPUT", eim.candidate_from_model_output, URLS[:2], ["READABLE"]*2, ["a"*64]*2, raw)


def test_parser_binds_metadata(eim):
    raw = '{"relevance":["RELEVANT","NOT_APPLICABLE"],"relations":["UNKNOWN"]}'
    c = eim.candidate_from_model_output(URLS[:2], ["READABLE", "UNAVAILABLE"], ["a"*64, None], raw)
    assert c["sources"][1]["content_digest"] is None
    bad = raw.replace("UNKNOWN", "INDEPENDENT")
    rejected(eim, "INVALID_MODEL_OUTPUT", eim.candidate_from_model_output, URLS[:2], ["READABLE", "UNAVAILABLE"], ["a"*64, None], bad)


@pytest.mark.parametrize("mutation", [
    lambda c: c.update(extra=1), lambda c: c.pop("schema_version"),
    lambda c: c.update(schema_version="V2"), lambda c: c["sources"].pop(), lambda c: c["pairs"].pop(),
    lambda c: c["sources"][0].update(index=True), lambda c: c["sources"][0].update(index=1),
    lambda c: c["sources"][0].update(url="https://alice.github.io/a.txt"),
    lambda c: c["sources"][0].update(content_digest="A"*64), lambda c: c["sources"][0].update(content_digest=None),
    lambda c: c["sources"][0].update(read_status="bad"), lambda c: c["sources"][0].update(relevance="bad"),
    lambda c: c["sources"][0].update(relevance="NOT_APPLICABLE"),
    lambda c: c["sources"][0].update(read_status="UNAVAILABLE"),
    lambda c: c["pairs"].reverse(), lambda c: c["pairs"].__setitem__(1, c["pairs"][0]),
    lambda c: c["pairs"][0].update(i=False), lambda c: c["pairs"][0].update(j=1.0),
    lambda c: c["pairs"][0].update(relation="SELF"), lambda c: c["pairs"][0].update(reason="x"),
])
def test_candidate_rejection(eim, mutation):
    c = candidate(eim)
    mutation(c)
    rejected(eim, "INVALID_MODEL_OUTPUT", eim.validate_candidate, c, URLS)


@pytest.mark.parametrize("status,relevance,digest", [
    ("UNAVAILABLE", "RELEVANT", None), ("UNSUPPORTED", "NOT_APPLICABLE", "a"*64),
    ("READABLE", "NOT_APPLICABLE", "a"*64), ("READABLE", "RELEVANT", "a"*63),
])
def test_source_invariants(eim, status, relevance, digest):
    c = candidate(eim, n=2)
    c["sources"][0].update(read_status=status, relevance=relevance, content_digest=digest)
    rejected(eim, "INVALID_MODEL_OUTPUT", eim.validate_candidate, c, URLS[:2])


@pytest.mark.parametrize("relevance", ["NOT_RELEVANT", "UNCERTAIN"])
def test_noneligible_requires_unknown(eim, relevance):
    c = candidate(eim, n=2, relations=["DEPENDENT"], relevant=[relevance, "RELEVANT"])
    rejected(eim, "INVALID_MODEL_OUTPUT", eim.validate_candidate, c, URLS[:2])
    c["pairs"][0]["relation"] = "UNKNOWN"
    assert eim.postprocess(c, URLS[:2])["max_supported_independent_set"] == [1]


@pytest.mark.parametrize("relations,expected,status,counts", [
    (["INDEPENDENT"]*6, [0,1,2,3], "COMPLETE", (0,6,0)),
    (["DEPENDENT"]*6, [0], "COMPLETE", (6,0,0)),
    (["UNKNOWN"]*6, [0], "PARTIAL", (0,0,6)),
    (["DEPENDENT","INDEPENDENT","UNKNOWN","INDEPENDENT","UNKNOWN","UNKNOWN"], [0,2], "PARTIAL", (1,2,3)),
    (["INDEPENDENT","UNKNOWN","UNKNOWN","UNKNOWN","UNKNOWN","INDEPENDENT"], [0,1], "PARTIAL", (0,2,4)),
])
def test_postprocessing_cases(eim, relations, expected, status, counts):
    p = eim.postprocess(candidate(eim, relations=relations), URLS)
    assert p["max_supported_independent_set"] == expected
    assert p["max_supported_independent_set_size"] == len(expected)
    assert p["result_status"] == status
    assert tuple(p[k] for k in ("dependent_pair_count","independent_pair_count","unknown_pair_count")) == counts


def test_no_single_eligible_and_nontransitivity(eim):
    c = candidate(eim, relevant=["NOT_APPLICABLE"]*4, statuses=["UNAVAILABLE","UNSUPPORTED"]*2)
    assert eim.postprocess(c, URLS)["max_supported_independent_set"] == []
    c["sources"][2].update(read_status="READABLE", content_digest="b"*64, relevance="RELEVANT")
    assert eim.postprocess(c, URLS)["max_supported_independent_set"] == [2]
    c = candidate(eim, n=3, relations=["DEPENDENT","INDEPENDENT","DEPENDENT"])
    assert eim.postprocess(c, URLS[:3])["max_supported_independent_set"] == [0,2]


def test_exhaustive_four_node_relations(eim):
    # Independent oracle: sorted power set instead of production combinations-by-size.
    for relations in itertools.product(eim.RELATIONS, repeat=6):
        c = candidate(eim, relations=list(relations))
        feasible = []
        for mask in range(16):
            subset = [i for i in range(4) if mask & (1 << i)]
            if not any(p["i"] in subset and p["j"] in subset and p["relation"] != "INDEPENDENT" for p in c["pairs"]):
                feasible.append(subset)
        expected = sorted(feasible, key=lambda s: (-len(s), s))[0]
        result = eim.postprocess(c, URLS)
        assert result["max_supported_independent_set"] == expected
        assert result["unknown_pair_count"] == relations.count("UNKNOWN")
        assert result["result_status"] == ("PARTIAL" if "UNKNOWN" in relations else "COMPLETE")


def test_assessment_invariants_and_idempotency(eim):
    data = eim.normalize_inputs("key", "x", "", URLS)
    record = eim.build_assessment(CREATOR, data, candidate(eim))  # Human candidate, no consensus claim.
    assert eim.validate_assessment(record) == record
    rid, pdigest = record["request_id"], record["payload_digest"]
    assert eim.idempotency_preflight(None, rid, pdigest) is None
    before = copy.deepcopy(record)
    assert eim.idempotency_preflight(record, rid, pdigest) == {"request_id": rid, "disposition":"REUSED", "result_status":"PARTIAL"}
    rejected(eim, "IDEMPOTENCY_CONFLICT", eim.idempotency_preflight, record, rid, "b"*64)
    assert record == before
    assert eim.request_id("0x"+"cd"*20,"key") != rid
    assert eim.request_id(CREATOR,"another-key") != rid
    assert eim.payload_digest("changed", "", URLS) != pdigest
    for field, value in [("request_id","0"*64), ("payload_digest","0"*64), ("creator",CREATOR.upper()),
                         ("claim"," x "), ("result_status","COMPLETE"), ("unknown_pair_count",0),
                         ("max_supported_independent_set",[1]), ("max_supported_independent_set_size",True)]:
        bad = copy.deepcopy(record)
        bad[field] = value
        rejected(eim, "INVALID_MODEL_OUTPUT", eim.validate_assessment, bad)


def test_sdk_schema_and_atomic_boundary(eim, monkeypatch):
    from genlayer.py.get_schema import get_schema
    from gltest.direct import VMContext
    from gltest.direct.loader import _allocate_contract
    schema = get_schema(eim.EvidenceIndependenceMatrix)
    assert set(schema["methods"]) == {"assess","get_assessment","lookup_request","get_protocol_info"}
    assert schema["methods"]["assess"]["readonly"] is False
    assert all(schema["methods"][k]["readonly"] for k in schema["methods"] if k != "assess")
    (ROOT / "evidence/public-schema.json").write_text(json.dumps(schema, indent=2)+"\n")
    vm = VMContext()
    with vm.activate():
        obj = _allocate_contract(eim.EvidenceIndependenceMatrix, vm)
        assert obj.get_assessment("0"*64) == {"found":False}
        assert obj.lookup_request(CREATOR,"key")["found"] is False
        assert obj.get_protocol_info()["protocol_version"] == "EIM-V1-STUDIO"
        def unavailable_boundary(self, inputs):
            raise RuntimeError("test consensus failure")
        monkeypatch.setattr(eim.EvidenceIndependenceMatrix, "_obtain_candidate", unavailable_boundary)
        with pytest.raises(RuntimeError, match="test consensus failure"):
            obj.assess("key", "x", "", URLS)
        rid = eim.request_id(str(eim.gl.message.sender_address), "key")
        assert obj.get_assessment(rid) == {"found":False}
        for bad in ("0x"+"0"*64, "A"*64, "x", None):
            rejected(eim, "INVALID_INPUT", obj.get_assessment, bad)
    tree = ast.parse((ROOT / "contracts/evidence_independence_matrix.py").read_text())
    cls = next(node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == "EvidenceIndependenceMatrix")
    assert [node.target.id for node in cls.body if isinstance(node,ast.AnnAssign)] == ["assessments"]
    method = next(node for node in cls.body if isinstance(node,ast.FunctionDef) and node.name == "assess")
    writes = [node for node in ast.walk(cls) if isinstance(node,ast.Assign) and any(isinstance(t,ast.Subscript) and isinstance(t.value,ast.Attribute) and t.value.attr == "assessments" for t in node.targets)]
    assert len(writes) == 1
    calls = {node.func.id:node.lineno for node in ast.walk(method) if isinstance(node,ast.Call) and isinstance(node.func,ast.Name)}
    assert calls["build_assessment"] < calls["validate_assessment"] < writes[0].lineno
    boundary = next(node for node in ast.walk(method) if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "_obtain_candidate")
    assert boundary.lineno < calls["build_assessment"]
    # The Phase 1 boundary has now been implemented; callbacks are tested in test_consensus.py.
