import psutil
import os
import datetime

def get_system_uptime():
    # Get system uptime in seconds
    uptime_seconds = psutil.boot_time()

    # Convert uptime to a human-readable format
    uptime_str = str(datetime.timedelta(seconds=uptime_seconds))

    return uptime_str

def get_current_user():
    # Get the username of the currently logged-in user
    username = os.getlogin()
    return username

if __name__ == "__main__":
    uptime = get_system_uptime()
    current_user = get_current_user()

    print(f"System Uptime: {uptime}")
    print(f"Current User: {current_user}")
