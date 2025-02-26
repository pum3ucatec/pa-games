import tkinter as tk
from tkinter import messagebox

class Interfaz_ahorcado:
    def __init__(self):
        self.juego = Juego_ahorcado()

        self.ventana = tk.Tk()
        self.ventana.title("Juego del Ahorcado")
        self.ventana.geometry("400x500")

       
        self.label_palabra = tk.Label(self.ventana, text=" ".join(self.juego.palabra_mostrada), font=("Arial", 20))
        self.label_palabra.pack(pady=20)

        
        self.canvas = tk.Canvas(self.ventana, width=300, height=300)
        self.canvas.pack()
        self.dibujo = Dibujar_ahorcado(self.canvas)
        self.dibujo.dibujar_base()

       
        self.frame_botones = tk.Frame(self.ventana)
        self.frame_botones.pack(pady=20)
        self.crear_botones()

    def crear_botones(self):
        for letra in "abcdefghijklmnñopqrstuvwxyz":
            btn = tk.Button(self.frame_botones, text=letra, width=3, command=lambda l=letra: self.verificar_letra(l))
            btn.grid(row=ord(letra) // 10, column=ord(letra) % 10)

    def verificar_letra(self, letra):
        if self.juego.verificar_letra(letra):
            self.label_palabra.config(text=" ".join(self.juego.palabra_mostrada))
            if self.juego.ha_ganado():
                messagebox.showinfo("¡Ganaste!", "¡Has adivinado la palabra!")
                self.ventana.quit()
        else:
            self.dibujo.dibujar_parte(self.juego.intentos)
            if self.juego.ha_perdido():
                messagebox.showinfo("¡Perdiste!", f"La palabra era: {''.join(self.juego.palabra_secreta)}")
                self.ventana.quit()
                
                def ejecutar(self):
                    self.ventana.mainloop()

                
                if __name__ == "__main__":
                    app = Interfaz_ahorcado()
                    app.ejecutar()