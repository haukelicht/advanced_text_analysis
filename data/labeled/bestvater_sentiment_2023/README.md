# Measuring sentiment and stance in tweets and survey responses from Bestvater & Monroe (2023)

author: Hauke Licht & Naomi Yagai\
date: 2024-01-30

### Description

In their 2023 *Political Analysis* paper "Sentiment is Not Stance: Target-Aware Opinion Classification for Political Text Analysis," Bestvater and Monroe classified the sentiment (positive/negative) and stance (approving/opposing) of three datasets:

1. tweets containing opinions about the 2017 Women's March
2. open-ended survey responses expressing opinions on Donald Trump
3. tweets expressing opinions about the 2018 nomination of Brett Kavanaugh to the U.S. Supreme Court

They compared measurements of supervised classifiers trained on either human-coded samples (tweets about the Women's March and Brett Kavanaugh) or automatically labeled samples (open-ended survey responses) with those of dictionary-based approaches.

## Tweets about the Women's March

### The raw data

The authors randomly sampled 20,000 English tweets from the corpus of Felmlee et al. (2020).

Felmee et al. (2020) collected 2.5 million geo-located tweets about the 2017 Women's March and its sister marches to examine the sentiment of discourse around the movement as well as how it varied geographically (excluding Alaska and Hawaii).

According to Felmee et al. (2020), article section "Methods" (pp. 7),

> Geo-located tweets were collected for the entire continental U.S. using the Twitter Streaming Application Programming Interface (API)....
Tweets were collected for the 20th, 21st and 22nd January 2017 and saved to a text file in JSON format using a node.js application.
Messages about the March were identified using terms specific to the event (i.e., women, march, women(s)march, woman(s)march)....
We searched for these terms, and for combinations of the terms, to identify tweets related to the March....
retweets were not included.

The authors also explain about the corpus and their sampling in their article section "2. Example I: Sentiment and Stance in Tweets About the 2017 Women’s March" (pp. 237-238).

### Annotation procedure

The annotation procedure is described in the supplementary materials "Appendix".

The annotation was performed by two coders using the annotation platform Labelbox.
The coders were shown a target (either the Women's March or the confirmation of Brett Kavanaugh, in this case, the former) along with the text of a tweet on that topic.
They were asked to answer two questions about the text: 1) whether the general sentiment of the language used in the text is positive or negative and 2) whether the specific stance the author expresses toward the provided target is approving or opposing. 
They maximized the number of unique texts each coder labelled following Barbera et al. (2021). 
However, they selected samples of 211 tweets to be annotated by both coders to check inter-coder reliability.

Each tweet was coded by each coder along two coding dimensions.

-   *sentiment:* 1 if the sentiment of the language used in the text is positive, 0 if negative.
-   *stance:* 1 if the specific stance the author expresses toward the provided target is approving, 0 if opposing.

### The data

source: replication data on Harvard Dataverse: <https://dataverse.harvard.edu/file.xhtml?fileId=5374866&version=1.0> in the file 'WM_tweets_groundtruth.tsv'

### Problems

The double-coded tweets to check inter-coder reliability were included in the original dataset. 
Since a majority winner does not exist in these tweets, they were removed from the dataset to prevent contradicting annotations.

### Cleaned data

Corresponding to the analysis, we provide the following CSV files:

- sentiment classification: 
"bestvater_sentiment_2023-womensmarch_tweets_sentiment.tsv"
    - column 'label' indicates the annotation: 1 if the sentiment is positive, 0 if negative.
    - column 'text' records the coded tweet.
    - column 'metadata__row_number' indicates the original row number of each tweet before cleaning the data. 

- stance classification: 
"bestvater_sentiment_2023-womensmarch_tweets_stance.tsv"
    - column 'label' indicates the annotation: 1 if the stance the author expresses towards the Women's March is approving, 0 if opposing.
    - column 'text' records the coded tweet.
    - column 'metadata__row_number' indicates the original row number of each tweet before cleaning the data. 
    

## Open-ended survey responses on Trump

### The raw data

The Mood of the Nation poll (MOTN) regularly field from YouGov and the McCourtney Institute of Democracy at Penn State is a nationally-representative survey in the U.S. that focuses on collecting and analyzing free-form text responses.

According to their article section "4 Example II: Sentiment and Stance in Open-Ended Survey Responses About Donald Trump" (pp. 245-246),

> The corpus used in this example is drawn from nine MOTN waves, conducted between November 16, 2016 and September 26, 2019. 
We pool survey waves and questions to generate a corpus of 35,842 documents, where each document is a response to one of the four core open-ended questions (“what about American politics makes you feel proud, hopeful, angry, and worried”).
Then, we subset the corpus to just documents that mention Donald Trump, for a final N of 7,146.
These documents are then automatically labeled for sentiment and stance. 

The corpus is in English.

### Annotation procedure

The annotation is explained in their article section "4. Example II: Sentiment and Stance in Open-Ended Survey Responses About Donald Trump" (pp. 246).

The corpus pools responses to one of the four core open-ended questions (as explained above) that mention Donald Trump. 
Regarding that these questions are sentiment-laden in construction, for sentiment, responses to the *proud* or *hopeful* question were labelled positive and responses to the *angry* and *worried* questions were labelled negative. 
Since every document is associated with the respondent's answers to other closed-form responses, the stance was labelled either supportive or opposing towards Donald Trump from other objective measures of approval contained in the survey.

