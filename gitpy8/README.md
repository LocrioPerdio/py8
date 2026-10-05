# The Matrix — Welcome to the Real World of Data Engineering

This project is an introduction to some of the fundamental tools used in Python data engineering:

* Virtual environments
* Python package management
* Dependency management with `pip` and Poetry
* Data analysis and visualization
* Environment variables
* `.env` configuration files
* Secure handling of sensitive configuration

The project is divided into three exercises, each focusing on a different aspect of Python development and environment management.

---

## Requirements

* Python 3.10 or later
* `pip`
* `venv`
* Poetry (required for Exercise 1)
* `python-dotenv` (required for Exercise 2)

The project follows the requirements specified in the assignment, including type annotations and `flake8` compatibility.

---

# Exercise 0 — Entering the Matrix

Directory:

```text
ex0/
```

Main file:

```text
construct.py
```

This exercise demonstrates how Python virtual environments work.

The program detects whether it is currently running inside a virtual environment and displays information about the Python installation.

It uses:

* `sys`
* `os`
* `site`

### Features

The program:

* Detects whether a virtual environment is active.
* Displays the current Python executable.
* Displays the virtual environment name and path.
* Shows the package installation directory.
* Provides instructions for creating and activating a virtual environment when none is detected.

This follows the assignment requirement for `construct.py`.

## Usage

From the `ex0` directory:

```bash
python3 construct.py
```

### Without a virtual environment

The program reports that the system is running in the global Python environment and provides instructions to create one:

```bash
python3 -m venv matrix_env
source matrix_env/bin/activate
```

On Windows:

```powershell
matrix_env\Scripts\activate
```

Then run the program again.

### With a virtual environment

```bash
python3 -m venv matrix_env
source matrix_env/bin/activate
python3 construct.py
```

The program should report that it is running inside an isolated environment.

The virtual environment itself should **not** be committed to the repository.

---

# Exercise 1 — Loading Programs

Directory:

```text
ex1/
```

Files:

```text
loading.py
requirements.txt
pyproject.toml
```

This exercise focuses on Python dependency management using both `pip` and Poetry.

The program creates simulated Matrix data using NumPy, processes it with Pandas and generates a visualization using Matplotlib.

The assignment specifically requires NumPy to be the source of the simulated dataset rather than using hardcoded lists or `range()`.

## Dependencies

The project uses:

* `numpy==1.25.0`
* `pandas==2.1.0`
* `matplotlib==3.7.2`

These dependencies are defined in both:

```text
requirements.txt
```

and:

```text
pyproject.toml
```

## Installation with pip

From the `ex1` directory:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python3 loading.py
```

## Installation with Poetry

Install the dependencies with:

```bash
poetry install
```

Then run:

```bash
poetry run python loading.py
```

These are the two dependency-management approaches required by the exercise.

## Program behavior

When executed, the program:

1. Checks whether the required packages are installed.
2. Checks their installed versions.
3. Reports missing or incorrect dependencies.
4. Generates 1000 simulated data points using NumPy.
5. Creates a Pandas DataFrame.
6. Generates a Matplotlib visualization.
7. Saves the resulting graph as:

```text
matrix_analysis.png
```

Example:

```text
LOADING STATUS: Loading programs...

[OK] pandas (2.1.0) - Data manipulation ready
[OK] numpy (1.25.0) - Numerical computation ready
[OK] matplotlib (3.7.2) - Visualization ready

Analyzing Matrix data...
Processing 1000 data points...
Generating visualization...

Analysis complete!
Results saved to: matrix_analysis.png
```

---

# Exercise 2 — Accessing the Mainframe

Directory:

```text
ex2/
```

Files:

```text
oracle.py
requirements.txt
.env.example
.gitignore
```

This exercise demonstrates configuration management using environment variables and `.env` files.

The objective is to keep configuration and sensitive information outside the source code. The assignment specifically requires the use of `python-dotenv` rather than implementing a custom `.env` parser.

## Dependency

The exercise uses:

```text
python-dotenv
```

Install it with:

```bash
pip install -r requirements.txt
```

## Configuration

The program uses the following environment variables:

```text
MATRIX_MODE
DATABASE_URL
API_KEY
LOG_LEVEL
ZION_ENDPOINT
```

These variables represent application configuration such as:

* Development or production mode
* Database connection
* API authentication
* Logging level
* External service endpoint

The assignment requires real secrets to be kept out of version control and the `.env` file to be included in `.gitignore`.

## Setup

Create the local `.env` file from the example:

```bash
cp .env.example .env
```

Then edit `.env` with the required configuration values.

Run:

```bash
python3 oracle.py
```

## Environment variable override

Environment variables can also be supplied directly when executing the program:

```bash
MATRIX_MODE=production API_KEY=secret123 python3 oracle.py
```

Environment variables provided directly by the shell take precedence over values loaded from `.env`.

---

# Project Structure

```text
.
├── ex0/
│   └── construct.py
│
├── ex1/
│   ├── loading.py
│   ├── requirements.txt
│   └── pyproject.toml
│
└── ex2/
    ├── oracle.py
    ├── requirements.txt
    ├── .env.example
    └── .gitignore
```

---

# Concepts Learned

Through the three exercises, this project covers:

### Virtual environments

Virtual environments provide isolated Python environments where packages can be installed without modifying the global Python installation.

### pip

`pip` installs Python packages from a dependency list such as:

```text
requirements.txt
```

### Poetry

Poetry provides dependency management and project configuration through:

```text
pyproject.toml
```

### Environment variables

Environment variables allow applications to receive configuration without hardcoding values directly into the source code.

### `.env` files

`.env` files provide a convenient way to store development configuration locally.

They should not contain production secrets in a repository and should be excluded from version control.

### Dependency checking

The project checks whether required dependencies are available and reports missing or incorrect versions instead of failing without explanation.

---

# AI Usage

AI tools were used as a learning and development support tool during this project.

They were used for:

* Understanding Python concepts and standard libraries.
* Exploring virtual environments and dependency management.
* Clarifying errors and debugging approaches.
* Reviewing code and documentation.
* Improving understanding of `pip`, Poetry and environment variables.

AI-generated suggestions were reviewed, tested and adapted to the project requirements. The final code was understood and validated by the author.

AI was used as a support tool rather than as a replacement for understanding the implementation, in accordance with the project's guidance on responsible AI usage.

---

# Peer Review

During the peer review, the main concepts demonstrated by this project are:

* Why virtual environments are useful.
* How Python dependencies can be managed with `pip`.
* How Poetry differs from `pip`.
* How environment variables can be used for configuration.
* Why sensitive information should not be hardcoded or committed to Git.
* How these tools contribute to maintainable and configurable Python applications.

The objective is not only to make the programs work, but also to understand the reasoning behind the tools and be able to explain the implementation.

