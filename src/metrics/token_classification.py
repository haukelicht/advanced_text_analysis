import numpy as np

from seqeval.metrics import classification_report as seqeval_classification_report

from transformers.trainer_utils import PredictionOutput

from typing import List, Dict

# ------------------------------------------------
#  Token classification (span extraction)
# ------------------------------------------------

def _correct_iob2(labels: List[str]) -> List[str]:
    prev = None
    edit = list()
    for i, l in enumerate(labels):
        if (i == 0 or prev == 'O') and l[0] == 'I':
            edit.append(i)
        prev = l
    if len(edit) > 0:
        labels = [l.replace('I-', 'B-') if i in edit else l for i, l in enumerate(labels)]
    return labels

def parse_token_classifier_prediction_output(p: PredictionOutput):
    predictions, labels = p
    predictions = np.argmax(predictions, axis=2)
    return labels, predictions


def compute_token_classification_metrics(
        y_true: List[List[int]], 
        y_pred: List[List[int]], 
        label2id: Dict[str, int], 
    ) -> Dict[str, float]:
    
    label_list = list(label2id.keys())
    types = list(set([l[2:] for l in label_list if l != 'O']))
    
    # encode label IDs to labels
    predictions = [
        _correct_iob2([label_list[p] for (p, l) in zip(preds, labs) if l != -100])
        for preds, labs in zip(y_pred, y_true)
    ]
    labels = [
        _correct_iob2([label_list[l] for (_, l) in zip(preds, labs) if l != -100])
        for preds, labs in zip(y_pred, y_true)
    ]

    metrics = ['precision', 'recall', 'f1-score']
    keys = ['macro avg', 'micro avg'] + types
    results = {}
    
    # Span level (Seqeval)
    result = seqeval_classification_report(labels, predictions, output_dict=True, zero_division=0.0)
    # flatten
    result = {k: result[k] for k in keys if k in result}
    # format
    result = {
        # format: metric name <=> metric value
        str(f"{k.replace(' avg', '')}_{m.replace('f1-score', 'f1')}"): scores[m] 
        # iterate over class-wise results
        for k, scores in result.items()
        # iterate over metrics
        for m in metrics
    }
    
    return result
