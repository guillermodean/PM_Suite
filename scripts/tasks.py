import json
import os
import sys
from scripts.utils import fancy_print

class Task:
    def __init__(self, task_id, name, time_spent=0, status="open"):
        self.task_id = task_id
        self.name = name
        self.time_spent = time_spent
        self.status = status

def get_main_dir_path():
    # Check if running as one-file executable
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS
    else:
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def load_tasks():
    main_dir_path = get_main_dir_path()
    tasks_file_path = os.path.join(main_dir_path, 'static', 'data', 'tasks.json')
    
    if os.path.exists(tasks_file_path):
        with open(tasks_file_path, 'r') as file:
            tasks_data = json.load(file)
            tasks = [Task(task['id'], task['name'], task['time_spent'], task['status']) for task in tasks_data]
    else:
        tasks = []

    return tasks

def save_tasks(tasks):
    main_dir_path = get_main_dir_path()
    tasks_file_path = os.path.join(main_dir_path, 'static', 'data', 'tasks.json')
    
    # Create necessary directories if they don't exist
    os.makedirs(os.path.dirname(tasks_file_path), exist_ok=True)

    tasks_data = [{"id": task.task_id, "name": task.name, "time_spent": task.time_spent, "status": task.status} for task in tasks]
    with open(tasks_file_path, 'w') as file:
        json.dump(tasks_data, file, indent=2)

def show_tasks(tasks, status):
    fancy_print("")
    filtered_tasks = [task for task in tasks if task.status == status]

    if filtered_tasks:
        print(f"{'Open' if status == 'open' else 'closed'} Tasks:")
        for i, task in enumerate(filtered_tasks, start=1):
            print(f"{i}. [ID: {task.task_id}] {task.name} - Time spent: {task.time_spent} seconds")
    else:
        print(f"No {'open' if status == 'open' else 'completed'} tasks found.")

def add_task(tasks):
    fancy_print("")
    new_task_name = input("Enter the new task name: ")
    new_task_id = len(tasks) + 1  # Generate a new ID
    new_task = Task(new_task_id, new_task_name)
    tasks.append(new_task)
    save_tasks(tasks)
    fancy_print("")
    print(f"Task '{new_task_name}' added successfully.")

def close_task(tasks):
    show_tasks(tasks, status="open")
    if tasks:
        task_number = int(input("Enter the number of the task to close: "))
        if 1 <= task_number <= len(tasks):
            closed_task = tasks[task_number - 1]
            closed_task.status = "closed"
            save_tasks(tasks)
            fancy_print("")
            print(f"Task '{closed_task.name}' closed successfully.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to close.")

def listtask():
    tasks = load_tasks()

    while True:
        print("\nTask Manager Menu:")
        print("1. Show Open Tasks")
        print("2. Show Completed Tasks")
        print("3. Add Task")
        print("4. Close Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            show_tasks(tasks, status="open")
        elif choice == '2':
            show_tasks(tasks, status="closed")
        elif choice == '3':
            add_task(tasks)
        elif choice == '4':
            close_task(tasks)
        elif choice == '5':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    listtask()
