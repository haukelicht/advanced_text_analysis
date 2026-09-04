"""Download the Bonikowski et al. (2022) crowd-coded dataset files.

Run this script from anywhere; by default it writes the CSV files next to this
script. Existing files are left untouched unless --force is passed.
"""

from __future__ import annotations

from pathlib import Path
from urllib.request import urlretrieve


FILES = {
    "bonikowski_politics_2022-campaignspeech_populism.csv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/bonikowski_politics_2022/bonikowski_politics_2022-campaignspeech_populism.csv",
    "bonikowski_politics_2022-campaignspeech_nationalism_highpride.csv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/bonikowski_politics_2022/bonikowski_politics_2022-campaignspeech_nationalism_highpride.csv",
    "bonikowski_politics_2022-campaignspeech_nationalism_lowpride.csv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/bonikowski_politics_2022/bonikowski_politics_2022-campaignspeech_nationalism_lowpride.csv",
    "bonikowski_politics_2022-campaignspeech_authoritarianism.csv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/bonikowski_politics_2022/bonikowski_politics_2022-campaignspeech_authoritarianism.csv",
    "bonikowski_politics_2022-campaignspeech_nationalism_exclusion.csv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/bonikowski_politics_2022/bonikowski_politics_2022-campaignspeech_nationalism_exclusion.csv",
    "bonikowski_politics_2022-campaignspeech_nationalism_inclusion.csv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/bonikowski_politics_2022/bonikowski_politics_2022-campaignspeech_nationalism_inclusion.csv",
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
