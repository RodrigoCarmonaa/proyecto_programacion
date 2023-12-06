from opensimplex import OpenSimplex
import tkinter as tk
from PIL import Image, ImageTk
from random import choice, randint
import random
import logging
import time
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

    def atacar(self, presa):
        if presa:
            # El animal inflige daño a la presa
            presa.recibir_ataque(self)

    def recibir_ataque(self, atacante):
        # El animal recibe daño del atacante
        self.vida -= atacante.energia

        # Si la vida del animal cae a cero o menos, muere
        if self.vida <= 0:
            self.vida = 0
            self.energia = 0


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



class Cria(Animal):
    def __init__(self, nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida):
        super().__init__(nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida)
        self.etapa_crecimiento = 1  # Podrías añadir una etapa de crecimiento inicial



#####################################################################
#                           DEPREDADOR
#####################################################################
class Depredador(Animal):
    def __init__(self, nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida):
        super().__init__(nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida)

    def cazar(self, presas):
        presa = self.buscar_presa(presas)
        self.moverse(presa)
        self.atacar(presa)

    def ciclo_vida(self):
        self.vida -= 1
        self.energia -= 1

class Leon(Depredador):
    def __init__(self, nombre, especie, ubicacion, vida, energia, hambre, sed, ciclo_vida):
        super().__init__(nombre, especie, ubicacion, vida, energia, velocidad=20, hambre=hambre, sed=sed, ciclo_vida=ciclo_vida)

    def cazar(self, presas):
        presa = self.buscar_presa(presas)
        self.moverse(presa)
        self.atacar(presa)
        self.energia -= 20  # Reduzco energía específica del león al cazar
        self.velocidad += 8  # Incremento de velocidad específico del león al cazar

    def comer(self):
        self.energia += 30


    def reproducirse(self, animales):
            companero = self.buscar_companero(animales)
            if companero:
                probabilidad = randint(1, 10)
                if probabilidad == 3:
                    nueva_cria = Animal(f"NuevoAnimal_{randint(1, 10)}", self.especie, self.ubicacion, vida=1, energia=1, velocidad=1, hambre=1, sed=1)
                    logging.info(f"{self.nombre} se reprodujo y dio a luz a una nueva cría llamada {nueva_cria.nombre}")
                    return nueva_cria

    
    def dormir(self):
        self.energia += 50
        
        

class Hiena(Organismo):
    def __init__(self, posicion, nombre="", especie="", dieta=""):
        super().__init__(posicion, nombre=nombre, especie=especie, dieta=dieta)
        self.velocidad = 20
        self.vida = 100

    def cazar(self):
        self.energia -= 20
        self.velocidad += 8

    def comer(self):
        self.energia += 30

    def dormir(self):
        self.energia += 50   
#####################################################################
#                           PRESA
#####################################################################
class Presa(Animal):
    def __init__(self, nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida):
        super().__init__(nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida)

    def huir(self, depredadores):
        depredador = self.buscar_depredador(depredadores)
        self.moverse(depredador)

    def huir(self, depredadores):
        depredador = self.buscar_depredador(depredadores)
        self.moverse(depredador)    

    def ciclo_vida(self):
        self.vida -= 1
        self.energia -= 1

class Jirafa(Presa):
    def __init__(self, posicion, nombre="", especie="", dieta=""):
        super().__init__(posicion, nombre=nombre, especie=especie, dieta=dieta)
        self.velocidad = 18

    def huir(self):
        self.energia -= 20
        self.velocidad += 10

    def comer(self):
        self.energia += 30

    def dormir(self):
        self.energia += 50

class Gacela(Presa):
    def __init__(self, posicion, nombre="", especie="", dieta=""):
        super().__init__(posicion, nombre=nombre, especie=especie, dieta=dieta)
        self.velocidad = 15
        self.vida = 100

    def huir(self):
        self.energia -= 20
        self.velocidad += 10

    def comer(self):
        self.energia += 30

    def dormir(self):
        self.energia += 50

class Rinoceronte(Organismo):
    def __init__(self, posicion, nombre="", especie="", dieta=""):
        super().__init__(posicion, nombre=nombre, especie=especie, dieta=dieta)
        self.velocidad = 15
        self.vida = 150

    def comer(self):
        self.energia += 30

    def dormir(self):
        self.energia += 50

class Tortuga(Organismo):
    def __init__(self, posicion, nombre="", especie="", dieta=""):
        super().__init__(posicion, nombre=nombre, especie=especie, dieta=dieta)
        self.velocidad = 5
        self.vida = 100

    def comer(self):
        self.energia += 30

    def dormir(self):
        self.energia += 50
        
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


"""
#####################################################################
    
#####################################################################
#                           VENTANA
#####################################################################
"""

