# Submission A — Intelligent Contracts

**Title:**Evidence Independence Matrix
**One-line description:**A reusable GenLayer primitive for claim-scoped visible-source dependence and maximum supported pairwise-independent evidence sets.
**Category / positioning:**Intelligent Contract primitive;provenance/evidence coordination, not a truth oracle.
**Status:**Local package ready;remote final-source publication BLOCKED, so this is not a Portal-ready claim yet.

## Problem / primitive

Repeated reports may share one original observation.2–4URLs are not necessarily2–4independent evidence sources. EIM records each pair's supported DEPENDENT/INDEPENDENT/UNKNOWN relation and derives an immutable shareable maximum pairwise set. DAO reviewers,research tools and AI evidence workflows can call the4-method contract without EchoMap.

## Why GenLayer / consensus design

A private ChatGPT response or operator-controlled server has no independently validated shared state. GenLayer's bounded native HTTP/model execution allows Leader interpretation to be validated by multiple participants before storing one candidate. Leader independently fetches/normalizes/digests,classifies all relevance/pairs and strictly parses. Custom run_nondet_unsafe Validator independently reacquires evidence,requires exact schema/status/digest/URL/index/order and checks every proposed label under frozen rules. Positive relation acceptance requires internal grounded spans/fact types. No Leader reasoning,no regenerated-equal-token requirement,no convenience equivalence/format-only/overall-score replacement.

## Equivalence / safety / state

ACR-001-SAFETY-1 evidence-bound validation:all deterministic/evidence-binding fields strictly equal;every semantic field independently rule-supported. Any mismatch/unsupported label/parser/runtime failure disagrees. No merging,repair or error→UNKNOWN. UNKNOWN-first,claimscope/non-transitivity remain. Single assessments mapping stores immutable full Assessment/source observations/pairs/counts/COMPLETE orPARTIAL/maxset;no source bodies/reasoning/anchors/score/pending state. Deterministic identifiers,idempotency,maximum-set tie-break and atomic write remain.

## Public methods / authorization

assess(client_key,claim,context,urls):anyactualsender,NEW/REUSED request/status return. get_assessment(request_id),lookup_request(creator,client_key),get_protocol_info():public reads. Same creator/key/payload REUSED before nondeterminism;changedpayload conflicts;othercreator separate namespace. No admin/debug method.

## Deployment / repository / source identity

Repository:https://github.com/halihalibt/evidence-independence-matrix. Final implementation publication pending;do not treat current remote fixture-only state as complete.
Canonical contract:`0x7045b893E15B699e04494aA3849730bC6Aa1C864`;Stable Studionet61999;RPC https://studio.genlayer.com/api;protocolEIM-V1-STUDIO/schemaEIM-CANDIDATE-V1/consensusACR-001-SAFETY-1.
Deployment source commit:`4874fd469cb5477b9d8f8ec9dbc19252a6112e6e` (local,bundle recoverable;remotecommit link not verified),fileSHA256 `121deb7f9a2a0ae4c7704e96d74b3678054ccd2dbed77ff7e3373fa75749c095`. Documentation/publication commit will be recorded separately.
Deployment tx:[0x2486995a27e99c7d3bd1da857e9af39b330eb2092f066edb780aa44caacd3007](https://explorer-studio.genlayer.com/tx/0x2486995a27e99c7d3bd1da857e9af39b330eb2092f066edb780aa44caacd3007),FINALIZED/SUCCESS/MAJORITY_AGREE.

## Verified NEW / transactions / consensus evidence

Controlled NEW:[0xec875a1a5de724b7fd6a407e851ba736393ae508f330c1b94059c9f72191d7f4](https://explorer-studio.genlayer.com/tx/0xec875a1a5de724b7fd6a407e851ba736393ae508f330c1b94059c9f72191d7f4);request`68b9090d638738bd0236b084aff95ae7551d8df11da9b282aaa536ecd448258f`. ActualPARTIAL1D/2I/3U,[A,C],size2;1round/0rotation/4distinctsuccessfulparticipants. SYNTHETIC DEMO not real municipal observation.
Public-document NEW:[0x77ddb362ff4fa11dc9a827de14f143da266c3c9c82d018950c9fc9376b45f4bb](https://explorer-studio.genlayer.com/tx/0x77ddb362ff4fa11dc9a827de14f143da266c3c9c82d018950c9fc9376b45f4bb);request`5c8aae111e19f6b193d5a8b4b8dce4697f424166922cd2116b49343b620c7b46`. FixedERC-20/IERC20 material;actualDEPENDENT/COMPLETE,3successfulparticipants.
REUSED:[0x8c0ea62020311b5718fe53bab1f3f4bad3aeca2ab2429e5eb719683c939ef9f8](https://explorer-studio.genlayer.com/tx/0x8c0ea62020311b5718fe53bab1f3f4bad3aeca2ab2429e5eb719683c939ef9f8);samecontrolledrecord unchanged,3successfulparticipants.
See ONCHAIN_EVIDENCE.md and EVIDENCE_INDEX.md for rawreceipts/analyses/finalizedreadbacks. Actual counts exclude idle/error and duplicateleader entries. No privatecandidate/operator/model-diversity inference.

## How to verify / tests / reviewer path

OpenREADME→source→customLeader/Validator→ONCHAIN_EVIDENCE→canonicalStudio get_protocol_info/get_assessment existingrequest. No EchoMap/walletwrite required.277localcases PASS with scriptedexternalboundaries;3Nodevectors PASS. Exactlocks/commands inREADME. Realnetwork positiveexamples proved;negativecontrols NOT REAL-NETWORK VERIFIED.

## Known limitations

Visibleclaims do not authenticate ultimateprovenance. Nondeterministicsemantics/consensus canfail;laterrealdisagreement is preserved. OnlyboundedGitHubtext sources/testnet. No universalaccuracy/trustlessness/all-provider-independence promise. SeeKNOWN_LIMITATIONS.md/SECURITY_AND_TRUST_MODEL.md. Final public-source audit remains BLOCKED until publication succeeds.
