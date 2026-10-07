"""Load actual content-addressed SDK, not a stand-in genlayer module."""
import hashlib
import sys
from pathlib import Path
import pytest
from gltest.direct import VMContext, load_contract_class
from gltest.direct.sdk_loader import download_artifacts

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_SHA256 = "4f0b358ec98ec148be9b95cdfb0f0e1a6cbe64da0194fdfac3fffc6f5d1d93e2"

@pytest.fixture(scope="session")
def eim():
    archive = download_artifacts("v0.2.16")
    with archive.open("rb") as stream:
        assert hashlib.file_digest(stream, "sha256").hexdigest() == ARTIFACT_SHA256
    vm = VMContext()
    vm._sender = bytes.fromhex("ab" * 20)
    vm._contract_address = bytes.fromhex("cd" * 20)
    vm._chain_id = 61999
    cls = load_contract_class(ROOT / "contracts/evidence_independence_matrix.py", vm, sdk_version="v0.2.16")
    return sys.modules[cls.__module__]
