from dataclasses import dataclass
from typing import Optional

@dataclass
class Task:
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

    def __post_init__(self):
        if not self.title or not self.title.strip():
            raise ValueError("Task title is required and cannot be empty.")
