# Python setup with conda on macOS

This macOS-specific guide describes one way to set up Python and conda for the course.

To follow the setup instructions below, you'll need to work in the Terminal app.
You can open it in three different ways:

1. press "Command" (the ⌘ key) + "White space" (the spacebar), type "Terminal"  in the search field, and hit Enter
2. open the Launchpad, type "Terminal" in the search field, then click Terminal
3. in the Finder, open the /Applications/Utilities folder, then double-click "Terminal.app"

See https://support.apple.com/en-gb/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac

## Installation with homebrew

*Homebrew* is a package manager for macOS.

### Install homebrew

Please follow the instructions here: https://docs.brew.sh/Installation

### Install Miniforge

Once you have installed Homebrew, use it to install Miniforge, a lightweight Conda installer:

```shell
brew install --cask miniforge
```

After installation, open a new Terminal window and verify that Conda is available:

```shell
conda --version
python --version
```

If those commands do not work, consult the Miniforge installation notes here: https://github.com/conda-forge/miniforge

## Installation without homebrew

We recommend installation and setup through Homebrew.

But if you do *not* want to (or cannot) use Homebrew, you can manually install

- *Miniforge* from https://github.com/conda-forge/miniforge#miniforge3, or
- *Anaconda* as described [here](https://www.anaconda.com/download/) and [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html)


## Create a new conda environment

First check whether your Mac uses Apple silicon or an Intel processor: https://support.apple.com/

### macOS without Apple silicon

```shell
# create
conda create -y -n advanced_text_analysis python=3.11 pip

# activate
conda activate advanced_text_analysis

# verify python and pip versions and paths
python --version
which python # <== should contain 'miniforge3/envs/advanced_text_analysis/bin'

pip --version
which pip # <== should contain 'miniforge3/envs/advanced_text_analysis/bin'
```


### macOS with Apple silicon (ARM)

Source: https://towardsdatascience.com/python-conda-environments-for-both-arm64-and-x86-64-on-m1-apple-silicon-147b943ffa55

```shell
# create
CONDA_SUBDIR=osx-arm64 conda create -y -n advanced_text_analysis python=3.11 pip

# activate
conda activate advanced_text_analysis

# verify python and pip versions and paths
python --version
which python # <== should contain 'miniforge3/envs/advanced_text_analysis/bin'

pip --version
which pip # <== should contain 'miniforge3/envs/advanced_text_analysis/bin'
```


## Install required python packages

It's best to first check if there would be any version conflicts:

```shell
pip install --dry-run --ignore-installed -r https://raw.githubusercontent.com/haukelicht/advanced_text_analysis/main/setup/requirements.txt
```

If so, report the issue to hauke.licht@uibk.ac.at.

If not, install the packages:

```shell
# install all required packages in the correct versions
pip install -r https://raw.githubusercontent.com/haukelicht/advanced_text_analysis/main/setup/requirements.txt
```


### Only for macOS with Apple silicon: Check whether `torch` can use Apple silicon

*Note:* if your Mac has Apple silicon (M1/M2/... chip), you need to have at least macOS 12.3 (Monterey) installed.

```shell
sw_vers | grep ProductVersion
```

If not, update your operating system.

Next, you can check that Apple silicon support is available to `torch`:

```shell
python -c 'import torch.backends.mps as mps; print(mps.is_available())' # <== should be True
```





