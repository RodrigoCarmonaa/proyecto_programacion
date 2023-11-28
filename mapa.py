from opensimplex import OpenSimplex
import tkinter as tk
from PIL import Image, ImageTk
import random
from random import choice


# Definir el tamaño del mapa
filas = 27
columnas = 40

# Generar el ruido de Simplex para el mapa de biomas
biome_map = OpenSimplex(seed=random.randint(1, 10000))

# Generar el ruido de Simplex para el mapa de biomas
biome_noise = [[0 for _ in range(columnas)] for _ in range(filas)]

scale = 20.0  # Ajusta esta escala para modificar el ruido
for i in range(filas):
    for j in range(columnas):
        biome_noise[i][j] = biome_map.noise2(i / scale, j / scale)

# Asignar biomas basados en el ruido de Simplex generado
mapa_numerico = []
for fila in biome_noise:
    mapa_fila = []
    for valor in fila:
        if valor < -0.5:
            mapa_fila.append(0)  # Azul
        elif valor < 0.0:
            mapa_fila.append(1)  # Verde
        else:
            mapa_fila.append(2)  # Café
    mapa_numerico.append(mapa_fila)



class Ventana(tk.Tk):
    def __init__(self, filas, columnas, ancho_celda, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filas = filas
        self.columnas = columnas
        self.ancho_celda = ancho_celda
        self.mapa_numerico = mapa_numerico

        # Cargar imágenes de animales
        self.lion_image = Image.open("leon.png")
        self.jirafa_image = Image.open("jirafa.png")
        self.hiena_image = Image.open("hiena.png")
        self.gacela_image = Image.open("gacela.png")
        self.rinoceronte_image = Image.open("rinoceronte.png")
        self.elefante_image = Image.open("elefante.png")
        self.tortuga_image = Image.open("tortuga.png")

        # Posiciones iniciales de los animales
        self.hiena_posicion = [4, 2]
        self.jirafa_posicion = [3, 5]
        self.leon_posicion = [5, 8]
        self.gacela_posicion = [1, 1]
        self.rinoceronte_posicion = [8, 15]
        self.elefante_posicion = [12, 20]
        self.tortuga_posicion = [15, 25]

        # Direcciones iniciales de los animales
        self.direccion_leon = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_jirafa = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_hiena = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_gacela = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_rinoceronte = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_elefante = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_tortuga = choice(["arriba", "abajo", "izquierda", "derecha"])

        self.agua_image = Image.open("agua.png")
        self.tierra_image = Image.open("tierra.png")
        self.pasto_image = Image.open("pasto.png")

        # Escalar las imágenes de fondo al tamaño de la celda
        self.agua_image = self.agua_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.tierra_image = self.tierra_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.pasto_image = self.pasto_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)

        # Convertir las imágenes de fondo a formato Tkinter
        self.agua_image = ImageTk.PhotoImage(self.agua_image)
        self.tierra_image = ImageTk.PhotoImage(self.tierra_image)
        self.pasto_image = ImageTk.PhotoImage(self.pasto_image)


            
        self.crear_cuadricula()
        self.crear_fondo()
        self.mostrar_animales()
        self.mover_animales()
        
    def crear_fondo(self):
            for fila in range(self.filas):
                for columna in range(self.columnas):
                    imagen_fondo = None
                    if self.mapa_numerico[fila][columna] == 0:
                        imagen_fondo = self.agua_image
                    elif self.mapa_numerico[fila][columna] == 1:
                        imagen_fondo = self.pasto_image
                    elif self.mapa_numerico[fila][columna] == 2:
                        imagen_fondo = self.tierra_image

                    if imagen_fondo:
                        x_posicion = columna * self.ancho_celda
                        y_posicion = fila * self.ancho_celda
                        self.canvas.create_image(x_posicion, y_posicion, anchor=tk.NW, image=imagen_fondo, tags="fondo") 

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

    def mostrar_animales(self):
        # Eliminar cualquier instancia previa de los animales
        self.canvas.delete("leon", "jirafa", "hiena", "gacela", "rinoceronte", "elefante", "tortuga")

        # Redimensionar imágenes de animales
        self.lion_image = self.lion_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.jirafa_image = self.jirafa_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.hiena_image = self.hiena_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.gacela_image = self.gacela_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.rinoceronte_image = self.rinoceronte_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.elefante_image = self.elefante_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.tortuga_image = self.tortuga_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)

        # Convertir imágenes a formato Tkinter
        self.lion_image = ImageTk.PhotoImage(self.lion_image)
        self.jirafa_image = ImageTk.PhotoImage(self.jirafa_image)
        self.hiena_image = ImageTk.PhotoImage(self.hiena_image)
        self.gacela_image = ImageTk.PhotoImage(self.gacela_image)
        self.rinoceronte_image = ImageTk.PhotoImage(self.rinoceronte_image)
        self.elefante_image = ImageTk.PhotoImage(self.elefante_image)
        self.tortuga_image = ImageTk.PhotoImage(self.tortuga_image)

        # Posiciones de los animales
        posiciones = {
            "leon": self.leon_posicion,
            "jirafa": self.jirafa_posicion,
            "hiena": self.hiena_posicion,
            "gacela": self.gacela_posicion,
            "rinoceronte": self.rinoceronte_posicion,
            "elefante": self.elefante_posicion,
            "tortuga": self.tortuga_posicion,
        }

        # Imágenes de los animales
        imagenes = {
            "leon": self.lion_image,
            "jirafa": self.jirafa_image,
            "hiena": self.hiena_image,
            "gacela": self.gacela_image,
            "rinoceronte": self.rinoceronte_image,
            "elefante": self.elefante_image,
            "tortuga": self.tortuga_image,
        }

        # Mostrar cada animal en el lienzo
        for tag, image in imagenes.items():
            x_posicion = posiciones[tag][0] * self.ancho_celda
            y_posicion = posiciones[tag][1] * self.ancho_celda
            self.canvas.create_image(x_posicion, y_posicion, anchor=tk.NW, image=image, tags=tag)

    def mover_animales(self):
        # Eliminar instancias previas de los animales
        self.canvas.delete("leon", "jirafa", "hiena", "gacela", "rinoceronte", "elefante", "tortuga")

        # Mover cada animal individualmente
        self.leon_posicion = self.mover_animal_individual("leon", self.leon_posicion, self.direccion_leon)
        self.jirafa_posicion = self.mover_animal_individual("jirafa", self.jirafa_posicion, self.direccion_jirafa)
        self.hiena_posicion = self.mover_animal_individual("hiena", self.hiena_posicion, self.direccion_hiena)
        self.gacela_posicion = self.mover_animal_individual("gacela", self.gacela_posicion, self.direccion_gacela)
        self.rinoceronte_posicion = self.mover_animal_individual("rinoceronte", self.rinoceronte_posicion, self.direccion_rinoceronte)
        self.elefante_posicion = self.mover_animal_individual("elefante", self.elefante_posicion, self.direccion_elefante)
        self.tortuga_posicion = self.mover_animal_individual("tortuga", self.tortuga_posicion, self.direccion_tortuga)

        # Establecer un retardo y llamar a la función nuevamente
        self.after(300, self.mover_animales)

    def mover_animal_individual(self, tag, posicion, direccion):
        # Eliminar la instancia previa del animal
        self.canvas.delete(tag)

        # Realizar el movimiento según la dirección
        if direccion == "arriba":
            posicion[1] -= 1
        elif direccion == "abajo":
            posicion[1] += 1
        elif direccion == "izquierda":
            posicion[0] -= 1
        elif direccion == "derecha":
            posicion[0] += 1

        # Limitar la posición del animal dentro de los límites de la cuadrícula
        posicion[0] = max(0, min(posicion[0], self.columnas - 1))
        posicion[1] = max(0, min(posicion[1], self.filas - 1))

        # Actualizar la posición de la imagen del animal en el lienzo
        x_posicion = posicion[0] * self.ancho_celda
        y_posicion = posicion[1] * self.ancho_celda

        # Establecer nueva dirección aleatoria para el próximo movimiento
        if tag == "leon":
            image = self.lion_image
            self.direccion_leon = choice(["arriba", "abajo", "izquierda", "derecha"])
        elif tag == "jirafa":
            image = self.jirafa_image
            self.direccion_jirafa = choice(["arriba", "abajo", "izquierda", "derecha"])
        elif tag == "hiena":
            image = self.hiena_image
            self.direccion_hiena = choice(["arriba", "abajo", "izquierda", "derecha"])
        elif tag == "gacela":
            image = self.gacela_image
            self.direccion_gacela = choice(["arriba", "abajo", "izquierda", "derecha"])
        elif tag == "rinoceronte":
            image = self.rinoceronte_image
            self.direccion_rinoceronte = choice(["arriba", "abajo", "izquierda", "derecha"])
        elif tag == "elefante":
            image = self.elefante_image
            self.direccion_elefante = choice(["arriba", "abajo", "izquierda", "derecha"])
        elif tag == "tortuga":
            image = self.tortuga_image
            self.direccion_tortuga = choice(["arriba", "abajo", "izquierda", "derecha"])

        self.canvas.create_image(x_posicion, y_posicion, anchor=tk.NW, image=image, tags=tag)
        return posicion
    
    

if __name__ == "__main__":
    ventana = Ventana(filas=27, columnas=40, ancho_celda=25)
    ventana.mainloop()

