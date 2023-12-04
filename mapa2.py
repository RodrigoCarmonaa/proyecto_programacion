from opensimplex import OpenSimplex
import random

# Definir el tamaño del mapa
filas = 27
columnas = 40

# Generar el ruido de Simplex para el mapa de biomas
biome_map = OpenSimplex(seed=random.randint(1, 10000))

# Generar el ruido de Simplex para el mapa de biomas
escalador = 20.0  # Escala para ajustar el ruido, afecta la rugosidad del mapa
biome_noise = [[0 for _ in range(columnas)] for _ in range(filas)]

scale = 20.0  # Adjust this scale to modify the noise
for i in range(filas):
    for j in range(columnas):
        biome_noise[i][j] = biome_map.noise2(i / scale, j / scale)  # Change this line

# Assign biomes based on the simplex noise generated
mapa = []
for fila in biome_noise:
    mapa_fila = []
    for valor in fila:
        if valor < -0.5:
            mapa_fila.append(0)  # Azul
        elif valor < 0.0:
            mapa_fila.append(1)  # Verde
        else:
            mapa_fila.append(2)  # Café
    mapa.append(mapa_fila)

# Imprimir la matriz con números en colores
for fila in mapa:
    print(' '.join(str(x) for x in fila))
