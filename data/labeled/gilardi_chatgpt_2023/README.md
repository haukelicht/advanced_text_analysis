# Gilardi et al. (2023): Evaluating ChatGPT for text classification

author: Hauke Licht\
date: 2024-02-25

## Description

In their 2023 PNAS paper "ChatGPT outperforms crowd workers for text-annotation tasks", 
Fabrizio Gilardi, Meysam Alizadeh, and Maël Kubli
evaluate the performance of ChatGPT in zero-shot text classification.

## The data 

Their replication data records a sample of 6,183 documents, including tweets and news articles from Alizadeh et al. ([2022](https://doi.org/10.51685/jqd.2022.023)) and tweets posted in 2023 (not in training data of first ChatGPT model).

The replication materials are available at https://doi.org/10.7910/DVN/PQYF6M

## Annotation procedure

Their study focuses on content related to the topic of content moderation.

Their data contains four corpora

1. a corpus of tweets posted pre-2023 by common Twitter user relating to the topic of content moderation
2. a simlar corpus of tweets posted by common Twitter users in 2023 (not covered by the ChatGPT model they evaluated)  relating to the topic of content moderation
3. tweets posted by Members of the U.S. Congress relating to the topic of content moderation
4. news article headlines (plus first 200 words of article full text) relating to the topic of content moderation

Which annotation task they applied depended on the corpus

### "Common user" tweets

For "common user" tweets, they collect annotations along the five coding dimenions:

- *relevance*: determine whether a tweet is about content moderation or not
	- label classes: "relevant" (1), "irrelevant" (0)
- *problem/solution frame*: classify whether a tweet frames content moderation as solution, a problem, neither, or both
	- label classes: "problem", "solution", "neither", "both"
- *policy frame*: classify the policy issue emphasized in the tweet when discussing content moderation
	- label classes: 15 categories, ranging from "economy" to "cutlural identity"
- *stance detection*: classify whether tweet expresses a positive stance towards Section 230, a negative stance, or a neutral stance
	- label classes: "negative", "neutral", "positive"
- *topic detection*: classify what other related topics the tweet discusses
	- label classes: "section 230", "trump ban", "complaints", "twitter support", "platform policies", and "other" 

### Member of Congress tweets

For Member of Congress tweets, they collect annotations along two coding dimenions:

- *relevance*: is the tweet discussing a political issue
	- label classes:  "relevant" (1), "irrelevant" (0)
- *policy frame*: classify the policy issue emphasized in the tweet when discussing content moderation
	- label classes: 15 categories, ranging from "economy" to "cutlural identity"

### News articles

For news articles, they collect annotations along two coding dimenions:

- *relevance*: determine whether a tweet is about content moderation or not
	- label classes: "relevant" (1), "irrelevant" (0)
- *problem/solution frame*: classify whether a tweet frames content moderation as solution, a problem, neither, or both
	- label classes: "problem", "solution", "neither", "both"

## The data

We have prepared the commun user tweets data, focusing on the relevance, problem/solution frame, and stance classification tasks:

1. relevance classifications: "gilardi_chatgpt_2023-content_moderation_relevance.csv"
	- column 'label' indicates the classification: 1 "relevant", 0 "irrelevant
	- column 'text' records the coded tweet's text
2. problem/solution frame classifications: "gilardi_chatgpt_2023-content_moderation_frame.csv"
	- column 'label' indicates the frame category: "problem", "solution", "neither", "both"
	- column 'text' records the coded tweet's text
3. stance classification: "gilardi_chatgpt_2023-section230_stance.csv"
	- column 'label' indicates the expressed stance on Section 230: "negative", "neutral", "positive"
	- column 'text' records the coded tweet's text
