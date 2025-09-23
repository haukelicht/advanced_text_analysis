import os
import json
import pandas as pd

from typing import List, Union, Optional

def _is_file(path: str) -> bool:
    return os.path.exists(path) and os.path.isfile(path)

def _is_dir(path: str) -> bool:
    return os.path.exists(path) and os.path.isdir(path)

def _get_col_separator(path: str) -> Union[str, None]:
    sep = None
    if path.endswith('.csv'):
        sep = ','
    elif path.endswith('.tsv') or path.endswith('.tab'):
        sep = '\t'
    return sep

def read_tabular(path: str, columns: Optional[List[str]]=None, **kwargs) -> 'pd.DataFrame':
    if not _is_file(str(path)):
        raise FileNotFoundError(f'File not found: {path}')

    sep = _get_col_separator(str(path))
    if sep is None:
        raise ValueError(f'Unsupported file format. `path` Must be a .tsv, .tab, or .csv file.')

    df = pd.read_csv(path, sep=sep, **kwargs)
    if columns is not None:
        for c in columns:
            assert c in df.columns, f'Column {c} not found in the dataframe.'
        df = df[columns]
    return df

def write_jsonlines(data: List[dict], path: str, **kwargs):
    d = os.path.dirname(path)
    if not _is_dir(d):
        raise FileNotFoundError(f'Directory not found: {d}')
    if _is_file(path):
        raise FileExistsError(f'File already exists: {path}')
    
    with open(path, 'w') as f:
        for d in data:
            f.write(json.dumps(d) + '\n')

def read_jsonlines(path: str) -> List[dict]:
    if not _is_file(path):
        raise FileNotFoundError(f'File not found: {path}')
    
    with open(path, 'r') as f:
        data = [json.loads(l.rstrip()) for l in f]
    return data
