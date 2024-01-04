import ctypes
import time
import keyboard
import random


# Function to move the mouse to a random position
def move_mouse_randomly():
    print("Moving the mouse, press CTRL+C key to stop it.")
    try:
        print("Mickey moves...")
        while not keyboard.is_pressed(hotkey="esc"):
            move_mouse()
            time.sleep(30) 
            
            # Adjust the sleep time as needed

    except KeyboardInterrupt:
        print("\nScript stopped by user.")



def move_mouse():
    # Get the screen dimensions
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)

    # Set the new mouse position to a random point on the screen
    new_x = random.randint(0, screen_width)
    new_y = random.randint(0, screen_height)

    ctypes.windll.user32.SetCursorPos(new_x, new_y)

# Display message and wait for any key press to stop
