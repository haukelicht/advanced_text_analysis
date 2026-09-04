"""Download the Miller et al. (2020) dataset files.

Run this script from anywhere; by default it writes the TSV files next to this
script. Existing files are left untouched unless --force is passed.
"""

from __future__ import annotations

from pathlib import Path
from urllib.request import urlretrieve


FILES = {
    "miller_active_2020-tweets_refugeetopic.csv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/miller_active_2020/miller_active_2020-tweets_refugeetopic.csv",
    "miller_active_2020-news_articletag_muslim_identity.csv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/miller_active_2020/miller_active_2020-news_articletag_muslim_identity.csv",
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
