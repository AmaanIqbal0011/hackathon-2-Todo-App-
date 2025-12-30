import pytest

def test_add_task(task_manager):
    task = task_manager.add_task("Buy milk", "At the corner store")
    assert task.id == 1
    assert task.title == "Buy milk"
    assert len(task_manager.get_all_tasks()) == 1

def test_get_task_by_id(task_manager):
    task_manager.add_task("Task 1")
    task = task_manager.get_task_by_id(1)
    assert task is not None
    assert task.title == "Task 1"

def test_update_task(task_manager):
    task_manager.add_task("Old Title")
    success = task_manager.update_task(1, title="New Title")
    assert success
    assert task_manager.get_all_tasks()[0].title == "New Title"

def test_delete_task(task_manager):
    task_manager.add_task("To Delete")
    success = task_manager.delete_task(1)
    assert success
    assert len(task_manager.get_all_tasks()) == 0

def test_toggle_completion(task_manager):
    task_manager.add_task("Toggle Me")
    task_manager.toggle_task_completion(1)
    assert task_manager.get_all_tasks()[0].completed
    task_manager.toggle_task_completion(1)
    assert not task_manager.get_all_tasks()[0].completed
