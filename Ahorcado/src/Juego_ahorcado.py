import tkinter as tk
from tkinter import messagebox
import random

class Juego_ahorcado:
    def __init__(self):
        self.palabras=["sistemas" ,"ucatec","programacion","santi","javier"]
        self.palabra_secreta= list(random.choice(self.palabras))
        self.palabra_mostrada=["_"]*len(self.palabra_secreta)
        self.intentos=6 
    
    def verificar_letra(self,letra):
        if letra in self.palabra_secreta:
        
            for i, l in enumerate(self.palabra_secreta):
                if l == letra:
                    self.palabra_mostrada[i]=letra
            return True
        
        else:
            self.intentos-=1
            return False
    
    def ganaste(self):
        return "_" not in self.palabra_mostrada
    
    def perdiste(self):
        return self.intentos == 0 