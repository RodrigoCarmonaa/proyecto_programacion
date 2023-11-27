
import tkinter as tk
from PIL import Image, ImageTk
import random
from random import choice




class Ventana(tk.Tk):
    def __init__(self, filas, columnas, ancho_celda, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filas = filas
        self.columnas = columnas
        self.ancho_celda = ancho_celda
        self.lion_image = Image.open("leon.png")
        self.jirafa_image = Image.open("jirafa.png")
        self.jirafa_posicion = [3, 5]
        self.leon_posicion = [5, 8]  # Posición inicial del león
        self.crear_cuadricula()
        self.mostrar_leon()
        self.mostrar_jirafa()  # Agregada la llamada a mostrar_jirafa
        self.mover_leon()  # Inicia el movimiento del león

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



    def mostrar_leon(self):
        # Eliminar cualquier instancia previa del león
        self.canvas.delete("leon")

        lion_image = Image.open("leon.png")
        lion_image = lion_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        lion_image = ImageTk.PhotoImage(lion_image)

        x_posicion = self.leon_posicion[0] * self.ancho_celda
        y_posicion = self.leon_posicion[1] * self.ancho_celda

        self.canvas.create_image(x_posicion, y_posicion, anchor=tk.NW, image=lion_image, tags="leon")
        self.lion_image = lion_image

    def mover_leon(self):
        direccion = choice(["arriba", "abajo", "izquierda", "derecha"])  # Obtiene una dirección aleatoria
        
        self.canvas.delete("leon")

        # movimiento
        if direccion == "arriba":
            self.leon_posicion[1] -= 1  # Mueve el león hacia arriba
        elif direccion == "abajo":
            self.leon_posicion[1] += 1  # Mueve el león hacia abajo
        elif direccion == "izquierda":
            self.leon_posicion[0] -= 1  # Mueve el león hacia la izquierda
        elif direccion == "derecha":
            self.leon_posicion[0] += 1  # Mueve el león hacia la derecha

        # Limita la posición del león dentro de los límites de la cuadrícula
        self.leon_posicion[0] = max(0, min(self.leon_posicion[0], self.columnas - 1))
        self.leon_posicion[1] = max(0, min(self.leon_posicion[1], self.filas - 1))

        # Actualiza la posición de la imagen del león en el lienzo
        x_posicion = self.leon_posicion[0] * self.ancho_celda
        y_posicion = self.leon_posicion[1] * self.ancho_celda
        self.canvas.create_image(x_posicion, y_posicion, anchor=tk.NW, image=self.lion_image, tags="leon")

        self.after(100, self.mover_leon)
    def mostrar_jirafa(self):
        self.canvas.delete("jirafa")

        jirafa_image = Image.open("jirafa.png")
        jirafa_image = jirafa_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        jirafa_image = ImageTk.PhotoImage(jirafa_image)

        x_posicion = self.jirafa_posicion[0] * self.ancho_celda
        y_posicion = self.jirafa_posicion[1] * self.ancho_celda

        self.canvas.create_image(x_posicion, y_posicion, anchor=tk.NW, image=jirafa_image, tags="jirafa")
        self.jirafa_image = jirafa_image

if __name__ == "__main__":
    ventana = Ventana(filas=17, columnas=30, ancho_celda=40)
    ventana.mainloop()

