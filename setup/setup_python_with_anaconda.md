# Setup Python with Anaconda

## About Anaconda

In the course we will use [*Anaconda*](https://www.anaconda.com/). 
On [Wikipedia](https://en.wikipedia.org/wiki/Anaconda_(Python_distribution)), Anaconda is described as a

> ... distribution of the Python and R programming languages for scientific computing, that aims to simplify package management and deployment.
> The distribution includes data-science packages suitable for Windows, Linux, and macOS.

If you [ask ChatGPT](https://chat.openai.com/share/958fe6cc-b411-43e5-b156-23fb6ef4fb3f) why and how Anaconda is useful for teaching data science-related topics, you'll learn -- among other things -- that this is because

> 1. ... Anaconda comes with a powerful package manager called Conda ... [which] allows users to easily install, update, and manage various data science libraries and tools. 
> 2. ... Anaconda is available for Windows, macOS, and Linux, making it suitable for a diverse range of students using different operating systems.
> 4. ... Anaconda enables the creation of isolated virtual environments ... [which] [allow] students to work on different projects with different dependencies without interference.
> 5. ... Anaconda includes Jupyter Notebook, ... [which] are widely used ... for creating interactive and shareable documents that combine code, explanations, and visualizations.
> 6. ... Anaconda, Inc. offers educational resources and tutorials specifically designed for teachers and students. 

## Setup instructions

To setup Anaconda for our course, you need to take three steps:

1. install Anaconda
2. verify your Anaconda installation (python and conda should be ready to go)
3. create a new conda environment
4. install required pacakages in your conda environment

Let's take these steps in turn!

**_Note:_** If you encounter any issues, email me (hauke.licht@uibk.ac.at) or [post an issue](https://github.com/haukelicht/advanced_text_analysis/issues).

### 1. Install Anaconda

We recommend manual installation.
For this, you need to download the installer for your operation system (Windows or macOS), and then run the installer to configure Anaconda for use on your computer 

#### Windows

Download the Installer from https://www.anaconda.com/download/success#windows

With the installer downloaded, the following two links provide detailed follow-up instructions: 

- https://www.datacamp.com/tutorial/installing-anaconda-windows
- https://www.anaconda.com/docs/getting-started/anaconda/install#windows-installation

*Notes:*

1. The screenshots in the first link are a little outdated, but the instructions remain valid.
2. In step six described in the first link, please opt for the "Alternative Aproach" (i.e., automatically add Anaconda to your PATH variable at installation time) 

#### MacOS/Linux

Download the Installer from https://www.anaconda.com/download/success#mac or 
follow the instructions in ['setup_macos.md'](./setup_macos.md)

*Notes:* 

- If your computer has Apple silicon (i.e., and M1/M2/... chip), choose "64-bit (Apple silicon) Graphical Installer". Otherwise, choose ""64-bit (Intel chip) Graphical Installer""
- If you *don't know* whether your Mac has Apple silicon, follow these instructions to find out: https://www.howtogeek.com/706226/how-to-check-if-your-mac-is-using-an-intel-or-apple-silicon-processor

With the installer downloaded, the following two links provide detailed follow-up instructions: 

- https://www.datacamp.com/tutorial/installing-anaconda-mac-os-x
- https://www.anaconda.com/docs/getting-started/anaconda/install#macos-linux-installation

**_Important note:_** When asked to select the destination of the installation (step 4 in the second link), please choose "Install for me only" (e.g., use your Application folder)

### 2. Verify your Anaconda installation

follow the instructions here: 

- Windows: https://www.anaconda.com/docs/getting-started/anaconda/install#windows-installation:how-do-i-verify-my-installers-integrity
- macOS/Linux: https://www.anaconda.com/docs/getting-started/anaconda/install#macos-linux-installation:how-do-i-verify-my-installers-integrity

### 3. Create a new conda environment

#### Using the Anaconda Navigator app

The  Anaconda Navigator app should have open when you finished your Anaconda installation.
If not, open it from your applications (see [here](https://docs.anaconda.com/free/navigator/getting-started/#navigator-starting-navigator) for instructions).

Then, follow the instructions [here](https://docs.anaconda.com/free/navigator/tutorials/create-python35-environment/),  taking into account the following notes:

- in step 4, use 'advanced_text_analysis_gesis_2025' as environment name
- in step 5, use the python version that starts with '3.11' (or higher)
- in step 7, choose "open Terminal" and go to the next step of our setup process 

#### Using the command line

- on Windows: Open the Anaconda Prompt
- on macOS: Open the Terminal app

To create a new conda environment, run the following lines:

**_Note:_** If you are a Mac user and your MacBook has an M1, M2, or M3 chip, put `CONDA_SUBDIR=osx-arm64` in front of `conda create` when running the code below

```shell
conda create --name advanced_text_analysis_gesis_2025 python=3.12 pip

conda activate advanced_text_analysis_gesis_2025
```


- The part after `--name` is the name of the environment. So our new environment is called 'advanced_text_analysis_gesis_2025'
- `python=3.12` specifies that we want to use python version 3.12 in this environment
- `pip` specifies that we want to pre-install pip

### 4. Install required pacakages

It's best to first check if there would be any version conflicts.

So first, run the following command in the Anaconda Prompt (Windows)/Terminal (macOS):

```shell
pip install --dry-run --ignore-installed -r https://raw.githubusercontent.com/haukelicht/advanced_text_analysis/main/setup/requirements.txt
```

If this raises any error messages, report them to hauke.licht@uibk.ac.at.

If not, install the packages by running the following command in the Anaconda Prompt (Windows)/Terminal (macOS):

```shell
# install all required packages in the correct versions
pip install -r https://raw.githubusercontent.com/haukelicht/advanced_text_analysis/main/setup/requirements.txt
```

## Errors and issues

If you encounter any issues, [post an issue](https://github.com/haukelicht/advanced_text_analysis/issues) or email Hauke (via hauke.licht@uibk.ac.at).
