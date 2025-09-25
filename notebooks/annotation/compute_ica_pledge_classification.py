from pathlib import Path
import pandas as pd
from scipy.stats import entropy
from krippendorff import alpha as k_alpha

data_path = "../../data/labeled/fornaciari_we_2021"
data_path = Path(data_path)

# ## Read the annotations
groups = ['group1', 'group2', 'group3']

k_alphas = {}

for group in groups:
    
    annotations_path = data_path / "annotations" / "classification" / group

    fps = list(annotations_path.glob('*.csv'))
    annotations = pd.concat({fp.stem: pd.read_csv(fp) for fp in fps}, ignore_index=False).reset_index(level=0, names=['annotator'])
    tmp = annotations[['annotator', 'text_id', 'label']].copy()
    tmp['label'] = (tmp['label'].str.lower()=='pledge').astype(int)
    tmp = tmp.pivot_table(index='annotator', columns='text_id', values='label').fillna(0).astype(int)
    k_alphas[group] = k_alpha(tmp.values, level_of_measurement='nominal')

print(pd.DataFrame.from_dict(k_alphas, orient='index', columns=['k_alpha']).round(3).to_markdown())
