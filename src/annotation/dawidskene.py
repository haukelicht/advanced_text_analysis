import numpy as np
import pandas as pd
from concurrent.futures import ProcessPoolExecutor as Pool

from dataclasses import dataclass

from typing import Optional, Union, List

@dataclass
class DawidSkeneModelOutput:
    """
    Output of fitted Dawid-Skene model

    Attributes:
    pi: np.ndarray (n_classes)
        posterior label class prevalence
        sha
    theta: np.ndarray (n_workers, n_classes, n_classes)
        posterior worker abilities
    z: np.ndarray (n_items, n_classes)
        posterior item label class probabilities
    worker_reliabilities: dict
        workers' reliability scores computed as the diagonal of the posterior abilitiy estimates matrix

    """
    pi: np.ndarray
    theta: np.ndarray
    z: np.ndarray
    worker_reliabilities: dict

    def __repr__(self):
        return f"DawidSkeneModelOutput(pi={self.pi}, theta={self.theta}, z={self.z}, worker_reliabilities={self.worker_reliabilities})"

class DawidSkeneModel:
    """
    Dawid-Skene model for categorical annotation aggregation.

    Source: https://github.com/kajyuuen/Bayesian-Dawid-Skene/blob/master/EM%20Dawid-Skene.ipynb
    
    Attributes:
    n_classes: int
        Number of classes

    Methods:
    """
    def __init__(
        self,
        n_classes: int,
        max_iter: int = 100,
        tolerance: float = 0.01,
        verbose: bool = True
    ) -> None:
        """
        Initialize Dawid-Skene model

        Args:
        n_classes: int
            Number of classes
        max_iter: int

        tolerance: float
        """
        assert n_classes > 1, "Number of classes must be greater than 1"
        assert max_iter > 0, "max_iter must be greater than 0"
        assert tolerance > 0, "tolerance must be greater than 0"

        self.n_classes = n_classes
        self.max_iter = max_iter
        self.tolerance = tolerance
        self.verbose = verbose
    
    def __repr__(self):
        return f"DawidSkeneModel(n_classes={self.n_classes}, max_iter={self.max_iter}, tolerance={self.tolerance})"

    @staticmethod
    def _list2array(class_num, dataset_list):
        task_num, worker_num, class_num = len(dataset_list), len(dataset_list[0]), class_num
        dataset_tensor = np.zeros((task_num, worker_num, class_num))

        for task_i in range(task_num): 
            for worker_j in range(worker_num): 
                if isinstance(dataset_list[task_i][worker_j], list):
                    for predict_label_k in dataset_list[task_i][worker_j]:
                        dataset_tensor[task_i][worker_j][predict_label_k] += 1
                elif dataset_list[task_i][worker_j] is None or np.isnan(dataset_list[task_i][worker_j]):
                    continue
                else:
                    predict_label = int(dataset_list[task_i][worker_j])
                    dataset_tensor[task_i][worker_j][predict_label] += 1

        return dataset_tensor
    
    def _run(self, dataset, gold: Optional[np.ndarray]=None):
        self.task_num, self.worker_num, _ = dataset.shape
        self.dataset_tensor = dataset
        
        # init posterior label class probabilities
        predict_label = np.ones((self.task_num, self.n_classes)) + self.dataset_tensor.sum(1)*0.01
        predict_label /= predict_label.sum(1).reshape(-1, 1)
        if gold is not None:
            idxs = ~np.logical_or(np.isnan(gold), gold==-1)
            predict_label[idxs,:] = np.eye(self.n_classes)[gold[idxs].astype(int)]
        
        flag = True
        prev_error_rates, prev_predict_label = None, None
        self.iter_num = 0

        while flag:
            error_rates = self._m_step(predict_label)
            next_predict_label = self._e_step(predict_label, error_rates)
            log_L = self._get_likelihood(predict_label, error_rates)

            if self.iter_num == 0:
                if self.verbose:
                    # logging.info("{}\t{}".format(self.iter_num, log_L))
                    print(f"{self.iter_num}\t{log_L}")
            else:
                if self.verbose and self.iter_num % 50 == 0:
                    # logging.info("{}\t{}".format(self.iter_num, log_L))
                    print(f"{self.iter_num}\t{log_L}")
                marginal_predict = np.sum(predict_label, 0) / self.task_num
                prev_marginal_predict = np.sum(prev_predict_label, 0) / self.task_num
                marginals_diff = np.sum(np.abs(marginal_predict - prev_marginal_predict))
                error_rates_diff = np.sum(np.abs(error_rates - prev_error_rates))

                if self._check_condition(marginals_diff, error_rates_diff, self.iter_num):
                    flag = False

            prev_error_rates = error_rates
            prev_predict_label = predict_label
            # NOTE: if you want to hard-code gold examples labels, uncomment the following two lines:
            # if gold is not None:
            #     next_predict_label[idxs,:] = np.eye(self.n_classes)[gold[idxs].astype(int)]
            predict_label = next_predict_label
            self.iter_num += 1

        worker_reliability = {}
        for i in range(self.worker_num):
            ie_rates = marginal_predict * error_rates[i, :, :]
            reliability = np.sum(np.diag(ie_rates))
            worker_reliability[i] = reliability
            
        return marginal_predict, error_rates, worker_reliability, predict_label

    def _check_condition(self, marginals_diff, error_rates_diff, iter_num):
        return (marginals_diff < self.tolerance and error_rates_diff < self.tolerance) or iter_num > self.max_iter

    def _m_step(self, predict_label):
        error_rates = np.zeros((self.worker_num, self.n_classes, self.n_classes))

        # Equation 2.3
        for i in range(self.n_classes):
            worker_error_rate = np.dot(predict_label[:, i], self.dataset_tensor.transpose(1, 0 ,2))
            sum_worker_error_rate = worker_error_rate.sum(1)
            sum_worker_error_rate = np.where(sum_worker_error_rate == 0 , -10e9, sum_worker_error_rate)
            error_rates[:, i, :] = worker_error_rate / sum_worker_error_rate.reshape(-1,1)                                                                        
        return error_rates
    
    def _e_step(self, predict_label, error_rates):
        marginal_probability = predict_label.sum(0) / self.task_num
        next_predict_label = np.zeros([self.task_num, self.n_classes])
    
        # Equation 2.5
        for i in range(self.task_num):
            class_likelood = self._get_class_likelood(error_rates, self.dataset_tensor[i])
            next_predict_label[i] = marginal_probability * class_likelood
            sum_marginal_probability = next_predict_label[i].sum()
            sum_marginal_probability = np.where(sum_marginal_probability == 0 , -10e9, sum_marginal_probability)
            next_predict_label[i] /= sum_marginal_probability
        return next_predict_label
    
    def _get_likelihood(self, predict_label, error_rates):
        log_L = 0
        marginal_probability = predict_label.sum(0) / self.task_num

        # Equation 2.7
        for i in range(self.task_num):
            class_likelood = self._get_class_likelood(error_rates, self.dataset_tensor[i])
            log_L += np.log((marginal_probability * class_likelood).sum())
        return log_L

    def _get_class_likelood(self, error_rates, task_tensor):
        # \sum_{j=1}^J p_{j} \prod_{k=1}^K \prod_{l=1}^J\left(\pi_{j l}^{(k)}\right)^{n_{il}^{(k)}}
        return np.power(error_rates.transpose(0, 2, 1), np.broadcast_to(task_tensor.reshape(self.worker_num, self.n_classes, 1), (self.worker_num, self.n_classes, self.n_classes))).transpose(1, 2, 0).prod(0).prod(1)
    
    def fit(
        self,
        df: pd.DataFrame,
        items_col: str,
        annotators_col: str,
        annotations_col: str,
        gold: Optional[Union[pd.Series,np.ndarray,List]]=None
    ):
        """
        Fit Dawid-Skene model

        Args:
        df: pd.DataFrame
            DataFrame containing the annotation data
        items_col: str
            Name of column containing the item IDs
        annotators_col: str
            Name of column containing the annotator IDs
        annotations_col: str
            Name of column containing the annotation labels

        Returns:
        DawidSkeneModelOutput
            Output of fitted Dawid-Skene model
        """
        assert len(df) > 0, "DataFrame is empty"
        assert items_col in df.columns, f"Column '{items_col}' not found in DataFrame"
        assert annotators_col in df.columns, f"Column '{annotators_col}' not found in DataFrame"
        assert annotations_col in df.columns, f"Column '{annotations_col}' not found in DataFrame"
        assert df[items_col].nunique() > 1, "At least two items are required"
        assert df[annotators_col].nunique() > 1, "At least two annotators are required"
        assert df[annotations_col].nunique() > 1, "At least two labels are required"

        # get index mappings
        self.annotations_col_ = annotations_col
        self.classes_ = df[annotations_col].unique()
        self.annotation_id2idx_ = {lid: idx for idx, lid in enumerate(self.classes_)}
        
        self.items_col_ = items_col
        self.n_items = df[items_col].nunique()
        self.items_ = df[items_col].unique()
        self.item_id2idx_ = {pid: idx for idx, pid in enumerate(self.items_)}
        
        self.annotators_col_ = annotators_col
        self.n_annotators = df[annotators_col].nunique()
        self.annotators_ = df[annotators_col].unique()
        self.annotator_id2idx_ = {cid: idx for idx, cid in enumerate(self.annotators_)}
        
        dataset = pd.DataFrame({
            'item': df[items_col].map(self.item_id2idx_),
            'annotator': df[annotators_col].map(self.annotator_id2idx_),
            'annotation': df[annotations_col].map(self.annotation_id2idx_),
        })
        dataset = dataset.pivot(index='item', columns='annotator', values='annotation').to_numpy().tolist()
        dataset = DawidSkeneModel._list2array(self.n_classes, dataset)

        if gold is not None:
            if isinstance(gold, pd.Series):
                gold = gold.map(self.annotation_id2idx_).values
            elif isinstance(gold, (list, np.ndarray)):
                gold = np.array([g if np.isnan(g) else self.annotation_id2idx_[int(g)] for g in gold])
        
        pi, worker_abilities, worker_reliabilities, pred_labels = self._run(dataset, gold=gold)

        # post-process
        annotator_idx2dx = {idx: lid for lid, idx in self.annotator_id2idx_.items()}
        worker_reliabilities = {annotator_idx2dx[i]: r for i, r in worker_reliabilities.items()}

        self.fitted_ = DawidSkeneModelOutput(pi, worker_abilities, pred_labels, worker_reliabilities)
        return self.fitted_
    
    def fit_transform(
            self,
            df: pd.DataFrame,
            items_col: str,
            annotators_col: str,
            annotations_col: str,
            gold: Optional[Union[pd.Series,np.ndarray,List]]=None
        ):
        self.fit(df, items_col, annotators_col, annotations_col, gold=gold)
        out = pd.DataFrame(self.fitted_.z, columns=self.classes_, index=self.items_)
        out['posterior_label'] = out.idxmax(axis=1)
        return out
    


