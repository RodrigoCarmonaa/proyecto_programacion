from opensimplex import OpenSimplex
import tkinter as tk
from PIL import Image, ImageTk
from random import choice
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
        self.atacar(presa)

    def ciclo_vida(self):
        self.vida -= 1
        self.energia -= 1

class Leon(Depredador):
    def __init__(self, nombre, especie, ubicacion, vida, energia,velocidad, hambre, sed, ciclo_vida):
        super().__init__(nombre, especie, ubicacion, vida, energia, velocidad, hambre=hambre, sed=sed, ciclo_vida=ciclo_vida)


    def cazar(self, presas):
        presa = self.buscar_presa(presas)
        self.moverse(presa)
        self.atacar(presa)
        self.energia -= 20  # Reduzco energía específica del león al cazar
        self.velocidad += 8  # Incremento de velocidad específico del león al cazar

    def comer(self):
        self.energia += 30

    def dormir(self):
        self.energia += 50

class Hiena(Depredador):
    def __init__(self, nombre, especie, ubicacion, vida, energia,velocidad, hambre, sed, ciclo_vida):
        super().__init__(nombre, especie, ubicacion, vida, energia, velocidad, hambre=hambre, sed=sed, ciclo_vida=ciclo_vida)
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
        if depredador:
            self.moverse(depredador)

    def ciclo_vida(self):
        super().ciclo_vida()
        self.hambre -= 1
        self.sed -= 1

class Jirafa(Presa):
    def __init__(self, nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida):
        super().__init__(nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida)
        self.velocidad = 18

    def huir(self):
        self.energia -= 20
        self.velocidad += 10

    def comer(self):
        self.energia += 30

    def dormir(self):
        self.energia += 50

class Gacela(Presa):
    def __init__(self, nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida):
        super().__init__(nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida)
        self.velocidad = 15
        self.vida = 100

    def huir(self):
        self.energia -= 20
        self.velocidad += 10

    def comer(self):
        self.energia += 30

    def dormir(self):
        self.energia += 50

class Rinoceronte(Presa):
    def __init__(self, nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida):
        super().__init__(nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida)
        self.velocidad = 15
        self.vida = 150

    def comer(self):
        self.energia += 30

    def dormir(self):
        self.energia += 50

class Tortuga(Presa):
    def __init__(self, nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida):
        super().__init__(nombre, especie, ubicacion, vida, energia, velocidad, hambre, sed, ciclo_vida)
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
        self.animales = []

    def agregar_evento_aleatorio(self, evento):
        self.eventos_aleatorios.append(evento)

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def ejecutar_eventos_aleatorios(self):
        for evento in self.eventos_aleatorios:
            evento()

    def ejecutar_ciclo_animales(self):
        for animal in self.animales:
            animal.ciclo_vida()
            animal.actualizar_estado(1)

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
#                           VENTANA
#####################################################################

class Ecosistema(tk.Tk):
    def __init__(self, filas, columnas, ancho_celda, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filas = filas
        self.columnas = columnas
        self.ancho_celda = ancho_celda
        self.mapa_numerico = mapa_numerico
        self.area_afectada = self.generar_impacto_3x3()
        self.area_afectada += [[random.randint(0, 26), random.randint(0, 39)] for x in range(19)]
        
        
        
        # Configurar el sistema de registro para la ventana
        logging.basicConfig(filename='movimientos.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')
# ----------------------------------------------
# Propiedades que se usaran para crear el fondo.
# ----------------------------------------------
        self.agua_image = Image.open("imagenes/agua.png")
        self.tierra_image = Image.open("imagenes/tierra.png")
        self.pasto_image = Image.open("imagenes/pasto.png")

        self.agua_image = self.agua_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.tierra_image = self.tierra_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.pasto_image = self.pasto_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)

        # Convertir las imágenes de fondo a formato Tkinter
        self.agua_image = ImageTk.PhotoImage(self.agua_image)
        self.tierra_image = ImageTk.PhotoImage(self.tierra_image)
        self.pasto_image = ImageTk.PhotoImage(self.pasto_image)

        self.proceso_diluvio = False
        self.crear_cuadricula()
        self.crear_fondo()        
        
        self.animales()
        
        
