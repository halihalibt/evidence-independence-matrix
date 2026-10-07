# ENVIRONMENT_LOCK — EIM / EchoMap — PHASE0 COMPLETE

Updated UTC: 2026-10-06T17:51:30.984813+00:00
Updated Asia/Shanghai: 2026-10-07T01:51:30.984813+08:00

**PHASE0 Gate: PASS — environment/API/toolchain binding only. PHASE1 authorization: NOT_GRANTED. STOP.**

## Authority and evidence boundaries

Architecture Freeze unchanged,58,042bytes, SHA256 `c2c8de7785c528b24eea126d58a74576d7e39746021560b448cfd358c65a2687`. Protocol EIM-V1-STUDIO; candidate EIM-CANDIDATE-V1. F01–F20 and A/B/C/D/E remain authoritative. No ACR, no semantic change, no business implementation/repository/deployment/assess. Current file replaces prior BLOCKED snapshots; historical documents preserved under phase-0-gates/before_completion_* and phase-0-recovery/before_recovery_*.

PASS certifies a reproducible compatible API/dependency/test path and free funding entry; it does not certify EIM behavior, real consensus or future release behavior. Hosted internal server commit/native executor build is not exposed by obtained evidence and remains UNVERIFIED; it is not guessed from a template header or reference tag. The contract API is locked by the **actual Stable template content-addressed Depends** and its verified official release artifacts. GenVM v0.2.16 below is the exact adopted release artifact for that dependency/testing combination, not a claim to have queried a private hosted binary version.

## Stable network — retained facts, no repeated connectivity investigation

Network StableStudionet only; Chain61999/0xf22f already live-confirmed. RPC https://studio.genlayer.com/api ; Studio https://studio.genlayer.com/ ; canonical Explorer https://explorer-studio.genlayer.com . No network switch, RC stack, proxy, paidRPC, APIpurchase. Explorer transaction pages for EIM have not been verified because EIM is not deployed.

Existing working paths curl/Nodefetch/genlayer-js/CloudBrowser retained. Pythonurllib1010 **NOT_A_BLOCKER**. CLI missing-account state is a local prerequisite, not a network failure; CLI network signing remains untested. Selected subsequent Work route: official JS SDK on original StableRPC; Studio UI is also accessible.

## Exact adopted compatibility combination

| Component | Exact lock | Evidence |
|---|---|---|
| Node/npm |24.19.0 /11.9.0|Prior actual runtime command outputs retained |
| Host Python |3.12.14|Installed isolated test environment and successful exactSDK capability imports |
| genlayer-js |1.1.8|Official non-RC artifact/provenance, officialCLI dependency, Stable deployed web submission-path match and live originalRPC reads |
| GenLayerCLI package |genlayer0.39.2|Official non-RC diagnostic install; account prerequisite not classified as network issue |
| Viem diagnostic SDK dependency |2.57.3|Full resolved npm lock retained |
| GenVM runner artifact release |v0.2.16|Official asset downloaded,216630904bytes; SHA256 matches official release metadata |
| Contract ABI header |v0.2.16|Observed actual Stable template; unchanged |
| Contract dependency |`py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6`|Exact Stable template hash exists in adopted officialarchive |
| Transitive contract standard library |`py-lib-genlayer-std:11rhn002yfajawsz7fai6mykznbxkxs6l91iskj5cm82c92qhy3v`|Actual py-genlayer runner.json Depends; extracted exact source |
| Transitive CPython runner |`cpython:1bk9g3zgym0rrpd9lk584cxfaa4rg0cz36w6xhzkqdj1m2p4xa9n`|Actual runner manifest; CPythonJSON/hashlib files inspected |
| Transitive cloudpickle runner |`py-lib-cloudpickle:1dlk6mnfabi0z7r39635amyfzw8xb6rm8bv4pmgv6ji1bfx9hghd`|Actual runner manifest; extracted vendorversion3.1.0.dev0; immutablehash, not a selected RCSDK |
| Testing package |genlayer-test0.29.2|Officialwheel/metadata and actualisolatedinstall |
| Python network client |genlayer-py0.16.3|Satisfies testpackage >=0.13.0,<0.17.0; actualinstall |
| pytest |9.1.1|Actualinstalled --version; environment-only probes, no business tests |
| Python package manager |pip25.0.1|Exact `python_toolchain_exact.txt`; pipcheck reports no broken requirements |

