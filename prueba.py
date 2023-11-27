import tkinter as tk
from PIL import Image, ImageTk
from random import choice

class Ventana(tk.Tk):
    def __init__(self, filas, columnas, ancho_celda, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filas = filas
        self.columnas = columnas
        self.ancho_celda = ancho_celda
        self.lion_image = Image.open("leon.png")
        self.jirafa_image = Image.open("jirafa.png")
        self.hiena_image = Image.open("hiena.png")
        self.hiena_posicion = [4, 2]
        self.jirafa_posicion = [3, 5]
        self.leon_posicion = [5, 8]
        self.direccion_leon = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_jirafa = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_hiena = choice(["arriba", "abajo", "izquierda", "derecha"])

        self.crear_cuadricula()
        self.mostrar_animal()
        self.mover_animal()  # Inicia el movimiento del león

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

    def mostrar_animal(self):
        # Eliminar cualquier instancia previa del león
        self.canvas.delete("leon", "jirafa", "hiena")

        lion_image = self.lion_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        jirafa_image = self.jirafa_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        hienas_image = self.hiena_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)

        lion_image = ImageTk.PhotoImage(lion_image)
        jirafa_image = ImageTk.PhotoImage(jirafa_image)
        hienas_image = ImageTk.PhotoImage(hienas_image)

        x_posicion1 = self.leon_posicion[0] * self.ancho_celda
        y_posicion2 = self.leon_posicion[1] * self.ancho_celda
        x_posicion3 = self.jirafa_posicion[0] * self.ancho_celda
        y_posicion4 = self.jirafa_posicion[1] * self.ancho_celda
        x_posicion5 = self.hiena_posicion[0] * self.ancho_celda
        y_posicion6 = self.hiena_posicion[1] * self.ancho_celda

        self.canvas.create_image(x_posicion1, y_posicion2, anchor=tk.NW, image=lion_image, tags="leon")
        self.canvas.create_image(x_posicion3, y_posicion4, anchor=tk.NW, image=jirafa_image, tags="jirafa")
        self.canvas.create_image(x_posicion5, y_posicion6, anchor=tk.NW, image=hienas_image, tags="hiena")
        self.lion_image = lion_image
        self.jirafa_image = jirafa_image
        self.hiena_image = hienas_image

    def mover_animal(self):
        self.canvas.delete("leon")
        self.canvas.delete("jirafa")
        self.canvas.delete("hiena")

        # movimiento del león
        self.leon_posicion = self.mover_animal_individual("leon", self.leon_posicion, self.direccion_leon)

        # movimiento de la jirafa
        self.jirafa_posicion = self.mover_animal_individual("jirafa", self.jirafa_posicion, self.direccion_jirafa)

        # movimiento de la hiena
        self.hiena_posicion = self.mover_animal_individual("hiena", self.hiena_posicion, self.direccion_hiena)

        self.after(300, self.mover_animal)

    def mover_animal_individual(self, tag, posicion, direccion):
        # Elimina la instancia previa del animal
        self.canvas.delete(tag)

        # Realiza el movimiento según la dirección
        if direccion == "arriba":
            posicion[1] -= 1
        elif direccion == "abajo":
            posicion[1] += 1
        elif direccion == "izquierda":
            posicion[0] -= 1
        elif direccion == "derecha":
            posicion[0] += 1

        # Limita la posición del animal dentro de los límites de la cuadrícula
        posicion[0] = max(0, min(posicion[0], self.columnas - 1))
        posicion[1] = max(0, min(posicion[1], self.filas - 1))

        # Actualiza la posición de la imagen del animal en el lienzo
        x_posicion = posicion[0] * self.ancho_celda
        y_posicion = posicion[1] * self.ancho_celda

        if tag == "leon":
            image = self.lion_image
            self.direccion_leon = choice(["arriba", "abajo", "izquierda", "derecha"])
        elif tag == "jirafa":
            image = self.jirafa_image
            self.direccion_jirafa = choice(["arriba", "abajo", "izquierda", "derecha"])
        elif tag == "hiena":
            image = self.hiena_image
            self.direccion_hiena = choice(["arriba", "abajo", "izquierda", "derecha"])

        self.canvas.create_image(x_posicion, y_posicion, anchor=tk.NW, image=image, tags=tag)
        return posicion

if __name__ == "__main__":
    ventana = Ventana(filas=17, columnas=30, ancho_celda=40)
    ventana.mainloop()
