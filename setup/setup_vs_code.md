# Setting up VS Code

We will be using Visual Studio Code (VS Code) as a code editor in the workshop.
Please install **VS Code** before from https://code.visualstudio.com/Download.

You will also need to install **Python** and the **conda** package manager.
If you have not done so before. please refer to the setup instructions in [setup_python_with_anconda.md](./setup_python_with_anconda.md).
Alternatively, you can download and install

- Python as described [here](https://www.python.org/downloads)
- and conda as described [here](https://conda.io/projects/conda/en/latest/user-guide/install)

Finally, in VS code, you also need to install the Python and Jupyter **extensions**.
You can do this by clicking on the "Extensions" icon in the left-hand sidebar, searching for "Python" ("Jupyter") and clicking on the "Install" button.

You shouldn't run into any issues if you have admin rights on your computer.
But if you run into difficulties, please check https://code.visualstudio.com/docs/languages/python.
If you don't find a solution, you can also email Hauke at hauke.licht@uibk.ac.at.


### Conda environment

**_Note:_** You can skip this step if you have already completed steps 3 and 4 in [setup_python_with_anconda.md](./setup_python_with_anconda.md).

To ensure that everyone uses the same python and packages versions, we will create and use a virtual conda environment.
For this, you'll need to open 

- the *Anaconda Prompt* app if you are a Windows user, **_or_**
- the *Terminal* app if you are a Mac user

In the Anaconda Prompt/Terminal, execute the following lines (by copy-pasting them there and pressing Enter):

```bash
conda create -n advanced_text_analysis_gesis -y python=3.11 pip
conda activate advanced_text_analysis_gesis
conda install notebook
pip install -r https://raw.githubusercontent.com/haukelicht/advanced_text_analysis/main/setup/requirements.txt
```

### Selecting the conda environment in VS Code

When running some python script or a cell in a Jupyter notebook in VS Code, you will be prompted to select the python interpreter.

<img src="./imgs/vscode_python_environments_popup.png" alt="Pop-up in VS Code for selecting a python interpreter" style="width:400px;"/>

In our case, we will always select the `advanced_text_analysis_gesis` environment


**_Alternatives_** 

- create a native python virtual environment (like [this](https://realpython.com/lessons/creating-virtual-environment/)), and/or
- install the required python packages listed the [requirements.txt](setup/requirements.txt) file manually
