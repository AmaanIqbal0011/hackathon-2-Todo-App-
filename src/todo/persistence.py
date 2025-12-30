import json
import os
from typing import List, Dict
from .entities import Task

class Persistence:
    def __init__(self, file_path: str = "tasks.json"):
        self.file_path = file_path

    def save(self, tasks: List[Task]):
        data = [
            {
                "id": t.id,
                "title": t.title,
                "description": t.description,
                "completed": t.completed
            }
            for t in tasks
        ]
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def load(self) -> List[Task]:
        if not os.path.exists(self.file_path):
            return []

        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data: List[Dict] = json.load(f)
                return [
                    Task(
                        id=d["id"],
                        title=d["title"],
                        description=d.get("description"),
                        completed=d.get("completed", False)
                    )
                    for d in data
                ]
        except (json.JSONDecodeError, KeyError, IOError):
            # Graceful error handling for missing/corrupt files - FR-006 & SC-003
            return []
