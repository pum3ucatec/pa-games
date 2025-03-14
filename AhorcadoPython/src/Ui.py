import tkinter as tk
from tkinter import messagebox
from Game import Game

class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego del Ahorcado")
        self.root.geometry("400x300")

        self.game = Game(["python", "java", "ruby", "javascript", "linux"])  # Lista de palabras

        # Crear elementos de la interfaz
        self.label_word = tk.Label(root, text=self.game.get_display_word(), font=("Helvetica", 18))
        self.label_word.pack(pady=20)

        self.entry_letter = tk.Entry(root, font=("Helvetica", 14))
        self.entry_letter.pack(pady=10)

        self.button_guess = tk.Button(root, text="Adivinar", font=("Helvetica", 14), command=self.on_guess_clicked)
        self.button_guess.pack(pady=10)

        self.label_attempts = tk.Label(root, text=f"Intentos restantes: {self.game.attempts_left}", font=("Helvetica", 12))
        self.label_attempts.pack(pady=10)

    def on_guess_clicked(self):
        letter = self.entry_letter.get()
        self.entry_letter.delete(0, tk.END)
        
        if len(letter) != 1 or not letter.isalpha():
            messagebox.showwarning("Advertencia", "Por favor, ingresa una sola letra.")
            return

        if not self.game.guess(letter):
            messagebox.showwarning("Advertencia", "Ya has adivinado esa letra.")

        self.label_word.config(text=self.game.get_display_word())
        self.label_attempts.config(text=f"Intentos restantes: {self.game.attempts_left}")

        if self.game.is_won():
            messagebox.showinfo("¡Ganaste!", "¡Felicidades, has ganado!")
            self.reset_game()
        elif self.game.is_lost():
            messagebox.showinfo("Perdiste", f"Has perdido. La palabra era: {self.game.word}")
            self.reset_game()

    def reset_game(self):
        self.game = Game(["python", "java", "ruby", "javascript", "linux"])
        self.label_word.config(text=self.game.get_display_word())
        self.label_attempts.config(text=f"Intentos restantes: {self.game.attempts_left}")
