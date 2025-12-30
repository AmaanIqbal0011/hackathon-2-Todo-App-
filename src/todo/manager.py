from typing import List, Optional
from .entities import Task

class TaskManager:
    def __init__(self, tasks: Optional[List[Task]] = None):
        self._tasks: List[Task] = tasks if tasks is not None else []
        self._next_id: int = 1
        if self._tasks:
            self._next_id = max(t.id for t in self._tasks) + 1

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        task = Task(id=self._next_id, title=title, description=description)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        return self._tasks

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        return next((t for t in self._tasks if t.id == task_id), None)

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        if title is not None:
            if not title.strip():
                raise ValueError("Title cannot be empty")
            task.title = title
        if description is not None:
            task.description = description
        return True

    def delete_task(self, task_id: int) -> bool:
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        self._tasks.remove(task)
        return True

    def toggle_task_completion(self, task_id: int) -> bool:
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        task.completed = not task.completed
        return True
