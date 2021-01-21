# Description

A codespace is a development environment described via code. When a codespace is created, it is
always done so in the context of a repository branch from which the settings for the codespace are
extracted. These settings must reside in a file named
[`devcontainer.json`](https://code.visualstudio.com/docs/remote/devcontainerjson-reference) located
either at the repository root or inside a folder named `.devcontainer`.

This branch contains only a single file (`README.md` &mdash; you are looking a it), and thus no
 settings specifying how a codespace should be created (i.e., no `devcontainer.json`). A codespace
 created for this branch will therefore use the default settings available for all configuration
 parameters.

A codespace created using the default settings will not be generally useful for development
purposes, but is already a great starting point for editing files, for manually bootstraping more
complex codespaces and for running experiments inside a safe environment.

# Usage instructions

Create a codespace for this branch by clicking `Code` > `Open with Codespaces` > `New codespace`.
When it is ready, you will be able to play with the editor (e.g. install some plugins you like or
write a script) and also to explore the contents of the Docker container which the codespace is based
on (you can open a terminal by clicking the menu icon, then `Terminal` > `New Terminal`).

Broke something? The system is (virtually) catching fire? No problem! Simply leave the codespace by
clicking the GitHub icon (on the top-left corner), then delete it and create a new one!