from random import choice
from os import path
from time import sleep
from plyer import tts


def need_an_excuse():
    """
    Chooses a random sentence from stonks.txt or a project delay excuse
    and prints it to the console.
    """
    file_path = path.join(path.dirname(__file__), "..", "static", "data", "excuses.txt")

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

