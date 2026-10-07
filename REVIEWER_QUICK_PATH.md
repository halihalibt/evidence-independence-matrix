# Reviewer quick path — Intelligent Contract

1. Read README's primitive and Why GenLayer sections (30seconds).
2. Inspect contracts/evidence_independence_matrix.py:classify_snapshot,validation_prompt,validate_snapshot_candidate,custom run_nondet_unsafe and assess atomic save. Leader classification and independent evidence-bound Validator are distinct responsibilities.
3. Open ONCHAIN_EVIDENCE.md for canonical deployed address, real controlled/public NEW, participant receipts and finalized records (60seconds).
4. In Stable Studio, select that contract and view get_protocol_info(); then get_assessment with the existing controlled request from the index. These are reads, no wallet write required. Do not deploy or create another assessment merely to review.
5. Inspect277 local tests evidence/security model and known limitations. Optional local suite is documented in README; no EchoMap install required.

The deployment-source commit is preserved by the source bundle. Full source/evidence are public at publication checkpoint `a54a4fde7a6d601de0ef470687e1104e0eb989cc`. This is separate from the deployed source commit.
