# EIM-V1-STUDIO — implementation protocol binding

The approved `ARCHITECTURE_FREEZE_V1.md` is the normative source. SHA-256:
`c2c8de7785c528b24eea126d58a74576d7e39746021560b448cfd358c65a2687`.
The repository preserves that source unchanged. Approved ACR-001 overrides only
Validator reclassification/equality requirements; see ARCHITECTURE_CHANGE_REQUEST_001.md.

## Deterministic inputs and identifiers

`client_key` is 1–64 ASCII letters, digits, `_` or `-`, with no trimming/casefold.
Claim is 1–600 normalized Unicode code points; required context is 0–400.
Text normalization converts CRLF/CR to LF, removes the opening BOM and strips
whole-text surrounding whitespace. Internal whitespace, case, punctuation and
language remain unchanged. Python Unicode `str.strip()` defines surrounding
whitespace; the finite Node vector check spells out the same whitespace set.
Lone surrogate text cannot encode as UTF-8 and is rejected, not replaced.

URLs are a list of 2–4 ASCII HTTPS strings, maximum normalized size 512 UTF-8
bytes each. Scheme/host lowercase; default port 443 omitted; empty path `/`;
path case and escape spelling preserved. Duplicate normalized URLs are errors;
full normalized strings sort in ASCII order. Forbidden: credentials, non-443
ports, query/fragment (including empty delimiters), backslash, controls, IP
literals, dot path segments (including `%2e` spellings). Permitted host is exactly
`raw.githubusercontent.com` or one legal ASCII GitHub owner label (1–39 characters,
alphanumeric with single internal hyphens) followed by `.github.io`. Permitted
literal path suffixes are `.txt`, `.md`, `.adoc`, `.sol`.

Creator is an actual write sender, lowercased 20-byte hex address. Canonical JSON
has UTF-8 Unicode strings, normal JSON escaping, no extra spaces, array ordering:

- request ID: SHA-256 of `["EIM-V1-STUDIO", creator, client_key]`.
- payload digest: SHA-256 of `["EIM-V1-STUDIO", claim, context, sorted_urls]`.

Both are 64 lowercase hex characters without `0x`. `payload_digest` is a helper
for already normalized inputs; public write always validates/normalizes first.
Static vectors preserve exact canonical byte strings and independently computed
Node SHA-256 expectations, checked by Python and Node.

## Records and storage

Memory dataclasses have exactly the fields in Freeze A4. The **only** persistent
field is `assessments: TreeMap[str, str]`. Its value encodes complete Assessment
JSON; public views decode it and retain all fields and null values. This is the
spec's permitted equivalent storage encoding, not a second state structure.
Assessment records are immutable; no pending state, counters, admin map or index.

SourceObservation fields: `index,url,read_status,content_digest,relevance`.
PairDecision fields: `i,j,relation`. Assessment fields: `protocol_version,request_id,
creator,client_key,payload_digest,claim,context,urls,sources,pairs,result_status,
max_supported_independent_set,max_supported_independent_set_size,
dependent_pair_count,independent_pair_count,unknown_pair_count`.

Frozen enums are READABLE/UNAVAILABLE/UNSUPPORTED;
RELEVANT/NOT_RELEVANT/UNCERTAIN/NOT_APPLICABLE;
INDEPENDENT/DEPENDENT/UNKNOWN; COMPLETE/PARTIAL; NEW/REUSED.
No SELF, confidence, explanations, timestamps, transaction hashes or participant
counts are stored. Body limit 32768 bytes; analyzed text limit 8000 code points;
native GET enforcement is implemented.

## Strict candidate boundary

Raw model JSON has exactly `relevance` and `relations` arrays. Strict parser
rejects duplicate keys (also nested), non-JSON constants, code fences, extra
content, missing/extra keys and wrong types. It does not clean malformed output.
Code binds indices, URLs, read statuses and digests; model cannot write them.
Candidate has exactly `schema_version=EIM-CANDIDATE-V1,sources,pairs`.
Sources have length n with fixed index/URL order; pairs have length n(n−1)/2
and contain every i<j once in lexicographic order. Boolean/float indices fail.
READABLE requires a 64 lowercase hex digest and relevance other than
NOT_APPLICABLE; non-readable requires null digest and NOT_APPLICABLE.
A pair touching a non-READABLE or non-RELEVANT source must be UNKNOWN; violations
reject the whole candidate and are never repaired.

## Derived results and idempotency

Counts come from all pairs. Any UNKNOWN gives PARTIAL, otherwise COMPLETE;
COMPLETE does not mean the claim is true. Eligible sources are READABLE+RELEVANT.
Enumerate at most 16 subsets; every pair in a selected subset must be INDEPENDENT.
Select maximum size, then minimum lexicographic ascending index list. No eligible
source gives []/0; eligible nodes without I edges give the earliest singleton/1.
DEPENDENT is non-transitive; UNKNOWN is never assumed INDEPENDENT. Assessment
validation recomputes all derived fields and identity/payload bindings.

Same creator/key and payload gives immediate REUSED; changed payload gives
IDEMPOTENCY_CONFLICT. Different creators have separate namespaces; a new key
permits a new observation, including after PARTIAL. Pure preflight is tested
using manually constructed existing records. Phase 2 also tests full mocked
NEW/REUSED paths; real finalized NEW/REUSED evidence is indexed in ../ONCHAIN_EVIDENCE.md.

