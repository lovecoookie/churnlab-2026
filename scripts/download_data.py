"""Fetch the commit-pinned IBM Telco churn CSV if absent, then record its source and hash."""

import hashlib
import json
import urllib.request
from pathlib import Path

URL = (
    "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/"
    "1fd6fd70906479be1712e64cfc0ea89f58466629/data/Telco-Customer-Churn.csv"
)
EXPECTED_SHA256 = "16320c9c1ec72448db59aa0a26a0b95401046bef5d02fd3aeb906448e3055e91"

csv_path = Path("data/raw/telco.csv")
meta_path = Path("data/raw/telco.source.json")
csv_path.parent.mkdir(parents=True, exist_ok=True)

if not csv_path.exists():
    print(f"Downloading {URL}")
    with urllib.request.urlopen(URL, timeout=60) as response:
        csv_path.write_bytes(response.read())
else:
    print(f"{csv_path} already exists, not downloading")

actual_sha256 = hashlib.sha256(csv_path.read_bytes()).hexdigest()
if actual_sha256 != EXPECTED_SHA256:
    raise ValueError(
        f"Source hash mismatch: expected {EXPECTED_SHA256}, got {actual_sha256}"
    )

metadata = {
    "source_url": URL,
    "sha256": actual_sha256,
    "file": csv_path.as_posix(),
    "size_bytes": csv_path.stat().st_size,
}
meta_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")
print(json.dumps(metadata, indent=2))