class Ventana(tk.Tk):
    def __init__(self, filas, columnas, ancho_celda, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filas = filas
        self.columnas = columnas
        self.ancho_celda = ancho_celda
        self.mapa_numerico = mapa_numerico
        
        # Configurar el sistema de registro para la ventana
        logging.basicConfig(filename='movimientos.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')

        # Cargar imágenes de animales
        self.lion_image = Image.open("imagenes/leon.png")


        # Posiciones iniciales de los animales
        self.leon2_posicion = [5, 5]
        self.leon_posicion = [5, 8]
        self.leon3_posicion = [5, 5]
        self.leon4_posicion = [5, 5]
        self.leon5_posicion = [5, 8]
        self.leon6_posicion = [5, 4]
        self.leon7_posicion = [5, 3]
        self.leon8_posicion = [5, 25]
        self.leon9_posicion = [5, 0]


        # Direcciones iniciales de los animales
        self.direccion_leon = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_leon2 = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_leon3 = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_leon4 = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_leon5 = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_leon6 = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_leon7 = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_leon8 = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_leon9 = choice(["arriba", "abajo", "izquierda", "derecha"])
        
    x|    self.agua_image = Image.open("imagenes/agua.png")
        self.tierra_image = Image.open("imagenes/tierra.png")
        self.pasto_image = Image.open("imagenes/pasto.png")

        self.agua_image = self.agua_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.tierra_image = self.tierra_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.pasto_image = self.pasto_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)

        # Convertir las imágenes de fondo a formato Tkinter
        self.agua_image = ImageTk.PhotoImage(self.agua_image)
        self.tierra_image = ImageTk.PhotoImage(self.tierra_image)
        self.pasto_image = ImageTk.PhotoImage(self.pasto_image)

        #meteorito
        self.meteoritos_1_image = Image.open("imagenes/meteorito1.png")    ##RAA , añadir el 1 y 2 , ya que una estaba remplazando la otra
        self.meteoritos_2_image = Image.open("imagenes/meteorito2.png")    ##RAA , añadir el 1 y 2 , ya que una estaba remplazando la otra

        self.meteoritos_1_image = self.meteoritos_1_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)  ##RAA
        self.meteoritos_2_image = self.meteoritos_2_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)  ##RAA

        # Convertir las imágenes de fondo a formato Tkinter
        self.meteoritos_1_image = ImageTk.PhotoImage(self.meteoritos_1_image)    ##RAA
        self.meteoritos_2_image = ImageTk.PhotoImage(self.meteoritos_2_image)    ##RAA

        boton_meteorito = tk.Button(self, text="Generar Meteorito",command=self.generar_meteorito)   ##RAA
        boton_meteorito.pack()   ##RAA

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
            self.canvas.delete("leon", "jirafa", "hiena", "gacela", "rinoceronte", "elefante", "tortuga","leon2")

            # Redimensionar imágenes de animales
            self.lion_image = self.lion_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)


            # Convertir imágenes a formato Tkinter
            self.lion_image = ImageTk.PhotoImage(self.lion_image)


            # Posiciones de los animales
            posiciones = {
                "leon": self.leon_posicion,
                "leon2": self.leon2_posicion,
                "leon3": self.leon_posicion,
                "leon4": self.leon_posicion,
                "leon5": self.leon_posicion,
                "leon6": self.leon_posicion,
                "leon7": self.leon_posicion,
                "leon8": self.leon_posicion,
                "leon9": self.leon_posicion,

            }

            # Imágenes de los animales
            imagenes = {
                "leon": self.lion_image,
                "leon2": self.lion_image,
                "leon3": self.lion_image,
                "leon4": self.lion_image,
                "leon5": self.lion_image,
                "leon6": self.lion_image,
                "leon7": self.lion_image,
                "leon8": self.lion_image,
                "leon9": self.lion_image,

            }

    def mover_animales(self):
        # Eliminar instancias previas de los animales
        self.canvas.delete("leon", "jirafa", "hiena", "gacela", "rinoceronte", "elefante", "tortuga")

        # Mover cada animal individualmente y registrar el movimiento
        self.leon_posicion = self.mover_animal_individual("leon", self.leon_posicion, self.direccion_leon)
        self.registrar_movimiento("leon", self.leon_posicion)

        self.leon2_posicion = self.mover_animal_individual("leon2", self.leon2_posicion, self.direccion_leon2)
        self.registrar_movimiento("leon2", self.leon2_posicion)

        self.leon3_posicion = self.mover_animal_individual("leon3", self.leon3_posicion, self.direccion_leon3)
        self.registrar_movimiento("leon3", self.leon3_posicion)
        
        self.leon4_posicion = self.mover_animal_individual("leon4", self.leon4_posicion, self.direccion_leon4)
        self.registrar_movimiento("leon4", self.leon4_posicion)
        
        self.leon5_posicion = self.mover_animal_individual("leon5", self.leon5_posicion, self.direccion_leon5)
        self.registrar_movimiento("leon5", self.leon5_posicion)
        
        self.leon6_posicion = self.mover_animal_individual("leon6", self.leon6_posicion, self.direccion_leon6)
        self.registrar_movimiento("leon6", self.leon6_posicion)
        
        self.leon7_posicion = self.mover_animal_individual("leon7", self.leon7_posicion, self.direccion_leon7)
        self.registrar_movimiento("leon7", self.leon7_posicion)
        
        self.leon8_posicion = self.mover_animal_individual("leon8", self.leon8_posicion, self.direccion_leon8)
        self.registrar_movimiento("leon8", self.leon8_posicion)
        
        self.leon9_posicion = self.mover_animal_individual("leon9", self.leon9_posicion, self.direccion_leon9)
        self.registrar_movimiento("leon9", self.leon9_posicion)

        # Establecer un retardo y llamar a la función nuevamente
        self.after(300, self.mover_animales)

        animales_en_posiciones = {
            "leon": self.leon_posicion,
            "leon2": self.leon2_posicion,
            "leon3": self.leon_posicion,
            "leon4": self.leon_posicion,
            "leon5": self.leon_posicion,
            "leon6": self.leon_posicion,
            "leon7": self.leon_posicion,
            "leon8": self.leon_posicion,
            "leon9": self.leon_posicion,
        }
        
        

    def mostrar_nueva_cria(self, nueva_cria):
        self.lion_image = self.lion_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.lion_image = ImageTk.PhotoImage(self.lion_image)
            
        x_posicion = nueva_cria.ubicacion[0] * self.ancho_celda
        y_posicion = nueva_cria.ubicacion[1] * self.ancho_celda

        self.canvas.create_image(x_posicion, y_posicion, anchor=tk.NW, image=self.lion_image, tags="nueva_cria")
        
    
    def generar_impacto_3x3(self):
        centro_x = random.randint(1, 25)
        centro_y = random.randint(1, 38)
        return [[centro_x + dx, centro_y + dy] for dx in range(-1, 2) for dy in range(-1, 2)]

    def generar_meteorito(self):
        self.area_afectada = self.generar_impacto_3x3()
        self.area_afectada += [[random.randint(0, 26), random.randint(0, 39)] for x in range(19)]
        for area_afectada in self.area_afectada:
            imagen_fondo = self.meteoritos_2_image
            x_posicion = area_afectada[1] * self.ancho_celda
            y_posicion = area_afectada[0] * self.ancho_celda
            try:
                self.canvas.create_image(x_posicion, y_posicion, anchor=tk.NW, image=imagen_fondo, tags="fondo")
                logging.info(f"El meteorito realizó un impacto en las coordenadas ({x_posicion // self.ancho_celda}, {y_posicion // self.ancho_celda})")
            except Exception as e:
                print(f"Ocurrió un error: {e}")

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
        elif tag == "leon2":
            image = self.lion_image
            self.direccion_leon2 = choice(["arriba", "abajo", "izquierda", "derecha"])   
        elif tag == "leon3":
            image = self.lion_image
            self.direccion_leon3 = choice(["arriba", "abajo", "izquierda", "derecha"])
        elif tag == "leon4":
            image = self.lion_image
            self.direccion_leon4 = choice(["arriba", "abajo", "izquierda", "derecha"])
        elif tag == "leon5":
            image = self.lion_image
            self.direccion_leon5 = choice(["arriba", "abajo", "izquierda", "derecha"])
        elif tag == "leon6":
            image = self.lion_image
            self.direccion_leon6 = choice(["arriba", "abajo", "izquierda", "derecha"])
        elif tag == "leon7":
            image = self.lion_image
            self.direccion_leon7 = choice(["arriba", "abajo", "izquierda", "derecha"])
        elif tag == "leon8":
            image = self.lion_image
            self.direccion_leon8 = choice(["arriba", "abajo", "izquierda", "derecha"])
        elif tag == "leon9":
            image = self.lion_image
            self.direccion_leon9 = choice(["arriba", "abajo", "izquierda", "derecha"])
                 

        self.canvas.create_image(x_posicion, y_posicion, anchor=tk.NW, image=image, tags=tag)
        return posicion
    
    def registrar_movimiento(self, animal, posicion):
        mensaje = f"{animal} se movió a la posición {posicion}"
        logging.info(mensaje)

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

if __name__ == "__main__":
    ventana = Ventana(filas=27, columnas=40, ancho_celda=25)

    ventana.mainloop()

