# PHASE4_FINAL_CLOSURE

Updated UTC: 2026-10-07T09:50:54.834982+00:00

**PHASE 4 = PASS / CLOSED. LIVENESS = PASS. SEMANTIC SAFETY = PASS.**
Final deployment, both NEW examples, REUSED, lookup and protocol evidence now all refer to the same final canonical contract. No prior-address carry-forward is needed for these final Gate requirements. Historical deployments/results remain preserved. PHASE5/Repository B/EchoMap NOT_STARTED / NOT_AUTHORIZED.

## Canonical identity

|Field|Final fact|
|---|---|
|Canonical Contract|0x7045b893E15B699e04494aA3849730bC6Aa1C864|
|Source Commit|4874fd469cb5477b9d8f8ec9dbc19252a6112e6e|
|Source SHA256|121deb7f9a2a0ae4c7704e96d74b3678054ccd2dbed77ff7e3373fa75749c095|
|Protocol Version|EIM-V1-STUDIO|
|Schema Version|EIM-CANDIDATE-V1|
|Rules Identifier|EIM-V1-STUDIO|
|Consensus manifest revision|ACR-001-SAFETY-1|
|Network / Chain ID|Stable Studionet /61999|
|RPC|https://studio.genlayer.com/api|
|Explorer|https://explorer-studio.genlayer.com|

Protocol/state/IDs retain EIM-V1-STUDIO under the previously documented approved version strategy. Consensus revision + source commit/SHA + distinct address distinguish the safety implementation without changing business enums or adding public fields. Source commit local and bundled, not claimed published in the public fixture GitHub commit; remote source publication belongs to later authorized packaging. No code, Freeze, ACR, prompt, fixture or deployment change in this closure; no new source commit needed.

## Final canonical transactions

