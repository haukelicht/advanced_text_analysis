import pandas as pd
import numpy as np

from bertopic import BERTopic 

# import gensim.corpora as corpora
# from gensim.models.coherencemodel import CoherenceModel

from sklearn.metrics import (
    silhouette_score, # <== compute overall, corpus-level score
    silhouette_samples # <== compute sample/document-level scores
)
# import matplotlib.pyplot as plt

# from typing import Union, List, Literal, Tuple, Dict

# def compute_coherece(
#         model: BERTopic, 
#         docs: Union[pd.Series, List[str]], 
#         coherence_metric: Literal['u_mass', 'c_v', 'c_uci', 'c_npmi']='c_v',
#     ) -> Tuple[Dict[str, Union[float, Dict[int, float]]], CoherenceModel]:
#     """
#     Compute coherence scores for a BERTopic model.

#     Parameters:
#         model (BERTopic): The BERTopic model.
#         docs (Union[pd.Series, List[str]]): The documents to compute coherence on.
#             Must be a pandas Series or a list of strings.
#         coherence_metric (Literal['u_mass', 'c_v', 'c_uci', 'c_npmi'], optional): The coherence metric to use. 
#             Allowed values are 'u_mass', 'c_v', 'c_uci', 'c_npmi' (see https://radimrehurek.com/gensim/models/coherencemodel.html)
#             Defaults to 'c_v'.

#     Returns:
#         Tuple[Dict[str, Union[float, Dict[int, float]]], CoherenceModel]: 
#            A tuple containing the coherence scores and the coherence model.
#             - scores (Dict[str, Union[float, Dict[int, float]]]): The coherence scores.
#                 - overall (float): The overall coherence score.
#                 - by_topic (Dict[int, float]): The coherence score for each topic.
#             - coherence_model (CoherenceModel): The coherence model object.

#     """
#     # get topic top-n words
#     topic_words = [
#         [word for word, _ in words if len(word) > 0] # for top-n words words in topic
#         for tid, words in model.topic_representations_.items() # iterate over topics
#         if tid > -1 # exclude outlier topic
#     ]
#     topic_words = [topic for topic in topic_words if len(topic)>0]

#     # extract vectorizer and analyzer from BERTopic
#     vectorizer = model.vectorizer_model
#     analyzer = vectorizer.build_analyzer()
    
#     if isinstance(docs, list):
#         docs = np.array(docs)
#     cleaned_docs = model._preprocess_text(docs)
#     toks = [analyzer(doc) for doc in cleaned_docs]

#     # get topics
#     topics = model.topics_

#     # pre-process documents
#     documents = pd.DataFrame({"Document": toks, "ID": range(len(docs)), "Topic": topics})
#     documents_per_topic = documents.groupby(['Topic'], as_index=False).agg({'Document': 'sum'})

#     # extract features for Topic Coherence evaluation
#     # words = vectorizer.get_feature_names_out()
#     tokens = documents_per_topic.Document.to_list()
#     dictionary = corpora.Dictionary(tokens)
#     corpus = [dictionary.doc2bow(token) for token in tokens]
    
#     # compile coherence model
#     coherence_model = CoherenceModel(
#         topics=topic_words, 
#         texts=tokens, 
#         corpus=corpus,
#         dictionary=dictionary, 
#         coherence=coherence_metric
#     )

#     # evaluate coherence
#     scores = {
#         'overall': coherence_model.get_coherence(),
#         'by_topic': {tid: c for tid, c in enumerate(coherence_model.get_coherence_per_topic())}
#     }
    
#     return scores, coherence_model

# def plot_topic_coherence_scores(scores, add_overall=True, figsize=(7, 5)):
#     coherences_df = pd.DataFrame(
#         scores['by_topic'].values(), 
#         index=range(len(scores['by_topic'])), 
#         columns=['coherence']
#     )
#     # create new plot
#     plt.figure(figsize=figsize)
#     coherences_df.sort_values(by='coherence', inplace=True)
#     coherences_df['coherence'].plot(kind='barh')
#     if add_overall:
#         # draw a vertical line at the overall coherence score
#         plt.axvline(scores['overall'], color='red', linestyle='--')
#     plt.xlim(0, 1)
#     plt.show()

def compute_silhouette_scores(model: BERTopic, remove_outliers: bool=True, seed: int=42):
    """
    Compute silhouette scores for a BERTopic model.

    Parameters:
        model (BERTopic): The BERTopic model.
        remove_outliers (bool, optional): Whether to remove outliers before computing silhouette scores. 
            Defaults to True.
        seed (int, optional): The random seed. Defaults to 42.

    Returns:

        Dict[str, Union[float, pd.DataFrame]]: A dictionary containing the silhouette scores.
            - overall (float): The overall silhouette score.
            - by_topic (pd.DataFrame): The silhouette scores by topic.
                - topic (int): The topic id.
                - mean (float): The mean silhouette score.
                - std (float): The standard deviation of the silhouette scores.

    """
    if remove_outliers:
        idxs = np.where(np.array(model.topics_) > -1)[0]
        embeddings = model.umap_model.embedding_[idxs, :]
        topics = np.array(model.topics_)[idxs].tolist()
    else:
        embeddings = model.umap_model.embedding_
        topics = model.topics_
    
    overall = silhouette_score(
        X=embeddings, 
        labels=topics, 
        sample_size=None, 
        random_state=seed
    )
    by_topic = silhouette_samples(X=embeddings, labels=topics)
    by_topic = pd.DataFrame({'topic': topics, 'silhouette_score': by_topic})
    by_topic = by_topic.groupby('topic').agg(['mean', 'std'])
    # remove stacked columns
    by_topic.columns = by_topic.columns.droplevel(0)
    by_topic.reset_index(inplace=True)
    out = {
        'overall': overall,
        'by_topic': by_topic
    }
    return out