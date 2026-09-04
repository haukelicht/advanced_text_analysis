"""Download the Licht et al. (2025) pairwise comparison dataset files.

Run this script from anywhere; by default it writes the CSV files next to this
script. Existing files are left untouched unless --force is passed.
"""

from __future__ import annotations

from pathlib import Path
from urllib.request import urlretrieve


FILES = {
    "carlson_pairwise_2017-immigration_fear.jsonl": "https://raw.githubusercontent.com/haukelicht/scalar_measurement/refs/heads/main/data/processed_data/carlson_montgomery2017_immigration/data.jsonl",
    "carlson_pairwise_2017-wiscads.jsonl": "https://raw.githubusercontent.com/haukelicht/scalar_measurement/refs/heads/main/data/processed_data/carlson_montgomery2017_wiscads/data.jsonl",
    "park_when_2019-grandstanding.jsonl": "https://raw.githubusercontent.com/haukelicht/scalar_measurement/refs/heads/main/data/processed_data/park2019/data.jsonl",
}


def download_file(url: str, filename: str, force: bool = False) -> bool:
    destination = Path(filename)
    if destination.exists() and not force:
        return False

    destination.parent.mkdir(parents=True, exist_ok=True)
    urlretrieve(url, destination)
    return True

for filename, url in FILES.items():
    if download_file(url, filename, force=True):
        print(f"Downloaded {filename}")
    else:
        print(f"Skipped {filename} (already exists)")