Write order is normalize → IDs → existing record/preflight → immutable memory
snapshot → custom consensus → candidate validation/derivation → complete
Assessment validation → one mapping assignment. Phase 2 replaces the Phase 1
interface stop with the formal custom callback path. Structural and focused
harness tests check no write inside callbacks, errors/disagreement leave no
record, and REUSED/conflict never fetch, invoke a model or enter consensus.
Real canonical consensus and failure no-write observations are indexed in ../ONCHAIN_EVIDENCE.md; local fault-injection proofs remain harness-scoped.

Normalization is performed exactly once. An input with whitespace before a BOM
may legally retain that BOM after frozen normalization; stored-text validation
checks that result without consuming it again. Source digest hashes exactly the
normalized text used in the current participant's prompt. Hash vectors/rules
are unchanged.

## Business methods and errors

`assess(client_key,claim,context,urls)` write, any sender; result fields
`request_id,disposition,result_status`. `get_assessment(request_id)` public view,
invalid hex gives INVALID_INPUT; valid absent ID gives found=false.
`lookup_request(creator,client_key)` public view, returns ID/found and existing
payload_digest/result_status. `get_protocol_info()` public view returns protocol
and candidate schema, relation-rule identifier **EIM-V1-STUDIO**, limits/source rules.
Business protocol identifier and IDs remain unchanged by user instruction.
Consensus revision ACR-001 is explicitly documented separately and bound to source/address;
superseded diagnostic deployments and the final canonical instance are not interchangeable.

Errors retain the frozen taxonomy: INVALID_INPUT, UNSUPPORTED_URL,
DUPLICATE_URL, IDEMPOTENCY_CONFLICT, INVALID_MODEL_OUTPUT,
SOURCE_TEMPORARILY_UNAVAILABLE and MODEL_EXECUTION_FAILED. Runtime failures
never become UNKNOWN success. Real finality/participants for canonical examples are indexed in ../ONCHAIN_EVIDENCE.md; private Validator internals remain unexposed.

## Phase 2 custom consensus binding

`gl.vm.run_nondet_unsafe(leader,validator)` is the only consensus path.
Both callbacks capture only `(claim,context,tuple(urls))`; no persistent object,
state or Leader answer is captured by classification. Leader executes
`classify_snapshot`. Under approved ACR-001, Validator accepts only the SDK's
success `Return` wrapper, validates the Leader schema, independently refetches,
normalizes and hashes every source. URL/index/order/read_status/content_digest
remain strictly bound. One raw-text prompt independently validates every proposed
relevance/pair against unchanged definitions; strict boolean arrays must all be true.
No regenerated-candidate token comparison or Leader reasoning. Any mismatch,
unsupported field or Validator operational/parsing exception returns false.
No convenience equivalence wrapper, error-text equivalence, merge or override.

Each participant uses native `gl.nondet.web.get` with no credentials/headers,
in fixed URL order. 429/5xx/408/425 and HTTP operational exceptions abort the
candidate as temporary failure. Confirmed non-temporary 4xx (including
404/410/401/403) and 204 no-content are UNAVAILABLE; surfaced redirects or
partial/other non-200 responses are UNSUPPORTED, with no manual follow-up GET.
The API exposes status/headers/body, not final URL: internal redirect provenance
is not observable or guaranteed. A surfaced redirect is refused conservatively.

For 200, check raw body bytes before normalization, strict UTF-8, 8000-code-point
limit; observable MIME must be public text (excluding HTML/JS/CSS), and obvious
HTML/login/error envelopes are rejected. Missing MIME relies on UTF-8 and obvious
page-envelope checks. These checks cannot authenticate publishers or reliably
identify every disguised error/HTML fragment. No truncation, recursive fetch,
JS rendering, decompression framework, cache or retries is added.

Use the exact fixed template via one-pass placeholder substitution of canonical
JSON. Claim/context/source content are data; placeholders inside data are never
expanded a second time. Raw `exec_prompt(response_format='text')` is strictly
parsed; provider/empty/non-text response is MODEL_EXECUTION_FAILED, malformed
JSON or candidate is INVALID_MODEL_OUTPUT. If all sources are non-readable,
construct the frozen NA/UNKNOWN candidate directly without a model call.
A source instruction never selects URLs, changes enums, adds output fields or
changes the code-controlled metadata.

Mock prompt-injection tests protect structured boundary/parser/protocol rules;
they do not establish immunity of a real model. All actual model judgment,
network rounds/threshold/participants and finalized result proofs are deferred.

## Current verification boundary

The final production source hash and deployment-source commit are documented in ../DEPLOYMENT_MANIFEST_STUDIONET.md. Approved ACR-001 and its evidence-anchor safety tightening changed Validator validation, not the original Leader definitions, state or methods.277 local tests passed with scripted external boundaries; tests inject faults only in the harness. No production debug method/mock path was added.

Canonical deployment, synthetic/public-document NEW, REUSED and finalized reads have real Stable Studionet evidence. The successful controlled matrix is an actual stored result, distinct from a local fixture expectation. Other real requests have disagreed and stored no Assessment. Finite positive examples do not prove universal semantic correctness or liveness. Real-model negative controls remain NOT REAL-NETWORK VERIFIED. The original Phase3/4 history remains preserved separately.
