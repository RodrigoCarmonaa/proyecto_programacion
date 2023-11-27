# Purpose: Animación de un león en una cuadrícula
import tkinter as tk
from PIL import Image, ImageTk
import random
from random import choice
from visual import leon1



class Ventana(tk.Tk):
    def __init__(self, filas, columnas, ancho_celda, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filas = filas
        self.columnas = columnas
        self.ancho_celda = ancho_celda
        self.animal_imagenes = {
                "leon": Image.open("leon.png"),
                # Puedes agregar más animales aquí
            }
        self.posiciones_animales = {
                "leon": [5, 8],  # Posición inicial del león
                # Agrega aquí más posiciones iniciales para otros animales
            }
        self.crear_cuadricula()
        self.mostrar_animales()
        self.mover_animales()  # Inicia el movimiento de los animales

    def crear_cuadricula(self):
        # Crear la cuadrícula una vez al inicio
            canvas = tk.Canvas(self, width=self.columnas * self.ancho_celda, height=self.filas * self.ancho_celda)
            canvas.pack()

            for i in range(1, self.filas):
                y = i * self.ancho_celda
                canvas.create_line(0, y, self.columnas * self.ancho_celda, y)

            for j in range(1, self.columnas):
                x = j * self.ancho_celda
                canvas.create_line(x, 0, x, self.filas * self.ancho_celda)

            self.canvas = canvas  # Guardar una referencia al canvas para su uso posterior


if __name__ == "__main__":
    ventana = Ventana(filas=17, columnas=30, ancho_celda=40)
    ventana.mainloop()

