# Adding common tasks commands

There are alot of development tasks that require interacting with a CLI.
These commands can get complicated so usually the team stores them in a file and never commits them.

## Solution

[Taskipy](https://github.com/illBeRoy/taskipy) is a python package that allows us to define tasks in
our pyproject.toml file.

For example, we want to run all formatting rules on our source folder.
Instead of asking everyone to remember the command.
We create a new command called format.
and tell everyone to use
`poetry run task format`

## Adding new Tasks

1. Go to the pyproject.toml file.
2. Go to the `[tool.taskipy.tasks]` section
3. Copy one of tasks and modify them to your needs
