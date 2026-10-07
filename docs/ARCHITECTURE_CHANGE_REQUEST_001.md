# ARCHITECTURE CHANGE REQUEST — ACR-001

Status: **APPROVED BY USER** for implementation, gated redeployment and one initial controlled assessment. Phase 5 remains unauthorized. Authority: user's explicit ACR-001 instruction in this conversation. This addendum overrides only the affected Validator execution/equivalence requirements; the original Freeze and Leader prompt are preserved byte-for-byte.

## Original Decision

Validator independently fetches all sources, normalizes and hashes them, classifies a full candidate, and requires exact equality of relevance and pair enums with the Leader's independently generated candidate. Any material mismatch rejects the entire result.

## Studionet Evidence

Stable Studionet 61999, old contract `0x6DbdE095C83a68B7932f7dE80Ba0642043F5Ce03`. Transaction `0x040d64c7d795f5562532c292c55318a13fc6bee15d1653b37b98d9db2cd0e3d9` finalized MAJORITY_DISAGREE after four rounds/three rotations; finalized assessment and lookup absent. Approved Phase4A found stable bytes/text/digests across 20 reads, B–C labels I/U/D, D relevance R/NR, and one invalid-JSON classification. Phase4B did not expose historical Validators' private candidates: these facts demonstrate liveness failure/semantic variance but do not prove the exact cause of every historical vote. Historical root classification G remains preserved.

## New Decision — Evidence-Bound Candidate Validation

Leader unchanged. Validator refetches every frozen URL itself, independently normalizes/hashes, and strictly validates full Leader schema, indexes, URLs, ordering, read_status and digests. Any mismatch rejects before semantic validation. It then independently evaluates every proposed relevance and pair label against the original definitions using its own evidence and claim/context. Only canonical labels are supplied, never Leader reasoning. A single raw-text model call returns two ordered boolean validation arrays; strict JSON parser requires exact keys, lengths and actual booleans. All field validations must be true. There is no overall score, repair, merge or new candidate.

DEPENDENT requires positive claim-relevant shared/derived-origin evidence. INDEPENDENT requires both relevant readable materials, positive distinguishable acquisition paths and no visible claim-related common/derived origin. UNKNOWN requires insufficient evidence for either positive standard or insufficient provenance/relevance, not execution failure. Relevance follows frozen R/NR/U definitions; alternative first-choice tokens alone are not a reason to reject a supported label.

## Preserved Guarantees

All enums, input limits, normalization, candidate/Assessment/storage schemas, four public methods, identifiers, idempotency, single atomic save, error taxonomy, no failure-to-UNKNOWN, non-transitivity, maximum pairwise set, Leader classification prompt, external scope, Stable-only/61999, free Faucet funding, Repository A/B boundary. Custom run_nondet_unsafe remains the sole consensus mechanism. No convenience equivalence wrappers, tolerance, per-cell consensus or retries. Digest/schema/failure checks remain deterministic and strict.

## Changed Guarantees

Independent evidence acquisition and semantic judgment remain; independent generation of a second complete semantic candidate and exact equality of its semantic tokens are deliberately removed. Consensus now attests rule support of every Leader-proposed label. Conditioning on labels introduces anchoring risk; validation prompt treats proposed labels as untrusted hypotheses, requires positive standards and excludes reasoning. This is a substantive approved consensus change, not a syntax adapter or guarantee of model immunity.

## Affected Freeze Sections

F07: material fields retained but semantic fields validated rather than compared to regenerated enums. F08 and A8/A9/A11/A12: independent full reclassification/equality replaced by independent evidence-bound field validation. A16/F18 test expectations that require identical prompts or no candidate visibility are superseded only for Validator. B9 external flow wording changes accordingly. No other section is overridden; original Freeze/handoff files remain intact, read together with this approved addendum.

## Safety Analysis

Strict deterministic evidence binding precedes AI. Wrong supported-edge flips, obvious relevance flips, digest corruption, missing pair, illegal enum and injection are negative controls. Parser requires duplicate-key rejection, no silent correction, actual boolean types. Any model/HTTP/parsing failure makes Validator disagree; Leader failure still aborts without write. No snapshots store evidence text or private model reasoning. A valid UNKNOWN is accepted only when the rules permit it, never as a fallback. Shared model biases remain possible and are not eliminated by this change.

## Liveness Analysis

Different independent first-choice tokens need not reject a rule-supported proposal. Repeated frozen-candidate validation must be stable before redeployment; mocked acceptance alone does not prove live semantic stability. No promise of eventual agreement or fixed output. Local Gate failure/uncertain necessary evidence stops execution; one failed controlled real consensus stops further business submissions.

