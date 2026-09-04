"""Download the Licht & Sczepanski (2025) dataset files.

Run this script from anywhere; by default it writes the JSONL files next to this
script. Existing files are left untouched unless --force is passed.
"""

from __future__ import annotations

import shutil
from pathlib import Path
from urllib.request import Request, urlopen


FILES = {
    "licht_detecting_2025-uk_manifestos.jsonl": "https://dataverse.harvard.edu/api/access/datafile/10707729",
    "licht_detecting_2025-de_manifestos.jsonl": "https://dataverse.harvard.edu/api/access/datafile/10707623",
    "licht_detecting_2025-uk_parlspeech.jsonl": "https://dataverse.harvard.edu/api/access/datafile/10707679",
}

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"


def download_file(url: str, filename: str, force: bool = True) -> bool:
    destination = Path(__file__).resolve().with_name(filename)
    if destination.exists() and not force:
        return False

    destination.parent.mkdir(parents=True, exist_ok=True)
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request) as response, destination.open("wb") as output_file:
        shutil.copyfileobj(response, output_file)
    return True

for filename, url in FILES.items():
    if download_file(url, filename):
        print(f"Downloaded {filename}")
    else:
        print(f"Skipped {filename} (already exists)")
