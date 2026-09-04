# Task Database MCP Server

In this hands-on, I connected an MCP server to a SQLite database and created tools to manage tasks.

## What I built

The tasks are stored in a SQLite database, and the MCP server allows a client to create, view, update, and delete tasks.

The server also has a Resource that can provide the current list of tasks.

## What can it do?

The server has four tools:

- **create_task** — creates a new task.
- **list_tasks** — shows all the tasks.
- **update_task** — changes a task's title or completion status.
- **delete_task** — deletes a task.

It also has one Resource:

- **tasks://all** — provides the current list of tasks from the database.

## Tools vs Resources

One thing I learned from this project is the difference between Tools and Resources.

In simple terms:

- **Tools** → the AI asks the server to do something.
- **Resources** → the AI asks the server to provide some information.

For example:

> Create a task → Tool  
> Delete a task → Tool  
> Show all the tasks → Resource

## How it works

The basic flow is:

MCP Client  
↓  
MCP Server  
↓  
Tools / Resources  
↓  
SQLite Database

For example, when `create_task` is called, the server adds the task to the SQLite database.

When `list_tasks` is called, the server reads the tasks from the database and returns them.

The `tasks://all` Resource also reads the database and provides the current task information.

## Technologies used

- Python
- MCP Python SDK
- SQLite
- MCP Inspector
