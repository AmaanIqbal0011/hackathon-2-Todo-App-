import pytest
import sys
import os

# Add src to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from todo.manager import TaskManager

@pytest.fixture
def task_manager():
    return TaskManager()
