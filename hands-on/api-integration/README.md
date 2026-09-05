# API Integration MCP Server

In my previous hands-ons, I worked with simple tools, local files, and a SQLite database.

This time, I connected an MCP server to an external REST API.

I used JSONPlaceholder, a free fake API made for testing and learning.

## What I built

I created an MCP server that can retrieve user information from an external API.

The server has two tools that make requests to the API and return the information to the MCP client.

## What can it do?

The server has two tools:

- **get_user** — gets information about a specific user using their user ID.
- **list_users** — gets a list of all users from the API.

For example:

> Get information about user 1.

The MCP server calls the external API, gets the user information, and returns it.

## How it works

The basic flow is:

MCP Client  
↓  
MCP Server  
↓  
MCP Tool  
↓  
External REST API  
↓  
Response

For example, when `get_user` is called, the server sends a request to the JSONPlaceholder API.

The API returns the user data in JSON format.

The server then picks the required information and returns it in a simple format.

## Technologies used

- Python
- MCP Python SDK
- Requests
- REST API
- JSONPlaceholder
- MCP Inspector

## What I learned

This hands-on helped me understand how MCP can connect an AI application to an external API.