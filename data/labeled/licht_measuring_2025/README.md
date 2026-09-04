# Pairwise comparisons for measuring scalar constructs from Licht et al. (2025)

author: Hauke Licht\
date: 2026-09-04

## Description

url: https://doi.org/10.18653/v1/2025.emnlp-main.1635

This dataset accompanies Licht et al.'s 2025 EMNLP paper, *Measuring scalar constructs in social science with LLMs*.

The paper studies how large language models can be used to measure latent scalar constructs from political text. The data in this folder are pairwise-comparison annotations taken from three secondary sources used in the paper:

- Carlson and Montgomery's immigration-fear data
- Carlson and Montgomery's Wisconsin-ads data
- Park et al.'s grandstanding data

The annotation task is pairwise comparison: given two texts, choose the one that is stronger on the target construct. The released files also retain the original direct scalar scores from the source datasets when they are available.

## Data format

Each JSONL record contains a single comparison or source observation. Common fields include:

- `pair_id`: pairwise comparison ID
- `id1`, `id2`: item identifiers for the two texts being compared
- `text1`, `text2`: the paired texts
- `label`: pairwise winner, where `1` means the first text is stronger on the target construct and `2` means the second text is stronger
- `unanimous`: whether the pairwise annotation was unanimous
- `pairwise_annotations`: raw annotator votes when available
- `direct_measure1`, `direct_measure2`: direct scalar scores from the source data when available
- `direct_annotations1`, `direct_annotations2`: raw direct-score annotations when available
- `metadata`: source-specific metadata such as worker, state, candidate, congress, or speech details

## Source

source: Licht, Hauke, Rupak Sarkar, Patrick Y. Wu, Pranav Goel, Niklas Stoehr, Elliott Ash, and Alexander Miserlis Hoyle. 2025. “Measuring Scalar Constructs in Social Science with LLMs.” *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing*. DOI: <https://doi.org/10.18653/v1/2025.emnlp-main.1635>

## Cleaned data

Corresponding to the source data, we provide the following files:

- `carlson_pairwise_2017-immigration_fear.jsonl`: pairwise comparisons for the immigration-fear construct
- `carlson_pairwise_2017-wiscads.jsonl`: pairwise comparisons for the Carlson and Montgomery Wisconsin-ads construct
- `park_when_2019-grandstanding.jsonl`: pairwise comparisons for the grandstanding construct

## Download data files

| dataset_key | file | url |
|---|---|---|
| licht_measuring_2025 | carlson_pairwise_2017-immigration_fear.jsonl | https://raw.githubusercontent.com/haukelicht/scalar_measurement/refs/heads/main/data/processed_data/carlson_montgomery2017_immigration/data.jsonl |
| licht_measuring_2025 | carlson_pairwise_2017-wiscads.jsonl | https://raw.githubusercontent.com/haukelicht/scalar_measurement/refs/heads/main/data/processed_data/carlson_montgomery2017_wiscads/data.jsonl |
| licht_measuring_2025 | park_when_2019-grandstanding.jsonl | https://raw.githubusercontent.com/haukelicht/scalar_measurement/refs/heads/main/data/processed_data/park2019/data.jsonl |