import random

class Game:
    def __init__(self, word_list):
        self.word_list = word_list
        self.word = random.choice(self.word_list).lower()
        self.guesses = []
        self.attempts_left = 6
    
    def guess(self, letter):
        letter = letter.lower()
        if letter in self.guesses:
            return False  # Ya has adivinado esta letra
        self.guesses.append(letter)
        
        if letter not in self.word:
            self.attempts_left -= 1
        
        return True
    
    def get_display_word(self):
        return ''.join([letter if letter in self.guesses else '_' for letter in self.word])
    
    def is_won(self):
        return all(letter in self.guesses for letter in self.word)
    
    def is_lost(self):
        return self.attempts_left <= 0
