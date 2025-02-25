import tkinter as tk
from tkinter import messagebox
from src.Game import Game
from src.WordList import WordList

class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ahorcado")
        
        self.word_list = WordList()
        self.new_game()

        self.label_word = tk.Label(root, text=self.game.get_display_word(), font=("Arial", 24))
        self.label_word.pack(pady=10)

        self.entry_letter = tk.Entry(root, font=("Arial", 16))
        self.entry_letter.pack(pady=5)

        self.button_guess = tk.Button(root, text="Adivinar", command=self.make_guess)
        self.button_guess.pack(pady=5)

        self.label_attempts = tk.Label(root, text=f"Intentos: {self.game.attempts} / {self.game.max_attempts}", font=("Arial", 14))
        self.label_attempts.pack(pady=10)

        self.button_reset = tk.Button(root, text="Nuevo Juego", command=self.new_game)
        self.button_reset.pack(pady=5)

    def new_game(self):
        self.game = Game(self.word_list.get_random_word())

        if hasattr(self, "label_word"):
            self.label_word.config(text=self.game.get_display_word())
            self.label_attempts.config(text=f"Intentos: {self.game.attempts} / {self.game.max_attempts}")

    def make_guess(self):
        letter = self.entry_letter.get()
        if not letter or len(letter) != 1:
            messagebox.showwarning("Advertencia", "Ingresa una sola letra")
            return

        if self.game.guess(letter):
            self.label_word.config(text=self.game.get_display_word())
            self.label_attempts.config(text=f"Intentos: {self.game.attempts} / {self.game.max_attempts}")

        if self.game.is_won():
            messagebox.showinfo("Felicidades", "¡Has ganado!")
            self.new_game()
        elif self.game.is_lost():
            messagebox.showinfo("Fin del juego", f"Perdiste. La palabra era: {self.game.word}")
            self.new_game()

        self.entry_letter.delete(0, tk.END)
