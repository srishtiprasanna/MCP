# What is MCP?

MCP stands for Model Context Protocol. It is a standard way for an AI application to connect with external tools and data.

An LLM can understand and generate text, but by itself it cannot directly do things like access a database, read a file, call an API, search GitHub, or perform some action in another system.

MCP acts like a bridge between the AI and these external capabilities.

For example, instead of building a separate integration every time an AI needs to use a database or an API, MCP provides a common way for the AI to communicate with it.


# How does MCP work?

There are mainly three parts:

Host → Client → Server

Host: The AI application that the user interacts with.

Client: The part of the host that communicates with MCP servers.

Server: Provides the actual tools or data that the AI can use.

For example:

            User
             ↓
      AI Application
             ↓
         MCP Client
             ↓
         MCP Server
             ↓
   External tool / data / API


# What can an MCP Server provide?

There are three main things:

1. Tools

Tools are basically actions that the AI can ask the server to perform.

For example:

- calculate_sum()
- search_database()
- send_email()
- create_ticket()
- add_task()  

So the AI/client can discover these tools and call them when required.


2. Resources

Resources are information that the AI can read.

For example, an MCP server could provide access to:

- A file
- Database information
- Documentation
- Application data

The difference  is:

Tool = do something

Resource = get/read something


3. Prompts

Prompts are reusable instructions or prompt templates that an MCP server can provide.

They can be useful when there is a particular way an application wants an AI to perform a task.


# Why is MCP useful?

Without MCP, an AI application may need to have different custom integrations for different services.

For example:

AI → Custom code → Database

AI → Custom code → GitHub

AI → Custom code → API

AI → Custom code → Files

             AI Application
                   ↓
               MCP Client
                   ↓
              MCP Protocol
                   ↓
              MCP Servers
              ↙    ↓    ↘
          Database  API  Files

The main idea is standardization. The AI application doesn't need to know all the internal details of every external system. It can communicate with an MCP server through the standard MCP protocol.

Hands-on: Built a simple Task Manager MCP server using Python and tested the tools using MCP Inspector.

# References
https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro
https://www.geeksforgeeks.org/artificial-intelligence/model-context-protocol-mcp/


