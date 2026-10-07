> **ACR-001 CURRENT OVERRIDE:** old address is SUPERSEDED PHASE-4 DIAGNOSTIC DEPLOYMENT. New implementation local Gate BLOCKED; do not deploy/resubmit. Historical procedure/evidence below is retained, not current approval to use old consensus. See canonical.json and docs/ARCHITECTURE_CHANGE_REQUEST_001.md.

# Standalone Stable Studio procedure — PHASE 4 partial checkpoint

PHASE 4 is authorized and one canonical deployment has succeeded. See
`deployment/canonical.json` and the PHASE4 evidence. Resume that contract; do not
repeat deployment when restoring this checkpoint. Assessment verification is
blocked on controlled assessment consensus failure. Public fixtures are published and verified. The numbered steps below were prepared
in PHASE 3 and serve as the verification procedure.
Use this repository alone; EchoMap and any backend are unnecessary.

1. Confirm the passed pre-deployment checklist and exact source commit; the local
   source commit is recorded in the canonical manifest; the Public remote contains README and fixtures only; deployed source commit
   remains local/bundled and separate from publishing commit. Preserve the source SHA
   and the first two lines (`v0.2.16` / locked py-genlayer Depends).
2. Open the approved https://studio.genlayer.com Stable application. Confirm chain
   61999 and canonical https://studio.genlayer.com/api; use approved RPC/SDK paths,
   not Studio-dev, Bradbury or a different network.
3. Prepare the actual deployment account securely. Free funding uses Studio
   account menu → Fund account; the observed supported RPC is sim_fundAccount
   followed by eth_getBalance. Earlier PHASE 0 funding was only a diagnostic
   account and does not prove the deployer's current balance. Never place keys
   in this repository or evidence. No resource purchase is permitted.
4. Load the single contracts/evidence_independence_matrix.py source in Studio,
   select its one contract and empty constructor. Use the locked Stable legacy
   estimate/sign/submit flow: eth_estimateGas, eth_gasPrice and nonce before
   signed legacy transaction submission. The SDK 1.1.8 implementation handles
   addTransaction ABI fallback. sim_getFeeConfig is absent; do not call it or
   substitute RC fee fields. The earlier empty-data 500000 estimate is not a
   business workload profile, and earlier gasPrice 0 is not a live guarantee.
5. Capture actual deploy transaction and canonical address, explorer links and
   source commit. No guessed address/hash or second business contract.
6. Read get_protocol_info; bind published immutable synthetic URLs and prepared
   fixed public-document URLs. Submit new client keys only in authorized PHASE 4.
   Target 5 and require at least 3 actual participants including Leader.
7. For each NEW assessment require FINALIZED + execution success + matching
   get_assessment on TransactionHashVariant.LATEST_FINAL. Record available real
   participant evidence; callback counts in tests do not satisfy this condition.
8. Preserve on-chain results. A mismatch with local semantic expectations is
   investigated, never edited or hidden by hardcoding. Archive results, input
   bindings/digests, transaction/explorer links and standalone reviewer steps.

Canonical address, deployment transaction/source commit and deployment
finality/source/protocol reads are verified in the canonical manifest. Real
controlled assess was submitted once and reached FINALIZED/MAJORITY_DISAGREE;
latest-final get_assessment/lookup found=false. Its receipt NEW/PARTIAL is a rejected
proposal, not a successful record. Real public-document NEW/REUSED await a
successful controlled record under original PHASE4 authorization. Keep Gate BLOCKED.
