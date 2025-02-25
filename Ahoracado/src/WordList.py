import random

class WordList:
    def __init__(self):
        self.words = ["Python", "Elefante", "Programacion", "Ahorcado", "Computadora"]

    def get_random_word(self):
        return random.choice(self.words).lower()
