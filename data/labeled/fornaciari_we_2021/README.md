# Sentence-level policy pledge annotations of English and Swedish manifesto sentences

Paper: Fornaciari et al. ([2021](https://doi.org/10.18653/v1/2021.findings-acl.301))
Data: [Github](https://github.com/fornaciari/MiMac_taxes/raw/refs/heads/main/jupyter_xsl_preproc_210130170501/all210126.xlsx)

## Definition of pledge

Fornaciari et al. point to Thomson et al.'s' ([2017](https://doi.org/10.1111/ajps.12313), 532; emphases added) definition:

> For a statement to qualify as a pledge, it must contain **language indicating commitment** to some future action or outcome.
> Pledges include both firm commitment language, such as “we will” or “we promise to,” as well as more softly described intention, such as “we support” or “we favor,” as long as parties indicate that they support the action or outcome referred to unequivocally.
> What determines whether a statement qualifies as a pledge is the **testability of the action or outcome** to which the party is committing itself.
> **A pledge is a statement committing a party to an action or outcome that is testable**:
> That is, we can gather evidence and make an argument that the action or outcome was either accomplished or not.
> Many statements that begin with hard commitment language would be considered rhetoric, not pledges, because they do not meet the testability criteria — for example, “we will ensure that our government shows respect for families” or “we support fair treatment for all.”
> We define a pledge as **a statement committing a party to one specific action or outcome that can be clearly determined to have occurred or not** [*post hoc*].

However, Thomson et al. discuss the pros and cons of this narrow definition (see the [Supporting Information](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1111%2Fajps.12313&file=ajps12313-sup-0001-SuppMat.pdf) for their paper).


## Download data files

| dataset_key        | file                                        | url                                                                                                                            |
|:-------------------|:--------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| fornaciari_we_2021 | fornaciari_we_2021-pledge_binary.tsv        | https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/fornaciari_we_2021/fornaciari_we_2021-pledge_binary.tsv        |
| fornaciari_we_2021 | fornaciari_we_2021-pledge_binary_sample.tsv | https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/fornaciari_we_2021/fornaciari_we_2021-pledge_binary_sample.tsv |
| fornaciari_we_2021 | annotation_set_05.csv                       | https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/fornaciari_we_2021/annotation_set_05.csv                       |
| fornaciari_we_2021 | annotation_set_04.csv                       | https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/fornaciari_we_2021/annotation_set_04.csv                       |
| fornaciari_we_2021 | annotation_set_03.csv                       | https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/fornaciari_we_2021/annotation_set_03.csv                       |
| fornaciari_we_2021 | annotation_set_02.csv                       | https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/fornaciari_we_2021/annotation_set_02.csv                       |
| fornaciari_we_2021 | annotation_set_01.csv                       | https://cta-text-datasets.s3.eu-central-1.amazonaws.com/labeled/fornaciari_we_2021/annotation_set_01.csv                       |