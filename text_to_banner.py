#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog
import pyfiglet

def on_button_click():
    texto = cuadro_texto.get()
    banner = pyfiglet.figlet_format(texto)
    archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if archivo:
        with open(archivo, "w") as f:
            f.write(banner)

def on_button_click2():
    texto = cuadro_texto.get()
    banner = pyfiglet.figlet_format(texto)
    print(banner)

ventana = tk.Tk()

ventana.title("SpringBoot Banner Creator")

label = tk.Label(ventana, text="Ingresa el texto que deseas convertir a banner:")

cuadro_texto = tk.Entry(ventana, width=30)

boton = tk.Button(ventana, text="Guardar en txt", command=on_button_click)
boton2 = tk.Button(ventana, text="mostrar en consola", command=on_button_click2)

label.pack(pady=10)
cuadro_texto.pack(pady=10)
boton.pack(pady=10)
boton2.pack(pady=10)

ventana.geometry("400x200")

ventana.mainloop()