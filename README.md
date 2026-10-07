# Evidence Independence Matrix

A reusable GenLayer Intelligent Contract that maps **claim-scoped visible provenance relationships** among2–4 public text sources and stores a maximum supported **pairwise independent set**. It does not determine whether a claim is true.

Several reports can repeat one original source. EIM gives collaborators a shared record of which pairs have supported shared/derived origins, distinguishable acquisition paths, or insufficient provenance. Other developers can use the4-method primitive for DAO evidence prechecks, research source selection or AI evidence workflows without installing EchoMap.

**Canonical:**`0x7045b893E15B699e04494aA3849730bC6Aa1C864` · Stable Studionet61999 · EIM-V1-STUDIO /EIM-CANDIDATE-V1 · consensus revision ACR-001-SAFETY-1. [Deployment](DEPLOYMENT_MANIFEST_STUDIONET.md) · [Real evidence](ONCHAIN_EVIDENCE.md) · [Reviewer quick path](REVIEWER_QUICK_PATH.md).

## Why GenLayer

ChatGPT can analyze the documents, but one private answer gives collaborators no jointly validated persistent record. A conventional server can implement the algorithm; its operator still controls fetches, interpretation and publication. GenLayer provides native bounded HTTP/model execution, multiple participants validating one candidate, and shared chain state that applications can independently read.

Leader fetches/normalizes/digests all sources and proposes the complete canonical classification. Custom Validator independently fetches and hashes those materials, strictly binds evidence fields and checks **each** proposed relevance/pair label against the rules. Positive relations need grounded verbatim provenance/acquisition anchors. Validator receives no Leader reasoning, is not format-only and does not regenerate enums for exact-token equality. Unsupported semantic fields or digest mismatch disagree; temporary failures cannot become UNKNOWN.

Deterministic code rejects malformed/duplicate-key model JSON, enforces schema/order/invariants, handles creator-key idempotency, computes counts/status/maximum set and saves only after complete accepted validation. These enforced boundaries plus independent semantic validation distinguish the contract from an unrestricted model-response wrapper. [Security model](SECURITY_AND_TRUST_MODEL.md).

## Relations and state

| Relation | Required visible evidence |
|---|---|
|DEPENDENT|positive claim-related shared original material or derivation/citation|
|INDEPENDENT|both claim-relevant, identifiable distinct acquisition paths, no visible shared/derived claim-related origin|
|UNKNOWN|neither positive standard established, or insufficient provenance/relevance; never an execution-error fallback|

Different domains do not prove independence; same event/conclusion/wording does not prove dependence. UNKNOWN-first and non-transitivity remain: no relation is inferred through a third pair. The maximum set contains only READABLE/RELEVANT sources with INDEPENDENT edges for every selected pair, ties broken lexicographically; it is not a count of ultimate evidence families.

Only immutable assessments mapping values persist:claim/context/normalized URLs, creator/key/request/payload IDs, SourceObservation(read_status/digest/relevance), every PairDecision, counts, COMPLETE/PARTIAL and maximum set. No raw source body, score, explanation, internal anchors or pending business record. COMPLETE does not mean truth.

| Public method | Authorization / result |
|---|---|
|assess(client_key,claim,context,urls)|any actual sender;NEW/REUSED with request_id/result_status|
|get_assessment(request_id)|public view;found:false or complete stored Assessment|
|lookup_request(creator,client_key)|public view;derivedID/found and stored payload/status if present|
|get_protocol_info()|public view;protocol/schema/rules/limits/source scope|

Same creator/key/payload returns REUSED before HTTP/model/consensus; a changed payload gives IDEMPOTENCY_CONFLICT. New creator has an independent namespace. Failed validation/consensus leaves no partial Assessment. See [full protocol](PROTOCOL_SPEC.md).

## Review without sending a transaction

Controlled existing request:`68b9090d638738bd0236b084aff95ae7551d8df11da9b282aaa536ecd448258f`. [Actual onchain result and receipts](ONCHAIN_EVIDENCE.md):PARTIAL1D/2I/3U,[A,C],size2; **SYNTHETIC DEMO**. Real ERC-20/IERC20 request:`5c8aae111e19f6b193d5a8b4b8dce4697f424166922cd2116b49343b620c7b46`:actual DEPENDENT/COMPLETE. Both use this canonical contract. Use Studio's get_protocol_info/get_assessment views or the saved finalized records; EchoMap is optional. Minimum3 distinct successful participants was met for canonical NEW examples; configured5 is not claimed to be5 active validators.

## Local tests and exact environment

277 local tests PASS,0errors/failures/skips, retained unchanged; [XML](evidence/semantic-safety/all-tests.xml). HTTP/model responses are scripted; these tests do not prove real-model negative-control reliability.3 Node vectors passed in final packaging.

```sh
python -m venv .venv
.venv/bin/python -m pip install -r requirements.lock
.venv/bin/python -m pytest -q
node tests/vectors/verify_vectors.mjs
```

Python3.12.14; Node24.19.0; genlayer-test0.29.2; genlayer-py0.16.3; exact GenVM v0.2.16/content-addressed Depends from the production header. [Environment lock](docs/ENVIRONMENT_LOCK.md) and requirements.lock pin dependencies. Official test artifact download may be needed on first run; no private node, backend or paid provider is needed. The local harness does not send RPC business transactions.

## Trust limits and historical record

[Known limitations](KNOWN_LIMITATIONS.md):visible declarations may be false/omit shared origins; semantic results can vary and consensus can fail. Real negative controls remain NOT REAL-NETWORK VERIFIED. No claim of trustlessness, fully decentralized operation, universal accuracy or immunity. [Approved Freeze](docs/ARCHITECTURE_FREEZE_V1.md),[ACR-001](docs/ARCHITECTURE_CHANGE_REQUEST_001.md) and[safety patch](docs/ACR001_SEMANTIC_SAFETY_PATCH.md) preserve authority history. Superseded addresses are isolated in deployment history, never fallback canonical contracts.

Publication checkpoint:local final documentation/source package ready; full source remote publication is BLOCKED by current GitHub connector failure. Deployed source commit `4874fd469cb5477b9d8f8ec9dbc19252a6112e6e` is preserved in [bundle](deployment/canonical-source.bundle); production SHA256 `121deb7f9a2a0ae4c7704e96d74b3678054ccd2dbed77ff7e3373fa75749c095`. Do not infer that the local source commit is already available at a remote /tree URL.
