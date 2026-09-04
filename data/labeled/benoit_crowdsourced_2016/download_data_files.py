"""Download the Benoit et al. (2016) crowd-coded dataset files.

Run this script from anywhere; by default it writes the CSV files next to this
script. Existing files are left untouched unless --force is passed.
"""

from __future__ import annotations

from pathlib import Path
from urllib.request import urlretrieve


FILES = {
    "benoit_crowdsourced_2016-econ_policy_stance.csv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/benoit_crowdsourced_2016/benoit_crowdsourced_2016-econ_policy_stance.csv",
    "benoit_crowdsourced_2016-immigration_policy.csv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/benoit_crowdsourced_2016/benoit_crowdsourced_2016-immigration_policy.csv",
    "benoit_crowdsourced_2016-social_policy_stance.csv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/benoit_crowdsourced_2016/benoit_crowdsourced_2016-social_policy_stance.csv",
    "benoit_crowdsourced_2016-subsidies_stance.csv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/benoit_crowdsourced_2016/benoit_crowdsourced_2016-subsidies_stance.csv",
    "benoit_crowdsourced_2016-policy_area.csv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/benoit_crowdsourced_2016/benoit_crowdsourced_2016-policy_area.csv",
    "benoit_crowdsourced_2016-immigration_policy_stance.csv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/benoit_crowdsourced_2016/benoit_crowdsourced_2016-immigration_policy_stance.csv",
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
