\# BOOTSTRAP



A small CLI utility that creates a new Python project directory, sets up a virtual environment inside it, and optionally installs any Python packages you specify.



\## What it does



When you run the script, it will:



1\. Prompt you for a project name.

2\. Create a project directory with that name.

3\. Create a `.venv` virtual environment inside the project.

4\. Optionally install one or more packages into the virtual environment using `pip`.



\## Requirements



\* Python 3.8 or later

\* Internet connection (if installing packages)



\## Usage



Run the script:



```bash

python bootstrap.py

```



Example:



```text

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* BOOTSTRAPPER \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*



Enter your project name: my\_project

Enter the packages you want to install separated by a single space or leave empty:

requests flask

```



This creates the following structure:



```text

my\_project/

└── .venv/

```



with `requests` and `flask` installed in the virtual environment.



\## Features



\* Creates a project directory automatically.

\* Creates an isolated Python virtual environment.

\* Installs multiple packages in one step.

\* Works on both Windows and Linux.

\* Basic error handling for failed package installations.



\## Future Improvements



\* Generate a `requirements.txt` file.

\* Create a starter `main.py`.

\* Generate a `.gitignore`.

\* Automatically activate the virtual environment after creation.

\* Support installing packages from a `requirements.txt` file.



