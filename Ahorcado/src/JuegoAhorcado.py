import random

class JuegoAhorcado:
    def __init__(self):
        self.palabras = ["python", "programacion", "ahorcado", "desarrollo", "openai"]
        self.palabra_secreta = random.choice(self.palabras)
        self.letras_adivinadas = []
        self.intentos_restantes = 6

    def adivinar_letra(self, letra):
        if letra in self.letras_adivinadas:
            return False
        self.letras_adivinadas.append(letra)
        if letra not in self.palabra_secreta:
            self.intentos_restantes -= 1
        return True

    def palabra_mostrada(self):
        return " ".join([letra if letra in self.letras_adivinadas else "_" for letra in self.palabra_secreta])

    def ha_ganado(self):
        return "_" not in self.palabra_mostrada()

    def ha_perdido(self):
        return self.intentos_restantes <= 0