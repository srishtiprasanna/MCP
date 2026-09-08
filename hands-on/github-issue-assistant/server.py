import os
import requests
from mcp.server import MCPServer


server = MCPServer(
    name="GitHub Issue Assistant",
    description="An MCP server for working with GitHub issues."
)


GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise RuntimeError("GITHUB_TOKEN environment variable is not set.")


BASE_URL = "https://api.github.com"


def get_headers():
    return {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }


@server.tool()
def get_repo_issues() -> str:
    """Get issues from the MCP GitHub repository."""

    url = f"{BASE_URL}/repos/srishtiprasanna/MCP/issues"

    response = requests.get(
        url,
        headers=get_headers(),
        timeout=5
    )

    if response.status_code != 200:
        return f"GitHub API error: {response.status_code}"

    issues = response.json()

    if not issues:
        return "No issues found."

    result = []

    for issue in issues:
        result.append(
            f"#{issue['number']} - {issue['title']} - {issue['state']}"
        )

    return "\n".join(result)


@server.tool()
def search_issues(query: str) -> str:
    """Search for issues in the MCP GitHub repository."""

    url = f"{BASE_URL}/search/issues"

    params = {
        "q": f"{query} repo:srishtiprasanna/MCP is:issue"
    }

    response = requests.get(
        url,
        headers=get_headers(),
        params=params,
        timeout=5
    )

    if response.status_code != 200:
        return (
            f"GitHub API error: {response.status_code}\n"
            f"Details: {response.text}"
        )

    data = response.json()
    issues = data.get("items", [])

    if not issues:
        return f"No issues found matching: {query}"

    result = []

    for issue in issues:
        result.append(
            f"#{issue['number']} - {issue['title']} - {issue['state']}"
        )

    return "\n".join(result)


@server.tool()
def create_issue(title: str, body: str) -> str:
    """Create a new issue in the MCP GitHub repository."""

    url = f"{BASE_URL}/repos/srishtiprasanna/MCP/issues"

    data = {
        "title": title,
        "body": body
    }

    response = requests.post(
        url,
        headers=get_headers(),
        json=data,
        timeout=5
    )

    if response.status_code != 201:
        return (
            f"GitHub API error: {response.status_code}\n"
            f"Details: {response.text}"
        )

    issue = response.json()

    return (
        f"Issue created successfully.\n"
        f"#{issue['number']} - {issue['title']}\n"
        f"URL: {issue['html_url']}"
    )


@server.tool()
def close_issue(issue_number: int) -> str:
    """Close an issue in the MCP GitHub repository."""

    url = f"{BASE_URL}/repos/srishtiprasanna/MCP/issues/{issue_number}"

    data = {
        "state": "closed"
    }

    response = requests.patch(
        url,
        headers=get_headers(),
        json=data,
        timeout=5
    )

    if response.status_code != 200:
        return (
            f"GitHub API error: {response.status_code}\n"
            f"Details: {response.text}"
        )

    issue = response.json()

    return (
        f"Issue #{issue['number']} closed successfully.\n"
        f"Title: {issue['title']}"
    )
    
if __name__ == "__main__":
    server.run()