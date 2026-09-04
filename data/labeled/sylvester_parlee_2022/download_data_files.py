"""Download the Sylvester et al. (2022) ParlEE dataset files.

Run this script from anywhere; by default it writes the CSV files next to this
script. Existing files are left untouched unless --force is passed.
"""

from __future__ import annotations

from pathlib import Path
from urllib.request import urlretrieve


FILES = {
    "sylvester_parlee_2022-uk_cap_annotations.csv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/sylvester_parlee_2022/sylvester_parlee_2022-uk_cap_annotations.csv"
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
