"""
This module contains classes for interacting with language models (LLMs) from different providers.
The classes are designed to be used as wrappers around the respective APIs, providing a consistent interface for interacting with the models.
The classes are designed to be used as drop-in replacements for each other, allowing users to easily switch between different LLMs without having to change their code.
"""

import os

import numpy as np

import json
from json import JSONDecodeError

from transformers import AutoTokenizer
from transformers.utils.hub import GatedRepoError
from huggingface_hub.utils import HfHubHTTPError as HTTPError

from transformers.utils import logging
logging.get_logger("transformers").setLevel(logging.ERROR)
import tiktoken

from tqdm.auto import tqdm

from dataclasses import dataclass
from typing import Any, Dict, List, Union, Optional

@dataclass
class _TokenCounterBase:

    def count_tokens(self, input: Union[str, List[str]]) -> Union[int, List[int]]:
        """
        Count the number of tokens in the input.

        Args:
            input (Union[str, List[str]]): The input to tokenize. Can be a string or a list of strings.

        Returns:
            Union[int, List[int]]: The number of tokens in the input. If the input is a list, returns a list of token counts.
        """
        pass
    
    def __call__(self, input: Union[str, List[str]]) -> Union[int, List[int]]:
        """
        Call the tokenizer on the input. This is equivalent to calling count_tokens.

        Args:
            input (Union[str, List[str]]): The input to tokenize. Can be a string or a list of strings.

        Returns:
            Union[int, List[int]]: The number of tokens in the input. If the input is a list, returns a list of token counts.
        """
        return self.count_tokens(input)


@dataclass
class HFTokenCounter(_TokenCounterBase):
    tokenizer_name: str
    
    def __post_init__(self):
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.tokenizer_name)
        except (OSError, GatedRepoError, HTTPError) as e:
            raise Exception((
                f"You don't have access to model {self.tokenizer_name}. "
                "Go to https://huggingface.co/{self.tokenizer_name} to request access. "
                "Then try instantiating the model/embedder again."
            ))
        
    def count_tokens(self, input: Union[str, List[str]]) -> Union[int, List[int]]:
        if (is_str := isinstance(input, str)):
            input = [input]
        toks = self.tokenizer(input, truncation=False, return_length=True)['length']
        if is_str:
            toks = toks[0]
        return toks

class OpenAITokenCounter(_TokenCounterBase):
    def __init__(self, encoding_name: Union[str, None] = None, model: Union[str, None] = None):
        """
        Initialize the tokenizer with either a model or an encoding name.

        Args:
            encoding_name (Union[str, None]): The name of the encoding to use. Default is None.
            model (Union[str, None]): The model to use for encoding. Default is None.

        Raises:
            ValueError: If neither model nor encoding_name is provided.
            ValueError: If both model and encoding_name are provided.
        """
        # ensure that either model or encoding_name is provided
        if model is None and encoding_name is None:
            raise ValueError("Either `model` or `encoding_name` must be provided.")
        if model is not None and encoding_name is not None:
            raise ValueError("Only one of `model` or `encoding_name` can be provided.")
        if encoding_name:
            self.encoding = tiktoken.get_encoding(encoding_name)
        else:
            self.encoding = tiktoken.encoding_for_model(model)
    
    def count_tokens(self, input: Union[str, List[str]]) -> Union[int, List[int]]:
        if isinstance(input, str):
            return len(self.encoding.encode(input))
        else:
            toks = self.encoding.encode_batch(input)
            return [len(t) for t in toks]
