import time
import keyboard
from plyer import notification
from tqdm import tqdm

def pomodoro_timer():
    # Get user input for task duration and name
    task_duration = int(input("Enter the duration of the Pomodoro in minutes: "))
    task_name = input("Enter the name of the task: ")

    # Convert duration to seconds
    duration_seconds = task_duration * 60

    print(f"Pomodoro started for {task_name}. Duration: {task_duration} minutes. Press 'P' to pause it")

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

    # Notification when time is up
    notification_title = "Pomodoro Completed"
    notification_message = f"Task: {task_name}\nTime: {task_duration} minutes is up!"
    notification.notify(
        title=notification_title,
        message=notification_message,
        app_name='Pomodoro Timer'
    )
    print("Pomodoro completed!")

if __name__ == "__main__":
    pomodoro_timer()
