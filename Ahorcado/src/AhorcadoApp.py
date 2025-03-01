import tkinter as tk
from tkinter import messagebox
from JuegoAhorcado import JuegoAhorcado

class AhorcadoApp:
    def __init__(self):
        self.juego = JuegoAhorcado()
        self.ventana = tk.Tk()
        self.ventana.title("Juego del Ahorcado")
        self.ventana.geometry("400x500")

        self.label_palabra = tk.Label(self.ventana, text=self.juego.palabra_mostrada(), font=("Arial", 24))
        self.label_palabra.pack(pady=20)

        self.canvas = tk.Canvas(self.ventana, width=300, height=300)
        self.canvas.pack()

        self.label_intentos = tk.Label(self.ventana, text=f"Intentos restantes: {self.juego.intentos_restantes}", font=("Arial", 16))
        self.label_intentos.pack(pady=10)

        self.entry_letra = tk.Entry(self.ventana, font=("Arial", 16))
        self.entry_letra.pack(pady=10)

        self.boton_adivinar = tk.Button(self.ventana, text="Adivinar", command=self.adivinar_letra, font=("Arial", 16))
        self.boton_adivinar.pack(pady=10)

        self.dibujar_ahorcado()

    def dibujar_ahorcado(self):
        self.canvas.delete("all")
        partes_ahorcado = [
            lambda: self.canvas.create_line(50, 250, 150, 250),  # Base
            lambda: self.canvas.create_line(100, 250, 100, 50),  # Poste
            lambda: self.canvas.create_line(100, 50, 200, 50),   # Travesaño
            lambda: self.canvas.create_line(200, 50, 200, 100),  # Cuerda
            lambda: self.canvas.create_oval(180, 100, 220, 140), # Cabeza
            lambda: self.canvas.create_line(200, 140, 200, 200), # Cuerpo
            lambda: self.canvas.create_line(200, 160, 180, 140), # Brazo izquierdo
            lambda: self.canvas.create_line(200, 160, 220, 140), # Brazo derecho
            lambda: self.canvas.create_line(200, 200, 180, 240), # Pierna izquierda
            lambda: self.canvas.create_line(200, 200, 220, 240)  # Pierna derecha
        ]
        for i in range(6 - self.juego.intentos_restantes):
            if i < len(partes_ahorcado):
                partes_ahorcado[i]()

    def adivinar_letra(self):
        letra = self.entry_letra.get().lower()
        print(f"Letra ingresada: {letra}")  # Depuración

        if len(letra) != 1 or not letra.isalpha():
            messagebox.showwarning("Entrada inválida", "Por favor, ingresa una sola letra.")
            return

        if not self.juego.adivinar_letra(letra):
            messagebox.showwarning("Letra repetida", "Ya has intentado con esa letra.")
            return

        print(f"Palabra mostrada: {self.juego.palabra_mostrada()}")  # Depuración
        print(f"Intentos restantes: {self.juego.intentos_restantes}")  # Depuración

        self.label_palabra.config(text=self.juego.palabra_mostrada())
        self.label_intentos.config(text=f"Intentos restantes: {self.juego.intentos_restantes}")
        self.dibujar_ahorcado()

        if self.juego.ha_ganado():
            messagebox.showinfo("¡Felicidades!", "¡Has adivinado la palabra!")
            self.ventana.quit()
        elif self.juego.ha_perdido():
            messagebox.showinfo("Game Over", f"La palabra era: {self.juego.palabra_secreta}")
            self.ventana.quit()

if __name__ == "__main__":
    app = AhorcadoApp()
    app.ventana.mainloop()