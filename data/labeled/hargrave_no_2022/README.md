# Pairwise comparisons of sentence pairs from Hargrave and Blumenau (2022)

author: Hauke Licht\
date: 2024-01-10

## Description

In the 2022 BJPolS paper "No Longer Conforming to Stereotypes? Gender, Political Style and Parliamentary Debate in the UK," Lotte Hargrave and Jack Blumenau analyze the rhetorical style of male and female MPs in the house of commons along eight dimensions:

- affective language
- positive emotions
- negative emotions
- factual language
- human narrative
- aggressive language
- complex language
- repetitiveness

Their measurements are mainly generated with a on word embedding-based text scaling appraoch.
But the collect a number of (pairwise) human judgments to validate their measurements.

## Annotation procedure

In the supporting materials, they describe their annotation procedure as follows:

> We wrote a web app which presented two research assistants with pairs of  sentences (sampled from all sentences in our corpus).
> Coders were asked to complete two tasks. 
> First, a *style-comparison task* required them to select which of the two sentences was more typical of a particular style. 
> Second, a *style-intensity task* required them to rate the degree to which each sentence was representative of the selected style on a  5 point scale.
> ...
> Each coder completed 70 comparisons per style, on average, meaning that we have on average 140 individual sentence-ratings per style.

Note that the authors also included 'minimal definitions of the speech-styles
of interest to ensure that the human coding related to the style dimensions 
identified in the literature review.'

- *affective language*: "Your task is to select the sentence which you believe uses more emotional language, which might be either positive or negative emotion; such as expressing criticism, praise, disapproval, pride, empathy or fear.",                       
- *positive emotions*: "Your task is to select the sentence which you believe uses more positive language, which might include expressing empathy, praise, pride, celebration or congratulations.",
- *negative emotions*: "Your task is to select the sentence which you believe uses more negative language, which might include expressing criticism, fear, unpleasantness, sadness or disapproval.",
- *factual language*: "Your task is to select the sentence which you believe uses more factual language, which might include the use of numbers, statistics, numerical quantifiers, figures and empirical evidence.",
- *human narrative*: "Your task is to select the sentence which you believe uses more human narrative, which might include referring to personal examples or experiences; the experiences and stories of other people; constituency stories; illustrative examples; drawing on human interest stories; or referring to individual people, including other Members of Parliament.",
- *aggressive language*: "Your task is to select the sentence which you believe uses more aggressive language, which might include criticisms or insults aimed at other MPs, people, groups, legislation, the government, parties or organizations; language that suggests forceful action; or confrontational, declamatory or adversarial language.",
- *complex language*: "Your task is to select the sentence which you believe uses more complex language, where complexity is defined as the use of elaborate and sophisticated language that is challenging to read and understand.",
- *repetitiveness*: "Your task is to select the sentence which you believe uses more repetitive language, where the sentence includes words and phrases that are used more than once."

These instructions can be regarded as prompts.

## The data

source: replication data on the BJPolS' harvard dataverse: https://doi.org/10.7910/DVN/PPSFLT, file 'validation_data.Rdata'

### Cleaned data


### Cleaned data

We provide the following tab-separated files:

- Compare the level of affective language used: "hargrave_no_2022-affect.tsv"
- Compare the level of aggressive language used: "hargrave_no_2022-aggression.tsv"
- Compare the level of complex language used: "hargrave_no_2022-complexity.tsv"
- Compare the level of factual language used: "hargrave_no_2022-fact.tsv"
- Compare the level of human narrative used: "hargrave_no_2022-human_narrative.tsv"
- Compare the level of negative emotions used: "hargrave_no_2022-negative_emotion.tsv"
- Compare the level of positive emotions used: "hargrave_no_2022-positive_emotion.tsv"
- Compare the level of repetitiveness used: "hargrave_no_2022-repetition.tsv"

Each of these files has the following columns:

- pair_id: unqiue text pair ID
- text1_id: unique ID of first text  in pair (i.e., text1)
- text2_id: unique ID of second text in pair (i.e., text2)
- text1: text of first sentence
- text2: text of second sentence
- label: comparison label ("text1" if text1 has been judged more intense, "text2" if text1 has been judged more intense, and "both" if text1 and text2 were judged equally intense)
- metadata__intercoder: `TRUE` if the pair was in the set the authors' used to asses intercoder reliability
- metadata__comparison: numeric comparison label (1 if label "text1", -1 if "text2", 0 if "both")
- metadata__intensity1: majority winner label of coders' sentence-level intensity ratings for text 1 (if exists)
- metadata__intensity1_num: median value of coders' sentence-level intensity ratings for text 1
- metadata__intensity2: majority winner label of coders' sentence-level intensity ratings for text 2 (if exists)
- metadata__intensity2_num: median value of coders' sentence-level intensity ratings for text 2
