from mcp.server import MCPServer
from database import init_db, get_connection


server = MCPServer(
    name="Task Database",
    description="An MCP server for managing tasks stored in SQLite."
)

# Create the database/table when the server starts
init_db()


@server.tool()
def create_task(title: str) -> str:
    """Create a new task in the database."""

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
    """List all tasks in the database."""

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
def update_task(task_id: int, title: str, completed: bool) -> str:
    """Update the title and completion status of a task."""

    connection = get_connection()

    cursor = connection.execute(
        """
        UPDATE tasks
        SET title = ?, completed = ?
        WHERE id = ?
        """,
        (title, completed, task_id)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        return f"Task {task_id} not found."

    connection.close()

    return f"Task {task_id} updated successfully."


@server.tool()
def delete_task(task_id: int) -> str:
    """Delete a task from the database."""

    connection = get_connection()

    cursor = connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        return f"Task {task_id} not found."

    connection.close()

    return f"Task {task_id} deleted successfully."
@server.resource("tasks://all")
def get_all_tasks() -> str:
    """Return all tasks from the database."""

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

if __name__ == "__main__":
    server.run()