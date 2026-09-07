# Smart Task Assistant MCP Server

In my previous hands-ons, I worked with MCP tools, local files, a SQLite database, and an external API.

This time, I built a more complete task management MCP server with multiple tools working with the same database.

The goal was to understand how an MCP server can provide different capabilities that an AI can use depending on what the user asks.

## What I built

I created a task management MCP server using Python and SQLite.

The server provides different tools for creating, viewing, searching, completing, and analyzing tasks.

All the tools work with the same SQLite database, so changes made by one tool can be seen by the other tools.

## What can it do?

The server has six tools:

- **create_task** — creates a new task.
- **list_tasks** — shows all tasks and their current status.
- **search_tasks** — searches for tasks using a word or phrase.
- **get_task_stats** — shows the total, completed, and pending tasks.
- **get_next_task** — finds the next pending task.
- **complete_task** — marks a task as completed.

For example:

> "Find my MCP tasks."

The `search_tasks` tool searches the database and returns the matching tasks.

Or:

> "How many tasks have I completed?"

The `get_task_stats` tool calculates the task statistics and returns the result.

## How it works

The basic flow is:

MCP Client  
↓  
MCP Server  
↓  
MCP Tools  
↓  
SQLite Database

All the tools use the same database.

For example, when `complete_task` is called, the task is updated in the database.

When `get_task_stats` is called afterwards, it reads the updated database and shows the new statistics.

This shows how different MCP tools can work with shared data.

## Technologies used

- Python
- MCP Python SDK
- SQLite
- MCP Inspector

## What I learned

This hands-on helped me understand how multiple MCP tools can work together with a shared database.