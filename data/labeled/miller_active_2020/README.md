# Identifying policy areas or sentiment in tweets, Wikipedia talk pages, and news articles from Miller, Linder & Mebane (2020)

author: Hauke Licht & Naomi Yagai\
date: 2024-01-30

## Description

In their 2020 *Political Analysis* paper "Active Learning Approaches for Labeling Text: Review and Assessment of the Performance of Active Learning Approaches," Miller and his colleagues contribute three human-annotated text datasets:

1. tweets by German Twitter users coded for whether a tweet is about the refugee topic (yes/no)
2. comments on the Wikipedia talk page coded (yes/no) on multiple dimensions: toxic, severely toxic, obscene, threat, insult, and identity-based hate speech
3. articles from the Breitbart news website coded for whether they contain specific references to Muslim identity (yes/no)

Their measurements are generated through an active learning approach based on human-coded samples.

## Dataset 1: Tweets about refugee topic

### The raw data

The dataset is obtained from Linder (2017) which studied public reactions to refugee allocation in the 2015 German refugee crisis. 
Linder (2017)'s dataset was constructed based on a larger set of tweets collected by Barberá (2016): <http://pablobarbera.com/static/less-is-more.pdf>.

Although Linder (2017) does not specify which data is taken from Barberá (2016), based on the time frame, it is assumed that the author used the data mentioned in the article section "Applications: Estimating Public Opinion with Social Media Data and Sociodemographic Weights".
Here, it is assumed that tweets were collected from 3.3 billion Twitter users around the world from the beginning of 2015 to the beginning of 2016 (for further verification, please check Barberá, 2016).

Linder (2017) then selected a random sample of 25,000 German Twitter users and collected approximately 5 million tweets of these 25,000 users from the Twitter search API. 
To construct the corpus, a random sample of 24,420 tweets from all tweets in German language was subset from the larger dataset.

For details, check Linder (2017), article section "8.1 Data" (pp. 23-24). <http://dx.doi.org/10.2139/ssrn.3026393>

The authors also explain about the corpus in their article section "4.1 Data" (pp. 540).

### Annotation procedure

The obtained dataset is fully annotated by Linder (2017).
The corpus was coded by German-speaking coders selected from the online platform CrowdFlower (now called Figure Eight).
Each tweet was labeled as being about the refugee topic or not.
In a pilot study, 3000 tweets were annotated by three Crowdflower workers as well as the author (Linder), performing an intercoder agreement of 93% (check Linder: 2017, article section "8.1 Data", pp. 23-24).
Of all 24,000 tweets, about 700 are labeled as being about a refugee topic. 

The authors explain about the annotation in their article section "4.1 Data" (pp. 540).

The authors used these labels in the obtained dataset for their simulation.

Their annotation procedure is described in their article section "4. Simulation Study" (pp. 540).

Each study simulates the data labeling process iteratively. 
First, a batch of documents was selected using the querying algorithm for active learning or random sampling for passive learning. 
Next, these documents were added to the training data available to the classifier at that iteration. 
They drew 20 documents at each iteration and stopped once they had processed 25% of the documents in the corpus or all positive samples were labelled. 
They refer to one labeling process completed in this manner as a run. 
In most cases, they repeated each run 50 times to obtain Monte Carlo estimates of the performance statistics of the various algorithms.

Note that the authors induced various degrees of class imbalance into the datasets to demonstrate the performance of the various algorithms under realistic conditions.
They created new datasets with different levels of class imbalance by oversampling and undersampling the positive class from the original corpora. 
They used the following positive class proportions: 0.01, 0.05, 0.10, and 0.50.

Each tweet was coded by each coder whether it was about a refugee topic.

-   *annotation:* 1 if it is about a refugee topic, 0 if not.

No information is found on the coding instructions in Linder (2017).

### The data

source: replication data on Harvard Dataverse: <https://dataverse.harvard.edu/file.xhtml?persistentId=doi:10.7910/DVN/T88EAX/UQ1TWY&version=1.0>, 'data' in the file 'simulation_code.zip', 'replication_materials.zip'

### Problems

The tweet ID from the original dataset is stored using scientific notations (e.g., "6.64559E+17").
Thus, the IDs are abbreviated as a result, causing duplication in the variable "metadata_tweet_id".
It must be noted that the individual Twitter accounts cannot be uniquely identified for this reason.

### Cleaned data

Corresponding to the analysis, we provide the following CSV file:

