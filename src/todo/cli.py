import sys
from .manager import TaskManager

class CLIInterface:
    def __init__(self, manager: TaskManager):
        self.manager = manager

    def display_menu(self):
        print("="*25)
        print("-- TODO CLI --")
        print("="*25)
        print("\n")
        print("1. VIEW TASKS")
        print("2. ADD TASK")
        print("3. UPDATE TASK")
        print("4. DELETE TASK")
        print("5. MARK as COMPLETE")
        print("6. EXIT")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nSelect an option (1-6): ")

            try:
                if choice == "1":
                    self.view_tasks()
                elif choice == "2":
                    self.add_task()
                elif choice == "3":
                    self.update_task()
                elif choice == "4":
                    self.delete_task()
                elif choice == "5":
                    self.toggle_task()
                elif choice == "6":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"Error: {e}")

    def view_tasks(self):
        tasks = self.manager.get_all_tasks()
        if not tasks:
            print("\nNo tasks found.")
            return

        print("\nID | Status | Title")
        print("-" * 30)
        for task in tasks:
            status = "[X]" if task.completed else "[ ]"
            print(f"{task.id:2} | {status:6} | {task.title}")

    def add_task(self):
        title = input("Enter task title (required): ")
        description = input("Enter task description (optional): ")
        try:
            task = self.manager.add_task(title, description if description else None)
            print(f"Task '{task.title}' added with ID {task.id}.")
        except ValueError as e:
            print(f"Error: {e}")

    def update_task(self):
        try:
            task_id = int(input("Enter task ID to update: "))
            title = input("Enter new title (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")

            success = self.manager.update_task(
                task_id,
                title=title if title.strip() else None,
                description=description if description.strip() else None
            )
            if success:
                print(f"Task {task_id} updated successfully.")
            else:
                print(f"Task with ID {task_id} not found.")
        except ValueError:
            print("Invalid input. Please enter a numeric ID.")

    def delete_task(self):
        try:
            task_id = int(input("Enter task ID to delete: "))
            if self.manager.delete_task(task_id):
                print(f"Task {task_id} deleted successfully.")
            else:
                print(f"Task with ID {task_id} not found.")
        except ValueError:
            print("Invalid input. Please enter a numeric ID.")

    def toggle_task(self):
        try:
            task_id = int(input("Enter task ID to toggle completion: "))
            if self.manager.toggle_task_completion(task_id):
                task = self.manager.get_task_by_id(task_id)
                status = "completed" if task.completed else "incomplete"
                print(f"Task {task_id} is now {status}.")
            else:
                print(f"Task with ID {task_id} not found.")
        except ValueError:
            print("Invalid input. Please enter a numeric ID.")
