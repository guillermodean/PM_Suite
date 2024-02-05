from random import choice
from os import path
import sys
import os
from time import sleep
from plyer import tts

def get_main_dir_path():
    return getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))

def need_an_excuse(mainpath):
    """
    Chooses a random sentence from stonks.txt or a project delay excuse
    and prints it to the console.
    """
    main_dir_path = mainpath
    file_path = path.join(main_dir_path, "static", "data", "excuses.txt")

    with open(file_path, "r") as f:
        project_delays = f.readlines()

    sleep(0.5)
    print("\nHold tight! I'm coming up with a great excuse...")
    sleep(2)

    # Choose between stonks sentence and project delay excuse
    sentence = choice(project_delays)
    print("\n\t" + sentence)

    try:
        tts.speak(sentence)
    except Exception as e:
        pass

