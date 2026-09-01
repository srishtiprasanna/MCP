from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Task Manager")

tasks = []
next_id = 1


@mcp.tool()
def add_task(title: str) -> str:
    """Add a new task."""
    global next_id

    task = {
        "id": next_id,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    next_id += 1

    return f"Task {task['id']} added: {title}"


@mcp.tool()
def list_tasks() -> str:
    """List all tasks."""
    if not tasks:
        return "No tasks found."

    result = []

    for task in tasks:
        status = "✓" if task["completed"] else " "
        result.append(
            f"[{status}] {task['id']}: {task['title']}"
        )

    return "\n".join(result)


@mcp.tool()
def complete_task(task_id: int) -> str:
    """Mark a task as completed."""
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return f"Task {task_id} completed."

    return f"Task {task_id} not found."


if __name__ == "__main__":
    mcp.run()