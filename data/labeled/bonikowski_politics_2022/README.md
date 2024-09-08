# Measuring radical right rhetorics in U.S. presidential campaigns from Bonikowski et al. (2022)

author: Hauke Licht & Naomi Yagai\
date: 2024-01-30

## Description

In their 2022 *Sociological Methods & Research* paper "Politics as Usual? Measuring Populism, Nationalism, and Authoritarianism in U.S. Presidential Campaigns (1952--2020) with Neural Language Models," Bonikowski and his colleagues measure the prevalence of radical right rhetoric in U.S. presidential campaigns by identifying three components on six dimensions:

- populism
- nationalism (exclusionary) 
- nationalism (inclusive)
- nationalism (high national pride)
- nationalism (low national pride)
- authoritarianism

Their measurements are generated through a neutral language model (RoBERTa model) utilising transfer learning. 
To fine-tune the classifier, they collect human-annotated documents.

## The raw data

The authors explain the corpus in their article section "Presidential Campaign Data, 1952–2020" (pp. 1737-1738) as follows.

> Our analyses rely on a corpus of presidential campaign speeches by Democratic and Republican Party nominees, beginning with the 1952 contest between Dwight Eisenhower and Adlai Stevenson and concluding with the 2020 election featuring Donald Trump and Joe Biden.
The data are a composite of two sources: the Annenberg/Pew Archive of Presidential Campaign Discourse (Annenberg 2000), which covers the 1952-1996 elections, and speeches from the UC Santa Barbara American Presidency Project (UCSB 2021), spanning the 2000-2020 elections...
Two Republican campaigns are missing from the data: Barry Goldwater’s 1964 campaign and George W. Bush’s 2000 campaign. 
The final corpus consists of 2,956 speeches split into 71,808 paragraphs (we justify treating paragraphs as the primary units of analysis in the methods section).

The corpus is in English.

## Annotation procedure

The annotation procedure is described in their article section "The Hand-Coding Process" (pp. 1747-1749).

They randomly sampled 2,224 paragraphs from the corpus.
Before coding, they generated labeling guidelines for each dimension and refined them by collectively discussing potentially ambiguous cases.
Every paragraph was then labeled by two coders independently for each dimension and any resulting disagreements were adjudicated by a third coder.

Each paragraph was coded by each coder along six coding dimensions:

-   *Populism:* 1 if present, 0 if absent in a given paragraph
-   *Exclusion:* 1 if present, 0 if absent in a given paragraph
-   *Inclusion:* 1 if present, 0 if absent in a given paragraph
-   *High_pride:* 1 if present, 0 if absent in a given paragraph
-   *Low_pride:* 1 if present, 0 if absent in a given paragraph
-   *Authoritarianism:* 1 if present, 0 if absent in a given paragraph

## The data

source: replication data on Open-Science Foundations (OSF): <https://osf.io/z7c53?view_only=b98f0ce1f64e46f29b643db7d75a4462>, file 'main_data.csv'

### Cleaned data

Corresponding to the analysis, we provide the following CSV files:

- 1. populism rhetoric classification: 
"bonikowski_politics_2022-campaignspeech_populism.csv"
    - column 'label' indicates the annotation: 1 when present, 0 when absent
    - column 'text' records the coded campaign speech paragraph
    - 'metadata__speech_id' indicates the speech ID
    - 'metadata__party' indicates the party of the candidate who gave the speech: "rep" for the Republican Party and "dem" for the Democratic Party
    - 'metadata__term' indicates the year of the campaign
    - 'metadata__comp' indicates [[needs to be clarified]]
    - 'metadata__populist_old_keywords' indicates [[needs to be clarified]]
    - 'metadata__par_id' indicates [[needs to be clarified]]
    - 'metadata__campaign' indicates the campaign year and party (e.g., "1960rep")
    - 'metadata__party_incumbent' indicates whether the party was incumbent or not: "1" if incumbent and "0" if opposition
    - 'metadata__recession' indicates whether there was a recession or not: "1" if yes, "0" if no
    - 'metadata__prior_president' indicates [[needs to be clarified]]
    - 'metadata__election_date' indicates the election date of the campaign
    - 'metadata__person' records the surname of the president candidate who gave the speech (e.g., "Clinton")
    - 'metadata__date' indicates the date the speech was given
    - 'metadata__name_date' indicates [[needs to be clarified]]  # missing values where T/F needed
    - 'metadata__weeks_to_election' calculates the weeks to the election date
    - 'metadata__cutoff_date' indicates the cutoff date the campaign speeches were collected from. 
    According to this variable, all speeches are collected from the 1st of September in the respective campaign year
    - column 'metadata__row_number' indicates the original row number of each paragraph before cleaning the data
- 2. nationalism rhetoric classification
    - 2.1. classification of the exclusionary dimension:
    "bonikowski_politics_2022-campaignspeech_nationalism_exclusion.csv"
    - 2.2. classification of the inclusive dimension:
    "bonikowski_politics_2022-campaignspeech_nationalism_inclusion.csv"
    - 2.3. classification of the high pride dimension:
    "bonikowski_politics_2022-campaignspeech_nationalism_highpride.csv"
    - 2.4. classification of the low pride dimension:
    "bonikowski_politics_2022-campaignspeech_nationalism_lowpride.csv"
  
- 3. authoritarianism rhetoric classification:
"bonikowski_politics_2022-campaignspeech_authoritarianism.csv"

