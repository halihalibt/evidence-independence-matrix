# Fixtures — independent Repository A assets

All expected relationships are local test oracles, not GenLayer decisions.
No fixture is a real deployed Assessment. Tests never fetch these URLs live.

## Controlled SYNTHETIC DEMO

`synthetic/v1/a.txt` is the fictional first-hand municipal measurement;
`b.txt` explicitly derives its claim from A; `c.txt` provides a separate
first-hand instrument reading; `d.txt` has unclear origin. Every document starts
with SYNTHETIC DEMO. Claim and expected matrix are frozen in `synthetic/manifest.json`.
The illustrative host is NOT PUBLISHED. In authorized PHASE 4 publish the short
fixed-version `.txt` assets once, bind verified allowed URLs, normalize/sort them
and map A/B/C/D labels to those indices; do not assume input label order.
Keep published versions immutable. No second contract or frontend is needed.

| Pair | Local expected relation | Visible origin rationale |
|---|---|---|
| A–B | DEPENDENT | B expressly uses A's sensor log |
| A–C | INDEPENDENT | C acquired its own separate field reading |
| A–D | UNKNOWN | D gives no acquisition or citation path |
| B–C | INDEPENDENT | B uses A, C uses its own measurement |
| B–D | UNKNOWN | D gives no origin |
| C–D | UNKNOWN | D gives no origin |

Expected D/I/U counts 1/2/3, PARTIAL, maximum supported pairwise independent
set [A,C], size 2. With illustrative sorted URLs its indices are [0,2]. This does
not prove real measurements, independent websites or ultimate evidence families.

## Real public documents

`public-documents/manifest.json` records exact URL, official ref commit, successful
HTTP headers, retained raw body SHA-256 and analyzed-text digest. ERC-20 uses the
verified full commit; IERC20 retains frozen v5.4.0. The latter declares the ERC-20
standard interface as defined in the ERC. The expected DEPENDENT relation concerns the
standard's normative balanceOf interface, not independent software authorship.
This is rationale only. Real Studionet assessment has NOT_RUN. Preserve actual
network output even if it differs; investigate under frozen rules.
The GitHub metadata API returned 403 in this runtime; official `git ls-remote`
and raw file HTTP succeeded and are the actual pinning/readability evidence.
The fetched source files retain their upstream licensing headers.

## Security and errors

`injection/source.txt` is deliberately hostile **untrusted data**. The local
mock tests prove fixed-template binding, strict schema and caller-only URLs,
not immunity of an actual LLM. No attack URL is fetched.
`errors/cases.json` names readable-status cases and execution-failure cases;
UNAVAILABLE/UNSUPPORTED are observations, while temporary web failures, model
failures and invalid model output abort without an Assessment.
The 3 malformed-candidate fixtures exercise completeness and ordering rather
than inventing pair indices in model output (the model returns only two arrays).
