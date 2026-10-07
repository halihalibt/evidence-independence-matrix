# Evidence index — Evidence Independence Matrix

| Evidence | What it proves | Verification class |
|---|---|---|
|[Final canonical deployment](DEPLOYMENT_MANIFEST_STUDIONET.md)|actual address/source hash/Depends and successful deployment|REAL STUDIONET VERIFIED|
|[Canonical NEW/REUSED records and receipts](ONCHAIN_EVIDENCE.md)|real controlled/public-document consensus, participants, finalized persistent records and idempotency|REAL STUDIONET VERIFIED|
|[277 tests XML](evidence/semantic-safety/all-tests.xml)|parser/digest/anchor/safety/idempotency/atomic ordering cases; scripted external boundaries|LOCAL /MOCK VERIFIED|
|[Canonical vector check](evidence/phase9-vectors.log)|3 cross-language SHA256/UTF8 JSON vectors|LOCAL VERIFIED|
|[Canonical source bundle](deployment/canonical-source.bundle)|recoverable immutable deployment-source commit; current source SHA matches|LOCAL VERIFIED + PUBLIC BUNDLE; canonical source bytes matched|
|[Approved safety patch](docs/ACR001_SEMANTIC_SAFETY_PATCH.md)|approved evidence-anchor rule changes, preserved state/API guarantees|APPROVED DESIGN +LOCAL TESTS|
|[Known limitations](KNOWN_LIMITATIONS.md)|negative controls and hidden-provenance/operator evidence limits|NOT REAL-NETWORK VERIFIED where stated|

Screenshots are supplemental; original receipts/finalized records are primary proof. Intelligent Contract review does not require EchoMap. [Quick path](REVIEWER_QUICK_PATH.md).
