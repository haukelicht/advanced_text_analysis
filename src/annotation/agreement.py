# code based on paper 
#
#   Alexander Braylan, Omar Alonso, and Matthew Lease. 2022.
#     Measuring Annotator Agreement Generally across Complex
#     Structured, Multi-object, and Free-text Annotation Tasks. In
#     Proceedings of the ACM Web Conference 2022 (WWW '22).
#     Association for Computing Machinery, New York, NY, USA,
#     1720–1730. https://doi.org/10.1145/3485447.3512242
#
# code taken from https://github.com/Praznat/annotationmodeling/blob/master/agreement.py

from multiprocessing import Pool
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from itertools import chain

def flatten(listoflists):
    return list(chain.from_iterable(listoflists))

def halfwhere(whereM):
    half_indices = whereM[0] > whereM[1]
    return (whereM[0][half_indices], whereM[1][half_indices])

def dist_pardo(i, j, label_i, label_j, dist_fn):
    return i, j, (dist_fn(label_i, label_j) if i > j else np.nan)

def get_distance_matrix_singlethreaded(all_labels, dist_fn, label_ij=None):
    if label_ij is None:
        label_distances = [[dist_fn(label_a, label_b) if i < j else np.nan
                            for i, label_a in enumerate(all_labels)]
                            for j, label_b in enumerate(all_labels)]
        return np.array(label_distances)
    else:
        result = np.nan * np.ones((len(all_labels), len(all_labels)))
        for a, b in zip(label_ij[0], label_ij[1]):
            result[a, b] = dist_fn(all_labels[a], all_labels[b])
        return result

def get_distance_matrix(all_labels, dist_fn, label_ij=None):
    result = np.nan * np.ones((len(all_labels), len(all_labels)))

    if label_ij is None:
        label_range = range(len(all_labels))
        args = flatten([[(a, b, all_labels[a], all_labels[b], dist_fn) for a in label_range] for b in label_range])
    else:
        args = [(a, b, all_labels[a], all_labels[b], dist_fn) for a, b in zip(label_ij[0], label_ij[1])]
    with Pool() as p:
        reduced = p.starmap(dist_pardo, args)

    for item in reduced:
        result[item[0], item[1]] = item[2]
    return result

def get_pair_sets(values, same_item_ij):
    ''' TODO refactor, this has the same pattern as get_distance_matrix '''
    result = np.nan * np.ones((len(values), len(values), 2))
    for a, b in zip(same_item_ij[0], same_item_ij[1]):
        result[a][b] = np.array([values[a], values[b]])
    vector = result[same_item_ij]
    return [list([pair[0], pair[1]]) for pair in vector]

class DoDa():

    def plot_distance_distributions(self, title=None, twinx=False):
        fig, ax = plt.subplots()
        DoH = ax.hist(self.observed_distances, color="b", alpha=0.5, bins=16)
        DoM, = ax.plot([self.observed_distances.mean(), self.observed_distances.mean()], [0, ax.get_ylim()[1]], "b:")
        ax2 = ax.twinx() if twinx else ax
        DeH = ax2.hist(self.expected_distances, color="r", alpha=0.5, bins=16)
        DeM, = ax2.plot([self.expected_distances.mean(), self.expected_distances.mean()], [0, ax2.get_ylim()[1]], "r:")
        plt.legend([DoM, DeM], ["observed distance", "expected distance"])
        if title is not None:
            plt.title(title)
        
    def get_krippendorff_alpha(self):
        return 1 - self.observed_distances.mean() / self.expected_distances.mean()

    def get_sigma(self, thresh=0.05, use_kde=True, debug=False):
        if use_kde:
            kde_De = stats.gaussian_kde(self.expected_distances)
            if debug:
                kde_Do = stats.gaussian_kde(self.observed_distances)
                plt.scatter(self.expected_distances, kde_De.pdf(self.expected_distances), color="r", alpha=0.5)
                plt.scatter(self.observed_distances, kde_Do.pdf(self.observed_distances), color="c", alpha=0.5)
                plt.show()
            pDeLtDo = np.array([kde_De.integrate_box_1d(0, d) for d in self.observed_distances])
            if debug:
                plt.scatter(self.observed_distances, pDeLtDo)
                self.plot_distance_distributions()
            frac_Do_above_thresh = np.mean(pDeLtDo >= thresh)
            return 1 - frac_Do_above_thresh
        else:
            bad_dist_thresh = np.quantile(self.expected_distances, thresh)
            frac_Do_above_thresh = np.mean(self.observed_distances >= bad_dist_thresh)
            frac_De_above_thresh = np.mean(self.expected_distances >= bad_dist_thresh)
            return 1 - frac_Do_above_thresh

    def get_ks(self, fast=True, debug=False):
        d_o = self.observed_distances.flatten()
        d_e = self.expected_distances.flatten()
        if fast:
            return stats.ks_2samp(d_o, d_e, alternative="greater").statistic
        else:
            return np.mean([1 - stats.ks_2samp([x], d_e, alternative="greater").pvalue for x in d_o])


