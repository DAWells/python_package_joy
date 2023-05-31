# Python Packaging, sheer joy
Following [this guide](https://python-packaging-tutorial.readthedocs.io/en/latest/index.html)
on packaging python packages. This guide is unfinished
but claims to use all the most modern practices including continuous
intergration with github actions.

Previous package `~/work/tools/testpackdw/` looks like it wasn't
using the most modern practices.

In this guide we'll create a simple python package called `boxed`,
set up tests, and run those tests using github actions,
check that the package works on multiple OSs and different python versions.

# Set up
## Version control
Use github to version control.

Using github's boiler plate [`.gitignore`](https://github.com/github/gitignore/blob/main/Python.gitignore) to prevent
version controlling venvs.

## Create venv
`python -m venv venv/.boxed`

This can be activated with `source venv/.boxed/bin/activate` and deactivated with `deactivate`.

# Creating the package

## Folder structure
├── docs
├── pyproject.toml
├── src
│   └── boxed
│   │   ├── __init__.py
│   │   └── boxed.py
└── tests

```mkdir -p src/boxed tests docs```

Save the package code as `src/boxed/boxed.py`.
Create `__init__.py` so it's actually a package:
`touch src/boxed/__init__.py`.

## TOML
Create and save the file `pyproject.toml`.

```
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "boxed"
version = "0.1.0"
```

## Install
You should now be ready to install the package (in the
venv).
Run `pip install -e .` from the parent directory i.e.
`python_package_joy`. This may require you to update pip,
an error message will explain how to do this.

The `-e` in our pip command means we can edit the package
and it will take effect without reinstalling.

Then you can import and run functions from your new package
```
from boxed.boxed import get_box
print(get_box(20, "Box"))
```
