from opensimplex import OpenSimplex
import tkinter as tk
from PIL import Image, ImageTk
import random

# Definir el tamaño del mapa
filas = 27
columnas = 40

# Generar el ruido de Simplex para el mapa de biomas
biome_map = OpenSimplex(seed=random.randint(1, 10000))

# Generar el ruido de Simplex para el mapa de biomas
escalador = 20.0  # Escala para ajustar el ruido, afecta la rugosidad del mapa
biome_noise = [[0 for _ in range(columnas)] for _ in range(filas)]

scale = 20.0  # Ajusta esta escala para modificar el ruido
for i in range(filas):
    for j in range(columnas):
        biome_noise[i][j] = biome_map.noise2(i / scale, j / scale)

# Definir los umbrales para los biomas
umbral_agua = -0.5
umbral_pasto = 0.0

# Generar la matriz de biomas
mapa = []
for fila in biome_noise:
    mapa_fila = []
    for valor in fila:
        if valor < umbral_agua:
            mapa_fila.append("agua")
        elif valor < umbral_pasto:
            mapa_fila.append("pasto")
        else:
            mapa_fila.append("tierra")
    mapa.append(mapa_fila)

# Definir las rutas de las imágenes de los biomas
ruta_agua = "agua.png"
ruta_pasto = "pasto.png"
ruta_tierra = "tierra.png"

# Cargar las imágenes con PIL
imagen_agua = Image.open(ruta_agua)
imagen_pasto = Image.open(ruta_pasto)
imagen_tierra = Image.open(ruta_tierra)


class Ventana(tk.Tk):
    def __init__(self, filas, columnas, ancho_celda, imagenes):
        super().__init__()
        self.filas = filas
        self.columnas = columnas
        self.ancho_celda = ancho_celda
        self.imagenes = imagenes
        self.canvas = tk.Canvas(self, width=columnas * ancho_celda, height=filas * ancho_celda)
        self.canvas.pack()
        self.matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

    def actualizar_matriz(self, nueva_matriz):
        self.matriz = nueva_matriz
        self.dibujar_matriz()

    def dibujar_matriz(self):
        self.canvas.delete("all")
        for i in range(self.filas):
            for j in range(self.columnas):
                bioma = self.matriz[i][j]
                x1, y1 = j * self.ancho_celda, i * self.ancho_celda
                x2, y2 = (j + 1) * self.ancho_celda, (i + 1) * self.ancho_celda

                if bioma == "agua":
                    imagen = self.imagenes["agua"]
                elif bioma == "pasto":
                    imagen = self.imagenes["pasto"]
                else:
                    imagen = self.imagenes["tierra"]

                self.canvas.create_image((x1 + x2) / 2, (y1 + y2) / 2, image=imagen)

# Definir el tamaño del mapa
filas = 27
columnas = 40

# Generar el ruido de Simplex para el mapa de biomas
# ...

# Crear el diccionario de imágenes
imagenes = {
    "agua": None,
    "pasto": None,
    "tierra": None
}

# Cargar las imágenes con PIL
ruta_agua = "agua.png"
ruta_pasto = "pasto.png"
ruta_tierra = "tierra.png"

imagen_agua = Image.open(ruta_agua)
imagenes["agua"] = ImageTk.PhotoImage(imagen_agua)

imagen_pasto = Image.open(ruta_pasto)
imagenes["pasto"] = ImageTk.PhotoImage(imagen_pasto)

imagen_tierra = Image.open(ruta_tierra)
imagenes["tierra"] = ImageTk.PhotoImage(imagen_tierra)

# Ejemplo de uso
ventana = Ventana(filas=27, columnas=40, ancho_celda=25, imagenes=imagenes)
ventana.actualizar_matriz(mapa)
ventana.mainloop()