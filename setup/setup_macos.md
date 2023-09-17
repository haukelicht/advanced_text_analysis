# Python setup with conda

To follow the setup instructions below, you'll need to work in the Terminal app.
You can open it in three different ways

1. press "Command" (the ⌘ key) + "White space" (the spacebar), type "Terminal"  in the search field, and hit Enter
2. open the Launchpad, type "Terminal" in the search field, then click Terminal
3. in the Finder, open the /Applications/Utilities folder, then double-click "Terminal.app"

see https://support.apple.com/en-gb/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac

## Installation with homebrew

*Homebrew* is a package manager for MacOS.

### Install homebrew

Please follow the instructions here: https://docs.brew.sh/Installation

### Install python and conda through minforge

Once you have installed homebrew, you can  use it to install python (version 3.10):

```shell
brew install python@3.10
whereis python
python --version
```

### Install conda through miniforge

Next, install *minigorge*, a minimal installer for Conda (see https://github.com/conda-forge/miniforge):

```shell
brew install --cask miniforge
```

## Installation without homebrew

We recommend installation and setup throgh homebrew.

But if you do *not* want to (or cannot) use homebrew, you can install manually install

- *miniforge* from https://github.com/conda-forge/miniforge#miniforge3, or 
- *Anaconda* as described [here](https://www.anaconda.com/download/) and [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html)


## Creat a new conda environment

First check if your Mac uses an Apple silicon instead of an Intel processors: https://support.apple.com/

### macOS (without Apple silicon M1/M2 processor)

```shell
# create
conda create -n advanced_text_analysis_gesis_2023 python=3.10 pip

# activate
conda activate advanced_text_analysis_gesis_2023

# verify python and pip versions and paths
python --version
which python # <== should be contain 'miniforge3/envs/advanced_text_analysis_gesis_2023/bin'

pip --version
which pip # # <== should be contain 'miniforge3/envs/advanced_text_analysis_gesis_2023/bin'
```


### macOS with Apple silicon (ARM)

source: https://towardsdatascience.com/python-conda-environments-for-both-arm64-and-x86-64-on-m1-apple-silicon-147b943ffa55

```shell
# create
CONDA_SUBDIR=osx-arm64 conda create -n advanced_text_analysis_gesis_2023 python=3.10 pip

# activate
conda activate advanced_text_analysis_gesis_2023

# verify python and pip versions and paths
python --version
which python # <== should be contain 'miniforge3/envs/advanced_text_analysis_gesis_2023/bin'

pip --version
which pip # # <== should be contain 'miniforge3/envs/advanced_text_analysis_gesis_2023/bin'
```


## Install required python packages

```shell
# for data wrangling
pip install numpy==1.25.2 pandas==2.0.3 

# for plotting
pip install seaborn==0.12.2 matplotlib==3.7.2

# for text processing and word embeddings
pip install nltk==3.8.1 gensim==4.3.1

# for stats and machine learning
pip install scipy==1.11.1 statsmodels==0.14.0 scikit-learn==1.3.0

# for deep learning
pip torch==2.1.0 tokenizers==0.13.3 datasets==2.14.2 transformers[sentencepiece]==4.31.0

# for using notebooks
pip notebook
```

### Only for macOS with Apple silicon M1/M2: Check torch's can use M1/M2 chip

*Note:* if your mac has an Apple silicon M1/M2 chip, you need to have at least macO 12.3 (Catalina) installed

```shell
sw_vers | grep ProductVersion
```

If not, update your operating system.

Next, you can check that Apple silicon M1/M2 chip available to `torch`: 

```shell
python -c 'import torch.backends.mps as mps; print(mps.is_available())' # <== should be True
```





