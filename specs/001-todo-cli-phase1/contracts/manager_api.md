# Internal API Contracts: Task Manager

The Task Manager provides an internal functional interface to the CLI.

## Methods

### `add_task(title: str, description: str = "") -> Task`
- **Inputs**: Task details.
- **Outputs**: Created Task object.
- **Errors**: `ValueError` if title is empty.

### `get_all_tasks() -> List[Task]`
- **Outputs**: List of all Task objects.

### `update_task(task_id: int, title: str = None, description: str = None) -> Task`
- **Inputs**: Task ID and new details.
- **Outputs**: Updated Task object.
- **Errors**: `TaskNotFoundError` if ID invalid.

### `delete_task(task_id: int) -> bool`
- **Inputs**: Task ID.
- **Outputs**: True if successful.
- **Errors**: `TaskNotFoundError` if ID invalid.

### `toggle_task_completion(task_id: int) -> Task`
- **Inputs**: Task ID.
- **Outputs**: Updated Task object.
- **Errors**: `TaskNotFoundError` if ID invalid.
