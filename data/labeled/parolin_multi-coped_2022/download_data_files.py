"""Download the Gilardi (2023) dataset files.

Run this script from anywhere; by default it writes the CSV files next to this
script. Existing files are left untouched unless --force is passed.
"""

from __future__ import annotations

from pathlib import Path
from urllib.request import urlretrieve


FILES = {
    "parolin_multi-coped_2022-test.txt":  "https://raw.githubusercontent.com/eventdata/ConfliBERT/main/data/cameo_ner/test.txt",
    "parolin_multi-coped_2022-train.txt": "https://raw.githubusercontent.com/eventdata/ConfliBERT/main/data/cameo_ner/train.txt",
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
