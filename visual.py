import PIL
import tkinter as tk
from PIL import Image, ImageTk
import random
from random import choice


class organismo:
    def __init__(self, posicion, vida, energia, velocidad):
        self.posicion = posicion
        self.vida = vida
        self.energia = energia
        self.velocidad = velocidad
        
class Planta(organismo):
    def __init__(self, posicion, tipo, vida, energia, velocidad, ciclo_vida, tiempo_sin_agua):
        super().__init__(posicion, vida, energia, velocidad)
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
class Animal(organismo):
    def __init__(self, posicion, especie, vida, energia, velocidad, hambre, sed, ciclo_vida):
        super().__init__(posicion, vida, energia, velocidad)
        self.especie = especie
        self.hambre = hambre
        self.sed = sed
        self.campo_vision = 2  # Campo de visión alrededor del animal
        self.ciclo_vida = ciclo_vida  # Número de iteraciones antes de morir sin comida o agua
        self.tiempo_sin_comida = 0
        self.tiempo_sin_agua = 0

    def moverse_aleatoriamente(self):
        direccion = choice(["arriba", "abajo", "izquierda", "derecha"])

        if direccion == "arriba":
            self.posicion[1] -= 1
        elif direccion == "abajo":
            self.posicion[1] += 1
        elif direccion == "izquierda":
            self.posicion[0] -= 1
        elif direccion == "derecha":
            self.posicion[0] += 1

        # Limitar la posición dentro de los límites de la cuadrícula o el entorno
        self.posicion[0] = max(0, min(self.posicion[0], self.columnas - 1))
        self.posicion[1] = max(0, min(self.posicion[1], self.filas - 1))

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
    def __init__(self, posicion, vida, energia, velocidad, hambre, sed, ciclo_vida):
        super().__init__(posicion, vida, energia, velocidad, hambre, sed, ciclo_vida)

    def cazar(self, presas):
        # Lógica de caza: El depredador busca presas y las persigue
        presa = self.buscar_presa(presas)
        self.moverse(presa)
        self.alimentarse(presa)

    def ciclo_vida(self):
        # Añade lógica para el ciclo de vida de los depredadores, por ejemplo, decrementa su vida y energía con el tiempo
        self.vida -= 1
        self.energia -= 1


class Presa(Animal):
    def __init__(self, posicion, vida, energia, velocidad , hambre, sed, ciclo_vida):
        super().__init__(posicion, vida, energia, velocidad, hambre, sed, ciclo_vida)

    def huir(self, depredadores):
        # Lógica de huida: La presa busca depredadores y trata de huir
        depredador = self.buscar_depredador(depredadores)
        self.moverse(depredador)

    def ciclo_vida(self):
        # Añade lógica para el ciclo de vida de las presas, por ejemplo, decrementa su vida y energía con el tiempo
        self.vida -= 1
        self.energia -= 1


########################################################################################################

class Leon(Depredador):
    def __init__(self, posicion, vida, energia, velocidad, nombre, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad)
        self.nombre = nombre
        self.especie = especie
        self.dieta = dieta
        self.velocidad = 20
        self.vida = 100


    def cazar(self, presa):
        # La función de caza específica para el león, disminuye la vida y aumenta la energía
        if isinstance(presa, Presa):
            self.energia += presa.vida
            presa.vida = max(0, presa.vida - 30)  # Asumiendo que la presa pierde 30 de vida al ser cazada
            self.vida = min(100, self.vida + 10)  # El león gana 10 de vida al cazar

    def dormir(self):
        self.energia += 50

        
class jirafa(organismo):
    def __init__(self, posicion, vida, energia, velocidad, nombre, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad)
        self.nombre = nombre
        self.especie = especie
        self.dieta = dieta
        self.velocidad = 18
        self.vida = 100

    def huir(self):
        self.energia -= 20
        self.velocidad += 10

    def comer(self):
        self.energia += 30

    def dormir(self):
        self.energia += 50
            
class hiena(organismo):
    def __init__(self, posicion, vida, energia, velocidad, nombre, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad)
        self.nombre = nombre
        self.especie = especie
        self.dieta = dieta
        self.velocidad = 20
        self.vida = 100

    def cazar(self):
        self.energia -= 20
        self.velocidad += 8

    def comer(self):
        self.energia += 30

    def dormir(self):
        self.energia += 50        

class rinoceronte(organismo):
    def __init__(self, posicion, vida, energia, velocidad, nombre, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad)
        self.nombre = nombre
        self.especie = especie
        self.dieta = dieta
        self.velocidad = 15
        self.vida = 150

    def comer(self):
        self.energia += 30

    def dormir(self):
        self.energia += 50        

class mamba_negra(organismo):
    def __init__(self, posicion, vida, energia, velocidad, nombre, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad)
        self.nombre = nombre
        self.especie = especie
        self.dieta = dieta
        self.velocidad = 10
        self.vida = 100

    def cazar(self):
        self.energia -= 20
        self.velocidad += 2

    def comer(self):
        self.energia += 30

    def dormir(self):
        self.energia += 50

