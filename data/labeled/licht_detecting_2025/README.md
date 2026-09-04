# Group mentions detected in political rhetoric from Licht & Sczepanski (2025)

author: Hauke Licht\
date: 2026-09-04

## Description

This dataset is derived from the annotations used in Licht and Sczepanski's 2025 British Journal of Political Science article, *Detecting Group Mentions in Political Rhetoric: A Supervised Learning Approach*.

The task is span extraction: identify phrases in political texts that refer to social groups, and distinguish them from other annotated spans that are not social-group mentions.

## Label semantics

The cleaned span annotations use two labels:

- `SG`: social-group mention
- `other`: any other annotated span in the source data that is not a social-group mention

In practice, `SG` covers references such as groups of people, voters, workers, families, veterans, or similar collective social categories. `other` covers non-social-group mentions that were also marked in the source annotations, such as institutions, offices, committees, government bodies, countries, or other non-group references.

Examples from the data:

- `the public` in “I fear that the public will not be as resistant to that message as they would have been a week ago.” is tagged as `SG`
- `charities` and `the lobbying Bill` in “... Ministers still need to explain why charities were not consulted before the lobbying Bill was published.” are tagged as `SG` and `other`, respectively
- `the Department` and `the British Transport police` in “The Department takes this issue exceptionally seriously, as do all train operators and the British Transport police.” are tagged as `other`
- `veterans' breakfast clubs` and `veterans` in “Does the Minister welcome the establishment of veterans' breakfast clubs ...” are tagged as `SG`

The exact span boundaries are character-based in the cleaned files and token-based in the raw annotation files.

## Data format

The folder contains both raw and cleaned JSONL files.

- raw files (`licht_detecting_2025-uk_manifestos.jsonl`, `licht_detecting_2025-de_manifestos.jsonl`, `licht_detecting_2025-uk_parlspeech.jsonl`): tokenized documents with per-annotator token labels and a released token-label sequence
- cleaned files (`*-cleaned.jsonl`): span-level annotations with text and character-offset labels

Typical fields include:

- `text`: the sentence or document text
- `tokens`: tokenized text, in the raw files
- `annotations`: annotator-specific token labels, in the raw files
- `labels`: the released token labels, or the annotated token-label sequence in the raw files
- `label`: character-offset spans in the cleaned files
- `metadata`: source information such as `sentence_id`, `party`, `speaker`, `year`, and `date`

## Source

source: Licht, Hauke, and Ronja Sczepanski. 2025. “Detecting Group Mentions in Political Rhetoric: A Supervised Learning Approach.” *British Journal of Political Science* 55: e119. DOI: <https://doi.org/10.1017/S0007123424000954>

## Cleaned data

Corresponding to the source data, we provide the following files:

- `licht_detecting_2025-uk_manifestos-cleaned.jsonl`
- `licht_detecting_2025-de_manifestos-cleaned.jsonl`
- `licht_detecting_2025-uk_parlspeech-cleaned.jsonl`

## Download data files

| dataset_key | file | url |
|---|---|---|
| licht_detecting_2025 | licht_detecting_2025-uk_manifestos.jsonl | https://dataverse.harvard.edu/api/access/datafile/10707729 |
| licht_detecting_2025 | licht_detecting_2025-de_manifestos.jsonl | https://dataverse.harvard.edu/api/access/datafile/10707623 |
| licht_detecting_2025 | licht_detecting_2025-uk_parlspeech.jsonl | https://dataverse.harvard.edu/api/access/datafile/10707679 |