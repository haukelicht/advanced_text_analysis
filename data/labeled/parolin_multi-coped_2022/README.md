
## Multi-CoPED CAMEO NER annotations from Parolin et al. (2022)

author: Hauke Licht\
date: 2026-09-04

## Description

This dataset is derived from the Multi-CoPED benchmark introduced by Skorupa Parolin and colleagues in their 2022 AIES paper, *Multi-CoPED: A Multilingual Multi-Task Approach for Coding Political Event Data on Conflict and Mediation Domain*.

The task here is token-level named-entity recognition for political event coding in the CAMEO scheme. Each token is tagged as part of an event source, target, or relation, or as outside of any event mention.

In plain language:

- the **source** is the actor or group initiating the event
- the **target** is the actor, group, or entity receiving the action or being affected by it
- the **relation** is the event phrase that links source and target, such as a meeting, agreement, request, attack, or statement

Examples from the data:

- "President Bush and Egyptian President Hosni Mubarak agreed ..." labels the first entity as a source and the event phrase as a relation
- "... the United States would remove irritants damaging relations between the two NATO allies" labels the United States as a source and the allies as the target
- "a Palestinian guerrilla group claimed responsibility for attacks on Israeli troops" labels the group as a source, the Israeli troops as the target, and the attack-related wording as the relation

The exact span boundaries depend on the sentence, but the annotation always follows that source-target-relation structure.

## Data format

The cleaned dataset is provided as JSONL, with one document per line:

- `tokens`: tokenized sentence text
- `labels`: token-level BIO-style tags aligned with `tokens`

The label inventory used in the source files is:

- `B-S` / `I-S`: source span
- `B-T` / `I-T`: target span
- `B-R` / `I-R`: relation span
- `O`: outside any annotated span

The original source splits are also included as plain-text files in CoNLL-style format.

## Source

source: Skorupa Parolin et al. (2022), *Multi-CoPED: A Multilingual Multi-Task Approach for Coding Political Event Data on Conflict and Mediation Domain*, Proceedings of the 2022 AAAI/ACM Conference on AI, Ethics, and Society (AIES '22), 700--711. DOI: <https://doi.org/10.1145/3514094.3534178>

## Cleaned data

Corresponding to the source data, we provide the following files:

- `parolin_multi-coped_2022-cameo_ner.jsonl`: JSONL version with `tokens` and `labels`
- `parolin_multi-coped_2022-train.txt`: original train split in token-label format
- `parolin_multi-coped_2022-test.txt`: original test split in token-label format

## Download data files

| dataset_key | file | url |
|---|---|---|
| parolin_multi-coped_2022 | parolin_multi-coped_2022-cameo_ner.jsonl | https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/parolin_multi-coped_2022/parolin_multi-coped_2022-cameo_ner.jsonl |
| parolin_multi-coped_2022 | parolin_multi-coped_2022-train.txt | https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/parolin_multi-coped_2022/parolin_multi-coped_2022-train.txt |
| parolin_multi-coped_2022 | parolin_multi-coped_2022-test.txt | https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/parolin_multi-coped_2022/parolin_multi-coped_2022-test.txt |