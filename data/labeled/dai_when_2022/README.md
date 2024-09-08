# Identifying populist rhetoric in U.S. presidential campaign speeches from Dai & Kustov (2022)

author: Hauke Licht & Naomi Yagai\
date: 2024-01-12

## Description

In their 2022 *Political Communication* paper "When Do Politicians Use Populist Rhetoric? Populism as a Campaign Gamble," Dai and Kustov assess the prevalence of populist rhetoric across U.S. presidential campaign speeches (1952--2016).

Their measurements are generated through a novel automated text analysis method utilizing active learning and word embedding.

## The raw data

The authors built a comprehensive U.S. presidential campaign corpus consisting of 4,314 speeches from 1952 to 2016.

The authors explain the corpus in their article section "Data" (pp. 388) as follows.

> The speeches are collected from two data sources: The Annenberg/Pew Archive of Presidential Campaign Discourse (Annenberg, 2000) and The American Presidency Project (Woolley & Peters, 2008) hosted at the University of California, Santa Barbara.
The Annenberg/Pew Archive of Presidential Campaign Discourse includes transcripts of campaign speeches delivered by the Democratic and Republican presidential nominees between September 1st and the election day, as well as their nomination acceptance speeches. 
Overall, it covers 12 elections and 21 presidential campaigns from 1952 to 1996 with 2,406 speeches...
We use the American Presidency Project to expand on the Annenberg/Pew Archive data by adding five most recent elections from 2000 to 2016 and incorporating all speeches delivered during presidential campaigns. 
The average speech length is 2,167 words, and 90% of the speeches are between 500 words to 5000 words.

Regarding their analysis, the authors also mention that
> While our speech data and populism measurement include speeches and populism score by all candidates and span from the day of candidacy announcement to the election day, we only include the speeches delivered by the final candidates from the two parties from January to the election day to test our theoretical model, which results in 3,436 speeches.

The corpus is in English.

## Annotation procedure

Speeches are divided into sub-speeches of 10 paragraphs. 
These sub-speeches are treated as a document in the classification task.

The annotation procedure is described in their article section "Measurement of Populist Rhetoric" (pp. 388-393). 

The authors randomly sampled 73 out of 4,314 speeches which contain 407 sub-speeches.
This was stratified to have at least two speeches from every decade to account for possible variations of populist language over time.
The sample was then coded by the first human coder.
The second coder coded a smaller set of 69 sub-speeches from the sample to evaluate inter-coder reliability. 
In case of discrepancies, this was resolved using the majority rule with a third coder.
After training the classifier and applying it to the entire corpus, the authors used active learning to identify the most informative documents (in this case, documents that the classifier was most uncertain about the labeling).
These queried documents were then coded by the human coder and added to re-train the classifier again to query new documents to code.
This additional coding process was repeated 9 times until they labelled an additional 180 sub-speeches.

Each sub-speech was coded by each coder either as populist or not following the below definition explained in the article pp. 389.

-   *Pop:* accept if considered populist, reject if not considered populist.

> A text is considered populist if and only if it (1) recognizes the people instead of the elite as the only legitimate source of power (people-centric); 
(2) creates separation between us and them (anti-pluralist);
and, in doing so, (3) stipulates the separation of us and them on moral grounds (good versus evil; Dai, 2019; Hawkins, 2009)

## The data

source: obtained via emailing the authors.

### Descriptives

Number of documents: 587

Number of annotations per document: 1 to 3

$$more to be added$$

### Problems

*none known*

### Cleaned data

Corresponding to the analysis, we provide the following CSV file:

- populist rhetoric classification: 
"dai_when_2022-campaignspeech_populism.csv"
	- column 'label' indicates the annotation: "accept" when considered populist, "reject" when not considered populist
	- column 'text' records the coded sub-speeches
	- column 'metadata__candidate' indicates the candidate name of the sub-speech
  - column 'metadata__title' contains a brief description of the sub-speech (the type of the campaign speech e.g., remark and interview and where it was given)
  - column 'metadata__year' indicates the year the sub-speech was given
  - column 'metadata__test' indicates [[needs to be clarified]]
  - column 'metadata__row_number' indicates the original row number of each sub-speech before cleaning the data 

Number of unique documents/text:

Label distribution: ...
