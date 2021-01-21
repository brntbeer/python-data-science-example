# Description

This branch contains an example of a basic, manually-crafted codespace which can be used (and
actually _was_ used!) to develop a simple Python application.

The important files here are
[`devcontainer.json`](https://github.com/dassencio/codespaces-demo-python/blob/simple/.devcontainer/devcontainer.json)
and
[`Dockerfile`](https://github.com/dassencio/codespaces-demo-python/blob/simple/.devcontainer/Dockerfile),
which together define everything we need inside our development environment:

- Base operating system
- System packages
- Python modules
- Editor plugins
- Editor settings.

# Usage instructions

Create a codespace for this branch by clicking `Code` > `Open with Codespaces` > `New codespace`.
When it is ready, start a debugging session by running `Launch octocat.py` inside the Run view.