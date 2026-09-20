import numpy as np

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from scipy.stats import pearsonr, spearmanr

from transformers.trainer_utils import PredictionOutput

from typing import List, Dict

# ------------------------------------------------
#  Sequence scoring (regression)
# ------------------------------------------------

def parse_sequence_scorer_prediction_output(p: PredictionOutput):
    logits, labels = p.predictions, p.label_ids
    predictions = np.squeeze(logits, axis=-1) if logits.ndim > 1 else logits
    return labels, predictions

def compute_sequence_scoring_metrics(
        y_true: List[float],
        y_pred: List[float]
    ) -> Dict[str, float]:

    mse = mean_squared_error(y_true, y_pred)
    result = {
        'mse': mse,
        'rmse': np.sqrt(mse),
        'mae': mean_absolute_error(y_true, y_pred),
        'r2': r2_score(y_true, y_pred),
        'pearson_r': pearsonr(y_true, y_pred)[0],
        'spearman_r': spearmanr(y_true, y_pred)[0],
    }

    return result
