import ctypes
import time
import keyboard


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
    ctypes.windll.user32.SetCursorPos(
        screen_width // 2 + int((screen_width / 2) * (2 * time.time() % 1 - 1)),
        screen_height // 2 + int((screen_height / 2) * (2 * time.time() % 1 - 1))
    )
# Display message and wait for any key press to stop
