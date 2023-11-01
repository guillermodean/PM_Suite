from random import choice
from os import path
from time import sleep
from plyer import tts


def get_project_delay_excuse():
    """
    Returns a random project delay excuse.
    """
    file_path = path.join(path.dirname(__file__), "..", "static", "data", "excuses.txt")

    with open(file_path, "r") as f:
        project_delays = f.readlines()

    return choice(project_delays)


def need_an_excuse():
    """
    Chooses a random sentence from stonks.txt or a project delay excuse
    and prints it to the console.
    """
    stonks_file_path = path.join(path.dirname(__file__), "..", "static", "data", "excuses.txt")
    with open(stonks_file_path, "r") as f:
        stonks = f.readlines()

    sleep(0.5)
    print("\nHold tight! I'm coming up with a great excuse...")
    sleep(2)

    # Choose between stonks sentence and project delay excuse
    if choice([True, False]):  # 50% chance of choosing a project delay excuse
        sentence = get_project_delay_excuse()
    else:
        sentence = choice(stonks)

    print("\n\t" + sentence)

    try:
        tts.speak(sentence)
    except Exception as e:
        pass

if __name__ == "__main__":
    need_an_excuse()
