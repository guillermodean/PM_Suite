# main.py

from scripts import arrange, mickey, pomodoro, tasks, encrypt, intelligent,excuses, statistics  # Import the statistics module
import sys
import os
import time 
from pyfiglet import Figlet

class Task:
    def __init__(self, name, time_spent=0, status="open"):
        self.name = name
        self.time_spent = time_spent
        self.status = status

def print_bear_art():
    bear_art = """
          ____
        o8%8888,    ,o8%888,         
      o88%8888888.  888888%88;       
      8'-    -:8888b 8888   8;      
     <8       88888 8888   8;      
      88b. `-~ 88888 8888   8;      
       88b ~--~ 88888 8888   8;      
        88b.  , 88888 8888   8;      
         -~  '  ~~~~  ~~~~   ~~~~   

    """
    print(bear_art)

def print_better_logo():
    logo = """
           __________                                 
         .'----------`.                              
         | .--------. |                             
         | |########| |       __________              
         | |########| |      /__________\             
.--------| `--------' |------|    --=-- |-------------.
|        `----,-.-----'      |o ======  |             | 
|       ______|_|_______     |__________|             | 
|      /  %%%%%%%%%%%%  \                             | 
|     /  %%%%%%%%%%%%%%  \                            | 
|     ^^^^^^^^^^^^^^^^^^^^                            | 
+-----------------------------------------------------+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
"""
    print(logo)

def print_pmsuite_title():
    fig = Figlet(font='slant')
    title = fig.renderText('PM SUITE')
    print(title)

def menu():
    print("--------------------------------------------------------------------------------------------------------")
    print("1. Organize Desktop")
    print("2. Pomodoro Timer")
    print("3. Move Mouse Randomly")
    print("4. list organization")
    print("5. Tasks")
    print("6. Encrypt 'secrets' Folder")
    print("7. Decrypt 'secrets' Folder")
    print("8. Find something intelligent to say in a meeting")
    print("9. Need an excuse? Project delay?")
    print("10. Show Statistics")  # New option to show statistics
    print("11. Exit")
    print("--------------------------------------------------------------------------------------------------------")

def main():
    # Create an instance of the Task class
    sample_task = Task("Sample Task", 30, "closed")

    #print_bear_art()
    print_better_logo()
    print_pmsuite_title()

    while True:
        menu()
        choice = input("Select an option (1-11): ")

        if choice == '1':
            arrange.organize_desktop()
        elif choice == '2':
            pomodoro.pomodoro_timer()
        elif choice == '3':
            mickey.move_mouse_randomly()
        elif choice == '4':
            arrange.list_organization_folder()
        elif choice == '5':
            tasks.listtask()
        elif choice == '6':
            encryption_key = encrypt.generate_key()
            secrets_folder_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop', 'organization', 'secrets')
            encrypt.encrypt_folder(encryption_key, secrets_folder_path)
        elif choice == '7':
            key_path = input("Enter the path of the encryption key file: ")
            secrets_folder_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop', 'organization', 'secrets')
            encrypt.decrypt_folder(key_path, secrets_folder_path)
        elif choice == '8':
            intelligent.say_something_intelligent()
        elif choice == '9':
            excuses.need_an_excuse()
        elif choice == '10':
           # Calculate and display statistics
            statistics.main()
        elif choice == '11':
            print("Exiting.")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 11.")

if __name__ == "__main__":
    main()