Full Python transitive dependency pins: `evidence/phase-0-gates/python_toolchain_exact.txt`. Full npm SDK/CLI pins: `evidence/phase-0-recovery/inspection-package-lock.json`. No floating alias is an implementation lock. Business React/TypeScript/Vite files are not created; feature/build dependencies must be exact-pinned on initial authorized frontend installation, while this locked networkSDK remains authoritative. Frozen frontend stack is unchanged.

ArchiveSHA256: `4f0b358ec98ec148be9b95cdfb0f0e1a6cbe64da0194fdfac3fffc6f5d1d93e2`. Exact inner tarSHA256s in inner_runner_sha256.json. Official asset URL/digest and release details in artifact_binding_manifest.json. Large temporary universalarchive is reproducible from immutable releaseURL+verifieddigest; extracted relevant runners/source and manifests are preserved in evidence package.

## Explicit test runner binding / custom validator verification

`genlayer-test0.29.2` accepts explicit `sdk_version='v0.2.16'` in direct_deploy/load_contract_class and `setup_sdk_paths(...,version='v0.2.16')`. Always include exact contract headerDepends. Actual isolated loader resolved both required hashes; no current-release lookup/fallback used. Do not let default loader select a cached/newer release.

Vendored cloudpickle path must resolve the exact `py-lib-cloudpickle:1dlk6mnfabi0z7r39635amyfzw8xb6rm8bv4pmgv6ji1bfx9hghd` artifact (`src/`) for serialization capability checks; don't silently use another hostcloudpickle. The official std SDK declares:

`run_nondet_unsafe(leader_fn:Callable[[],T], validator_fn:Callable[[Result],bool], /)`.

The eager decorator returns T; its lazy member supports Lazy. Validator receives Return(calldata), UserError or VMError. ExactSDK maps serializable Leader and Validator callbacks to RunNondet; false or Validator exception causes Disagree in native execution. Existing custom responsibility remains: independent fetch, full reclassification and deterministic digest/relevance/pair comparisons; convenience equivalence wrappers forbidden.

Environment probe actually passed exactSDK imports, cloudpickle Leader/Validator roundtrip, **unpatched** SDK run_nondet_unsafe roundtrip through isolated mockWASI, Direct capturedcallback agreement, wrong-result rejection and error rejection. No EIM contractclass/fixture/classification/state exists. Direct/mockWASI does not perform real network consensus; real rejection/atomicwrite/participants evidence remains PHASE3/4. No business P0 test is claimed passed.

**Testing binding detail:** built-in0.29.2 mock_llm auto-parses JSON even on text requests. For rawJSON/malformed/duplicate-key tests, stub only external model boundary using raw `{'ok':raw_text}` handler, or an equivalent raw-return external callstub; actualparser and Validator body must run. This handler route was exercised with the exactSDK text API and preserved duplicatekeys. No official package source edited; no parser cleaning or predecode substitute allowed. This is a faithful test boundary binding, not a protocol change. Direct's unsafe capture adapter does not itself prove native closure pickling; keep explicit serialization assertions where needed.

## API mappings now bound to the exact standard-library hash

| Frozen behavior | Adopted exact API / evidence |
|---|---|
| Custom Leader/Validator |gl.vm.run_nondet_unsafe as above; success only Return; independent computations unchanged |
| Public/storage boundary |gl.Contract, gl.public.view/write, exported storage types; gl.storage.copy_to_memory uses in-memory manager; persistent writes after completed nondet/validation only |
| Native HTTP GET |gl.nondet.web.get(url); response.status:int, headers:dict[str,bytes], body:bytes orNone; no status_code substitution. ExactSDK mockbytes call passed |
| HTTP/model operational errors |nondet NondetException on returnederror; malformeddata/exceptions remain error notUNKNOWN. Error taxonomy staysFrozen |
| Raw model output |gl.nondet.exec_prompt(prompt,response_format='text'); exactSDK handlerreturns raw string unchanged. Caller must enforce string type and strictparser |
| Strictduplicate keys/digest |CPython artifactJSON decoder has object_pairs_hook; hashlib source/artifact present; host3.12.14 strictduplicate reject and SHA256 vector passed. Final contract tests on actualmodel/chain deferred |
| Storage memory separation |gl.storage.copy_to_memory exactsource present; purememory inputs only. Toolcopy availability is not atomicwrite test evidence |
| Finalized snapshot |SDK1.1.8 TransactionHashVariant.LATEST_FINAL='latest-final'; previous exactsource explicitforwarding retained |
| Transaction success |FINALIZED + execution success + matching finalized assessment remains required; defaultwaitACCEPTED and defaultnonfinalread insufficient |
| GenLayer transaction ID |Use SDKreturn and preserved receipt/trace paths; currentStablelocal signing path extracts NewTransaction/CreatedTransaction ID after outerreceipt; walletStudio branch returns RPCtxID. Actual EIM validation deferred |

