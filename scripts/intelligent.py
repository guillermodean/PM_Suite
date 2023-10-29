from random import choice
from os import path
from time import sleep
from plyer import tts


def say_something_intelligent():
    """
    Reads all the sentences from the static/data/stonks.txt file and chooses
    a random sentence and prints it to the console.
    """
    file_path = path.join(path.dirname(__file__), "..", "static", "data", "stonks.txt")

    with open(path.join(file_path), "r") as f:
        stonks = f.readlines()

    sleep(0.5)
    print("\nHold tight! I'm coming up with something intelligent...")
    sleep(2)

    sentence = choice(stonks)
    print("\n\t" + sentence)
    tts.speak(sentence)