def compute_mv(x):
    """Compute majoirty vote, assuming that there are only two label classes: 1 and 2"""
    cnts = x.value_counts(sort=False).to_numpy()
    if len(cnts) == 1:
        return x.iloc[0]
    if cnts[0] == cnts[1]:
        return 0
    if cnts[0] > cnts[1]:
        return 1
    else:
        return 2
    

from sklearn.metrics import precision_recall_fscore_support

def eval(gold_labels: pd.Series, mv_labels: pd.Series, ds_labels: pd.Series):
    """Custom function for evaluating majority voting-based and Dawid-Skene model-induced labels, respectively, against gold labels.

    Args:
        gold_labels (pd.Series): gold labels (values must be in {1, 2})
        mv_labels (pd.Series): majority voting-based labels (values must be in {1, 2, 0} where 0 indicates a tie)
        ds_labels (pd.Series): Dawid-Skene model-induced labels (values must be in {1, 2})

    Returns:
        dict: dictionary with evaluation metrics.
    """

    out = {
        # keep data (e.g., to allow for computing bootstrap confidence intervals on metrics)
        'data': {
            'gold_labels': gold_labels.tolist(),
            'mv_labels': mv_labels.tolist(),
            'ds_labels': ds_labels.tolist()
        },
        'share_ties': {
            'mv': (mv_labels == 0).mean(),
            'ds': (ds_labels == 0).mean()
        },
        'accuracy': {
            'mv': (mv_labels == gold_labels).mean(),
            'ds': (ds_labels == gold_labels).mean()
        },
        'precision': {},
        'recall': {},
        'f1': {}
    }

    out['precision']['mv'], out['recall']['mv'], out['f1']['mv'], _ = precision_recall_fscore_support(y_true=gold_labels, y_pred=mv_labels, labels=[1, 2], average=None)
    out['precision']['ds'], out['recall']['ds'], out['f1']['ds'], _ = precision_recall_fscore_support(y_true=gold_labels, y_pred=ds_labels, labels=[1, 2], average=None)

    # make nupy arrays lists
    for k in ['precision', 'recall', 'f1']:
        for m in ['mv', 'ds']:
            out[k][m] = out[k][m].tolist()
    
    return out