#----------------------------------------------------------
# Intefaz interactiva para el usuario, colocar en una funcion y luego llamarla
#---------------------------------------------------------
        frame = tk.Frame(master=self, width=250, height=200, bg="#171717")
        frame.place(x=930,y=40)
        mensaje= f'''
        Ciclo:{"colocar varible de conexión"}
        Animales: {"Num.-°"} habitantes
        muertes: {"colocar varible de conexión"}
        Plantas: {"colocar varible de conexión"}
        Tiempo: {"colocar varible de conexión"}
        Evento: {"Ninguno"}'''
        label = tk.Label(master=frame, text=mensaje,fg="#E6E6E6" , bg="#1A1A1A",justify="left")
        label.place(x=0,y=30)
        frame1 = tk.Frame(master=self, width=200, height=675, bg="black")
        frame1.place(x=940, y = 300)
        boton_meteorito = tk.Button(frame1, text="Generar Meteorito", command=self.generar_meteorito)
        boton_terremoto = tk.Button(frame1, text="Generar Terremoto", command=self.simular_terremoto) 
        boton_Estado = tk.Button(frame1, text="volver a la normalidad", command=self.resetear)  
        boton_Otro_evento = tk.Button(frame1, text="diluvio", command=self.generar_diluvio)  
        boton_Estado.place(x=35,y=0,width="150")   
        boton_terremoto.place(x=35,y=50,width="150")  
        boton_meteorito.place(x=35,y=100,width="150")   
        boton_Otro_evento.place(x=35,y=150,width="150")  
#--------------------------------------------------
# Animal: 
#-------------------------------------------------
    def instancia(self):
        # Direcciones iniciales de los animales
        self.direccion_leon = choice(["arriba", "abajo", "izquierda", "derecha"])  #RAA
        self.direccion_leon2 = choice(["arriba", "abajo", "izquierda", "derecha"]) #RAA

        self.direccion_jirafa = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_hiena = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_gacela = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_rinoceronte = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_elefante = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_tortuga = choice(["arriba", "abajo", "izquierda", "derecha"])