class InterAnnotatorAgreement(DoDa):
    @classmethod
    def create_from_experiment(cls, experiment, distance_fn=None):
        if distance_fn is None:
            distance_fn = experiment.distance_fn
        golddict = getattr(experiment, "golddict", None)
        return cls(experiment.annodf, experiment.item_colname, experiment.uid_colname, experiment.label_colname, distance_fn, golddict)

    def __init__(self, annodf, item_colname, uid_colname, label_colname, distance_fn, golddict=None, verbose=False):
        self.distance_fn = distance_fn
        self.annodf = annodf.sort_values(item_colname)
        self.annodf = self.annodf.rename(columns={item_colname:'item', uid_colname:"worker", label_colname:"label"})
        self.items = self.annodf["item"].values
        self.workers = self.annodf["worker"].values
        self.all_labels = self.annodf["label"].values
        self.golddict = golddict
        self.dist_from_gold = None
        self.observed_distances = None
        self.expected_distances = None
        self.distance_matrix = None
        self.verbose = verbose

    def __getstate__(self):
        to_serialize = ['observed_distances', 'expected_distances', 'distance_matrix', 'annodf', 'items_of_distances', 'workers_of_distances']
        state = dict(self.__dict__)
        return {k:state.get(k) for k in to_serialize}
    
    def setup(self, subsample_expected_distances=True, parallel_calc=False, precomputed_observed_distances=None):
        gdm = get_distance_matrix if parallel_calc else get_distance_matrix_singlethreaded

        same_item = np.array([[np.nan if item_a != item_b else 1 for item_a in self.items] for item_b in self.items])
        
        same_item_ij = halfwhere(np.where(~np.isnan(same_item)))
        if self.verbose: print("Calculating same-item distances")
        same_item_distM = gdm(self.all_labels, self.distance_fn, label_ij=same_item_ij)
        self.observed_distances = same_item_distM[same_item_ij]
        self.items_of_distances = get_pair_sets(self.items, same_item_ij)
        self.workers_of_distances = get_pair_sets(self.workers, same_item_ij)
        
        if precomputed_observed_distances is not None:
            self.expected_distances = precomputed_observed_distances
        else:
            different_item = np.array([[np.nan if item_a == item_b else 1 for item_a in self.items] for item_b in self.items])
            different_item_ij = halfwhere(np.where(~np.isnan(different_item)))
            if subsample_expected_distances:
                nsample = min(len(same_item_ij[0]), len(different_item_ij[0]))
                sample_i = np.random.choice(np.arange(len(different_item_ij[0])), size=nsample)
                different_item_ij = (different_item_ij[0][sample_i], different_item_ij[1][sample_i])
                if self.verbose: print("Calculating different-item distances")
                different_item_distM = gdm(self.all_labels, self.distance_fn, label_ij=different_item_ij)
                same_item_nonnan = np.where(~np.isnan(same_item_distM))
                different_item_nonnan = np.where(~np.isnan(different_item_distM))

                self.distance_matrix = np.nansum([same_item_distM, different_item_distM], axis=0)
            else:
                self.distance_matrix = gdm(self.all_labels, self.distance_fn)
            self.expected_distances = self.distance_matrix[different_item_ij]
    
    def plot_matrix(self, labels=None, figsize=8, title=None, show_grid=False):
        fix, ax = plt.subplots(figsize=(figsize, figsize))
        if labels is not None:
            for i, label in enumerate(self.all_labels):
                plt.annotate(label, (i, 0.15 + i), color="k")
        plt.imshow(self.distance_matrix, vmin=-0.1, vmax=1.5, cmap="plasma")
        ax = plt.gca()
        if show_grid:
            minor_grids = np.arange(-.5, self.distance_matrix.shape[0], 1)
            ax.set_xticks(minor_grids, minor=True)
            ax.set_yticks(minor_grids, minor=True)
            ax.grid(which='minor', color='w', linestyle='-', linewidth=1)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        if title is not None:
            plt.title(title)
        plt.show()


def split_items_by_gold_error(iaa, items_per_split=4):
    assert items_per_split >= 3
    if iaa.dist_from_gold is None:
        iaa.dist_from_gold = [iaa.distance_fn(label, iaa.golddict.get(item)) for item, label in zip(iaa.items, iaa.all_labels)]
    iaa.annodf["error"] = iaa.dist_from_gold

    error_sorted_items = iaa.annodf.groupby("item")["error"].mean().sort_values().index.values
    n_splits = int(len(error_sorted_items) / items_per_split)
    split_items = np.array_split(error_sorted_items, n_splits)
    return split_items

def split_iaa_by_item(iaa, split_items):
    mini_iaas = []
    for items in split_items:
        mini_df = iaa.annodf[iaa.annodf["item"].isin(items)]
        mini_iaa = InterAnnotatorAgreement(mini_df, "item", "worker", "label", iaa.distance_fn, verbose=iaa.verbose)
        mini_iaa.setup(parallel_calc=False, precomputed_observed_distances=iaa.expected_distances)
        mini_iaas.append(mini_iaa)
    return mini_iaas

# own
from itertools import chain

se_to_range = lambda a: set(range(a[0], a[1]))
def overlap_distance(ann1, ann2):
    if len(ann1) == 0 and len(ann2) == 0:
        return 0.0
    if len(ann1) == 0 or len(ann2) == 0:
        return 1.0
    set1 = set(chain.from_iterable(map(se_to_range, ann1)))
    set2 = set(chain.from_iterable(map(se_to_range, ann2)))
    intersection = set1 & set2
    # if no overlap, return 1.0
    if not intersection:
        return 1.0
    # jaccard distance
    # Jaccard distance = 1 - (size of intersection / size of union)
    union = set1 | set2
    return 1.0 - len(intersection) / len(union)
