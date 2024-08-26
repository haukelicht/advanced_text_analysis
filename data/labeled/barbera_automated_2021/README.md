# News articles coded for economic news topic and sentiment from Barberá et al. (2021)

author: Hauke Licht & Naomi Yagai\
date: 2024-01-12

## Description

In their 2021 *Political Analysis* paper "Automated Text Classification of News Articles: A Practical Guide," Barberá and colleagues analyze the tone of coverage of the US national economy in the New York Times. To this end, they identify articles about the economy and their tone (positive--negative).

Their measurements are generated through supervised text classification based on trained as well as crowd coders' annotations of news articles' texts.

## Annotation procedure

The authors have distributed multiple samples for annotation by trained coders and/or crowd coders. Here, we focus on dataset **5AC**, which records article-segment-level codings (i.e., of the first five sentences of an article) by 3-10 crowd coders. Each article segment was coded by each coder along two coding dimensions:

-   *relevance:* 'yes' if the article gives a coder indication of how the economy is performing, 'not sure' if a coder could not determine, and 'no' otherwise
-   *positivity:* a score ranging from 1 (very negative) to 9 (very positive) coders assign to relevant news articles (i.e., those for which *relevance* == 'yes')

## The data

source: replication data on Political Analysis' Harvard Dataverse: <https://dataverse.harvard.edu/file.xhtml?persistentId=doi:10.7910/DVN/MXKRDE/SCOMRU&version=1.2>
