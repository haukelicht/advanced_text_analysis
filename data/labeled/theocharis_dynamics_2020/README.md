# Measuring incivility in tweets from Theocharis et al. (2020)

author: Hauke Licht & Naomi Yagai\
date: 2024-01-30

## Description

In their 2020 *SAGE Open* paper "The Dynamics of Political Incivility on Twitter," Theocharis and his colleagues measure incivility in public responses to messages shared by Members of Congress in the United States on Twitter (civil/uncivil).

Their measurements are generated through supervised classification trained on human-coded samples.

## The raw data

The authors explain the data in their article section "Data Collection and Case Selection" (pp. 6) as follows.

> To initiate our data collection, we relied on the list of Twitter accounts of Members of Congress elected to the 115th Congress (2017-2018) available in the *unitedstates* GitHub account. 
We then downloaded all tweets that mention any of these politicians’ Twitter accounts directly from Twitter’s Streaming API (application programming interface).
Our full data set contains a total of 16,002,098 tweets mentioning a Member of Congress from October 17, 2016, until December 13, 2017.

The corpus is in English.

## Annotation procedure

Their annotation procedure is described in their article section "Method" (pp. 6-7).

Coders were selected through the online platform CrowdFlower (now called Figure Eight). 
4,000 tweets were randomly sampled from their full dataset. 
Each tweet was labelled by coders using the coding scheme explained below. 
Following standard best practices for crowd-coding (Benoit et al., 2016), inter-coder reliability was ensured by using CrowdFlower's quiz mode option, which discards coders whose agreement with a small set of "gold" posts that the authors labelled manually is lower than 80%.

Each tweet was coded by each coder as either civil or uncivil following the below instructions for each category (explained in section "Automatic Detection of Incivility in Social Media Posts", pp. 6-7).

-   *uncivil:* yes if labelled as uncivil, no if labelled as civil.

> *Civil:* a tweet that adheres to politeness standards, that is, written in a well-mannered and non-offensive way. 
Even if it criticises the Member of Congress, it does so in a respectful way. 
For example: "You are going to have more of the same with HRC, and you are partly responsible. Very disappointed in all of you in DC" or "Fantastic article! I appreciate your understanding of the weaknesses of #medicaid, thanks for your leadership!"

> *Uncivil:* an ill-mannered, disrespectful tweet that may contain offensive language.
This includes threatening one's rights (freedom to speak, life preferences), assigning stereotypes or hate speech, name-calling ("weirdo," "traitor," "idiot"), aspersion ("liar," "traitor"), pejorative speak or vulgarity, sarcasm, ALL CAPS, and incendiary, obscene, and/or humiliating language. 
For example: "Just like the Democrat taliban party was upfront with the AHCA. Hypocrites" or "Oh shut up David. You're a bore."

The authors also gave coders the following additional instructions:

> Note: we understand that civility can be subjective. 
Here we are looking not for your opinion, but rather what you think most people would respond in this situation. 
For example, some people may not find the word "weirdo" offensive, but generally it is considered impolite when it is used as an insult.

This coding scheme was inspired by the codebook developed by Theocharis, Y., Barberá, P., Fazekas, Z., Popa, S. A., & Parnet, O. (2016). A bad workman blames his tweets: The consequences of citizens' uncivil Twitter use when interacting with party candidates. *Journal of Communication*, 66(6), 1007-1031. <https://doi.org/10.1111/jcom.12259>

Theocharis et al. (2016) measured incivility by combining information in their categories "impolite versus polite" and "morality/democracy".
According to their article section "Automatic classification of social media posts" (pp. 1014),

> *Polite versus impolite* distinguishes between tweets that are written in a well-mannered and nonoffensive way versus tweets that are ill mannered, disrespectful, or contain offensive language.

> *Morality/Democracy* refers to whether the tweet contains a reference to moral and/or democracy issues, which are roughly covered by the Freedom and Democracy Domain and the Social Fabric Domain present in the EP Election Study 1979–2009, Manifesto Study (Braun et al., 2015).

The authors explain that

