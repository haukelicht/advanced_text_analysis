# Policy issue focus and stance in UK parliamentary speech crowd-coded by Benoit et al. (2016)

author: Hauke Licht\
date: 2024-02-25

## Description

In their 2016 *American Political Science Research* paper "Crowd-sourced Text Analysis: Reproducible and Agile Production
of Political Data"
Kenneth Benoit,
Drew Conway,
Benjamin E. Lauderdale,
Michael Laver, and
Slava Mikhaylov
demonstrate that crowd workers can be reliable political text coders.

In their empirical analyses, they distribute a sample of sentence taken from UK parties' election manifestos and parliamentary speeches in the UK House of Commons to crowd workers for coding along two main dimensions:

- policy area focus
- policy issue stance

They aggregate coders' judgments at the sentence level and evaluate the resulting annotations accuracy in a sample of expert-labeled gold-standard examples.

## Paper metadata

- article: https://doi.org/10.1017/S0003055416000058
- supporting materials: https://static.cambridge.org/content/id/urn:cambridge.org:id:article:S0003055416000058/resource/name/S0003055416000058sup001.pdf
- replication materials: https://github.com/kbenoit/CSTA-APSR

## Annotation procedure

Their analyses cover three applications:

1. policy area and policy issue stance classification in the areas of economic and social policy based on party manifestos
2. policy area and policy issue stance classification in the areas of immigration policy in parliamentary speeches
3. policy issue stance classification in the areas of state subsidies in parliamentary speeches

### 1. Economic and social policy area and issue stance classification

The corpus is compiled from the British Labour, Conversvative, and Liberal Democrats' election manifestsos. 

The annotation procedure is described in section "A METHOD FOR REPLICABLE CODING OF POLITICAL TEXT", "A simple coding scheme for economic and social policy" (p. 281)

> Our scheme first asks readers to classify each sentence in a document as referring to economic policy (left or right), to social policy (liberal or conservative), or to neither.
> ...
> If a sentence was classified as economic policy, we then ask readers to rate it on a fivepoint scale from very left to very right ...
> those classified as social policy were rated on a five-point scale from
liberal to conservative.

Sentences' policy area is indicated with the following label categories:

- 2: "economic policy"
- 3: "social policy"
- 1: neither

For sentence is category 2 ("economic policy"), stance labels are:

- -2: very left
- -1: somewhat left
-  0: neither left nor right
-  1: somewhat right
-  2: very right

For sentence is category 3 ("social policy"), stance labels are:

- -2: very liberal
- -1: somewhat liberal
-  0: neither liberal nor conservative
-  1: somewhat conservative
-  2: very conservative

### 2. Immigration policy area and issue stance classification

In this analysis, the paper authors assess the ability of crowd workers to reliably code stances on a specific issue: immigration.

The corpus used and annotation procedure applied in this analysis is described in section "CROWD-SOURCING DATA FOR SPECIFIC PROJECTS: IMMIGRATION POLICY" (pp. 289f.)

The corpus consists of sentences taken from the 2010 UK general election manifestos of eight parties.
The annotation procedure

> asked [workers] to label each sentence as referring to immigration policy or not.
> If a sentence did cover immigration, [workers] were
asked to rate it as pro- or anti-immigration, or neutral.

Whether or not a sentece refers to the issue of immigration is indicated with th following labels categories:

- 1: "Not immigration policy"
- 4: "Immigration policy"

**_Note:_** They use 4 to complement the labels used in their econ/social policy area classification scheme.

For sentence is category 4 ("Immigration policy"), stance labels are:

- -1: "Favorable and open immigration policy"
-  0: neutral
-  1: "Negative and closed immigration policy"

**_Note:_** They use -1 (1) for the positive (negative) stance in keeping with the political science convention of putting high stances on the positive pole of ideology scales.

## 3. Policy issue stance classification in the areas of state subsidies in parliamentary speeches

In this analysis, the paper authors assess the ability of crowd workers to reliably code non-English texts.

