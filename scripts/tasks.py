import json
import os

def load_tasks():
    # Load tasks from the JSON file
    tasks_file_path = 'tasks.json'
    if os.path.exists(tasks_file_path):
        with open(tasks_file_path, 'r') as file:
            tasks = json.load(file)
    else:
        tasks = []
    return tasks

def save_tasks(tasks):
    # Save tasks to the JSON file
    tasks_file_path = 'tasks.json'
    with open(tasks_file_path, 'w') as file:
        json.dump(tasks, file, indent=2)

def show_tasks(tasks):
    # Display the list of tasks
    if tasks:
        print("Current Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks found.")

def add_task(tasks):
    # Add a new task to the list
    new_task = input("Enter the new task: ")
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{new_task}' added successfully.")

def close_task(tasks):
    # Close a task by removing it from the list
    show_tasks(tasks)
    if tasks:
        task_number = int(input("Enter the number of the task to close: "))
        if 1 <= task_number <= len(tasks):
            closed_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{closed_task}' closed successfully.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to close.")

def listtask():
    tasks = load_tasks()

    while True:
        print("\nTask Manager Menu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Close Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            close_task(tasks)
        elif choice == '4':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    listtask()
