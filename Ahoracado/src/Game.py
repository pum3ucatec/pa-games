class Game:
    def __init__(self, word):
        self.word = word.lower()
        self.guessed_letters = set()
        self.max_attempts = 6
        self.attempts = 0

    def guess(self, letter):
        letter = letter.lower()
        if letter in self.guessed_letters:
            return False  # Letra ya intentada

        self.guessed_letters.add(letter)

        if letter not in self.word:
            self.attempts += 1
        
        return True

    def get_display_word(self):
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])

    def is_won(self):
        return all(letter in self.guessed_letters for letter in self.word)

    def is_lost(self):
        return self.attempts >= self.max_attempts
