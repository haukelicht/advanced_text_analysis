"""Download the Gilardi (2023) dataset files.

Run this script from anywhere; by default it writes the CSV files next to this
script. Existing files are left untouched unless --force is passed.
"""

from __future__ import annotations

from pathlib import Path
from urllib.request import urlretrieve


FILES = {
    "gilardi_chatgpt_2023-content_moderation_frame.csv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/gilardi_chatgpt_2023/gilardi_chatgpt_2023-content_moderation_frame.csv",
    "gilardi_chatgpt_2023-section230_stance.csv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/gilardi_chatgpt_2023/gilardi_chatgpt_2023-section230_stance.csv",
    "gilardi_chatgpt_2023-content_moderation_relevance.csv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/gilardi_chatgpt_2023/gilardi_chatgpt_2023-content_moderation_relevance.csv",
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
