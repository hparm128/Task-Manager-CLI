from TaskTracker import TaskTracker  # Import the TaskTracker class

# Display menu options for the user
menu = (
    "Hello and welcome to the task manager!\n"
    "Type 'a' to add a task\n"
    "Type 'd' to delete a task\n"
    "Type 'u' to update a task\n"
    "Type 's' to change the status of a task\n"
    "Type 'l' to list all tasks\n"
    "Type 'c' to list all completed tasks\n"
    "Type 'p' to list all tasks in progress\n"
    "Type 'm' to see the menu again\n"
    "Type 'q' to quit\n"
)

# Initialize TaskTracker with a JSON file to store tasks
tasks = TaskTracker('tasks.json')

# Print the menu when the program starts
print(menu)

# Start a loop to continually prompt the user for input
while True:
    # Get the user's menu selection
    selection = input("Please make a selection (m to see menu): ").lower()

    # Handle each possible user input
    if selection == "a":
        # Add a new task
        task = input("What is the task? ")
        tasks.add_task(task)
    elif selection == "d":
        # Delete an existing task
        task = input("What is the task to delete? ")
        tasks.delete_task(task)
    elif selection == "u":
        # Update an existing task's name
        task = input("What is the task to update? ")
        new_task = input("What is the new task name? ")
        tasks.update_task(task, new_task)
    elif selection == "s":
        # Update the status of an existing task
        task = input("What is the task to change the status of? ")
        status = input("What is the new status? ")
        tasks.update_status(task, status)
    elif selection == "l":
        # List all tasks
        tasks.list_all_tasks()
    elif selection == "c":
        # List all completed tasks
        tasks.list_completed_tasks()
    elif selection == "p":
        # List all tasks that are in progress
        tasks.list_in_progress_tasks()
    elif selection == "m":
        # Reprint the menu options
        print(menu)
    elif selection == "q":
        # Quit the program
        print("Goodbye!")
        break
    else:
        # Handle invalid input
        print("Invalid input. Please try again.")
