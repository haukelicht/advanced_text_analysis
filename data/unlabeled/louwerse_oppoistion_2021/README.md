# Opposition member speeches in COVID-19 debates in the UK *House of Commons*

author: Hauke Licht
date: 2024-09-23

## Description

In their 2021  paper "Opposition in times of crisis: COVID-19 in parliamentary debates", Tom Louwerse, Ulrich Sieberer, Or Tuttnauer, and Rudy B. Andeweg analyse how opposition parties expressed sentiment vis-à-vis government actions and policies during the first six months of 2020. 

## The data

Their original data collection covered four established parliamentary democracies: Germany, Israel, Netherlands, United Kingdom (UK).

We have obtained the UK corpus from the authors through email request.

### Cleaned data

We provide a CSV with the following columns:

- date: date of the debate
- debate_subject: subject/title of the debate
- speech_id: unique speech identifier
- speaker_id: unique speaker identifier
- speaker_name: name of the speaker
- speaker_party: party the speaker represented
- speaker_role: role of the speaker in the parl. organization
- chair: boolean indicator, TRUE if speech by the session chair 
- text: text of the speech. double white spaces "  " separate sentences
- words: number of words in the speech
