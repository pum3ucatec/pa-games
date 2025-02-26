import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from Interfaz_ahorcado import Interfaz_ahorcado

if __name__ == "__main__":
    app = Interfaz_ahorcado()
    app.ventana.mainloop()
