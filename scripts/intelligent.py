from random import choice
from os import path
import sys
from time import sleep
from plyer import tts


def get_main_dir_path():
    return getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))

def say_something_intelligent(mainpath):
    """
    Reads all the sentences from the static/data/stonks.txt file and chooses
    a random sentence and prints it to the console.
    """
    main_dir_path = mainpath
    file_path = path.join(main_dir_path, "static", "data", "stonks.txt")

    with open(file_path, "r") as f:
        stonks = f.readlines()

    sleep(0.5)
    print("\nHold tight! I'm coming up with something intelligent...")
    sleep(2)

    sentence = choice(stonks)
    print("\n\t" + sentence)

    try:
        tts.speak(sentence)
    except Exception as e:
        pass