|Operation|Transaction|Finality / execution / consensus|Rounds / rotations / actual successful identities|
|---|---|---|---|
|Deployment|[0x2486995a27e99c7d3bd1da857e9af39b330eb2092f066edb780aa44caacd3007](https://explorer-studio.genlayer.com/tx/0x2486995a27e99c7d3bd1da857e9af39b330eb2092f066edb780aa44caacd3007)|FINALIZED / SUCCESS / MAJORITY_AGREE|1 /0 /5|
|Controlled synthetic NEW|[0xec875a1a5de724b7fd6a407e851ba736393ae508f330c1b94059c9f72191d7f4](https://explorer-studio.genlayer.com/tx/0xec875a1a5de724b7fd6a407e851ba736393ae508f330c1b94059c9f72191d7f4)|FINALIZED / SUCCESS / MAJORITY_AGREE|1 /0 /4|
|Real public-document NEW|[0x77ddb362ff4fa11dc9a827de14f143da266c3c9c82d018950c9fc9376b45f4bb](https://explorer-studio.genlayer.com/tx/0x77ddb362ff4fa11dc9a827de14f143da266c3c9c82d018950c9fc9376b45f4bb)|FINALIZED / SUCCESS / MAJORITY_AGREE|1 /0 /3|
|REUSED controlled|[0x8c0ea62020311b5718fe53bab1f3f4bad3aeca2ab2429e5eb719683c939ef9f8](https://explorer-studio.genlayer.com/tx/0x8c0ea62020311b5718fe53bab1f3f4bad3aeca2ab2429e5eb719683c939ef9f8)|FINALIZED / SUCCESS / MAJORITY_AGREE|1 /0 /3|

Full/Normal consensus configured5 initial validators; actual counts include unique successful Leader/Validator execution identities, counting Leader duplicates once. Controlled4, public3, REUSED3 meet frozen minimum3; not represented as5 active validators. Idle/error identities not counted. Per-round addresses, execution results, votes, hashes/status changes/last_round and available model statistics remain in full native receipt/analysis files. Private field verdicts, provider/operator diversity and reasons for dissent/idle are not inferred or investigated. No receipt hash decoded as a semantic claim.

## Controlled synthetic finalized evidence
Request_id **68b9090d638738bd0236b084aff95ae7551d8df11da9b282aaa536ecd448258f**; client_key `acr001-safety-controlled-20261007`; payload_digest `e06b4af4688ba1f6a14bf60d8b350846ca8cf622c9945c4bf482ac60d7b83391`. Same frozen claim/context and four unchanged SYNTHETIC DEMO documents at commit5a11c820a28e23303298f12650377ee78faab0ba.
Finalized get_assessment found=true; full input/evidence digest binding and deterministic invariants verified. Exact actual matrix:

|Pair|Actual stored relation|
|---|---|
|A–B|DEPENDENT|
|A–C|INDEPENDENT|
|A–D|UNKNOWN|
|B–C|INDEPENDENT|
|B–D|UNKNOWN|
|C–D|UNKNOWN|

**1 DEPENDENT /2 INDEPENDENT /3 UNKNOWN; PARTIAL; maximum pairwise independent set [0,2]=[A,C],size2.** All sources READABLE/RELEVANT. Controlled transaction successful1round0rotation4actual identities. No result hardcoding/retry/new controlled transaction in this closure.

## Real public-document NEW on final canonical

Request_id **5c8aae111e19f6b193d5a8b4b8dce4697f424166922cd2116b49343b620c7b46**; new client_key `final-erc20-closure-20261007`; payload_digest `b49273ab5265b1f812cf230cc55cc4234172aa68015bb8b2828464ce477efd4d`.
Claim: ERC-20规范定义balanceOf用于返回指定账户的token余额。
Context: 判断范围为规范规定的接口，不是代码是否独立开发。

Exact PHASE3 URLs retained: ERC-20 fixed commit and OpenZeppelin IERC20 releasev5.4.0; no switch to mutable main/master or alternative materials. Fresh HTTP200, strictUTF8, frozen raw bytes, size/encoding/allowlist/query/fragment/extensions and normalized digest equality verified before submission; metadata in public-document-source-check.json. Canonical URL ordering sorts IERC20 first, ERC second, preserving their proper index/digest mapping.

|Index|Actual source URL|read_status|relevance|Actual normalized content_digest|
|---|---|---|---|---|
|0|https://raw.githubusercontent.com/OpenZeppelin/openzeppelin-contracts/v5.4.0/contracts/token/ERC20/IERC20.sol|READABLE|RELEVANT|4cbb8139ede4a09ec0e79b57e6b8eda9481c0ad731fc7745a0ec058847bc8350|
|1|https://raw.githubusercontent.com/ethereum/ERCs/f2f4ff22452dec9d340ba9b8b1ee33c962a613d6/ERCS/erc-20.md|READABLE|RELEVANT|5ad66b7c4d33aae514fc5fdffba24804a5b4b2edbda9662cb9e1ba60136ec587|

Actual relation **DEPENDENT**, result_status **COMPLETE**, counts1D/0I/0U; maxset[0],size1. Both relevance labels recorded above. Relation was not a precondition imposed on the model or Gate; authentic network result retained. FINALIZED/SUCCESS/MAJORITY_AGREE, found=true, full invariant/input/digest match. Only1 NEW submitted, no retry. Actual participant identities and votes in public-document-latest.json/public-document-analysis.json.

## REUSED and lookup

Exactly1 REUSED transaction using controlled record's same creator/key/claim/context/ordered URLs. Actual successful return **REUSED**, same request_id68b9090d638738bd0236b084aff95ae7551d8df11da9b282aaa536ecd448258f. Latest-final full Assessment equals the original controlled finalized record byte/content structure; no new request ID or changed record. Existing early preflight returns without persistent save/fetch/model/nondet block; local tests protect that unchanged path. Exposed Leader eq_outputs={}; other unavailable private execution details remain NOT_EXPOSED, not invented. Complete network receipts in reused-latest.json; scoped fields in reused-no-nondet-evidence.json. No claim of a separately exposed global mapping-count/state-diff interface.

Both final-canonical lookup_request calls use creator+client_key and latest-final read only, no write:

```json
{
  "public_document": {
    "found": true,
    "payload_digest": "b49273ab5265b1f812cf230cc55cc4234172aa68015bb8b2828464ce477efd4d",
    "request_id": "5c8aae111e19f6b193d5a8b4b8dce4697f424166922cd2116b49343b620c7b46",
    "result_status": "COMPLETE"
  },
  "controlled_after_reused": {
    "found": true,
    "payload_digest": "e06b4af4688ba1f6a14bf60d8b350846ca8cf622c9945c4bf482ac60d7b83391",
    "request_id": "68b9090d638738bd0236b084aff95ae7551d8df11da9b282aaa536ecd448258f",
    "result_status": "PARTIAL"
  }
}
```

## Final get_protocol_info (actual latest-final read)

Read once in this closure; matches final deployed implementation/unchanged frozen limits and source rules:

```json
{
  "limits": {
    "body_bytes": 32768,
    "claim": 600,
    "client_key": 64,
    "context": 400,
    "sources_max": 4,
    "sources_min": 2,
    "text_codepoints": 8000,
    "url_bytes": 512
  },
  "protocol_version": "EIM-V1-STUDIO",
  "relation_rules": "EIM-V1-STUDIO",
  "schema_version": "EIM-CANDIDATE-V1",
  "source_rules": {
    "extensions": [
      ".txt",
      ".md",
      ".adoc",
      ".sol"
    ],
    "hosts": [
      "raw.githubusercontent.com",
      "<legal-github-owner>.github.io"
    ],
    "scheme": "https"
  }
}
```

## Tests / safety evidence boundaries

|Class|Verified boundary|
|---|---|
|LOCAL SAFETY VERIFIED|277 local tests PASS retained (251 prior+26 safety),3 Node vectors; source unchanged; strict digest/schema/parser/anchors/error/idempotency/atomicity guards and scripted negative controls. No full suite rerun this closure|
|REAL CONTROLLED POSITIVE VERIFIED|Final-canonical one controlled NEW, exact frozen matrix, multi-participant consensus/finality/success, foundtrue; real public normative pair additionally succeeded|
|REAL NEGATIVE-CONTROL NOT VERIFIED|NOT REAL-NETWORK VERIFIED. No malicious-model/negative business transaction or new real-model harness executed; local mocks do not prove real-model rejection reliability|

REAL_MODEL_PREDEPLOY_GATE_UNAVAILABLE remains historical tooling limitation, not re-investigated. Finite positive examples are not universal provenance accuracy, hidden-origin authentication, prompt-injection immunity or a truth verdict for claims. Private Validator anchors/reasons not exposed. Controlled dissent and some idle/error nodes remain in honest raw evidence; no liveness re-diagnosis.

## Budget / files / final Gate

Closure used0 deployments,1 public NEW+1 REUSED =2 raw submissions,0retries/newclient-key gambling,0newFaucet requests/paid RPC/API, **cash0**. Existing free Faucet GEN only; after balance2000000000000000000wei. Official locked SDK1.1.8/viem2.57.3 legacy estimation/submission path, chain61999/value0/gasPrice0 guard retained. No production/test/Freeze/ACR changes, no大规模tests, noPhase5/B.

Evidence directory `evidence/phase4-final-closure`: full sanitized rpc.jsonl/native receipts, participant analyses, source checks/inputs, finalized reads/lookups, actual return gates, one final protocol read, submission/signing/one-shot intent records and final-closure-summary.json. Prior deployment/controlled/source bundle/test proof retained in evidence/semantic-safety; old diagnostic deployments retained separately. Complete final recovery package includes these artifacts and canonical source bundle, excluding signer secrets.

All8 user final Gate conditions now met on final canonical: deployment; controlled success; exact frozen matrix; real public NEW; REUSED; correct finalized lookup; protocol; consolidated evidence package.
**PHASE4 = PASS / CLOSED. STOP; wait for separate Repository B / EchoMap authorization.**
