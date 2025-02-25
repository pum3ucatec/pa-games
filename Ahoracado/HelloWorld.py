import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Saludo")
ventana.geometry("300x200")  # Tamaño de la ventana

# Crear una etiqueta (label)
etiqueta = tk.Label(ventana, text="Introduce tu nombre:")
etiqueta.pack()

# Crear un campo de texto (Entry)
campo_nombre = tk.Entry(ventana)
campo_nombre.pack()

# Función para saludar
def saludar():
    nombre = campo_nombre.get()  # Obtener el texto ingresado en el campo
    saludo = f"¡Hola, {nombre}!"
    mensaje.config(text=saludo)  # Mostrar el saludo en la etiqueta

# Crear un botón
boton_saludar = tk.Button(ventana, text="Saludar", command=saludar)
boton_saludar.pack()

# Crear una etiqueta vacía donde aparecerá el saludo
mensaje = tk.Label(ventana, text="")
mensaje.pack()

# Iniciar la interfaz gráfica
ventana.mainloop()
