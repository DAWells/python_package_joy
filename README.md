# Python Packaging, sheer joy
Following [this guide](https://python-packaging-tutorial.readthedocs.io/en/latest/index.html)
on packagin python packages. This guide is unfinished
but claims to use all the most modern practices including continuous
intergration with github actions.

Previous package `~/work/tools/testpackdw/` looks like it wasn't
using the most modern practices.

In this guide we'll create a simple python package called `boxed`,
set up tests, and run those tests using github actions,
check that the package works on multiple OSs and different python versions.

# Create venv
`python -m venv venv/.boxed`

Using github's boiler plate [`.gitignore`](https://github.com/github/gitignore/blob/main/Python.gitignore) to prevent
version controlling venvs.