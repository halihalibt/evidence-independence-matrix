# Canonical V1 vectors

Three static vectors include Unicode/emoji, CRLF/CR, BOM, Unicode surrounding
whitespace, quotes/backslash, internal whitespace, address case, default port,
path escape/case and URL sorting. Expected hashes were generated independently
with Node built-in crypto from explicit canonical arrays, not copied from the
contract implementation. Python tests compare raw inputs, normalized values,
canonical JSON and hashes; the Node checker independently checks normalization
for these legal examples and SHA-256. The checker is not a frontend or a complete
production URL validator. Future B must match these same vectors.
