import tkinter as tk
from PIL import Image, ImageTk
from random import choice
import logging
# -*- coding: utf-8 -*-

# Configurar el sistema de registro
logging.basicConfig(filename='prueba.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#####################################################################
#                           organismos 
#####################################################################
class Organismo:
    def __init__(self, nombre, ubicacion, vida, energia, velocidad):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.vida = vida
        self.energia = energia
        self.velocidad = velocidad


#####################################################################
#                           PLANTA
#####################################################################
class Planta(Organismo):
    def __init__(self, nombre, tipo, ubicacion, vida, energia, velocidad, ciclo_vida, tiempo_sin_agua):
        super().__init__(nombre, ubicacion, vida, energia, velocidad)
        self.tipo = tipo
        self.ciclo_vida = ciclo_vida
        self.tiempo_sin_agua = tiempo_sin_agua

    def crecer(self, cantidad_agua):
        factor_crecimiento = cantidad_agua / self.tiempo_sin_agua
        self.vida += factor_crecimiento
        self.energia += factor_crecimiento

    def morir(self):
        self.vida = max(0, self.vida - 1)
        self.energia = max(0, self.energia - 1)

    def ser_consumida(self):
        if self.vida > 0:
            self.vida -= 1
            self.energia -= 1

    def actualizar_estado(self, cantidad_agua):
        self.crecer(cantidad_agua)
        self.morir()

    def reproducirse(self):
        nueva_planta = Planta(f"NuevaPlanta_{choice(1, 100)}", self.tipo, self.ubicacion, vida=1, energia=1, velocidad=1, ciclo_vida=self.ciclo_vida, tiempo_sin_agua=self.tiempo_sin_agua)
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
        self.campo_vision = 2
        self.ciclo_vida = ciclo_vida
        self.tiempo_sin_comida = 0
        self.tiempo_sin_agua = 0

    def moverse(self, objetivo=None):
        if objetivo:
            direccion_x = objetivo.ubicacion[0] - self.ubicacion[0]
            direccion_y = objetivo.ubicacion[1] - self.ubicacion[1]
            distancia = max(abs(direccion_x), abs(direccion_y))

            if distancia > 0:
                direccion_x /= distancia
                direccion_y /= distancia

                if isinstance(objetivo, Planta):
                    velocidad = min(self.velocidad, objetivo.velocidad)
                else:
                    velocidad = min(self.velocidad * 2, objetivo.velocidad)

                nueva_ubicacion = (
                    self.ubicacion[0] + int(direccion_x * velocidad),
                    self.ubicacion[1] + int(direccion_y * velocidad)
                )
                self.ubicacion = nueva_ubicacion
        else:
            super().moverse()

    def buscar_presa(self, presas):
        for presa in presas:
            distancia = abs(self.ubicacion[0] - presa.ubicacion[0]) + abs(self.ubicacion[1] - presa.ubicacion[1])
            if distancia <= self.campo_vision and self.hambre > 0:
                return presa
        return None

    def buscar_charco(self, charcos):
        for charco in charcos:
            distancia = abs(self.ubicacion[0] - charco.ubicacion[0]) + abs(self.ubicacion[1] - charco.ubicacion[1])
            if distancia <= self.campo_vision and self.sed > 0:
                return charco
        return None

    def alimentarse(self, presa):
        if presa:
            self.energia += presa.vida
            self.hambre = max(0, self.hambre - presa.vida)

    def beber(self, charco):
        if charco:
            self.energia += charco.agua
            self.sed = max(0, self.sed - charco.agua)

    def reproducirse(self):
        nuevo_animal = Animal(f"NuevoAnimal_{choice(1, 100)}", self.especie, self.ubicacion, vida=1, energia=1, velocidad=1, hambre=1, sed=1)
        return nuevo_animal


#####################################################################
#                           DEPREDADOR
#####################################################################
class Depredador(Animal):
    def __init__(self, nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida):
        super().__init__(nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida)

    def cazar(self, presas):
        presa = self.buscar_presa(presas)
        self.moverse(presa)
        self.alimentarse(presa)

    def ciclo_vida(self):
        self.vida -= 1
        self.energia -= 1


#####################################################################
#                           PRESA
#####################################################################
class Presa(Animal):
    def __init__(self, nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida):
        super().__init__(nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida)

    def huir(self, depredadores):
        depredador = self.buscar_depredador(depredadores)
        self.moverse(depredador)

    def ciclo_vida(self):
        self.vida -= 1
        self.energia -= 1

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

#####################################################################
#                           SAVANA
#####################################################################
class SavanaAfricana:
    def __init__(self, temperatura, estacion_seca, estacion_lluvia, vegetacion, fauna):
        self.temperatura = temperatura
        self.estacion_seca = estacion_seca
        self.estacion_lluvia = estacion_lluvia
        self.vegetacion = vegetacion
        self.fauna = fauna

    def ciclo_estacional(self):
        pass

    def agregar_planta(self, planta):
        pass

    def agregar_animal(self, animal):
        pass



#####################################################################
#                           ECOSISTEMAS
#####################################################################
class Ecosistema:
    def __init__(self):
        self.organismos = []
        self.ambiente = []

    def ciclo_global(self):
        pass
    
#####################################################################
#                           VENTANA
#####################################################################

class Ventana(tk.Tk):
    def __init__(self, filas, columnas, ancho_celda, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filas = filas
        self.columnas = columnas
        self.ancho_celda = ancho_celda
        
        # Configurar el sistema de registro para la ventana
        logging.basicConfig(filename='movimientos.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')

        # Cargar imágenes de animales
        self.lion_image = Image.open("imagenes/leon.png")
        self.jirafa_image = Image.open("imagenes/jirafa.png")
        self.hiena_image = Image.open("imagenes/hiena.png")
        self.gacela_image = Image.open("imagenes/gacela.png")
        self.rinoceronte_image = Image.open("imagenes/rinoceronte.png")
        self.elefante_image = Image.open("imagenes/elefante.png")
        self.tortuga_image = Image.open("imagenes/tortuga.png")

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

        self.crear_cuadricula()
        self.mostrar_animales()
        self.mover_animales()

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

        # Mover cada animal individualmente y registrar el movimiento
        self.leon_posicion = self.mover_animal_individual("leon", self.leon_posicion, self.direccion_leon)
        self.registrar_movimiento("leon", self.leon_posicion)
        
        self.jirafa_posicion = self.mover_animal_individual("jirafa", self.jirafa_posicion, self.direccion_jirafa)
        self.registrar_movimiento("jirafa", self.jirafa_posicion)
        
        self.hiena_posicion = self.mover_animal_individual("hiena", self.hiena_posicion, self.direccion_hiena)
        self.registrar_movimiento("hiena", self.hiena_posicion)
        
        self.gacela_posicion = self.mover_animal_individual("gacela", self.gacela_posicion, self.direccion_gacela)
        self.registrar_movimiento("gacela", self.gacela_posicion)
        
        self.rinoceronte_posicion = self.mover_animal_individual("rinoceronte", self.rinoceronte_posicion, self.direccion_rinoceronte)
        self.registrar_movimiento("rinoceronte", self.rinoceronte_posicion)
        
        self.elefante_posicion = self.mover_animal_individual("elefante", self.elefante_posicion, self.direccion_elefante)
        self.registrar_movimiento("elefante", self.elefante_posicion)
        
        self.tortuga_posicion = self.mover_animal_individual("tortuga", self.tortuga_posicion, self.direccion_tortuga)
        self.registrar_movimiento("tortuga", self.tortuga_posicion)

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
    
    def registrar_movimiento(self, animal, posicion):
        mensaje = f"{animal} se movió a la posición {posicion}"
        logging.info(mensaje)

if __name__ == "__main__":
    ventana = Ventana(filas=27, columnas=40, ancho_celda=25)
    ventana.mainloop()

