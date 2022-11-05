[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

# pylint-behave

**`pylint-behave`** is a Pylint plugin to improve code analysis when analyzing a Behave project.

# Table of contents

* [Get started](#get-started)
  * [Installation](#installation)
  * [Usage](#usage)
* [Features](#features)
* [Testing](#testing)
  * [Requirements][#requirements]
  * [Set Python versions](#set-python-versions)
  * [Run][#run]
* [License](#license)
* [Changelog](#changelog)

# Get started

## Installation

This plugin can be simply installed by running:

```bash
pip install pylint-behave
```

if you want to install from a source distribution:

```bash
git clone https://github.com/eccanto/pylint-behave.git
cd pylint-behave/
python setup.py install
```

## Usage

Ensure **`pylint-behave`** is installed and on your **`PATH`**:

```bash
pylint --load-plugins=pylint_behave [options..] <path_to_your_code>
```

# Features

- Prevents warnings about *redefined names* in the Behave steps (**`step_impl`**).
    ```python
    @step('step 1')
    def step_impl():
        pass


    @given('given 1')
    def step_impl():
        pass

    ```

- Prevents warnings about *no names* in the Behave module (**`step`**, **`given`**, **`when`**, etc.).
    ```python
    from behave import step, given
    ```

# Testing

## Requirements

```bash
pip3 install -r requirements.txt
```

## Set Python versions

1. Install [pyenv](https://github.com/pyenv/pyenv)
2. Install python versions:
    ```bash
    for python_version in "3.7" "3.8" "3.9" "3.10" "3.11" "3.12" ; do pyenv install ${python_version}; done
    ```
3. Enable python versions:
    ```bash
    pyenv local "3.7" "3.8" "3.9" "3.10" "3.11" "3.12"
    ```

## Run

We use [tox](https://tox.wiki/en/latest/) and [pytest](https://docs.pytest.org/en/6.2.x) to run the
test suite:

```bash
tox
```

to run the test suite for a particular Python version, you can do:


```bash
tox -e py37
```

# License

[MIT](./LICENSE)

# Changelog

- 1.0.2 - Extended support for Python 3.10, 3.11 and 3.12, and update the documentation.
- 1.0.1 - Compatibility with pylint outdated versions.
- 1.0.0 - Initial version.
