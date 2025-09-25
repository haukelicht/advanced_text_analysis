import torch
import torch.nn as nn
import numpy as np

from sentence_transformers import SentenceTransformer
from setfit import SetFitModel, SetFitHead

from numpy.typing import NDArray
from typing import List, Dict, Optional, Mapping, Union

def get_class_weights(x: NDArray, multitarget: bool=False) -> NDArray:
    if not multitarget: assert x.ndim == 1, 'if multitarget=False, x.ndim must be 1'
    if multitarget: assert x.ndim == 2, 'if multitarget=True, x.ndim must be 2'

    if multitarget:
        # assume that multitarget feature indicators can only be True/False, i.e., 0/1
        w = x.sum()/x.sum(axis=0)
        w /= w.sum()
        return w
    else:
        _, cnts = np.unique(x, return_counts=True)
        w = sum(cnts)/cnts
        w /= w.sum()
        return w

class SetFitHeadWithClassWeights(SetFitHead):
    """
    A SetFit head that supports class-weights aware multi-class classification for end-to-end training.
    Binary classification is treated as 2-class classification.

    Args:
        in_features (`int`, *optional*):
            The embedding dimension from the output of the SetFit body. If `None`, defaults to `LazyLinear`.
        out_features (`int`, defaults to `2`):
            The number of targets. If set `out_features` to 1 for binary classification, it will be changed to 2 as 2-class classification.
        temperature (`float`, defaults to `1.0`):
            A logits' scaling factor. Higher values make the model less confident and lower values make
            it more confident.
        eps (`float`, defaults to `1e-5`):
            A value for numerical stability when scaling logits.
        bias (`bool`, *optional*, defaults to `True`):
            Whether to add bias to the head.
        device (`torch.device`, str, *optional*):
            The device the model will be sent to. If `None`, will check whether GPU is available.
        multitarget (`bool`, defaults to `False`):
            Enable multi-target classification by making `out_features` binary predictions instead
            of a single multinomial prediction.
        class_weights (`List[float]`, `numpy.typing.NDarray`, *optional*):
    """

    def __init__(
        self,
        class_weights: Optional[Union[List[float], NDArray]] = None,
        **kwargs
    ) -> None:
        super(SetFitHeadWithClassWeights, self).__init__(**kwargs)
        
        if len(class_weights) != self.out_features:
            raise ValueError(f'length of `class_weights` must be same as `out_features`')
        
        self.class_weights = torch.tensor(class_weights, dtype=self.linear.weight.dtype).to(self._device)


    def get_loss_fn(self) -> nn.Module:
        if self.multitarget:  # if sigmoid output
            return nn.BCEWithLogitsLoss(pos_weight=self.class_weights)
        return nn.CrossEntropyLoss(weight=self.class_weights)

    @property
    def device(self) -> torch.device:
        """
        `torch.device`: The device on which the model is placed.

        Reference from: https://github.com/UKPLab/sentence-transformers/blob/master/sentence_transformers/SentenceTransformer.py#L869
        """
        return next(self.parameters()).device
    
    def to(self, device: Union[str, torch.device]) -> "SetFitHeadWithClassWeights":
        """Move this SetFitHeadWithClassWeights to `device`, and then return `self`. This method does not copy.

        Args:
            device (Union[str, torch.device]): The identifier of the device to move the model to.

        Returns:
            SetFitHeadWithClassWeights: Returns the original model, but now on the desired device.
        """
        self.linear = self.linear.to(device)
        if hasattr(self, "class_weights"):
            self.class_weights = self.class_weights.to(device)
        return self
    
    def get_config_dict(self) -> Dict[str, Optional[Union[int, float, bool, List[float]]]]:
        return {
            "in_features": self.in_features,
            "out_features": self.out_features,
            "temperature": self.temperature,
            "bias": self.bias,
            "device": self.device.type,
            "multitarget": self.multitarget,
            "class_weights": self.class_weights.cpu().numpy().round(3).tolist()
        }

    def __repr__(self) -> str:
        return "SetFitHeadWithClassWeights({})".format(self.get_config_dict())

get_device = lambda: 'cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu'

def model_init(
        model_name: str,
        id2label: Mapping[int, str],
        multitarget_strategy: Optional[str]=None,
        class_weights: Optional[NDArray]=None,
        device: Optional[Union[str, torch.device]]=None
    ) -> "SetFitModel":
    if class_weights is not None:
      if multitarget_strategy is None:
        assert len(id2label) == len(class_weights), 'len(id2label) must equal len(class_weights)'

    if device is None:
        device = get_device()

    body = SentenceTransformer(model_name, device='cpu')

    head_kwargs = dict(
        in_features=body.get_sentence_embedding_dimension(),
        out_features=len(id2label),
        device='cpu',
        multitarget=isinstance(multitarget_strategy, str),
    )
    if class_weights is not None:
        head_kwargs['class_weights'] = class_weights
        head = SetFitHeadWithClassWeights(**head_kwargs)
    else:
        head = SetFitHead(**head_kwargs)

    return SetFitModel(
        model_head=head,
        model_body=body,
        multitarget_strategy=multitarget_strategy,
        labels=list(id2label.values()),
        id2label=id2label
    ).to(device)
