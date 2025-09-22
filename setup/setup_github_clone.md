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
![Open Terminal](./screenshots/macos_terminal.png)

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
5. Select a local folder (e.g., `Documents/advanced_text_analysis`) where you want to save it.
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

- Always `git pull` before starting work, to make sure you have the latest version.
- Do **not** edit files in the repository unless you are asked to. Changes may be overwritten when pulling updates.
- If you accidentally make edits, keep a backup copy outside the repository folder.
- If you see error messages when pulling, contact the course instructor.
