import json
import os
from scripts.utils import fancy_print

class Task:
    def __init__(self, name, time_spent=0, status="open"):
        self.name = name
        self.time_spent = time_spent
        self.status = status

def load_open_tasks():
    tasks_file_path = './static/data/tasks.json'
    if os.path.exists(tasks_file_path):
        with open(tasks_file_path, 'r') as file:
            tasks_data = json.load(file)
            open_tasks = [Task(task['name'], task['time_spent'], task['status']) for task in tasks_data if task['status'] == 'open']
    else:
        open_tasks = []
    return open_tasks

def load_closed_tasks():
    tasks_file_path = './static/data/tasks.json'
    if os.path.exists(tasks_file_path):
        with open(tasks_file_path, 'r') as file:
            tasks_data = json.load(file)
            closed_tasks = [Task(task['name'], task['time_spent'], task['status']) for task in tasks_data if task['status'] == 'closed']
    else:
        closed_tasks = []
    return closed_tasks

def save_tasks(tasks):
    tasks_file_path = './static/data/tasks.json'
    tasks_data = [{"name": task.name, "time_spent": task.time_spent, "status": task.status} for task in tasks]
    with open(tasks_file_path, 'w') as file:
        json.dump(tasks_data, file, indent=2)

def show_tasks(tasks, status="open"):
    fancy_print("")
    filtered_tasks = [task for task in tasks if task.status == status]
    
    if filtered_tasks:
        print(f"{'Open' if status == 'open' else 'Completed'} Tasks:")
        for i, task in enumerate(filtered_tasks, start=1):
            print(f"{i}. {task.name} - Time spent: {task.time_spent} seconds")
    else:
        print(f"No {'open' if status == 'open' else 'completed'} tasks found.")

def add_task(tasks):
    fancy_print("")
    new_task_name = input("Enter the new task name: ")
    new_task = Task(new_task_name)
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

def show_completed_tasks(tasks):
    show_tasks(tasks, status="closed")

def listtask():
    open_tasks = load_open_tasks()
    closed_tasks = load_closed_tasks()

    while True:
        print("\nTask Manager Menu:")
        print("1. Show Open Tasks")
        print("2. Show Completed Tasks")
        print("3. Add Task")
        print("4. Close Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            show_tasks(open_tasks, status="open")
        elif choice == '2':
            show_completed_tasks(closed_tasks)
        elif choice == '3':
            add_task(open_tasks)
        elif choice == '4':
            close_task(open_tasks)
        elif choice == '5':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    listtask()
