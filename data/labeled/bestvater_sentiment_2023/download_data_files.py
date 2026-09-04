"""Download the Bestvater and Monroe (2023) crowd-coded dataset files.

Run this script from anywhere; by default it writes the TSV files next to this
script. Existing files are left untouched unless --force is passed.
"""

from __future__ import annotations

from pathlib import Path
from urllib.request import urlretrieve


FILES = {
    "bestvater_sentiment_2023-kavanaugh_tweets_stance.tsv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/bestvater_sentiment_2023/bestvater_sentiment_2023-kavanaugh_tweets_stance.tsv",
    "bestvater_sentiment_2023-womensmarch_tweets_sentiment.tsv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/bestvater_sentiment_2023/bestvater_sentiment_2023-womensmarch_tweets_sentiment.tsv",
    "bestvater_sentiment_2023-womensmarch_tweets_stance.tsv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/bestvater_sentiment_2023/bestvater_sentiment_2023-womensmarch_tweets_stance.tsv",
    "bestvater_sentiment_2023-motn_responses_sentiment.tsv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/bestvater_sentiment_2023/bestvater_sentiment_2023-motn_responses_sentiment.tsv",
    "bestvater_sentiment_2023-kavanaugh_tweets_sentiment.tsv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/bestvater_sentiment_2023/bestvater_sentiment_2023-kavanaugh_tweets_sentiment.tsv",
    "bestvater_sentiment_2023-motn_responses_stance.tsv": "https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/bestvater_sentiment_2023/bestvater_sentiment_2023-motn_responses_stance.tsv",
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
