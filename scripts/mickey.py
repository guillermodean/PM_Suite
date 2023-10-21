import time
import keyboard
# import pyautogui
import random

def move_mouse_randomly():
    print("Mouse movement started. Press 's' to stop.")
    # while True:
    #     # Move the mouse to a random position on the screen
    #     screen_width, screen_height = pyautogui.size()
    #     target_x = random.randint(0, screen_width)
    #     target_y = random.randint(0, screen_height)
    #     pyautogui.moveTo(target_x, target_y, duration=1)

    #     # Wait for 20 seconds
    #     for _ in range(20):
    #         time.sleep(1)
    #         # Check for 's' key (stop)
    #         if keyboard.is_pressed('s'):
    #             print("Mouse movement stopped.")
    #             return

if __name__ == "__main__":
    move_mouse_randomly()
