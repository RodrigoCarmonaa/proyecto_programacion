import numpy as np
from opensimplex import OpenSimplex
from colorama import Fore, Style
from animales import Organismo, Animal, Planta, Ambiente, Ecosistema


class Mapa:
    def __init__(self, filas, columnas, escala=10.0, complejidad=16, persistencia=0.5, seed=None, suavizado=False):
        self.filas = filas
        self.columnas = columnas
        self.escala = escala
        self.complejidad = complejidad
        self.persistencia = persistencia
        self.seed = seed if seed is not None else np.random.randint(0, 1000)
        self.matriz = self.generar_mapa()
        self.suavizar() if suavizado else None

    def generar_mapa(self):
        noise = OpenSimplex(seed=self.seed)
        matriz = np.zeros((self.filas, self.columnas), dtype=int)

        for i in range(self.filas):
            for j in range(self.columnas):
                valor_ruido = noise.noise2(i / self.escala, j / self.escala)

                if valor_ruido < -0.3:
                    matriz[i, j] = 0  # Agua
                elif valor_ruido < -0.1:
                    matriz[i, j] = 2  # Arena
                elif valor_ruido < 0.6:
                    matriz[i, j] = 1  # Sabana (tono de pasto seco)
                else:
                    matriz[i, j] = 3  # Montañas

        return matriz

    def suavizar(self):
        # Agrega aquí tu lógica de suavizado si es necesaria
        pass  # Ejemplo: Implementa tu algoritmo de suavizado aquí

    def print_map_with_colors(self):
        for row in range(self.filas):
            for col in range(self.columnas):
                valor = self.matriz[row, col]
                if valor == 0:
                    print(Fore.BLUE + "░", end="")  # Agua
                elif valor == 1:
                    print(Fore.YELLOW + "▒", end="")  # Sabana
                elif valor == 2:
                    print(Fore.YELLOW + "▒", end="")  # Arena
                else:
                    print(Fore.WHITE + "█", end="")  # Montañas
            print(Style.RESET_ALL)


if __name__ == "__main__":
    mapa = Mapa(filas=32, columnas=32, escala=10.0, complejidad=16, persistencia=0.5, seed=None, suavizado=False)
    mapa.print_map_with_colors()
