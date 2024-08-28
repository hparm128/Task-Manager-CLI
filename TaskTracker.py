import json


class TaskTracker:
    def __init__(self, filename):
        """Initialize the TaskTracker with a JSON file."""
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from the JSON file.

        Returns:
            list: A list of tasks loaded from the file, or an empty list if the file is not found.
        """
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # Return an empty list if the file does not exist
            return []

    def save_tasks(self):
        """Save the current list of tasks to the JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, new_task):
        """Add a new task to the task list.

        Args:
            new_task (str): The name of the task to add.

        If the task already exists, a message is printed and the task is not added.
        """
        if any(task["Task"] == new_task for task in self.tasks):
            print("Task already exists.")
        else:
            self.tasks.append({"Task": new_task, "Status": "Not started"})
            self.save_tasks()

    def delete_task(self, task_to_delete):
        """Delete a task from the task list.

        Args:
            task_to_delete (str): The name of the task to delete.

        If the task is not found, a message is printed. Otherwise, the task is removed and the list is saved.
        """
        old_length = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.get("Task") != task_to_delete]
        new_length = len(self.tasks)
        if old_length == new_length:
            print("Task not found.")
        else:
            self.save_tasks()

    def update_task(self, task_to_update, new_task):
        """Update the name of an existing task.

        Args:
            task_to_update (str): The current name of the task.
            new_task (str): The new name for the task.

        If the task is found, its name is updated and the list is saved. Otherwise, a message is printed.
        """
        found = False
        for task in self.tasks:
            if task.get("Task") == task_to_update:
                task["Task"] = new_task
                found = True
                break
        if found:
            self.save_tasks()
        else:
            print("Task not found.")

    def update_status(self, task_to_update, status):
        """Update the status of an existing task.

        Args:
            task_to_update (str): The name of the task to update.
            status (str): The new status for the task.

        If the task is found, its status is updated and the list is saved. Otherwise, a message is printed.
        """
        found = False
        for task in self.tasks:
            if task.get("Task") == task_to_update:
                task["Status"] = status
                found = True
                break
        if found:
            self.save_tasks()
        else:
            print("Task not found.")

    def list_all_tasks(self):
        """Print all tasks and their statuses."""
        if not self.tasks:
            print("No tasks currently.")
        else:
            count = 1
            for task in self.tasks:
                print(f"{count}. {task['Task']} - {task['Status']}")
                count += 1

    def list_completed_tasks(self):
        """Print all tasks that are marked as 'Completed'."""
        completed_tasks = [task for task in self.tasks if task["Status"] == "Completed"]
        if not completed_tasks:
            print("No completed tasks currently.")
        else:
            count = 1
            for task in completed_tasks:
                print(f"{count}. {task['Task']}")
                count += 1

    def list_in_progress_tasks(self):
        """Print all tasks that are marked as 'In progress'."""
        in_progress_tasks = [task for task in self.tasks if task["Status"] == "In progress"]
        if not in_progress_tasks:
            print("No tasks in progress currently.")
        else:
            count = 1
            for task in in_progress_tasks:
                print(f"{count}. {task['Task']}")
                count += 1