- topic classification: 
"miller_active_2020-tweets_refugeetopic.csv"
    - column 'label' indicates the annotation: 1 if it is about a refugee topic, 0 if not.
    - column 'text' records the coded tweet.
    - column 'metadata__tweet_id' indicates the ID number of the Twitter account. 
    Individual accounts are unidentifiable since the number is stored using scientific notations.
    - column 'metadata__row_number' indicates the original row number of each tweet before cleaning the data. 

Number of unique documents/text:

Label distribution: ...

## Dataset 2: Toxic comments on Wikipedia talk pages

### Description

Comments in the the Wikipedia talk page dataset are coded on six dimensions:

-   toxic
-   severe_toxic
-   obscene
-   threat
-   insult
-   identity_hate

### The raw data

The authors explain about the corpus in their article section "4.1 Data" (pp. 540) as below.

> This corpus of 159,571 Wikipedia talk page comments includes annotations
of different kinds of toxic comments. 
The database was released as part of a machine learning competition, “Toxic Comment Classification Challenge” on the website Kaggle that is sponsored by ConversationAI, a team organized by Jigsaw and Google to build “tools to help improve online conversation.” 
The goal of this competition is to classify the types of toxic comments using the provided expert annotations. 

The corpus is in English.

### Annotation procedure

The authors used a selected label in the obtained dataset for their simulation. 

Their annotation procedure is described in their article section "Simulation Study".

Each study simulates the data labeling process iteratively. 
First, a batch of documents was selected using the querying algorithm for active learning or random sampling for passive learning. 
Next, these documents were added to the training data available to the classifier at that iteration. 
They drew 20 documents at each iteration and stopped once they had processed 25% of the documents in the corpus or all positive samples were labelled. 
They refer to one labeling process completed in this manner as a run. 
In most cases, they repeated each run 50 times to obtain Monte Carlo estimates of the performance statistics of the various algorithms.

Note that the authors induced various degrees of class imbalance into the datasets to demonstrate the performance of the various algorithms under realistic conditions.
They created new datasets with different levels of class imbalance by oversampling and undersampling the positive class from the original corpora.
They used the following positive class proportions: 0.01, 0.05, 0.10, and 0.50.

Each comment was coded along six coding dimensions:

-   *toxic:* 1 if the comment is toxic, 0 if not.
-   *severe_toxic:* 1 if the comment is severely toxic, 0 if not.
-   *obscene:* 1 if the comment is obscene, 0 if not.
-   *threat:* 1 if the comment is threatening, 0 if not.
-   *insult:* 1 if the comment is insulting, 0 if not.
-   *identity_hate:* 1 if the comment is about identity hate, 0 if not.

The authors chose the label toxic for their simulation since it has the most support of all represented classes. 
They explain that 
> "Toxic" comments are aggressive comments, violent comments, personal attacks, etc. that do not contribute to a healthy and productive discussion on talk pages. (article section "4.1 Data", pp. 540)

No further information is given about the definition of other labels.

### The data

source: replication data on Harvard Dataverse: <https://dataverse.harvard.edu/file.xhtml?persistentId=doi:10.7910/DVN/T88EAX/UQ1TWY&version=1.0>, in the file 'data' in 'simulation_code.zip' in 'replication_materials.zip'

### Cleaned data

We provide the following CSV files based on the classified type of toxic comments:

- Classification of toxic comments: 
"miller_active_2020-wikipedia_hatespeech_toxic.csv"
    - column 'label' indicates the annotation: 1 if the comment is toxic, 0 if not.
    - column 'text' records the coded Wikipedia comment.
    - column 'metadata__token', 'metadata__stem', and 'metadata_lemma' respectively store the pre-processed comment in forms of token, stem, and lemma.
    - column 'metadata__row_number' indicates the original row number of each comment before cleaning the data. 
    
- Classification of severely toxic comments: "miller_active_2020-wikipedia_hatespeech_severe_toxic.csv"
    - column 'label' indicates the annotation: 1 if the comment is severely toxic, 0 if not.
    - column 'text' records the coded Wikipedia comment.
    - column 'metadata__token', 'metadata__stem', and 'metadata_lemma' respectively store the pre-processed comment in forms of token, stem, and lemma.
    - column 'metadata__row_number' indicates the original row number of each comment before cleaning the data. 
    