# --------------------------------------------
# Instanciar Los animales, utilizando la clase animal
# --------------------------------------------
        self.Leon1 = Animal('Leon',[20, 20],100,100,2,None,"Carnivoro","m","joven",["Hervivoro,Plantas,Agua"],self.direccion_leon)
        self.Leon2 = Animal('Leon',[21, 20],100,100,2,None,"Carnivoro","f","joven",["Hervivoro,Plantas,Agua"],self.direccion_leon)
        self.hiena =  Animal('hiena',[4, 2],100,100,2,None,"Hervivoro","m","joven",["Hervivoro,Plantas,Agua"],self.direccion_hiena)
        self.jirafa = Animal('jirafa',[3,5],100,100,2,None,"Hervivoro","m","joven",["Plantas,Agua"],self.direccion_jirafa)
        self.gacela = Animal('gacela',[1, 1],100,100,2,None,"Carnivoro","m","joven",["Hervivoro,Plantas,Agua"],self.direccion_gacela)
        self.rinoceronte = Animal('rinoceronte',[8, 15],100,100,2,None,"Carnivoro","m","joven",["Hervivoro,Plantas,Agua"],self.direccion_rinoceronte)
        self.elefante = Animal('elefante',[12, 20],100,100,2,None,"Hervivoro","f","joven",["Plantas,Agua"],self.direccion_elefante)
        self.tortuga = Animal('tortuga',[15, 25],100,100,2,None,"Hervivoro","m","joven",["Plantas,Agua"],self.direccion_tortuga)
        self.Leon373 = Animal('Leon373',[10, 8],100,100,2,None,"Carnivoro","m","adulto",["Hervivoro,Plantas,Agua"],self.direccion_leon)
        self.Leon777 = Animal('Leon777',[10, 8],100,100,2,None,"Carnivoro","m","adulto",["Hervivoro,Plantas,Agua"],self.direccion_leon)

        self.Lista_Animales = {
            "animal1": self.Leon1,
            "animal2": self.Leon2,
            "animal3": self.hiena,
            "animal4": self.jirafa,
            "animal5": self.gacela,
            "animal6": self.rinoceronte,
            "animal7": self.elefante,
            "animal8": self.tortuga,
            "animal9": self.Leon373,
            "animal10": self.Leon777,
        }

    def resetear (self):
        self.restablecer_posicion_mapa()
    def animales (self):
        if not self.proceso_diluvio:
            self.instancia()
            self.Mostrar_Animales()
            self.Animales_Desplazandose()
        elif self.proceso_diluvio:
            self.canvas.delete("leon373", "leon", "hiena", "jirafa", "gacela", "rinoceronte", "elefante", "tortuga", "Leon777")

    def generar_diluvio(self):
        if not self.proceso_diluvio:
            self.proceso_diluvio = True
            # Desaparecer animales antes del diluvio
            self.desaparecer_animales()
            # Mostrar animales después del diluvio
            self.after(500, self.mostrar_animales_despues_diluvio)
            # Crear animación de diluvio
            self.animar_diluvio(0)

    def animar_diluvio(self, contador):
        if contador < 20:
            self.proceso_diluvio = True  # Ajusta el número de iteraciones según sea necesario
            self.canvas.delete("leon373", "leon", "hiena", "jirafa", "gacela", "rinoceronte", "elefante", "tortuga", "Leon777")  # Elimina el fondo actual

            for fila in range(self.filas):
                for columna in range(self.columnas):
                    if random.random() < 0.5:
                        x_posicion = columna * self.ancho_celda
                        y_posicion = fila * self.ancho_celda
                        self.canvas.create_image(x_posicion, y_posicion, anchor=tk.NW, image=self.agua_image, tags="fondo")

            self.after(100, self.animar_diluvio, contador + 1)
        else:
            self.proceso_diluvio = False
            self.mostrar_animales_despues_diluvio()
            
    def mostrar_animales_despues_diluvio(self):
        if not self.proceso_diluvio:
            self.Mostrar_Animales()
    

    def generar_impacto_3x3(self):
        centro_x = random.randint(1, 25)
        centro_y = random.randint(1, 38)
        return [[centro_x + dx, centro_y + dy] for dx in range(-1, 2) for dy in range(-1, 2)]

    def generar_meteorito(self):
        for area_afectada in self.area_afectada:
            imagen_fondo = self.meteoritos_2_image
            x_posicion = area_afectada[1] * self.ancho_celda
            y_posicion = area_afectada[0] * self.ancho_celda
            try:
                self.canvas.create_image(x_posicion, y_posicion, anchor=tk.NW, image=imagen_fondo, tags="fondo")
                logging.info(f"El meteorito realizó un impacto en las coordenadas ({x_posicion // self.ancho_celda}, {y_posicion // self.ancho_celda})")
            except Exception as e:
                print(f"Ocurrió un error: {e}")

    def simular_terremoto(self):
        # Almacena la posición original de la cuadrícula y del mapa
        self.posicion_original_cuadricula = self.obtener_posicion_cuadricula()
        self.posicion_original_mapa = self.canvas.canvasx(0), self.canvas.canvasy(0)
        # Simula el terremoto
        self.realizar_movimiento_terremoto(10)
        self.restablecer_posicion_mapa()


    def restablecer_posicion_mapa(self):
        # Restaura las posiciones originales de la cuadrícula
        x_actual, y_actual = self.obtener_posicion_cuadricula()
        delta_x_cuadricula = 0 - x_actual
        delta_y_cuadricula = 0 - y_actual
        self.canvas.move("all", delta_x_cuadricula, delta_y_cuadricula)

        # Restaura las posiciones originales del mapa
        delta_x_mapa = 0 - x_actual
        delta_y_mapa = 0 - y_actual
        self.canvas.move("fondo", delta_x_mapa, delta_y_mapa)  # Mueve solo el fondo (etiqueta "fondo")

        # Establece la posición original de la cuadrícula
        self.canvas.coords("all", 0, 0, self.columnas * self.ancho_celda, self.filas * self.ancho_celda)

        # Restaura las posiciones originales de las líneas de la cuadrícula
        for id_linea_horizontal, y in zip(self.ids_lineas_horizontales, range(self.ancho_celda, self.filas * self.ancho_celda, self.ancho_celda)):
            self.canvas.coords(id_linea_horizontal, 0, y, self.columnas * self.ancho_celda, y)

        for id_linea_vertical, x in zip(self.ids_lineas_verticales, range(self.ancho_celda, self.columnas * self.ancho_celda, self.ancho_celda)):
            self.canvas.coords(id_linea_vertical, x, 0, x, self.filas * self.ancho_celda)

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

    def restaurar_posiciones_originales(self):
        # Restaura las posiciones originales de la cuadrícula
        x_actual, y_actual = self.obtener_posicion_cuadricula()
        delta_x_cuadricula = self.posicion_original_cuadricula[0] - x_actual
        delta_y_cuadricula = self.posicion_original_cuadricula[1] - y_actual
        self.canvas.move("all", delta_x_cuadricula, delta_y_cuadricula)

        # Restaura las posiciones originales del mapa
        delta_x_mapa = self.posicion_original_mapa[0] - x_actual
        delta_y_mapa = self.posicion_original_mapa[1] - y_actual
        self.canvas.move("all", delta_x_mapa, delta_y_mapa)

    def realizar_movimiento_terremoto(self, contador):
        if contador > 0:
            self.mover_pantalla()
            self.canvas.lift("all")
            self.update()
            self.after(100, self.realizar_movimiento_terremoto, contador - 1)
        else:
            self.restablecer_posicion_mapa()
    
    def mover_pantalla(self):
        delta_x = random.randint(-1, 1)  # Ajusta el rango de movimiento en el eje x
        delta_y = random.randint(-1, 1)  # Ajusta el rango de movimiento en el eje y

         # Obtén las coordenadas actuales del área visible del mapa
        x_inicio, y_inicio = self.canvas.canvasx(0), self.canvas.canvasy(0)
        x_fin, y_fin = self.canvas.canvasx(self.winfo_width()), self.canvas.canvasy(self.winfo_height())

        if x_inicio + delta_x * self.ancho_celda >= 0 and x_fin + delta_x * self.ancho_celda <= self.canvas.winfo_width():
            self.canvas.move("all", delta_x * self.ancho_celda, 0)

        if y_inicio + delta_y * self.ancho_celda >= 0 and y_fin + delta_y * self.ancho_celda <= self.canvas.winfo_height():
            self.canvas.move("all", 0, delta_y * self.ancho_celda)

        # Mueve todos los elementos en el lienzo
        self.canvas.move("all", delta_x * self.ancho_celda, delta_y * self.ancho_celda)

    def obtener_posicion_cuadricula(self):
        # Obtener las coordenadas actuales de la cuadrícula
        x_actual = self.canvas.canvasx(0)
        y_actual = self.canvas.canvasy(0)

        # Actualizar la posición original
        self.posicion_original_cuadricula = self.canvas.canvasx(0), self.canvas.canvasy(0)

        return x_actual, y_actual
    
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
        self.canvas = tk.Canvas(self, width=self.columnas * self.ancho_celda, height=self.filas * self.ancho_celda)
        self.canvas.place(x=45,y=5)

        # Listas para almacenar los IDs de las líneas horizontales y verticales
        self.ids_lineas_horizontales = []
        self.ids_lineas_verticales = []

        for i in range(1, self.filas):
            y = i * self.ancho_celda
            id_linea_horizontal = self.canvas.create_line(0, y, self.columnas * self.ancho_celda, y)
            self.ids_lineas_horizontales.append(id_linea_horizontal)

        for j in range(1, self.columnas):
            x = j * self.ancho_celda
            id_linea_vertical = self.canvas.create_line(x, 0, x, self.filas * self.ancho_celda)
            self.ids_lineas_verticales.append(id_linea_vertical)

        # Guardar una referencia al canvas para su uso posterior
        self.posicion_original_cuadricula = self.obtener_posicion_cuadricula() # Guardar una referencia al canvas para su uso posterior
    
    def obtener_posicion_cuadricula(self):
        # Obtener las coordenadas actuales de la cuadrícula
        x_actual = self.canvas.canvasx(0)
        y_actual = self.canvas.canvasy(0)

        # Actualizar la posición original
        self.posicion_original_cuadricula = self.canvas.canvasx(0), self.canvas.canvasy(0)

        return x_actual, y_actual
    
    def Cargar_Imagenes_ANIMALES(self):
        self.lion_image = Image.open("imagenes/leon.png")            # [0]
        self.jirafa_image = Image.open("imagenes/jirafa.png")        # [1]
        self.hiena_image = Image.open("imagenes/hiena.png")          # [2]
        self.gacela_image = Image.open("imagenes/gacela.png")        # [3]
        self.rinoceronte_image = Image.open("imagenes/rinoceronte.png") # [4]
        self.elefante_image = Image.open("imagenes/elefante.png")  # [5]
        self.tortuga_image = Image.open("imagenes/tortuga.png")    # [6]
        self.lion00_image = Image.open("imagenes/cria_leon.png")  # [7]
        self.meteoritos_2_image = Image.open("imagenes/meteorito2.png")    ##RAA , añadir el 1 y 2 , ya que una estaba remplazando la otra
 
        # Redimensionar imágenes de animales
        self.lion_image = self.lion_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.jirafa_image = self.jirafa_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.hiena_image = self.hiena_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.gacela_image = self.gacela_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.rinoceronte_image = self.rinoceronte_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.elefante_image = self.elefante_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.tortuga_image = self.tortuga_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.lion00_image = self.lion00_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.meteoritos_2_image = self.meteoritos_2_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)  ##RAA

        # Convertir imágenes a formato Tkinter
        self.lion_image = ImageTk.PhotoImage(self.lion_image)
        self.jirafa_image = ImageTk.PhotoImage(self.jirafa_image)
        self.hiena_image = ImageTk.PhotoImage(self.hiena_image)
        self.gacela_image = ImageTk.PhotoImage(self.gacela_image)
        self.rinoceronte_image = ImageTk.PhotoImage(self.rinoceronte_image)
        self.elefante_image = ImageTk.PhotoImage(self.elefante_image)
        self.tortuga_image = ImageTk.PhotoImage(self.tortuga_image)
        self.lion00_image = ImageTk.PhotoImage(self.lion00_image)
        self.meteoritos_2_image = ImageTk.PhotoImage(self.meteoritos_2_image)
        # Añadir las imagenes a una lista 
        Animal = [self.lion_image, self.hiena_image,self.jirafa_image, self.gacela_image, self.rinoceronte_image, self.elefante_image, self.tortuga_image, self.lion00_image]
        # Retornar la lista 
        return Animal
  
    def Mostrar_Animales(self):
        if not self.proceso_diluvio:
            Animal = self.Cargar_Imagenes_ANIMALES()
            for animal,tipo_animal in self.Lista_Animales.items():
                Tipo_animal = self.Lista_Animales[animal]     
                if 'Leon' in Tipo_animal.nombre:
                    if 'joven' in Tipo_animal.edad:
                        Tipo_animal.Imagen_Animal = Animal[7]
                    elif 'adulto' in Tipo_animal.edad:
                        Tipo_animal.Imagen_Animal = Animal[0]
                elif 'hiena' in  Tipo_animal.nombre:
                    Tipo_animal.Imagen_Animal = Animal[1]
                elif 'jirafa' in  Tipo_animal.nombre:
                    Tipo_animal.Imagen_Animal = Animal[2]
                elif 'gacela' in  Tipo_animal.nombre:
                    Tipo_animal.Imagen_Animal = Animal[3]
                elif 'rinoceronte' in  Tipo_animal.nombre:
                    Tipo_animal.Imagen_Animal = Animal[4]
                elif 'elefante' in  Tipo_animal.nombre:
                    Tipo_animal.Imagen_Animal = Animal[5]
                elif 'tortuga' in  Tipo_animal.nombre:
                    Tipo_animal.Imagen_Animal = Animal[6]
                Tipo_animal.Prueba(self.canvas)
                Tipo_animal.mostrar_imagen()

    def cria_2(self):
        self.canvas.delete('Leon777')


    def desaparecer_animales(self):
        if not self.proceso_diluvio:
            self.canvas.delete("leon373", "leon", "hiena", "jirafa", "gacela", "rinoceronte", "elefante", "tortuga", "Leon777")


    def Animales_Desplazandose(self):
        self.canvas.delete("leon373","leon","hiena", "jirafa", "gacela", "rinoceronte", "elefante", "tortuga")

        self.Leon373.ubicacion = self.Leon373.animal_Moviendose(self.Leon373.nombre ,self.Leon373.ubicacion ,self.Leon373.Direccion )
        self.Leon1.ubicacion = self.Leon1.animal_Moviendose(self.Leon1.nombre,self.Leon1.ubicacion,self.Leon1.Direccion)      
        self.Leon2.ubicacion = self.Leon2.animal_Moviendose(self.Leon2.nombre,self.Leon2.ubicacion,self.Leon2.Direccion)
        self.hiena.ubicacion = self.hiena.animal_Moviendose(self.hiena.nombre, self.hiena.ubicacion ,self.hiena.Direccion)
        self.jirafa.ubicacion = self.jirafa.animal_Moviendose(self.jirafa.nombre, self.jirafa.ubicacion, self.jirafa.Direccion)  
        self.gacela.ubicacion = self.gacela.animal_Moviendose(self.gacela.nombre,self.gacela.ubicacion, self.gacela.Direccion)  
        self.rinoceronte.ubicacion = self.rinoceronte.animal_Moviendose(self.rinoceronte.nombre, self.rinoceronte.ubicacion, self.rinoceronte.Direccion)
        self.elefante.ubicacion = self.elefante.animal_Moviendose(self.elefante.nombre, self.elefante.ubicacion, self.elefante.Direccion)      
        self.tortuga.ubicacion = self.tortuga.animal_Moviendose(self.tortuga.nombre,self.tortuga.ubicacion, self.tortuga.Direccion)


        self.registrar_movimiento(self.Leon373.nombre, self.Leon373.ubicacion)
        self.registrar_movimiento(self.Leon1.nombre, self.Leon1.ubicacion)
        self.registrar_movimiento(self.Leon2.nombre, self.Leon2.ubicacion)
        self.registrar_movimiento(self.hiena.nombre, self.hiena.ubicacion )
        self.registrar_movimiento(self.jirafa.nombre, self.jirafa.ubicacion)
        self.registrar_movimiento(self.gacela.nombre,self.gacela.ubicacion)
        self.registrar_movimiento(self.rinoceronte.nombre, self.rinoceronte.ubicacion)
        self.registrar_movimiento(self.elefante.nombre,self.elefante.ubicacion)
        self.registrar_movimiento(self.tortuga.nombre, self.tortuga.ubicacion)

        self.Leon777.ubicacion = self.Leon777.animal_Moviendose(self.Leon777.nombre ,self.Leon777.ubicacion ,self.Leon777.Direccion )
        self.registrar_movimiento(self.Leon777.nombre, self.Leon777.ubicacion)
        
        self.after(300,self.Animales_Desplazandose)

    def registrar_movimiento(self, animal, posicion):
        mensaje = f"{animal} se movió a la posición {posicion}"
        logging.info(mensaje)

        return None
    
        

filas = 27
columnas = 35


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
    ecosistema = Ecosistema(filas=27, columnas= 35, ancho_celda=25)
    ecosistema.geometry("1190x675") # RAA
    ecosistema.config(bg="black")
    ecosistema.mainloop()
