from mcp.server.fastmcp import FastMCP
from pathlib import Path

mcp = FastMCP("Knowledge Base")

DATA_DIR = Path(__file__).parent / "data"


@mcp.tool()
def search_knowledge(query: str) -> str:
    """Search the company knowledge base for information."""
    
    results = []

    for file in DATA_DIR.glob("*.txt"):
        content = file.read_text(encoding="utf-8")

        if query.lower() in content.lower():
            results.append(
                f"--- {file.name} ---\n{content}"
            )

    if not results:
        return f"No information found for: {query}"

    return "\n\n".join(results)


@mcp.tool()
def get_document(document_name: str) -> str:
    """Get the complete contents of a knowledge base document."""

    file_path = DATA_DIR / document_name

    if not file_path.exists():
        return f"Document not found: {document_name}"

    return file_path.read_text(encoding="utf-8")


if __name__ == "__main__":
    mcp.run()