Each survey response was coded automatically along two coding dimensions.

-   *sentiment:* 1 to the responses to the *proud* and *hopeful* questions, 0 to the responses to the *angry* and *worried* questions.
-   *stance:* 1 if the stance expressed by the author towards Donald Trump is supportive, 0 if opposing (based on other objective measures of approval in the survey).

### The data

source: replication data on Harvard Dataverse: <https://dataverse.harvard.edu/file.xhtml?fileId=5374876&version=1.0> in the file 'MOTN_responses_groundtruth.tsv'

### Problems

There was a large number of duplicating text with contradicting annotations in the original dataset. 
Most of these were short text consisting one or few words e.g., "a new president", "donald trump", "donald trump election".
Thus, it is assumed that different authors wrote the same phrase in different question types or expressed different stances in other objective measures. 
Since the original dataset does not include an ID variable, these different observations (authors) could not be distinguished. 
Thus, these texts with contradicting annotations (mostly neutral statements) were removed from the dataset to prevent inconsistent labeling.

### Cleaned data

Corresponding to the analysis, we provide the following CSV files:

- sentiment classification: 
"bestvater_sentiment_2023-motn_responses_sentiment.tsv"
    - column 'label' indicates the annotation: 1 to the responses to the *proud* and *hopeful* questions, 0 to the responses to the *angry* and *worried* questions.
    - column 'text' records the coded survey response.
    - column 'metadata__wavenum' indicates the number of the MOTN wave.
    - column 'metadata__ideo5' indicates the author's ideological stance on a 5 scale. 
    The following 6 variables are included: "Very liberal", "Liberal", "Moderate", "Conservative", "Very conservative", and "Not sure".
    - column 'metadata__row_number' indicates the original row number of each survey response before cleaning the data. 

- stance classification: 
"bestvater_sentiment_2023-motn_responses_stance.tsv"
    - column 'label' indicates the annotation: 1 if the stance expressed by the author towards Donald Trump is supportive, 0 if opposing (based on other objective measures of approval in the survey).
    - column 'text' records the coded survey response.
    - column 'metadata__wavenum' indicates the number of the MOTN wave.
    - column 'metadata__ideo5' indicates the author's ideological stance on a 5 scale. 
    The following 6 variables are included: "Very liberal", "Liberal", "Moderate", "Conservative", "Very conservative", and "Not sure".
    - column 'metadata__row_number' indicates the original row number of each survey response before cleaning the data. 


## Tweets about Brett Kavanaugh

### The raw data

The authors sampled 3,660 English tweets from the corpus of Baumgartner (2018) regarding the contentious hearing of Brett Kavanaugh, who was accused for sexual assault while nominated for the U.S. Supreme Court.

According to their article section "5. Example III: Sentiment and Stance in Tweets About the Kavanaugh Confirmation" (pp. 249),

> While the hearings were underway, Baumgartner (2018) collected a corpus of over 50 million tweets about Kavanaugh, the confirmation process, and the assault allegations which we sample for this example and hand-code for sentiment and stance values as in the Women’s March example. 

No information of the original dataset could be obtained since the link attached in the article is not accessible.

### Annotation procedure

The annotation procedure is described in the supplementary materials "Appendix".

The annotation was performed by two coders using the annotation platform Labelbox.
The coders were shown a target (either the Women's March or the confirmation of Brett Kavanaugh, in this case, the latter) along with the text of a tweet on that topic.
They were asked to answer two questions about the text: 1) whether the general sentiment of the language used in the text is positive or negative and 2) whether the specific stance the author expresses toward the provided target is approving or opposing. 
They maximized the number of unique texts each coder labelled following Barbera et al. (2021). 
However, they selected samples of 200 tweets to be annotated by both coders to check inter-coder reliability.

Each tweet was coded by each coder along two coding dimensions.

-   *sentiment:* 1 if the sentiment of the language used in the text is positive, 0 if negative.
-   *stance:* 1 if the specific stance the author expresses toward the provided target is approving, 0 if opposing.

### The data

source: replication data on Harvard Dataverse: <https://dataverse.harvard.edu/file.xhtml?fileId=5374859&version=1.0> in the file 'kavanaugh_tweets_groundtruth.tsv'

### Problems

The double-coded tweets to check inter-coder reliability were included in the original dataset. 
Since a majority winner does not exist in these tweets, they were removed from the dataset to resolve contradicting annotations.

### Cleaned data

Corresponding to the analysis, we provide the following CSV files:

- sentiment classification: 
"bestvater_sentiment_2023-kavanaugh_tweets_sentiment.tsv"
    - column 'label' indicates the annotation: 1 if the sentiment is positive, 0 if negative.
    - column 'text' records the coded tweet.
    - column 'metadata__row_number' indicates the original row number of each tweet before cleaning the data. 

- stance classification: 
"bestvater_sentiment_2023-kavanaugh_tweets_stance.tsv"
    - column 'label' indicates the annotation: 1 if the stance the author expresses towards Brett Kavanaugh is approving, 0 if opposing.
    - column 'text' records the coded tweet.
    - column 'metadata__row_number' indicates the original row number of each tweet before cleaning the data. 
