from mcp.server import MCPServer
from database import init_db, get_connection


server = MCPServer(
    name="Smart Task Assistant",
    description="An MCP server for managing and analyzing tasks."
)

init_db()


@server.tool()
def create_task(title: str) -> str:
    """Create a new task."""
    connection = get_connection()

    cursor = connection.execute(
        "INSERT INTO tasks (title) VALUES (?)",
        (title,)
    )

    connection.commit()
    task_id = cursor.lastrowid
    connection.close()

    return f"Task {task_id} created: {title}"


@server.tool()
def list_tasks() -> str:
    """List all tasks."""
    connection = get_connection()

    rows = connection.execute(
        "SELECT id, title, completed FROM tasks ORDER BY id"
    ).fetchall()

    connection.close()

    if not rows:
        return "No tasks found."

    tasks = []

    for task_id, title, completed in rows:
        status = "Completed" if completed else "Pending"
        tasks.append(f"{task_id}. {title} - {status}")

    return "\n".join(tasks)


@server.tool()
def search_tasks(query: str) -> str:
    """Search for tasks by title."""
    connection = get_connection()

    rows = connection.execute(
        "SELECT id, title, completed FROM tasks WHERE title LIKE ? ORDER BY id",
        (f"%{query}%",)
    ).fetchall()

    connection.close()

    if not rows:
        return f"No tasks found matching: {query}"

    tasks = []

    for task_id, title, completed in rows:
        status = "Completed" if completed else "Pending"
        tasks.append(f"{task_id}. {title} - {status}")

    return "\n".join(tasks)


@server.tool()
def get_task_stats() -> str:
    """Get statistics about the tasks."""
    connection = get_connection()

    total = connection.execute(
        "SELECT COUNT(*) FROM tasks"
    ).fetchone()[0]

    completed = connection.execute(
        "SELECT COUNT(*) FROM tasks WHERE completed = 1"
    ).fetchone()[0]

    connection.close()

    pending = total - completed

    return (
        f"Total tasks: {total}\n"
        f"Completed: {completed}\n"
        f"Pending: {pending}"
    )


@server.tool()
def get_next_task() -> str:
    """Get the next pending task."""
    connection = get_connection()

    row = connection.execute(
        """
        SELECT id, title
        FROM tasks
        WHERE completed = 0
        ORDER BY id
        LIMIT 1
        """
    ).fetchone()

    connection.close()

    if not row:
        return "No pending tasks."

    task_id, title = row

    return f"Next task: {task_id}. {title}"


@server.tool()
def complete_task(task_id: int) -> str:
    """Mark a task as completed."""
    connection = get_connection()

    cursor = connection.execute(
        "UPDATE tasks SET completed = 1 WHERE id = ?",
        (task_id,)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        return f"Task {task_id} not found."

    connection.close()

    return f"Task {task_id} marked as completed."

if __name__ == "__main__":
    server.run()
    