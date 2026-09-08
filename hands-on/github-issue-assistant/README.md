# GitHub Issue Assistant MCP Server

## What I built

I created a GitHub Issue Assistant MCP server using Python and the GitHub REST API.

The server provides different tools for viewing, searching, creating, and closing issues in my GitHub repository.

The tools communicate with GitHub through the GitHub REST API.

## What can it do?

The server has four tools:

- **`get_repo_issues`** — gets the open issues from the repository.

- **`search_issues`** — searches for issues using a word or phrase.

- **`create_issue`** — creates a new issue in the repository.

- **`close_issue`** — closes an existing issue using its issue number.

For example:

> "Show me the issues in my repository."

The `get_repo_issues` tool gets the issues from GitHub and returns them.

Or:

> "Search for issues related to MCP."

The `search_issues` tool searches the repository and returns matching issues.

The server can also create and close issues through the GitHub API.

## How it works

The basic flow is:

MCP Client

↓

MCP Server

↓

MCP Tools

↓

GitHub REST API

↓

GitHub Repository

For example, when `create_issue` is called, the MCP server sends a POST request to the GitHub API.

When `close_issue` is called, it sends a PATCH request to update the issue's state.

This shows how MCP tools can act as a bridge between an AI application and an external service.

## Authentication

The server uses a GitHub fine-grained Personal Access Token to authenticate API requests.

The token is stored as an environment variable instead of being written directly in the code.