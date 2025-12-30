from .manager import TaskManager
from .persistence import Persistence
from .cli import CLIInterface

def main():
    persistence = Persistence("tasks.json")
    initial_tasks = persistence.load()
    manager = TaskManager(initial_tasks)
    cli = CLIInterface(manager)

    try:
        cli.run()
    finally:
        # Final save on exit
        persistence.save(manager.get_all_tasks())

if __name__ == "__main__":
    main()
