# EIM protocol specification

Protocol EIM-V1-STUDIO; candidate schema EIM-CANDIDATE-V1; deployed consensus revision ACR-001-SAFETY-1.

[Full input/normalization/identifier/state/method/error specification](docs/protocol.md) preserves the technical binding. [Approved Freeze](docs/ARCHITECTURE_FREEZE_V1.md), [ACR-001](docs/ARCHITECTURE_CHANGE_REQUEST_001.md) and [safety patch](docs/ACR001_SEMANTIC_SAFETY_PATCH.md) retain the authority history. Original Freeze has not been rewritten.

DEPENDENT requires positive claim-related shared original source/derivation. INDEPENDENT requires two readable relevant materials with identifiable distinguishable acquisition paths and no visible claim-related shared/derived origin. UNKNOWN means neither positive standard is established or provenance/relevance is insufficient. Different domains, same event/conclusion or similar wording alone do not establish a positive relation. Non-readable/non-relevant pairs must be UNKNOWN.

Leader builds the full candidate. Validator independently reacquires evidence and validates each proposed semantic field, with exact deterministic evidence binding and grounded positive-relation anchors; it does not demand independent enum regeneration equality. See [security model](SECURITY_AND_TRUST_MODEL.md). Persistent schemas/enums/public methods, canonical hashes, no-write failure handling, idempotency and non-transitive maximum pairwise-set calculation remain unchanged.

Exactly4 methods:assess(client_key,claim,context,urls) is a public sender-authorized write returning request_id/disposition/result_status; get_assessment(request_id),lookup_request(creator,client_key),get_protocol_info() are public wallet-free views. No admin/debug methods. Only immutable assessments mapping values persist. Claim truth, scores, explanations, Validator anchors and participant counts are not Assessment state.
