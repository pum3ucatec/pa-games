class Dibujar_ahorcado:
    def __init__(self, canvas):
        self.canvas=canvas
        self.partes=[
            lambda: self.canvas.create_oval(180, 80,220,120,width=3),#cabeza 
            lambda: self.canvas.create_line(200,120,200,180,width=3 ),#cuerpo
            lambda: self.canvas.create_line(200, 140, 170, 170,width=3),# Brazo izq
            lambda: self.canvas.create_line(200, 140, 230, 170,width=3),# Brazo der
            lambda: self.canvas.create_line(200, 180, 170, 220,width=3),# Pierna izq
            lambda: self.canvas.create_line(200, 180, 230, 220,width=3),# Pierna der
        ]

    def dibujar_base(self):
        self.canvas.create_line(50, 250, 200, 250, width=5)  # Base
        self.canvas.create_line(125, 50, 125, 250, width=5)  # Poste
        self.canvas.create_line(125, 50, 200, 50, width=5)  # Soporte
        self.canvas.create_line(200, 50, 200, 80, width=5)  # Cuerda

    def dibujar_parte(self, intentos_restantes):
        if intentos_restantes < len(self.partes):
            self.partes[len(self.partes) - intentos_restantes - 1]()
 
        