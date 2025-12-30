import pytest
from todo.entities import Task

def test_task_creation():
    task = Task(id=1, title="Test Task", description="Test Description")
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert not task.completed

def test_task_title_required():
    with pytest.raises(ValueError, match="Task title is required"):
        Task(id=1, title="")

def test_task_title_no_whitespace():
    with pytest.raises(ValueError, match="Task title is required"):
        Task(id=1, title="   ")
