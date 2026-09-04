# Pull a GitHub Repository

## About GitHub

In our course, we will use [*GitHub*](https://github.com/), a platform for hosting and sharing code.
GitHub allows you to download ("clone") repositories (folders with code, data, and documentation) directly to your computer.
You can then work with these files locally and keep them up to date.

## Setup instructions

To get started with GitHub, you need to clone the repository once to your computer.
There are two main ways to do this:

1. using the command line (Anaconda Prompt on Windows, Terminal on macOS)
2. using the GitHub Desktop app

After that, you can pull updates whenever something changes in the repository.


### 1. Cloning with the Command Line

#### _otherwise_, on Windows

- Open the **Anaconda Prompt** (installed with Anaconda).
![Open Anaconda Prompt](./screenshots/windows_anaconda_prompt.png)

- Navigate to a folder where you want to store the repository (e.g., your `Documents` folder):

```shell
cd %USERPROFILE%\Documents
```

- Clone the repository using its HTTPS link:

```shell
git clone https://github.com/haukelicht/advanced_text_analysis.git
```

#### _otherwise_. on macOS

- Open the **Terminal** app.

- Navigate to a folder where you want to store the repository (e.g., your `Documents` folder):

```shell
cd ~/Documents
```

- Clone the repository using its HTTPS link:

```shell
git clone https://github.com/haukelicht/advanced_text_analysis.git
```

*Notes:*

- Make sure `git` is installed. On macOS, you may be asked to install Xcode command line tools when running `git` the first time. On Windows, `git` comes bundled with Anaconda, so you are ready to go.
- It's best to keep all course-related repositories in a dedicated folder (e.g., `Documents/CourseRepos`).


### 2. Cloning with GitHub Desktop

If you prefer a graphical interface:

1. Install [GitHub Desktop](https://desktop.github.com/).
2. Open the app and log in with your GitHub account.
3. Go to **File > Clone Repository**.
4. Paste the repository's HTTPS link: https://github.com/haukelicht/advanced_text_analysis.git
5. Select a local folder (e.g., `Documents`) where you want to save it.
6. Click **Clone**.


### 3. Pulling Updates

Once the repository is cloned, you don't need to clone it again.
Instead, update it with the latest changes:

#### **Command line (Windows/macOS):**

```shell
cd path/to/repository
git pull
```

#### **GitHub Desktop:**

Click **Fetch origin** → **Pull origin** in the top bar.


### 4. Important Notes

- To make sure you have the latest version, always `git pull` before you start working on a notebook.
- To make sure that your local changes to notebooks and other files won't get lost, always save a copy of them with your name as suffix (e.g., save a copy of example_notebook.ipynb" as "example_notebook-hauke.ipynb"). Otherwise, your changes may be overwritten when pulling updates or you'll get [merge conflict](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/resolving-a-merge-conflict-using-the-command-line).
- If you see error messages when pulling, contact the course instructor.
