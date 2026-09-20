
## UK CAP annotations from ParlEE V4

author: Hauke Licht\
date: 2026-09-04

## Description

url: https://doi.org/10.7910/DVN/TLKVWY

This folder contains a UK subset of the ParlEE plenary speech annotations documented in Harvard Dataverse. The underlying dataset is the ParlEE plenary speeches V4 release, which provides sentence-level annotations for European parliamentary speeches with metadata on the speaker, party, date, whether the sentence concerns EU or domestic politics, and the relevant policy area using the Comparative Agendas Project (CAP) scheme.

The repository file here focuses on the UK CAP annotations and uses the CAP codebook in this folder to map numeric policy codes to topic names.

## Data format

The cleaned CSV is sentence-level data with one row per annotated sentence.

The main columns are:

- `text_id`: unique text ID
- `speaker`: speaker name
- `party`: speaker's party affiliation
- `date`: speech date
- `agenda`: agenda topic as provided in the source data
- `text`: annotated sentence text
- `cap_topic`: numeric Comparative Agendas Project policy code

The file [`cap_topic_codes.tsv`](cap_topic_codes.tsv) contains the codebook that maps CAP codes to topic labels.

## Source

source: Harvard Dataverse, *ParlEE plenary speeches V4 data set: Annotated full-text of 18 million sentence-level plenary speeches of eight European legislative chambers*, DOI: <https://doi.org/10.7910/DVN/TLKVWY>

## Cleaned data

Corresponding to the source data, we provide the following files:

- `sylvester_parlee_2022-uk_cap_annotations.csv`: sentence-level UK CAP annotations
- `cap_topic_codes.tsv`: CAP codebook used to interpret the `CAP` column

## Download data files

| dataset_key | file | url |
|---|---|---|
| sylvester_parlee_2022 | sylvester_parlee_2022-uk_cap_annotations.csv | https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/sylvester_parlee_2022/sylvester_parlee_2022-uk_cap_annotations.csv |