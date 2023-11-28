import tkinter as tk
import random

class Organismo:
    def __init__(self, nombre, ubicacion, vida, energia, velocidad):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.vida = vida
        self.energia = energia
        self.velocidad = velocidad

class Planta(Organismo):
    def __init__(self, nombre, tipo, ubicacion, vida, energia, velocidad, ciclo_vida, tiempo_sin_agua):
        super().__init__(nombre, ubicacion, vida, energia, velocidad)
        self.tipo = tipo
        self.ciclo_vida = ciclo_vida  # Duración del ciclo de vida en iteraciones
        self.tiempo_sin_agua = tiempo_sin_agua  # Número de iteraciones sin agua antes de secarse

    def crecer(self, cantidad_agua):
        # La planta crece en función de la cantidad de agua que recibe
        factor_crecimiento = cantidad_agua / self.tiempo_sin_agua
        self.vida += factor_crecimiento
        self.energia += factor_crecimiento

    def morir(self):
        # La planta muere cuando su ciclo de vida llega a cero o si no recibe agua durante un tiempo
        self.vida = max(0, self.vida - 1)
        self.energia = max(0, self.energia - 1)

    def ser_consumida(self):
        # La planta es consumida por un animal, disminuyendo su vida y energía
        if self.vida > 0:
            self.vida -= 1
            self.energia -= 1

    def actualizar_estado(self, cantidad_agua):
        # Actualiza el estado de la planta en cada iteración
        self.crecer(cantidad_agua)
        self.morir()

    def reproducirse(self):
        # Lógica de reproducción de la planta
        nueva_planta = Planta(f"NuevaPlanta_{random.randint(1, 100)}", self.tipo, self.ubicacion, vida=1, energia=1, velocidad=1, ciclo_vida=self.ciclo_vida, tiempo_sin_agua=self.tiempo_sin_agua)
        return nueva_planta


#####################################################################
#                           ANIMAL
#####################################################################
class Animal(Organismo):
    def __init__(self, nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida):
        super().__init__(nombre, ubicacion, vida, energia, velocidad)
        self.especie = especie
        self.hambre = hambre
        self.sed = sed
        self.campo_vision = 2  # Campo de visión alrededor del animal
        self.ciclo_vida = ciclo_vida  # Número de iteraciones antes de morir sin comida o agua
        self.tiempo_sin_comida = 0
        self.tiempo_sin_agua = 0

    def moverse(self, objetivo=None):
        if objetivo:
            # Calcula la dirección hacia el objetivo y mueve el animal en esa dirección
            direccion_x = objetivo.ubicacion[0] - self.ubicacion[0]
            direccion_y = objetivo.ubicacion[1] - self.ubicacion[1]
            distancia = max(abs(direccion_x), abs(direccion_y))

            if distancia > 0:
                direccion_x /= distancia
                direccion_y /= distancia

                # Ajusta la velocidad del depredador al encontrar a la presa
                if isinstance(objetivo, Planta):
                    velocidad = min(self.velocidad, objetivo.velocidad)
                else:
                    velocidad = min(self.velocidad * 2, objetivo.velocidad)

                # Mueve el animal en la dirección ajustada por su velocidad
                nueva_ubicacion = (
                    self.ubicacion[0] + int(direccion_x * velocidad),
                    self.ubicacion[1] + int(direccion_y * velocidad)
                )
                self.ubicacion = nueva_ubicacion
        else:
            # Se mueve a una nueva ubicación dentro de su campo de visión
            super().moverse()

    def buscar_presa(self, presas):
        # Busca presas dentro de su campo de visión
        for presa in presas:
            distancia = abs(self.ubicacion[0] - presa.ubicacion[0]) + abs(self.ubicacion[1] - presa.ubicacion[1])
            if distancia <= self.campo_vision and self.hambre > 0:
                return presa
        return None

    def buscar_charco(self, charcos):
        # Busca charcos de agua dentro de su campo de visión
        for charco in charcos:
            distancia = abs(self.ubicacion[0] - charco.ubicacion[0]) + abs(self.ubicacion[1] - charco.ubicacion[1])
            if distancia <= self.campo_vision and self.sed > 0:
                return charco
        return None

    def alimentarse(self, presa):
        # Se alimenta de la presa
        if presa:
            self.energia += presa.vida
            self.hambre = max(0, self.hambre - presa.vida)

    def beber(self, charco):
        # Bebe agua del charco
        if charco:
            self.energia += charco.agua
            self.sed = max(0, self.sed - charco.agua)

    def reproducirse(self):
        # Lógica de reproducción
        nuevo_animal = Animal(f"NuevoAnimal_{random.randint(1, 100)}", self.especie, self.ubicacion, vida=1, energia=1, velocidad=1, hambre=1, sed=1)
        return nuevo_animal