Platform-internal redirects remain platform responsibility, perFrozenA13; don't invent finalURL/DNS guarantees absent from API. Source status/type/UTF8/size checks remain frozen. No enum/schema/method/data expansion.

## Fee estimation / transaction submission — current Stable route locked

Do not call or assume sim_getFeeConfig. Its previously observed-32601 remains historical evidence; no repeat probe this round. Do not add v2RC distribution/feeValue/profile fields to this Stable family.

Verified deployed Stable frontend uses the same legacy deployContract/writeContract flow as lockedSDK1.1.8. Official Stable-family backend reference implements eth_estimateGas compatibility estimate and eth_gasPrice; actualStableRPC returned **0x7a120=500000 gas** and **0x0 gasprice**. Probe used emptydata, zero-value, consensus-address request solely for feeAPI capability; no model simulation or submission occurred. Referencebackend get_gas_estimate is constant500000, not measured GenVM/model workload. Do not call it a feeprofile or realistic computation measurement.

Later authorized submissions:

1. `client.deployContract` or `client.writeContract` with frozen arguments, explicit full-consensus `leaderOnly:false`, defaultinitialvalidators5 and rotations3 asSDKpreset; use unique canonical deployment only.
2. SDKencodes addTransaction(sender,recipient,initialValidators,maxRotations,txData), with its ABI compatibility fallback includingvalidUntil when needed; this5/6-input legacyABI fallback is not the Studio-dev v0.6 fee schema.
3. Estimate using `client.estimateTransactionGas({from,to:consensusMainAddress,data:encodedData,value:0n})` → RPC `eth_estimateGas` with `[{from,to,data,value:'0x0'}]`. Consensusaddress currently `0xb7278A61aa25c888815aFC32Ad3cC52fF24fE575` from exactstudionetpreset; don't replace businesscontractrecipient.
4. Read `eth_gasPrice` and `eth_getTransactionCount(address,'latest')`; SDKuses typelegacy, gas=currentestimate, gasPrice=liveresponse, nonce and chain61999.
5. Localaccount: sign then `eth_sendRawTransaction`, obtain outerreceipt and extracted GenLayertxID. Browserprovider: `eth_sendTransaction` through walletprovider. No signing/sending executed in PHASE0.
6. Preserve frozen tracking/finalizedsuccess condition. SDK's gas-estimationfallback200000 is SDKbehavior, not a successful estimate/profile. Surface estimate/transportfailure; no new product retry logic or altered finality.

Current bound Stable submission path has no required modern protocol-fee allocation fields or active feemanagermap in preset. Evidence is deployedfrontend+exactSDK+official Stable-family implementation+live compatibilityresponses, **not gasprice0 alone**. No business protocolfee amount or actualexecution expenditure was measured. Current fee strategy uses supported legacy estimate/sign/submit, freeStudioresources and zero businessvalue; modernRC measuredprofiling is NOT_APPLICABLE to this bound interface. If later actualStable version/API/fee requirements differ, stopaffectedwork and re-open environmentbinding; never inventfee0, silently switchSDK/network, buyresources or alterFrozen semantics. Only proven semantic conflict requiresACR.

## Faucet — actual free GEN credit

Authorized disposable diagnostic address: `0x8598ec74bD34a2FC75f12efEFBded50D5dd1768A`. This is not canonicaldeployment/userwallet; diagnostic signer ephemeral, no recoverable deployment credential provided or relied upon. Noaccountcredential transmitted/exported in evidence.

Official deployed Studio Faucet calls `sim_fundAccount(address,amountWei)` then `eth_getBalance(address,'latest')`. Directgenericrequest on lockedofficialclient is the supported observedpath; SDK's high-levelfundAccount has a localnetguard, so do not switchchain to invoke it. StudioUI equivalent: account dropdown→Newaccount as needed→Fundaccount→Amount→Fund→balance refresh. No externaltestnet faucet/mainnetETH prerequisite was used.

