from random import choice
from os import path


def say_something_intelligent():
    """
    Reads all the sentences from the static/data/stonks.txt file and chooses
    a random sentence and prints it to the console.
    """
    file_path = path.join(path.dirname(__file__), '..', 'static', 'data', 'stonks.txt')

    with open(path.join(file_path), 'r') as f:
        stonks = f.readlines()

    print('\n\t'+choice(stonks))