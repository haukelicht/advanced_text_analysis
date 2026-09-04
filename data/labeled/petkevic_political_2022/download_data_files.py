"""Download the Petkević et al. (2022) dataset files.

Run this script from anywhere; by default it writes the TSV files next to this
script. Existing files are left untouched unless --force is passed.
"""

from __future__ import annotations

from pathlib import Path
from urllib.request import urlretrieve


FILES = {
    "petkevic_political_2022-campaigntweets_incivility.csv" "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/petkevic_political_2022/petkevic_political_2022-campaigntweets_incivility.csv",
    "petkevic_political_2022-campaigntweets_negative_tones.csv" "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/petkevic_political_2022/petkevic_political_2022-campaigntweets_negative_tones.csv",
    "petkevic_political_2022-campaigntweets_personal_attacks.csv" "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/petkevic_political_2022/petkevic_political_2022-campaigntweets_personal_attacks.csv",
    "petkevic_political_2022-campaigntweets_policy_attacks.csv" "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/petkevic_political_2022/petkevic_political_2022-campaigntweets_policy_attacks.csv",
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