- Classification of obscene comments: "miller_active_2020-wikipedia_hatespeech_obscene.csv"
    - column 'label' indicates the annotation: 1 if the comment is obscene, 0 if not.
    - column 'text' records the coded Wikipedia comment.
    - column 'metadata__token', 'metadata__stem', and 'metadata_lemma' respectively store the pre-processed comment in forms of token, stem, and lemma.
    - column 'metadata__row_number' indicates the original row number of each comment before cleaning the data. 

- Classification of threatening comments:
"miller_active_2020-wikipedia_hatespeech_threat.csv"
    - column 'label' indicates the annotation: 1 if the comment is threatening, 0 if not.
    - column 'text' records the coded Wikipedia comment.
    - column 'metadata__token', 'metadata__stem', and 'metadata_lemma' respectively store the pre-processed comment in forms of token, stem, and lemma.
    - column 'metadata__row_number' indicates the original row number of each comment before cleaning the data. 

- Classification of insulting comments:
"miller_active_2020-wikipedia_hatespeech_insult.csv"
    - column 'label' indicates the annotation: 1 if the comment is insulting, 0 if not.
    - column 'text' records the coded Wikipedia comment.
    - column 'metadata__token', 'metadata__stem', and 'metadata_lemma' respectively store the pre-processed comment in forms of token, stem, and lemma.
    - column 'metadata__row_number' indicates the original row number of each comment before cleaning the data. 
    
- Classification of identity hate comments:
"miller_active_2020-wikipedia_hatespeech_identity_hate.csv"
    - column 'label' indicates the annotation: 1 if the comment is identity hate, 0 if not.
    - column 'text' records the coded Wikipedia comment.
    - column 'metadata__token', 'metadata__stem', and 'metadata_lemma' respectively store the pre-processed comment in forms of token, stem, and lemma.
    - column 'metadata__row_number' indicates the original row number of each comment before cleaning the data. 


##  Dataset 3: Breitbart news articles regarding Muslim identity

In their Breitbart articles dataset, Miller et al. indicate whether an article makes a specific reference to Muslim identity (yes/no).

### The raw data

The authors explain about the corpus in their article section "4.1 Data" (pp. 540) as below.

> This corpus of 174,847 news articles represents the population of articles on
the Breitbart news website. 
These articles each come with meta tags that are chosen by Breitbart authors and editors.
For this dataset, we use the label “Muslim identity,” which indicates whether a specific reference to Muslim identity was made in the article tags. 
This corpus is used to measure how moral and emotional frames in news media can increase support for violence against outgroups in Javed and Miller (2018). 
To make the simulations computationally more feasible we randomly sampled a subset of 25,000 articles for this study.

The corpus is in English.

No information is found about the original data from Javed and Miller (2018) since the article is unpublished.

### Annotation procedure

The authors used the selected label in the obtained dataset for their simulation.

Their annotation procedure is described in their article section "Simulation Study".

Each study simulates the data labeling process iteratively. 
First, a batch of documents was selected using the querying algorithm for active learning or random sampling for passive learning. 
Next, these documents were added to the training data available to the classifier at that iteration. 
They drew 20 documents at each iteration and stopped once they had processed 25% of the documents in the corpus or all positive samples were labelled. 
They refer to one labeling process completed in this manner as a run. 
In most cases, they repeated each run 50 times to obtain Monte Carlo estimates of the performance statistics of the various algorithms.

Note that the authors induced various degrees of class imbalance into the datasets to demonstrate the performance of the various algorithms under realistic conditions.
They created new datasets with different levels of class imbalance by oversampling and undersampling the positive class from the original corpora.
They used the following positive class proportions: 0.01, 0.05, 0.10, and 0.50.

Each news article was coded as referring to Muslim identity or not.

-   *muslim_identity:* 1 if a specific reference to Muslim identity was made in the article tags, 0 if not.

### The data

source: replication data on Harvard Dataverse: <https://dataverse.harvard.edu/file.xhtml?persistentId=doi:10.7910/DVN/T88EAX/UQ1TWY&version=1.0>, 'data' in the file 'simulation_code.zip', 'replication_materials.zip'


### Cleaned data

- Classification of toxic comments: 
"miller_active_2020-wikipedia_hatespeech_toxic.csv"
    - column 'label' indicates the annotation: 1 if the comment is toxic, 0 if not.
    - column 'text' records the coded Wikipedia comment.
    - column 'metadata__token', 'metadata__stem', and 'metadata_lemma' respectively store the pre-processed comment in forms of token, stem, and lemma.
    - column 'metadata__row_number' indicates the original row number of each news article before cleaning the data. 