- Time: 2026-10-06T17:38:54.543Z.
- Requested1GEN =1000000000000000000wei.
- Before0x0; after0xde0b6b3a7640000; actualcredit1000000000000000000wei.
- Fundingrecordreturned `0xe2a5c511ed0e5e5862c03888dd624005c39a41ee041ec8a310e8838e3f142c37`.
- RPCbalance independentread confirms receipt. This is faucetcredit, **not EIM NEW/deployment/multiValidator/finalizedbusiness evidence**.
- No user funds spent, no purchase. Limits/guaranteedfutureavailability not established. Canonical deploywallet selection and its real credit/budget remain authorized PHASE4 work; no automaticreuseofdiagnosticaccount.

## Gate / known limitations / stop

| PHASE0 requirement | Result | Evidence / boundary |
|---|---|---|
| Stable identity61999 | PASS_RETAINED | Previous curl/Node/SDK/runtime-config observations retained; not re-probed |
| Exact compatible contract/SDK/test combination | PASS_ENVIRONMENT_BINDING | Exact Stable template Depends found in verified v0.2.16 archive; explicit loader, imports, custom callback and serialization checks pass |
| Fee estimation/submission route | PASS_IMPLEMENTATION_BOUND | Live Stable web bundle + exact SDK source + non-mutating fee RPC results; no RC fee fields assumed |
| Free Faucet path | PASS_ACTUAL_CREDIT | sim_fundAccount returned funding record; balance0→1GEN independently read |
| Usable Work execution route | PASS_RETAINED | OriginalStable RPC official NodeSDK path works; no alternate network/provider |

B0-FEE/B0-GENVM/B0-TOOLCHAIN/B0-FAUCET resolved at environment-binding scope. B0-ACCESS previouslyresolved; Pythonclient no longer a blocker. CLIaccountsetup remains deferred, not required for selectedworkingSDKroute.

Business tests/build/realconsensus/walletsigning/actualdeploy/finalizedbusinessstate: NOT_RUN. Canonicalcontract: NOT_DEPLOYED. Hostedprivatecommit/binarybuild: UNVERIFIED; immutablecontractDepends/ABI/artifactbinding is precise. NoACR.

Next Exact Action: **STOP; await explicit PHASE1 authorization**. On authorization read latestprogress/current lock and PHASE1 master/spec portions; implement only RepositoryA skeleton+deterministiccore. Do not startPHASE2/deploy/frontend automatically.

## Evidence / official sources

Current evidence `evidence/phase-0-gates/`; earlier successfulconnectivity and originalfailures retained. Environmentprobe source+logs, exactlocks, selectedrunners/manifests and CPythonreference are included in PHASE0_REVIEW_PACKAGE.zip.

- Current deployed Stable implementation: https://studio.genlayer.com/assets/index-D-dlGG4S.js ; SHA256 d77377107773632d36f25127cc4240b693de2586cc1a5907713e58316136b7d0.
- Official Stable-family source reference, v0.121.24 commit2004fc4315f0d2a0266f2da730992ce1e33ecfcc (not asserted deployed server commit):
  https://github.com/genlayerlabs/genlayer-studio/blob/2004fc4315f0d2a0266f2da730992ce1e33ecfcc/backend/protocol_rpc/endpoints.py
  https://github.com/genlayerlabs/genlayer-studio/blob/2004fc4315f0d2a0266f2da730992ce1e33ecfcc/backend/protocol_rpc/rpc_methods.py
  https://github.com/genlayerlabs/genlayer-studio/blob/2004fc4315f0d2a0266f2da730992ce1e33ecfcc/frontend/package.json
- Exact official GenVM release: https://github.com/genlayerlabs/genvm/releases/tag/v0.2.16
- Exact runner archive: https://github.com/genlayerlabs/genvm/releases/download/v0.2.16/genvm-universal.tar.xz
- Official package provenance: https://registry.npmjs.org/genlayer-js ; https://registry.npmjs.org/genlayer ; https://pypi.org/pypi/genlayer-test/0.29.2/json ; https://pypi.org/pypi/genlayer-py/0.16.3/json . Version observations preserved in prior evidence; not re-fetched this round.
- Official definitions retained: https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle ; https://docs.genlayer.com/developers/decentralized-applications/reading-data ; https://docs.genlayer.com/developers/consensus-v06-migration .

