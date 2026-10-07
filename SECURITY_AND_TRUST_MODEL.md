# Security and trust model

The approved Freeze plus ACR-001 and its safety tightening govern the unchanged implementation.

Leader fetches every allowed URL, normalizes and hashes the exact analyzed text, classifies relevance/all pairs once, then strictly parses and validates a canonical candidate. The custom run_nondet_unsafe Validator independently fetches/normalizes/hashes those sources; read_status, digest, schema, index, URL and ordering must match exactly. It verifies each proposed relevance and pair label under the same evidence rules. It receives labels, not Leader reasoning, and does not regenerate an identical matrix.

Positive DEPENDENT/INDEPENDENT acceptance requires two internal short verbatim evidence anchors from the applicable source pair, with protocol fact types and exact substring checks. Semantic rule support is still a model judgment; literal anchors alone are insufficient. Unsupported labels, malformed/duplicate-key JSON, missing entries, digest differences and Validator failures reject agreement. No format-only/overall-reasonableness score, label repair, merge, confidence override or convenience equivalence wrapper exists. Anchors are not stored in Assessment or exposed as a new API.

Claim/context/source text/proposed labels are structured untrusted data. Embedded instructions or extra URLs have no protocol authority. Models receive bounded text and cannot initiate additional source fetching. Observable unsupported formats are rejected.429/5xx/timeout/DNS/model failure abort rather than create UNKNOWN. Native HTTP internally followed redirects are not fully observable; surfaced redirects are refused and hidden redirect provenance is not guaranteed.

Any sender may assess; creator derives from actual message sender. Repeated creator/key/payload returns REUSED before fetch/model/consensus; conflicting payload fails before nondeterministic work. All candidate validation/post-processing precedes the sole persistent write. No admin result override, pending business record, backend or second business contract exists.

## Verification boundary

LOCAL/MOCK:277 contract cases protect parser, anchors, negative candidates, digest mismatch, invariants, idempotency and atomic ordering. REAL STUDIONET:canonical deployment, controlled/public-document NEW, REUSED and finalized reads. REAL WALLET:EchoMap's separate successful frontend transaction. Real negative semantic-model controls remain NOT REAL-NETWORK VERIFIED. See [known limitations](KNOWN_LIMITATIONS.md) and [evidence index](EVIDENCE_INDEX.md).