class Depredador(Animal):
    def __init__(self, nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida):
        super().__init__(nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida)

    def cazar(self, presas):
        # Lógica de caza: El depredador busca presas y las persigue
        presa = self.buscar_presa(presas)
        self.moverse(presa)
        self.alimentarse(presa)

    def ciclo_vida(self):
        # Añade lógica para el ciclo de vida de los depredadores, por ejemplo, decrementa su vida y energía con el tiempo
        self.vida -= 1
        self.energia -= 1

    # Puedes agregar más funciones específicas para los depredadores


class Presa(Animal):
    def __init__(self, nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida):
        super().__init__(nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida)

    def huir(self, depredadores):
        # Lógica de huida: La presa busca depredadores y trata de huir
        depredador = self.buscar_depredador(depredadores)
        self.moverse(depredador)

    def ciclo_vida(self):
        # Añade lógica para el ciclo de vida de las presas, por ejemplo, decrementa su vida y energía con el tiempo
        self.vida -= 1
        self.energia -= 1

    # Puedes agregar más funciones específicas para las presas

#####################################################################
#                           AMBIENTE
#####################################################################
class Ambiente:
    def __init__(self):
        self.eventos_aleatorios = []

    def agregar_evento_aleatorio(self, evento):
        self.eventos_aleatorios.append(evento)

    def ejecutar_eventos_aleatorios(self):
        for evento in self.eventos_aleatorios:
            evento()


class SavanaAfricana:
    def __init__(self, temperatura, estacion_seca, estacion_lluvia, vegetacion, fauna):
        self.temperatura = temperatura
        self.estacion_seca = estacion_seca
        self.estacion_lluvia = estacion_lluvia
        self.vegetacion = vegetacion
        self.fauna = fauna

    def ciclo_estacional(self):
        return

    def agregar_planta(self, planta):
        return

    def agregar_animal(self, animal):
        return

class Ecosistema:
    def __init__(self):
        self.organismos = []
        self.ambiente = []

    def ciclo_global(self):
        # Implementa la lógica para simular el ciclo de vida global aquí
        return

class Ventana(tk.Tk):
    def __init__(self, filas, columnas, ancho_celda, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filas = filas
        self.columnas = columnas
        self.ancho_celda = ancho_celda
        self.crear_cuadricula()

        self.ecosistema = Ecosistema()
        self.inicializar_ecosistema()

        # Configurar el motor de eventos
        self.configure_event_motor()

    def inicializar_ecosistema(self):
        # Aquí puedes crear instancias de Planta, Animal, SavanaAfricana, etc.
        # y agregarlos al ecosistema
        planta = Planta("Planta1", "TipoPlanta", (1, 1), 1, 1, 1, 1, 1)
        animal = Animal("Animal1", "TipoAnimal", (2, 2), 1, 1, 1, 1, 1, 1)
        self.ecosistema.organismos.extend([planta, animal])
    def crear_cuadricula(self):
        canvas = tk.Canvas(self, width=self.columnas * self.ancho_celda, height=self.filas * self.ancho_celda)
        canvas.pack()

        for i in range(1, self.filas):
            y = i * self.ancho_celda
            canvas.create_line(0, y, self.columnas * self.ancho_celda, y)

        for j in range(1, self.filas):
            x = j * self.ancho_celda
            canvas.create_line(x, 0, x, self.filas * self.ancho_celda)

    def configure_event_motor(self):
        # Configuración de eventos aleatorios
        self.ecosistema.ambiente.agregar_evento_aleatorio(self.generar_evento_aleatorio)

        # Configuración de eventos cíclicos
        self.after(1000, self.ejecutar_eventos_ciclicos) 

    def ejecutar_eventos_ciclicos(self):
        # Lógica para eventos cíclicos
        print("Ejecutando evento cíclico")

        # Programar el próximo evento cíclico
        self.after(5000, self.ejecutar_eventos_ciclicos)

    def generar_evento_aleatorio(self):
        # Lógica para eventos aleatorios
        print("Generando evento aleatorio")

if __name__ == "__main__":
    ventana = Ventana(filas=15, columnas=15, ancho_celda=40)
    ventana.mainloop()
