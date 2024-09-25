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
from huggingface_hub.utils._errors import HTTPError

from transformers.utils import logging
logging.get_logger("transformers").setLevel(logging.ERROR)
import tiktoken

from openai import OpenAI
from replicate import Client as ReplicateClient
from ollama import Client as OllamaClient
from ollama import Options, ResponseError, RequestError

from tqdm.auto import tqdm

from dataclasses import dataclass
from typing import Any, Dict, List, Union, Optional

OLLAMA_MODELS_TOKENIZERS = {
    'llama3:8b': 'meta-llama/Meta-Llama-3-8B',
    'llama3:70b': 'meta-llama/Meta-Llama-3-70B',
    'llama3.1:8b': 'meta-llama/Llama-3.1-8B',
    'llama3.1:70b': 'meta-llama/Llama-3.1-70B',
    'mxbai-embed-large': 'mixedbread-ai/mxbai-embed-large-v1',
}

REPLICATE_MODELS_TOKENIZERS = {
    'meta/meta-llama-3-8b-instruct': 'meta-llama/Meta-Llama-3-8B-Instruct',
    'meta/meta-llama-3-70b-instruct': 'meta-llama/Meta-Llama-3-70B-Instruct',
}


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

@dataclass
class _LLMBase:
    system_prompt: str
    model: str

    def __post_init__(self):
        pass

    def create_completion(self, text: str, **kwargs):
        raise NotImplementedError
    
    def __call__(self, input: Union[str, List[str]], **kwargs) -> Union[str, List, List[List]]:
        if isinstance(input, str):
            return self.create_completion(input, **kwargs)
        else:
            output = []
            for text in tqdm(input):
                try:
                    tmp = self.create_completion(text, **kwargs)
                except ValueError as e:   
                    print(f"Error processing text: {text}. Error: {str(e)}")
                    tmp = None
                output.append(tmp)
            return output


@dataclass
class _EmbedderBase:
    model: str

    def __post_init__(self):
        pass

    def embed(self, text: str, **kwargs):
        raise NotImplementedError
    
    def __call__(self, input: Union[str, List[str]], **kwargs):
        if isinstance(input, str):
            input=[input]
        return self.embed(input, **kwargs)

@dataclass
class _LLMDefaultsBase:
    seed: int = 42
    temperature: float = 0.0
    json_output: bool = False

@dataclass
class _EmbedderDefaultsBase:
    seed: int = 42
    temperature: float = 0.0
    json_output: bool = False

@dataclass
class OpenAILLM(_LLMDefaultsBase, _LLMBase):
    model: str = 'gpt-4-0125-preview'
    api_key: Optional[str] = None
    base_url: Optional[str] = None
    
    def __post_init__(self):
        api_key = self.api_key or os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(base_url=self.base_url, api_key=api_key)
        self.tokens_counter = OpenAITokenCounter(model=self.model)
    
    def __repr__(self):
        return f"{__class__.__name__}(model='{self.model}', ...)"

    def __str__(self):
        return f"{__class__.__name__}(model='{self.model}', ...)"
    
    def create_completion(
            self, 
            text: str, 
            # # TODO: add examples
            # examples: Optional[None] = None,
            # shuffle_examples: bool = False,
            **kwargs
        ):
        
        messages = [ 
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": text.strip()}
        ]
        
        # # TODO: add examples
        # if examples:
        #     if shuffle_examples:
        #         random.Random(self.seed).shuffle(messages)
        #     for example in examples:
        #         messages += [(
        #             {"role": "user", "content": example['text'].strip()},
        #             {"role": "assistant", "content": example['mentions'].strip()}
        #         )]
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            seed=self.seed,
            temperature=self.temperature,
            response_format={"type": "json_object" if self.json_output else "text"},
            **kwargs
        )

        # TODO: improve response validation
        assert len(response.choices) == 1, "Response should have one 'choice'"
        assert response.choices[0].finish_reason == 'stop', f"Response incomplete, reason: '{response.choices[0].finish_reason}'"

        result = response.choices[0].message.content
        if not self.json_output:
            return result

        try:
            result = json.loads(result)
        except JSONDecodeError:
            # TODO: consider raising Warning and return None
            ValueError(f"assistant response is not JSON-formatted (got '{result}') ")
        except Exception as e:
            ValueError(f"Could not parse result as JSON (got '{result}') ")
        
        # TODO: consider adding option to apply custom response parsing function here

        return result


@dataclass
class OpenAIEmbedder(_EmbedderDefaultsBase, _EmbedderBase):
    model: str = 'text-embedding-3-small'
    api_key: Optional[str] = None
    base_url: Optional[str] = None
    
    def __post_init__(self):
        api_key = self.api_key or os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(base_url=self.base_url, api_key=api_key)
        self.tokens_counter = OpenAITokenCounter(model=self.model)
    
    def __repr__(self):
        return f"{__class__.__name__}(model='{self.model}', ...)"

    def __str__(self):
        return f"{__class__.__name__}(model='{self.model}', ...)"
    
    def embed(self, input: List[str], **kwargs) -> Dict:
        response = self.client.embeddings.create(
            input=[text.replace("\n", " ") for text in input],
            model=self.model,
            **kwargs
        )
        embeddings = [(e.index, e.embedding) for e in response.data]
        # sort embeddings by index
        embeddings = [e[1] for e in sorted(embeddings, key=lambda x: x[0])]
        return np.array(embeddings)

