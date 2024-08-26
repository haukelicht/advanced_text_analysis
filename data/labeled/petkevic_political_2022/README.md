# Negativity in campaign tweets coded from Petkevic & Nai (2022)

author: Hauke Licht & Naomi Yagai\
date: 2024-01-24

## Description

In their 2022 *American Politics Research* paper "Political Attacks in 280 Characters or Less: A New Tool for the Automated Classification of Campaign Negativity on Social Media," Petkevic and Nai measure the negativity in candidate's campaign tweets in the 2018 U.S. Senate Midterms. 
They identify the presence/absence of four phenomena:

- negative tone
- policy attack
- personal attack
- incivility

Their measurements are generated through a neural network classifier they trained on human-coded samples.

## The raw data

The authors explain the data in their article section "Measuring Negative Campaigning in Tweets", "Data and Procedure" (pp. 281) as below.

> The data (tweets) used in this study were collected via vicinitas.io, a website that allows for bulk downloading of tweets retroactively based on Twitter handles (usernames).
> Prior to it, an online search for Twitter pages of all contemporaneous Senate election candidates was performed to determine which of the candidates used Twitter for their political campaigns and what their Twitter handles were.
> The handles were then supplied to vicinitas.io to collect the tweets for the period of September 1, 2018 -- November 6, 2018 (the day of the election), for a total of N = 16,173 tweets. 

They additionally note that
> Three candidates did not, to the best of our knowledge, post any tweets in that period (even though they do have a twitter handle)... 
> The analyses discussed in this article thus concern the 63 remaining candidates. 
> The number of tweets per candidate collected varies considerably, from N = 24 ... to N = 1028 ... with an average of 256.7 tweets per candidate.

The corpus is in English.

## Annotation procedure

The annotation procedure is described in their article section "Measuring Negative Campaigning in Tweets", "Data and Procedure" (pp. 281).

> First, a random sample of 200 tweets was coded by four coders independently to check inter-coder reliability. 
> Regarding suboptimal scores, the codebook was reworked by analysing tweets where disagreements occurred and coders were consulted to establish systematic differences in the interpretation of negativity dimensions. 
> After introducing the new instructions, each coder was provided 100 tweets to annotate on each dimension. 
> This revealed the imbalance between labels since the majority was coded absent.
> Thus, each coder was provided multiple random samples to annotate until at least 200 were coded "present" for the respective dimension.

Each tweet was coded by each coder along four coding dimensions:

- *neg_tone:* 1 if present, 0 if absent in a given tweet
- *pol_att:* 1 if present, 0 if absent in a given tweet
- *pers_att:* 1 if present, 0 if absent in a given tweet
- *incivil:* 1 if present, 0 if absent in a given tweet

The authors have shared the final codeobok (i.e., coding instructions) with us via email on June 6, 2024.
They provide further descriptions of the coding dimensions and label categories:

- *Negative* tone: Attack or critique of opponent
  - 1: Presence of explicit attack or critique toward opponent
  - 0: No explicit attack or critique toward opponent
- *Policy attack: Attack or critique of a policy position of the opponent
  - 1: Presence of explicit attack or critique toward a policy proposition, political position, record once in office, ideas of the opponent
  - 0: No explicit attack or critique toward a policy proposition, political position, record once in office, ideas, of the opponent
- *Personal attack*: Attack or critique of the character or persona of the opponent
  - 1: Presence of explicit attack or critique of the character, profile, personality, persona, figure, image, aspect, physical attributes of the opponent
  - 0: No explicit attack or critique of the character, profile, personality, persona, figure, image, aspect, physical attributes of the opponent
- *Incivility*: Use of an uncivil language in the attack
  - 1: Use of a harsh, shrill, uncivil, offensive, vulgar language used in the attack (code only in the attack!)
  - 0: Normal and civil language in the attack, without use of a harsh, shrill, uncivil, offensive, vulgar language used in the attack


## The data

The raw data is available on OSF: https://osf.io/up826/files/osfstorage/5e3d6dc8f1369e01818acfa0


### Cleaned data

Corresponding to the analysis, we provide the following CSV files:

- identification of negative tone:
        "petkevic_political_2022-campaigntweets_negative_tones.csv"
    - column 'label' indicates the annotation: 1 when present, 0 when absent
    - column 'text' records the coded tweets
    - column 'metadata__row_number' indicates the original row number
      of each tweet before cleaning the data

- identification of policy attack:
  "petkevic_political_2022-campaigntweets_policy_attacks.csv"
    - column 'label' indicates the annotation: 1 when present, 0 when absent
    - column 'text' records the coded tweets
    - column 'metadata__row_number' indicates the original row number
      of each tweet before cleaning the data     

- identification of personal attack:
  "petkevic_political_2022-campaigntweets_personal_attacks.csv"
   - column 'label' indicates the annotation: 1 when present, 0 when absent
   - column 'text' records the coded tweets
   - column 'metadata__row_number' indicates the original row number
     of each tweet before cleaning the data

- identification of incivility:
  "petkevic_political_2022-campaigntweets_incivility.csv"
   - column 'label' indicates the annotation: 1 when present, 0 when absent
   - column 'text' records the coded tweets
   - column 'metadata__row_number' indicates the original row number
     of each tweet before cleaning the data
