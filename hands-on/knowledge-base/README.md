# Knowledge Base MCP Server

Built a simple MCP server that gives an AI access to a small collection of local documents.

The idea is that instead of the AI having to know everything itself, it can use the MCP server to look up information when needed.

I created a few sample company documents containing information about company details, policies, and products.

The MCP server can then search these documents or return a complete document when requested.

## What can it do?

The server has two tools:

- **search_knowledge** — searches the documents for a given word or phrase and returns the relevant information.
- **get_document** — returns the complete contents of a particular document.

For example, an AI could ask:

> "How many days of paid leave do employees get?"

The MCP server searches the knowledge base and can return the information from `policies.txt`.

## What I learned

In my first MCP hands-on, I used MCP to expose simple functions as tools.

In this hands-on, I connected tools to actual data stored in local files.

This helped me understand how MCP can be used to give an AI controlled access to external information instead of just performing simple actions.