from mcp.server import MCPServer
import requests


server = MCPServer(
    name="User API",
    description="An MCP server that retrieves user information from an external API."
)


@server.tool()
def get_user(user_id: int) -> str:
    """Get information about a user from an external API."""

    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    )

    if response.status_code != 200:
        return f"User {user_id} not found."

    user = response.json()

    return (
        f"Name: {user['name']}\n"
        f"Username: {user['username']}\n"
        f"Email: {user['email']}\n"
        f"City: {user['address']['city']}\n"
        f"Company: {user['company']['name']}"
    )

@server.tool()
def list_users() -> str:
    """Get a list of users from the external API."""

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    if response.status_code != 200:
        return "Could not retrieve users."

    users = response.json()

    result = []

    for user in users:
        result.append(
            f"{user['id']}. {user['name']} - {user['email']}"
        )

    return "\n".join(result)

if __name__ == "__main__":
    server.run()