# main.py

from scripts import arrange, mickey, pomodoro, tasks, encrypt, intelligent,excuses, statistics, notes  # Import the statistics module
import sys
from os import path
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
    venv_path = path.dirname(sys.executable)
    pyfiglet_path = path.join(venv_path, 'Lib', 'site-packages', 'pyfiglet')

    # Specify the path to the 'slant' font file
    font_path = path.join(pyfiglet_path, 'fonts', 'slant.flf')  # Adjust if necessary
    sys.path.insert(0, font_path)
    fig = Figlet(font='slant')
    title = fig.renderText('PM SUITE')
    print(title)
    sys.path.remove(font_path)

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
    print("11. Notes")
    print("12. Exit")
    print("--------------------------------------------------------------------------------------------------------")
def get_main_dir_path():
    return getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
def main():
    # Create an instance of the Task class
    sample_task = Task("Sample Task", 30, "closed")

    #print_bear_art()
    print_better_logo()
    # print_pmsuite_title()

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
            secrets_folder_path = path.join(os.path.join(path.expanduser('~')), 'Desktop', 'organization', 'secrets')
            encrypt.encrypt_folder(encryption_key, secrets_folder_path)
        elif choice == '7':
            key_path = input("Enter the path of the encryption key file: ")
            secrets_folder_path = path.join(path.join(path.expanduser('~')), 'Desktop', 'organization', 'secrets')
            encrypt.decrypt_folder(key_path, secrets_folder_path)
        elif choice == '8':
            mainpath = get_main_dir_path()
            intelligent.say_something_intelligent(mainpath)
        elif choice == '9':
            mainpath = get_main_dir_path()
            excuses.need_an_excuse(mainpath)
        elif choice == '10':
           # Calculate and display statistics
            statistics.main()
        elif choice == '11':
            notes.main_notes()
        elif choice == '12':
            print("Exiting.")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 11.")

if __name__ == "__main__":
    main()
