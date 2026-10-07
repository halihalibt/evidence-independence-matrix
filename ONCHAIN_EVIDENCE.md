# Canonical on-chain evidence

All entries below use Stable Studionet61999/canonical `0x7045b893E15B699e04494aA3849730bC6Aa1C864`. [Detailed final closure](evidence/PHASE4_FINAL_CLOSURE.md) contains inputs, actual digests, final protocol return and full network proof; this index is usable without EchoMap.

| Operation | Transaction | Actual result / participants |
|---|---|---|
| Deployment |[0x2486995a27e99c7d3bd1da857e9af39b330eb2092f066edb780aa44caacd3007](https://explorer-studio.genlayer.com/tx/0x2486995a27e99c7d3bd1da857e9af39b330eb2092f066edb780aa44caacd3007)|FINALIZED/SUCCESS/MAJORITY_AGREE;5 distinct successful identities|
| SYNTHETIC DEMO NEW |[0xec875a1a5de724b7fd6a407e851ba736393ae508f330c1b94059c9f72191d7f4](https://explorer-studio.genlayer.com/tx/0xec875a1a5de724b7fd6a407e851ba736393ae508f330c1b94059c9f72191d7f4)|FINALIZED/SUCCESS/MAJORITY_AGREE;1round/0rotation/4 distinct successful identities|
| Real public-document NEW |[0x77ddb362ff4fa11dc9a827de14f143da266c3c9c82d018950c9fc9376b45f4bb](https://explorer-studio.genlayer.com/tx/0x77ddb362ff4fa11dc9a827de14f143da266c3c9c82d018950c9fc9376b45f4bb)|FINALIZED/SUCCESS/MAJORITY_AGREE;1round/0rotation/3 distinct successful identities|
| Same-input REUSED |[0x8c0ea62020311b5718fe53bab1f3f4bad3aeca2ab2429e5eb719683c939ef9f8](https://explorer-studio.genlayer.com/tx/0x8c0ea62020311b5718fe53bab1f3f4bad3aeca2ab2429e5eb719683c939ef9f8)|FINALIZED/SUCCESS/MAJORITY_AGREE;3 distinct successful identities; same record|

Controlled request `68b9090d638738bd0236b084aff95ae7551d8df11da9b282aaa536ecd448258f`:PARTIAL,1D/2I/3U, maximum set[0,2]=[A,C],size2. A-B DEPENDENT,A-C/B-C INDEPENDENT,pairs withD UNKNOWN. Four frozen files are SYNTHETIC DEMO at commit5a11c820a28e23303298f12650377ee78faab0ba.
Public request `5c8aae111e19f6b193d5a8b4b8dce4697f424166922cd2116b49343b620c7b46`:IERC20 releasev5.4.0 and ERC-20 commitf2f4ff22452dec9d340ba9b8b1ee33c962a613d6; both READABLE/RELEVANT, actual DEPENDENT,COMPLETE,1D/0I/0U,set[0]/size1. Result was not imposed as a success condition.

## Raw receipts and finalized reads

[Controlled finalized record](evidence/semantic-safety/controlled-finalized-read.json); [public-document receipt](evidence/phase4-final-closure/public-document-latest.json) and [participant analysis](evidence/phase4-final-closure/public-document-analysis.json); [public finalized record](evidence/phase4-final-closure/public-document-finalized-read.json); [REUSED receipt](evidence/phase4-final-closure/reused-latest.json), [unchanged record](evidence/phase4-final-closure/reused-finalized-read.json), [no-nondet exposed fields](evidence/phase4-final-closure/reused-no-nondet-evidence.json); [protocol read](evidence/phase4-final-closure/final-protocol-read.json). Successful identities are counted once; idle/error entries do not count. Configured5 does not mean5 successfully executed every assessment.

## Honest failed observations

Historical disagreement records are preserved. Later EchoMap multi-refresh request `8bcc1dcb3ba13df648d68b9e81d01c2257695265c988a91cd5978d414076f350` finalized MAJORITY_DISAGREE with Leader execution SUCCESS and found:false; it is failure handling evidence, not a successful assessment. See EchoMap's recovery report for user-browser proof. No new transaction was sent during packaging; negative semantic-model controls remain NOT REAL-NETWORK VERIFIED.