> We consider incivility as a subcategory of impolite tweets that also refer to moral issues or democracy (e.g., tweets that make reference to one of the following topics: freedom and human rights, traditional morality, law and order, social harmony, freedom and human rights, democracy, constitutionalism). 
The basic assumption that guides our operationalization is that impolite remarks with direct democratic consequences constitute an uncivil tweet. 
To be more specific, by making impolite remarks such tweets stereotype and offend individuals/social groups and/or challenge their freedoms/rights, disrespecting thus collective democratic traditions. 


## The data

source: replication data on GitHub: <https://github.com/pablobarbera/incivility-sage-open/blob/master/data/perspective-scores-training.csv>, 'perspective-scores-training.csv' in file 'data'

### Cleaned data

Corresponding to the analysis, we provide the following CSV file:

- incivility classification: 
"theocharis_dynamics_2020-tweets-incivility.csv"
    - column 'label' indicates the annotation: "yes" when labeled as uncivil, "no" when labeled as civil
    - column 'text' records the coded tweets
    - column 'metadata__created_at' records the date and time the tweet was created as a character value. e.g., "Tue Apr 04 05:31:44 +0000 2017"
    - column 'metadata__toxicity' records the prediction score of the tweet for the negative speech category "toxicity" produced by Google's Perspective API
    - column 'metadata__severe_toxicity' records the prediction score of the tweet for the negative speech category "severe toxicity" produced by Google's Perspective API
    - column 'metadata__identity_attack' records the prediction score of the tweet for the negative speech category "identity attack" produced by Google's Perspective API
    - column 'metadata__insult' records the prediction score of the tweet for the negative speech category "insult" produced by Google's Perspective API
    - column 'metadata__profanity' records the prediction score of the tweet for the negative speech category "profanity" produced by Google's Perspective API
    - column 'metadata__sexually_explicit' records the prediction score of the tweet for the negative speech category "sexually explicit" produced by Google's Perspective API
    - column 'metadata__threat' records the prediction score of the tweet for the negative speech category "threat" produced by Google's Perspective API
    - column 'metadata__flirtation' records the prediction score of the tweet for the negative speech category "fliration" produced by Google's Perspective API
    - column 'metadata__attack_on_author' records the prediction score of the tweet for the negative speech category "attack on author" produced by Google's Perspective API
    - column 'metadata__attack_on_commenter' records the prediction score of the tweet for the negative speech category "attack on commenter" produced by Google's Perspective API
    - column 'metadata__incoherent' records the prediction score of the tweet for the negative speech category "incoherent" produced by Google's Perspective API
    - column 'metadata__inflammatory' records the prediction score of the tweet for the negative speech category "inflammatory" produced by Google's Perspective API
    - column 'metadata__likely_to_reject' records the prediction score of the tweet for the negative speech category "likely to reject" produced by Google's Perspective API
    - column 'metadata__obscene' records the prediction score of the tweet for the negative speech category "obscene" produced by Google's Perspective API
    - column 'metadata__spam' records the prediction score of the tweet for the negative speech category "spam" produced by Google's Perspective API
    - column 'metadata__unsubstantial' records the prediction score of the tweet for the negative speech category "unsubstantial" produced by Google's Perspective API
    - column 'metadata__row_number' indicates the original row number of each tweet before cleaning the data 
    
Note that external machine learning scores produced by Google's Perspective API is included in the data. 
This is because the authors ran all 20,000 tweets (the 4,000 original tweets annotated by human coders and the 16,000 additional tweets) through this API to improve the performance of their classifier by increasing their training set. 
Specifically, they first fit a classifier with the 4,000 original labels using the API's prediction scores as features.
They then predicted the labels for the additional 16,000 tweets.
Using these additional samples, they further train their classifier to predict incivility in their entire corpus.

According to the authors,

> Google’s Perspective API (application programming interface) generates predictions for a variety of negative speech categories, such as “toxic,” “hate speech,” “attacks,” and “profanity. (pp. 13)

For details, please check their article pp. 3, endnote 2 (pp. 13).
