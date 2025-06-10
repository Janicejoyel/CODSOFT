# TodoList Application
# Initialize empty task list
todo_list = []

def display_tasks():
    if not todo_list:
        print("Todo List is empty.\n")
    else:
        print("\nYour Todo List:")
        for idx, task in enumerate(todo_list, 1):
            status = "Done" if task['completed'] else "Pending"
            print(f"{idx}. {task['task']} [{status}]")
        print()

def add_task():
    task = input("Enter the new task: ")
    todo_list.append({"task": task, "completed": False})
    print("Task added successfully!\n")

def mark_completed():
    display_tasks()
    if todo_list:
        try:
            task_num = int(input("Enter the task number to mark as completed: "))
            if 1 <= task_num <= len(todo_list):
                todo_list[task_num - 1]['completed'] = True
                print("Task marked as completed!\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")

def remove_task():
    display_tasks()
    if todo_list:
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(todo_list):
                removed = todo_list.pop(task_num - 1)
                print(f"Removed task: {removed['task']}\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")

# Main Program Loop
while True:
    print("Todo List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("Exiting Todo List Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.\n")