The corpus is described in section "CROWD SOURCED TEXT ANALYSIS IN OTHER CONTEXTS AND LANGUAGES" (pp. 290f.).
The corpus is compiled from 36 speeches given in the European Parliament in a debate about a Commission report proposing an extension to a regulation permitting state aid to uncompetitive coal mines. 
All speeches were officially translated into each of the EU's 24 official language. (cf. p. 291)
The paper authors distributed a sample of speech sentence in their English, German, Spanish, Italian, Polish, and Greek versions to crowd coders

The annotation instructions are reported in the supporting materials, section "7. Instructions for Coding sentences from a parliamentary debate" (p. 28).
The task instructions read

> Your key task is to judge individual sentences from the debate according to which of two
contrasting positions they supported:
> -- Supporting the rapid phase-out of subsidies for uncompetitive coal mines. This was the essence of the council proposal, which would have let subsides end while offering limited state aid until 2014 only.
> -- Supporting the continuation of subsidies for uncompetitive coal mines. In the strong form, this involved rejecting the Commission proposal and favoring continuing subsidies indefinitely. In a weaker form, this involved supporting the compromise to extend limited
state support until 2018.

The stance clasification label categories are 

- -1: "Anti-subsidy"
-  0: "Neutral or inapplicable" 
-  1: "Pro-subsidy"

## The data

corresponding to the three analysis and separate classification tasks, we provide the following CSV files:

- 1: economic/social policy area classification: "benoit_crowdsourced_2016-policy_area.csv"
	- column 'label' indicates the policy area: 2 "economic policy", 3 "social policy", 1 "neither"
	- column 'text' records the coded manifesto sentence
	- columns 'metadata__pre_sentence' and 'metadata__post_sentence' reocord coded sentences' preceeding and following sentences (if any)
- 1.1: economic policy stance classification: "benoit_crowdsourced_2016-econ_policy_stance.csv"
	- subset of sentences coded into policy area 2 ("economic policy")
	- column 'label' indicates the policy issue stance (-2 left <-> 2 right)
	- column 'text' records the coded manifesto sentence
	- columns 'metadata__pre_sentence' and 'metadata__post_sentence' reocord coded sentences' preceeding and following sentences (if any)
- 1.2: social policy stance classification: "benoit_crowdsourced_2016-social_policy_stance.csv"
	- subset of sentences coded into policy area 3 ("social policy")
	- column 'label' indicates the policy issue stance (-2 liberal <-> 2 conservative)
	- column 'text' records the coded manifesto sentence
	- columns 'metadata__pre_sentence' and 'metadata__post_sentence' reocord coded sentences' preceeding and following sentences (if any)
- 2: immigration policy area classification: "benoit_crowdsourced_2016-immigration_policy.csv"
	- column 'label' indicates the policy area: 4 "immigration policy", 1 "not immigration policy"
	- column 'text' records the coded manifesto sentence
	- columns 'metadata__pre_sentence' and 'metadata__post_sentence' reocord coded sentences' preceeding and following sentences (if any)
- 2.1: immigration policy stance classification: "benoit_crowdsourced_2016-immigration_policy_stance.csv"
	- column 'label' indicates the policy issue stance (-1 favorabl/open <-> 1 negative/closed)
	- column 'text' records the coded manifesto sentence
	- columns 'metadata__pre_sentence' and 'metadata__post_sentence' reocord coded sentences' preceeding and following sentences (if any)
- 3: subsidies policy stance classification: "benoit_crowdsourced_2016-subsidies_stance.csv"
	- column 'label' indicates the policy issue stance (-1 pro <-> 1 contra)
	- column 'text' records the coded speech sentences
	- columns 'metadata__language' indicates a text's language
	- column 'metadata__sentence_id' indicates the sentence ID that is the same for a sentence's different language versions
	- columns 'metadata__pre_sentence' and 'metadata__post_sentence' reocord coded sentences' preceeding and following sentences (if any)