@dataclass
class OllamaLLM(_LLMDefaultsBase, _LLMBase):
    model: str = 'llama3.1:8b'
    host_address: str = 'http://localhost:11434'
    tokenizer_name: str = 'meta-llama/Llama-3.1-8B'

    def __post_init__(self):
        self.client = OllamaClient(host=self.host_address)
        self.tokens_counter = HFTokenCounter(tokenizer_name=self.tokenizer_name)
    
    def create_completion(
            self, 
            text: str, 
            # # TODO: add examples
            # examples: Optional[None] = None,
            # shuffle_examples: bool = False,
            **kwargs
        ) -> List:
        
        messages = [ 
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": text.strip()}
        ]
        
        # # TODO: add examples
        # if examples:
        #     if shuffle_examples:
        #         random.Random(self.seed).shuffle(messages)
        #     for example in examples:
        #         messages += [(
        #             {"role": "user", "content": example['text'].strip()},
        #             {"role": "assistant", "content": example['mentions'].strip()}
        #         )]
        
        options = Options(
            seed=self.seed,
            temperature=self.temperature,
            **kwargs
        )
        
        try:
            response = self.client.chat(
                model=self.model,
                messages=messages,
                options=options,
                format='json' if self.json_output else ''
            )
        except ResponseError as e:
            raise ValueError(f"model {self.model} not provided. First pull the model")
        except RequestError as e:
            raise ValueError(f"could not complete request. Reason: {str(e)}")
        except Exception as e:
            raise e

        # TODO: improve response validation
        assert response['done'], f"Response incomplete"

        result = response['message']['content']
        if not self.json_output:
            return result

        try:
            result = json.loads(result)
        except JSONDecodeError:
            # TODO: consider raising Warning and return None
            ValueError(f"assistant response is not JSON-formatted (got '{result}') ")
        except Exception as e:
            ValueError(f"Could not parse result as JSON (got '{result}') ")
        # TODO: consider adding option to apply custom response parsing function here
        
        return result

@dataclass
class OllamaEmbedder(_EmbedderDefaultsBase, _EmbedderBase):
    model: str = 'mxbai-embed-large'
    host_address: str = 'http://localhost:11434'
    tokenizer_name: str = 'mixedbread-ai/mxbai-embed-large-v1'

    def __post_init__(self):
        self.client = OllamaClient(host=self.host_address)
        self.tokens_counter = HFTokenCounter(tokenizer_name=self.tokenizer_name)
    
    def embed(self, input: List[str], **kwargs):
        res = self.client.embed(
            model=self.model,
            input=input,
            **kwargs
        )
        return np.array(res['embeddings'])


@dataclass
class _ReplicateModel(_LLMDefaultsBase, _LLMBase):
    api_key: Optional[str] = None
    base_url: Optional[str] = None
    timeout: int = 30
    max_tokens: int = 1024*2

    def __post_init__(self):
        api_key = self.api_key or os.getenv("REPLICATE_API_KEY")
        self.client = ReplicateClient(api_token=api_key, timeout=self.timeout)
        self.tokens_counter = HFTokenCounter(tokenizer_name=self.tokenizer_name)
    
    def create_completion(
            self, 
            text: str, 
            **kwargs
        ):
        
        response = self.client.run(
            ref=self.model,
            input={
                "system_prompt": self.system_prompt,
                "prompt": text.strip(),
                "temperature": self.temperature,
                "seed": self.seed,
                "max_new_tokens": self.max_tokens,
                # TODO: add handling of kwargs
                # TODO: consider passing `prompt_template` attribute value here as as input 
            }
        )

        result = ''.join(response)
        if not self.json_output:
            return result

        try:
            result = json.loads(result)
        except JSONDecodeError:
            # TODO: consider raising Warning and return None
            ValueError(f"assistant response is not JSON-formatted (got '{result}') ")
        except Exception as e:
            ValueError(f"Could not parse result as JSON (got '{result}') ")
        
        # TODO: consider adding option to apply custom response parsing function here

        return result

@dataclass
class ReplicateLlama3(_ReplicateModel, _LLMDefaultsBase, _LLMBase):
    model: str = 'meta/meta-llama-3.1-70b-instruct'
    tokenizer_name: str = 'meta-llama/Meta-Llama-3-70B-Instruct'    
    prompt_template: str = "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>",
    
    def __repr__(self):
        return f"{__class__.__name__}(model='{self.model}', ...)"

    def __str__(self):
        return f"{__class__.__name__}(model='{self.model}', ...)"

@dataclass
class ReplicateMixtral(_ReplicateModel, _LLMDefaultsBase, _LLMBase):
    model: str = 'mistralai/mixtral-8x7b-instruct-v0.1'
    tokenizer_name: str = 'mistralai/Mixtral-8x7B-Instruct-v0.1'
    prompt_template: str = "<s>[INST] {system_prompt} {prompt} [/INST]"

    def __repr__(self):
        return f"{__class__.__name__}(model='{self.model}', ...)"

    def __str__(self):
        return f"{__class__.__name__}(model='{self.model}', ...)"

from replicate.exceptions import ModelError
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
@dataclass
class PatientReplicateLlama3(ReplicateLlama3):
    """Wrapper of ReplicateLlama3 that retries API call to ensure against failures"""
    @retry(retry=retry_if_exception_type(ModelError), stop=stop_after_attempt(3), wait=wait_fixed(30))
    def __call__(self, input: Union[str, List[str]], **kwargs):
        # call the parent classe's 
        return super().__call__(input, **kwargs)