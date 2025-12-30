import os
import pytest
from todo.persistence import Persistence
from todo.entities import Task
from todo.manager import TaskManager

@pytest.fixture
def temp_file(tmp_path):
    return str(tmp_path / "tasks.json")

def test_persistence_save_load(temp_file):
    persistence = Persistence(temp_file)
    tasks = [Task(id=1, title="Test 1"), Task(id=2, title="Test 2", completed=True)]

    persistence.save(tasks)
    assert os.path.exists(temp_file)

    loaded_tasks = persistence.load()
    assert len(loaded_tasks) == 2
    assert loaded_tasks[0].title == "Test 1"
    assert loaded_tasks[1].completed

def test_persistence_manager_integration(temp_file):
    persistence = Persistence(temp_file)
    # Start with some tasks
    initial_tasks = [Task(id=1, title="Existing")]
    persistence.save(initial_tasks)

    # Load into manager
    tasks = persistence.load()
    manager = TaskManager(tasks)

    assert len(manager.get_all_tasks()) == 1
    manager.add_task("New Task")

    # Save back
    persistence.save(manager.get_all_tasks())

    # Verify reload
    reloaded_tasks = persistence.load()
    assert len(reloaded_tasks) == 2
    assert any(t.title == "New Task" for t in reloaded_tasks)
