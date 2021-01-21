# Description

This branch contains an example of a complex codespace with a large collection of libraries, modules
and tools which together form an environment where a machine learning application can be developed
with little to no initial setup effort needed.

This codespace was not created from scratch, but based on the
[`python-3-anaconda`](https://github.com/microsoft/vscode-dev-containers/tree/master/containers/python-3-anaconda)
codespace from the [`microsoft/vscode-dev-containers`](https://github.com/microsoft/vscode-dev-containers)
repository, where codespaces for various types of projects and programming languages are available.
Before setting up your own codespace configuration, it is always a good idea to look for a
publicly-available one which already has at least part of your needs covered (open source FTW!).
If you are lucky enough, you may even find a codespace which already has everything you want &mdash;
off the shelf! :smile:

There are two projects in this branch: the first one contains a test application (under
[`test-project`](https://github.com/dassencio/codespaces-demo-python/tree/complex/test-project)) and
the second one contains a Jupyter Notebook document with machine learning models for analyzing the
[Titanic dataset](https://www.openml.org/d/40945) (under
[`titanic`](https://github.com/dassencio/codespaces-demo-python/tree/complex/titanic)).

# Usage instructions

Create a codespace for this branch by clicking `Code` > `Open with Codespaces` > `New codespace`.
When it is ready, open and run
[`test-project/hello.py`](https://github.com/dassencio/codespaces-demo-python/blob/complex/test-project/hello.py).
This will show you if the codespace has been properly set up and also activate the `conda` environment which is
necessary for the next stage of the demo.

The second (and more interesting) part of the demo is on
[`titanic/titanic.ipynb`](https://github.com/dassencio/codespaces-demo-python/blob/complex/titanic/titanic.ipynb).
This is a Jupyer Notebook document containing two machine learning models used to analyze the
Titanic dataset. It illustrates how well Jupyter Notebook integrates with the web-based version of
Visual Studio Code and how the codespace enables the data analysis to be carried out without _any_
setup effort needed from the user.

**NOTE**: The analysis in
[`titanic/titanic.ipynb`](https://github.com/dassencio/codespaces-demo-python/blob/complex/titanic/titanic.ipynb)
closely follows [this tutorial](https://code.visualstudio.com/docs/python/data-science-tutorial).
Each step is thoroughly explained there, so follow the link if you wish to understand things in more
detail.
