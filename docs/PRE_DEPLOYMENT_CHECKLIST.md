> **ACR-001 CURRENT OVERRIDE:** old address is SUPERSEDED PHASE-4 DIAGNOSTIC DEPLOYMENT. New implementation local Gate BLOCKED; do not deploy/resubmit. Historical procedure/evidence below is retained, not current approval to use old consensus. See canonical.json and docs/ARCHITECTURE_CHANGE_REQUEST_001.md.

# PRE_DEPLOYMENT_CHECKLIST — PHASE 3

Gate: **PASS_LOCAL_PRE_DEPLOYMENT**. This is permission-ready evidence, not deployment authorization or real network consensus proof. PHASE 4 requires the user's separate approval.

| Item | Actual status / evidence |
|---|---|
| Contract source ready | PASS_LOCAL; one self-contained business contract; unchanged from approved PHASE 2 |
| Source SHA-256 | `b3cf82eb14a7d23d1c8c2059d6fbc57489c6d526cfc654cff9426530f07319a7` |
| Source commit / remote | NOT_CREATED; source commit before canonical deployment is PENDING PHASE 4 |
| Protocol / candidate schema | `EIM-V1-STUDIO` / `EIM-CANDIDATE-V1` |
| Architecture Freeze | Unchanged SHA `c2c8de7785c528b24eea126d58a74576d7e39746021560b448cfd358c65a2687` |
| Node / npm / Python / pip | Locked 24.19.0 / 11.9.0 / 3.12.14 / 25.0.1; Python/Node restored on matching runtime; exact requirements lock installed |
| JS SDK / CLI | Approved SDK 1.1.8 / CLI 0.39.2; no JS business code or chain calls in this phase |
| Test runner / client / pytest | genlayer-test 0.29.2 / genlayer-py 0.16.3 / pytest 9.1.1; pip check clean |
| GenVM / Depends | v0.2.16; `py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6` |
| Transitive std / cloudpickle | `py-lib-genlayer-std:11rhn002yfajawsz7fai6mykznbxkxs6l91iskj5cm82c92qhy3v`; `py-lib-cloudpickle:1dlk6mnfabi0z7r39635amyfzw8xb6rm8bv4pmgv6ji1bfx9hghd` |
| CPython runner | `cpython:1bk9g3zgym0rrpd9lk584cxfaa4rg0cz36w6xhzkqdj1m2p4xa9n` |
| Universal archive | Exact approved artifact downloaded; SHA `4f0b358ec98ec148be9b95cdfb0f0e1a6cbe64da0194fdfac3fffc6f5d1d93e2` verified |
| Tests | 211 PASS / 0 failure / 0 error / 0 skip; original94 + original74 + new43; all original node IDs retained |
| Synthetic fixture | Four labeled SYNTHETIC DEMO bodies; expected D/I/U=1/2/3, PARTIAL, [A,C], size2; URLs illustrative NOT_PUBLISHED |
| Real public fixtures | Exact ERC commit + IERC20 v5.4.0, HTTP200, allowed URLs, strict UTF8, <=32768 bytes / <=8000 normalized codepoints |
| ERC-20 size | 5601 raw bytes; 5600 normalized codepoints |
| IERC20 size | 2781 raw bytes; 2780 normalized codepoints |
| Injection / errors | Local structured-data and caller-URL boundary checks pass; taxonomy and no-write failure checks pass |
| Canonical prompt | CLASSIFICATION_PROMPT_V1 exact approved body; SHA `20b9a852c72ec4c240e52fc1db2afd78bca439f365b52465643047bc770d2ce1` |
| Public methods | Exactly assess(write), get_assessment(view), lookup_request(view), get_protocol_info(view); schema unchanged; no admin/debug public method |
| Deterministic core | Inputs/normalization/hash vectors/strict candidate/derived counts/MIS/non-transitivity/tie-break regressions pass |
| Validator / digest | Own fetch + complete own model call; wrong valid Leader answer and same enums/different digest reject in mock executor |
| Atomicity / idempotency | Seven fault locations leave no new record and preserve old record; reused/conflict bypass nondet, PARTIAL/new key/creator namespace tested |
| Standalone readiness | README, protocol, contract, tests, fixtures, input examples, environment lock and Studio procedure present; no EchoMap dependency |
| Expected network | Stable Studionet ONLY / Chain ID61999; https://studio.genlayer.com/api |
| Studio / Explorer | https://studio.genlayer.com / https://explorer-studio.genlayer.com |
| Fee strategy | Approved Stable legacy addTransaction + eth_estimateGas / eth_gasPrice / nonce / signed legacy submission; no sim_getFeeConfig or RC fee fields |
| Fee measurement boundary | PHASE0 empty-data estimate500000 / observed gasPrice0 was capability evidence only; real deployment/assessment cost and business profile NOT_RUN |
| Faucet readiness | PHASE0 observed sim_fundAccount then eth_getBalance confirmed diagnostic account0→1GEN; no new claim/credit/consumption in PHASE3; deployer funding PENDING PHASE4 |
| ACR / complexity | NONE / no HIGH; no new dependency, business feature, second contract or backend |

## Still-unverified real network facts — PENDING PHASE 4

- Canonical contract address / deployment transaction / actual source commit.
- Real public synthetic URL availability and immutable publishing binding.
- Native GenVM execution, HTTP/model/provider behavior, real semantic classification and real prompt-attack behavior.
- Native storage atomicity and actual consensus rejection/participant evidence; target5, minimum3 including Leader.
- Real verified request IDs, NEW assessment transactions, execution success, FINALIZED and matching LATEST_FINAL get_assessment.
- Real reuse transaction proof, deployment-account balance and actual business gas/resource expense.

No addresses/hashes/participant counts or chain results are invented. The suite mocks external boundaries; official Python SDK serialization/storage logic is exercised locally. Common-model bias, hidden origins and forged source claims remain frozen limitations. HTTP API does not expose final redirect URL and buffers before application-size checks; obvious HTML/error detection cannot identify every disguise.

Reviewer: `README.md` → `docs/protocol.md` → `fixtures/README.md` → `evidence/phase3-all-tests.xml` / `phase3-test-summary.json` → `docs/STUDIO_DEPLOYMENT.md`.
