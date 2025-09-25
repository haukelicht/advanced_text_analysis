import sys
sys.path.append("../..")

from pathlib import Path

import pandas as pd
import numpy as np

from nltk.tokenize import TreebankWordTokenizer

from krippendorff import alpha as k_alpha

from src.annotation.agreement import InterAnnotatorAgreement, overlap_distance, split_iaa_by_item

tokenizer = TreebankWordTokenizer()

# list(tokenizer.span_tokenize(text))
def character_to_token_spans(text: str, spans: list[tuple[int, int]]) -> list[tuple[int, int]]:
    token_spans = list(tokenizer.span_tokenize(text))
    token_span_list = []
    for span in spans:
        start_char, end_char = span
        # Find the first token that starts after or at the start_char
        start_token = next((i for i, (s, _) in enumerate(token_spans) if s >= start_char), None)
        # Find the last token that ends before or at the end_char
        end_token = next((i for i, (_, e) in reversed(list(enumerate(token_spans))) if e <= end_char), None)
        if start_token is not None and end_token is not None and start_token <= end_token:
            token_span_list.append((start_token, end_token + 1))  # +1 to make it exclusive
    return token_span_list


data_path = "../../data/labeled/fornaciari_we_2021"
data_path = Path(data_path)

k_alphas = {}
for group in ['group1', 'group2']:
    annotations_path = data_path / "annotations" / "extraction" / group

    fps = list(annotations_path.glob('*.jsonl'))

    annotations = pd.concat({fp.stem: pd.read_json(fp, lines=True) for fp in fps}, ignore_index=False).reset_index(level=0, names=['annotator'])

    # discard entity type
    annotations['label'] = annotations.label.apply(lambda x: [anno[:2] for anno in x])
    
    # add metadata and reformat the DataFrame
    if 'metadata' in annotations.columns:
        metadata = annotations['metadata'].apply(pd.Series)
        metadata.drop(columns=['label'], inplace=True)
        annotations[metadata.columns] = metadata
        annotations.drop(columns=['metadata'], inplace=True)

    annotations = annotations.sort_values(by=['text_id', 'annotator']).reset_index(drop=True)
    annotations = annotations[['text_id', 'text', 'annotator', 'label']]
    annotations['spans'] = annotations.apply(lambda x: [x['text'][lab[0]:lab[1]] for lab in x['label']], axis=1)

    # count number of annotations per annotator and text
    annotations['n_annos'] = annotations.label.map(len)
    annotations['no_annos'] = annotations['n_annos']==0

    # Let's apply this logic to all the data:
    # extract tokens
    annotations['tokens'] = annotations.apply(lambda x: tokenizer.tokenize(x['text']), axis=1)
    # determine token-level span informations
    annotations['token_spans'] = annotations.apply(lambda x: character_to_token_spans(x['text'], x['label']), axis=1)

    # Braylan et al.'s code requires that annotators and items are identified by integer IDs
    annotations['item_id'] = pd.Categorical(annotations['text_id']).codes
    annotations['annotator_id'] = pd.Categorical(annotations['annotator']).codes
    # create an agreement object with the entity distance function
    iaa = InterAnnotatorAgreement(
        annotations, 
        item_colname="item_id", 
        uid_colname="annotator_id", 
        label_colname="label", 
        distance_fn=overlap_distance
    )
    # compute agreement measures
    iaa.setup(parallel_calc=False)
    k_alphas[group] = iaa.get_krippendorff_alpha()

print(pd.DataFrame.from_dict(k_alphas, orient='index', columns=['k_alpha']).round(3).to_markdown())
