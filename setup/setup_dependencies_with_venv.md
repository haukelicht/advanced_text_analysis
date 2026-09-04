# Setup Dependencies with `venv`

**Important:** This is an alternative setup path for users who already have a working Python 3.11+ installation and prefer not to use Anaconda. I cannot guarantee full support if you run into issues with this route.

If you want the most reliable and beginner-friendly setup, please use [setup_python_with_anaconda.md](./setup_python_with_anaconda.md) instead.

## 1. Check your Python installation

Open a Terminal (macOS/Linux) or PowerShell / Command Prompt (Windows) and check that Python is available:

```shell
python --version
```

You should see Python 3.11 or higher.

## 2. Create a virtual environment

Go to the folder where you want to work with the course materials, then create a new environment:

```shell
python -m venv .venv
```

## 3. Activate the environment

### macOS / Linux

```shell
source .venv/bin/activate
```

### Windows PowerShell

```shell
.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```shell
.venv\Scripts\activate.bat
```

When the environment is active, your shell prompt usually shows `(.venv)` at the beginning.

## 4. Upgrade pip

```shell
python -m pip install --upgrade pip
```

## 5. Install the course requirements

```shell
pip install -r https://raw.githubusercontent.com/haukelicht/advanced_text_analysis/main/setup/requirements.txt
```

If you want to check whether the requirements can be resolved before installing them, run:

```shell
pip install --dry-run --ignore-installed -r https://raw.githubusercontent.com/haukelicht/advanced_text_analysis/main/setup/requirements.txt
```

## 6. Verify the setup

```shell
python --version
pip --version
```

If these commands work and the install completed without errors, the environment is ready.

## Notes

- Use this path only if you already know how to work with Python environments.
- If package installation fails, compare the error against the Anaconda-based instructions first.
- For macOS users with Apple silicon, a conda-based setup is still the recommended path for the course.