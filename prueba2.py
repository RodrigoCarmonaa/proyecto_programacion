from opensimplex import OpenSimplex
import tkinter as tk
from PIL import Image, ImageTk
from random import choice, randint
import random
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
#---------------------------------------------------------------------
#----------------------------------------
# Clase para todos los animales
#----------------------------------------
class Animal(Organismo):

    def __init__(self,nombre,ubicacion,vida_hp, energia, velocidad,Imagen_Animal,especie, Sexo, edad, Alimentacion,Direccion):
        super().__init__(nombre, ubicacion, vida_hp, energia, velocidad)
        self.velocidad = velocidad
        self.especie = especie

        self.sexo = Sexo
        self.edad = edad
        self.Alimentacion = Alimentacion

        self.nivel_hambre = 100
        self.nivel_sed = 100
        self.ciclo_de_vida = 0
        self.estado = "vivo"
        self.Periodo_reproducion = False

        self.Imagen_Animal = Imagen_Animal
        self.Direccion = Direccion
        self.canvas = self.Prueba()

    def Prueba(self,canva=None):
        self.canvas = canva

    def mostrar_imagen(self):
        self.canvas.create_image(self.ubicacion[0],self.ubicacion[1], anchor=tk.NW, image=self.Imagen_Animal, tags=self.nombre)

    def animal_Moviendose(self,tag,posicion,direccion,columnas=40,filas=27,ancho_celda=25):
        self.canvas.delete(tag)

        if direccion == "arriba":
            posicion[1] -= 1
        elif direccion == "abajo":
            posicion[1] += 1
        elif direccion == "izquierda":
            posicion[0] -= 1
        elif direccion == "derecha":
            posicion[0] += 1
        
        posicion[0] = max(0, min(posicion[0], columnas - 1))
        posicion[1] = max(0, min(posicion[1], filas - 1))

        x_posicion = posicion[0] * ancho_celda
        y_posicion = posicion[1] * ancho_celda

        self.Direccion = choice(["arriba", "abajo", "izquierda", "derecha"])

        self.canvas.create_image(x_posicion, y_posicion, anchor=tk.NW, image=self.Imagen_Animal, tags=self.nombre)
        return posicion
        
    def Morir(self,Tipo_de_muerte):
        print(f"El {self.nombre} ha muerto,{Tipo_de_muerte}")
        self.estado = "muerto"
        return 
    
    def reproducirse(self, otros):
            if self.estado != "muerto":
                for otro in otros:
                    if (
                        otro.estado != "muerto"
                        and self.especie == otro.especie
                        and self.__class__ == otro.__class__
                    ):
                        if random() < 0.1:
                            nueva_cria = self.__class__(
                                especie=self.especie,
                                posicion=(self.posicion[0] + random(), self.posicion[1] + random()),
                                vida=1,
                                energia=1,
                                velocidad=1,
                            )
                            return nueva_cria
            return None    
    
    
class Leon(Animal):
    pass
class Jirafa(Animal):
    pass
class Hiena(Animal):
    pass
class Gacela(Animal):
    pass
class Rinoceronte(Animal):
    pass
class Elefante(Animal):
    pass
class Tortuga(Animal):
    pass
class Ciervo(Animal):
    pass
class Antilopes(Animal):
    pass
class Bufalo(Animal):
    pass

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