"""Download the Hargrave and Blumenau (2022) crowd-coded dataset files.

Run this script from anywhere; by default it writes the TSV files next to this
script. Existing files are left untouched unless --force is passed.
"""

from __future__ import annotations

from pathlib import Path
from urllib.request import urlretrieve


FILES = {
    "hargrave_no_2022-repetition.tsv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/hargrave_no_2022/hargrave_no_2022-repetition.tsv",
    "hargrave_no_2022-aggression.tsv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/hargrave_no_2022/hargrave_no_2022-aggression.tsv",
    "hargrave_no_2022-fact.tsv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/hargrave_no_2022/hargrave_no_2022-fact.tsv",
    "hargrave_no_2022-negative_emotion.tsv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/hargrave_no_2022/hargrave_no_2022-negative_emotion.tsv",
    "hargrave_no_2022-positive_emotion.tsv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/hargrave_no_2022/hargrave_no_2022-positive_emotion.tsv",
    "hargrave_no_2022-complexity.tsv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/hargrave_no_2022/hargrave_no_2022-complexity.tsv",
    "hargrave_no_2022-human_narrative.tsv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/hargrave_no_2022/hargrave_no_2022-human_narrative.tsv",
    "hargrave_no_2022-affect.tsv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/hargrave_no_2022/hargrave_no_2022-affect.tsv",
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
