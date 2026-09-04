"""Download the Fornaciari et al. (2021) dataset files.

Run this script from anywhere; by default it writes the Excel files next to this
script. Existing files are left untouched unless --force is passed.
"""

from __future__ import annotations

from pathlib import Path
from urllib.request import urlretrieve


FILES = {
    "fornaciari_we_2021-pledge_annotations.xlsx": "https://github.com/fornaciari/MiMac_taxes/raw/refs/heads/main/jupyter_xsl_preproc_210130170501/all210126.xlsx",
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