class tortuga(organismo):
    def __init__(self, posicion, vida, energia, velocidad, nombre, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad)
        self.nombre = nombre
        self.especie = especie
        self.dieta = dieta
        self.velocidad = 5
        self.vida = 100

    def comer(self):
        self.energia += 30

    def dormir(self):
        self.energia += 50
        
class elefante(organismo):
    def __init__(self, posicion, vida, energia, velocidad, nombre, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad)
        self.nombre = nombre
        self.especie = especie
        self.dieta = dieta
        self.velocidad = 10
        self.vida = 180

    def comer(self):
        self.energia += 30

    def dormir(self):
        self.energia += 50        

    def beber(self):
        self.energia += 50
    
    def nadar(self):
        self.energia -= 20
        self.velocidad += 10
    
    def defender(self):
        self.energia -= 20            
    
class peces(organismo):
    def __init__(self, posicion, vida, energia, velocidad, nombre, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad)
        self.nombre = nombre
        self.especie = especie
        self.dieta = dieta
        self.velocidad = 15
        self.vida = 5

    def comer(self):
        self.energia += 30

    def nadar(self):
        self.energia -= 20
        self.velocidad += 10
        
class arbol(organismo):
    def __init__(self, posicion, vida, energia, velocidad, nombre, especie, dieta, altura):
        super().__init__(posicion, vida, energia, velocidad)
        self.nombre = nombre
        self.especie = especie
        self.dieta = dieta
        self.altura = altura
        self.velocidad = 0
        self.vida = 100

    def crecer(self):
        self.altura += 1

    def reproducir(self):
        return self

    def fotosintesis(self):
        self.energia += 50  
        
class arbusto(organismo):
    def __init__(self, posicion, vida, energia, velocidad, nombre, especie, dieta, altura):
        super().__init__(posicion, vida, energia, velocidad)
        self.nombre = nombre
        self.especie = especie
        self.dieta = dieta
        self.altura = altura
        self.velocidad = 0
        self.vida = 100

    def crecer(self):
        self.altura += 1

    def reproducir(self):
        return self

    def fotosintesis(self):
        self.energia += 50
        
class pasto(organismo):
    def __init__(self, posicion, vida, energia, velocidad, nombre, especie, dieta, altura):
        super().__init__(posicion, vida, energia, velocidad)
        self.nombre = nombre
        self.especie = especie
        self.dieta = dieta
        self.altura = altura
        self.velocidad = 0
        self.vida = 100

    def crecer(self):
        self.altura += 1

    def reproducir(self):
        return self

    def fotosintesis(self):
        self.energia += 50
        
class flores(organismo):
    def __init__(self, posicion, vida, energia, velocidad, nombre, especie, dieta, altura):
        super().__init__(posicion, vida, energia, velocidad)
        self.nombre = nombre
        self.especie = especie
        self.dieta = dieta
        self.altura = altura
        self.velocidad = 0
        self.vida = 100

    def crecer(self):
        self.altura += 1

    def reproducir(self):
        return self

    def fotosintesis(self):
        self.energia += 50
        
class frutos(organismo):
    def __init__(self, posicion, vida, energia, velocidad, nombre, especie, dieta, altura):
        super().__init__(posicion, vida, energia, velocidad)
        self.nombre = nombre
        self.especie = especie
        self.dieta = dieta
        self.altura = altura
        self.velocidad = 0
        self.vida = 100

    def crecer(self):
        self.altura += 1

    def desaparecer(self):
        self.vida += 15

class raices(organismo):
    def __init__(self, posicion, vida, energia, velocidad, nombre, especie, dieta, altura):
        super().__init__(posicion, vida, energia, velocidad)
        self.nombre = nombre
        self.especie = especie
        self.dieta = dieta
        self.altura = altura
        self.velocidad = 0
        self.vida = 100

    def crecer(self):
        self.altura += 1

    def reproducir(self):
        return self

    def fotosintesis(self):
        self.energia += 50
              
class hongos(organismo):
    def __init__(self, posicion, vida, energia, velocidad, nombre, especie, dieta, altura):
        super().__init__(posicion, vida, energia, velocidad)
        self.nombre = nombre
        self.especie = especie
        self.altura = altura
        self.velocidad = 0
        self.vida = 100

    def crecer(self):
        self.altura += 1

    def esporas(self):
        self.energia += 50

    def degradar(self):
        self.energia += 50    
                                        
        
class ambiente:
    def __init__(self, nombre, temperatura, humedad, viento):
        self.nombre = nombre
        self.temperatura = temperatura
        self.humedad = humedad
        self.viento = viento
        
class ecosistema:
    def __init__(self, nombre, organismos, ambiente):
        self.nombre = nombre
        self.organismos = organismos
        self.ambiente = ambiente

leon1 = Leon(posicion=[10, 15], vida=100, energia=80, velocidad=20, nombre="Simba", especie="Panthera leo", dieta="Carnívoro")