## Migration Impact / Old Contract Status

Old contract is **SUPERSEDED PHASE-4 DIAGNOSTIC DEPLOYMENT**. Keep original source commit, bundle, receipts, rejected candidates and no-write evidence. No state migration or upgrade transaction. New address is canonical only after successful authorized deployment and source/finality checks; existing old records are not fabricated or altered. Never call B or old/new deployment duplicates two active business contracts.

## Version Decision

Keep user-preserved `EIM-V1-STUDIO` and `EIM-CANDIDATE-V1` plus their existing ID algorithms; public interface remains unchanged. Bind the changed consensus explicitly by `consensus_revision: ACR-001` in deployment/control documentation and distinct source commit/address. This revision is not a public schema field. **Minimal version proposal, if a protocol-version bump is required: EIM-V1.1-STUDIO. NOT APPLIED; would require user approval because version participates in request_id/payload_digest and changes vectors.** No silent bump or mixed old/new address configuration.

## Test Gate

Preserve immutable approved baseline source/tests and rerun all original 211 tests first. Retain all test cases in the current suite, explicitly adapt only assertions/mocks superseded by ACR-001 and source-integrity pin. All unchanged invariants must pass. Add focused positive repeated validation, each-field negatives, strict validation-output parser, unavailable/no-readable, independent fetch, no-write, serialization and injection controls. Obtain bounded independent live-model validation through a nonpersistent official harness if available; do not count mocks as this evidence. Gate passes only if required repeated positives and negatives are stable, digest/schema/failure semantics intact and no HIGH complexity.

## Deployment Requirement / Budget

Only after local Gate PASS: one new source commit, one authorized Stable61999 deployment funded solely by Faucet GEN; require FINALIZED/execution SUCCESS/exact source. Then exactly one controlled NEW assessment with original pinned sources/claim/context. Stop immediately if rejected or otherwise required success missing. Only controlled success permits public-document NEW, REUSED and lookup verification. Do not enter Phase5. Complexity LOW-MEDIUM; one validation prompt/parser and thin test boundary, no new package/backend/service.

## Current Status

Original baseline regression: **211 passed**. Current implementation/mocked regression: **251 passed** (247 plus four explicit negative controls added before the quota interruption). Real-model predeployment Gate: **BLOCKED / REAL_MODEL_PREDEPLOY_GATE_UNAVAILABLE_FOR_VERIFIED_STABLE_PATHS**. Three total simulation attempts: original no-time -32603; UTC/existing-contract storage-forbidden before model; UTC/previous empty test-account Contract-not-found. No positive/negative actual model verdict obtained. No retry of identical failed calls. Redeployment/controlled NEW: NOT_RUN. See ACR001_REAL_MODEL_GATE.md; substitution by the first controlled NEW needs explicit user approval and is not implemented.


## Approved Gate-order Exception — 2026-10-07
User approved DEPLOY FIRST → ONE CONTROLLED NEW AS REAL-MODEL GATE. REAL_MODEL_PREDEPLOY_GATE_UNAVAILABLE remains a historical tooling boundary, not ACR failure. No more predeploy harness research. Exact current production source remains unchanged and 251 tests PASS_RETAINED. One new formal source commit/deployment, one controlled NEW with new client_key and unchanged pinned inputs; any failed Gate stops. Controlled success alone then permits minimum public-document NEW, one REUSED and lookup reads, never Phase5. Live semantic negative safety remains NOT VERIFIED.

Protocol version retained as EIM-V1-STUDIO: it identifies unchanged business rules/schema/hash format. Deployment consensus identity explicitly uses consensus_revision ACR-001 + immutable source commit/SHA + new address. This is the current user's expressly permitted no-version-bump option with explanation; no public schema or ID preimage changes. New and old consensus must never be described as interchangeable.


## Runtime Outcome — Approved Gate-order Exception
New canonical 0xbA3F0E8E45caF7665F0532313021Bb1B93b3c6eC, source commit f80ac8d3e50691e9b0e98d748dbb8da38acb8026. Approved runtime Gate PASS: controlled FINALIZED/SUCCESS/MAJORITY_AGREE,5actual identities, matching latest-final stored record. Public-document NEW/REUSED/lookup passed minimum network checks. Controlled B-C differs from frozen INDEPENDENT expectation: actual DEPENDENT. Overall Phase4 requires semantic expectation review; live negative safety unverified. No additional ACR or automatic Phase5.
