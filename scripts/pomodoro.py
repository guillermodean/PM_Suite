import time
import keyboard
from plyer import notification
from tqdm import tqdm
from scripts import tasks

def select_task(listTask):
    while True:
        tasks.show_tasks(listTask)

        try:
            selected_index = int(input("Select a task by entering the number (0 to cancel): "))
            if 0 <= selected_index <= len(listTask):
                return listTask[selected_index - 1] if selected_index > 0 else None
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def pomodoro_timer():
    listTask = tasks.load_tasks()
    new_task=input("Do you want to start pomodoro for a new task? Y/N")
    if new_task == "Y" or new_task == "y":
        tasks.add_task(listTask)
    selected_task = select_task(listTask)
    if selected_task is None:
        print( "do you want to create a new task")
        return  # User canceled task selection
    print(selected_task)
    task_name = selected_task
    task_duration = int(input("Enter the duration of the Pomodoro in minutes: "))

    duration_seconds = task_duration * 60
 # Setup tqdm progress bar
    with tqdm(total=duration_seconds, desc='Time Remaining', unit='s') as progress_bar:
        # Countdown loop
        while duration_seconds > 0:
            # Check for 'p' key (pause) or 'r' key (resume)
            if keyboard.is_pressed('p'):
                print("Timer paused. Press 'r' to resume.")
                while not keyboard.is_pressed('r'):
                    time.sleep(0.1)
                print("Timer resumed.")
            else:
                time.sleep(1)
                duration_seconds -= 1
                progress_bar.update(1)

    selected_task['time_spent'] += task_duration * 60
    tasks.save_tasks(listTask)

    # Notification when time is up
    notification_title = "Pomodoro Completed"
    notification_message = f"Task: {task_name}\nTime: {task_duration} minutes is up!"
    notification.notify(
        title=notification_title,
        message=notification_message,
        app_name='Pomodoro Timer'
    )
    erase_task= input("Do you want to mark the task as completed: Y/N")
    if erase_task == "Y" or erase_task == "y":
        tasks.close_task(listTask)
    print("Pomodoro completed!")

if __name__ == "__main__":
    pomodoro_timer()
