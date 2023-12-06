from opensimplex import OpenSimplex
import tkinter as tk
from PIL import Image, ImageTk
from random import choice
import random
import logging
import time 

# -*- coding: utf-8 -*-



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
    def __init__(self, nombre, tipo, ubicacion, vida, energia, velocidad, ciclo_vida, tiempo_sin_agua,Imagen_Planta):
        super().__init__(nombre, ubicacion, vida, energia, velocidad)
        self.tipo = tipo
        self.ciclo_vida = ciclo_vida
        self.tiempo_sin_agua = tiempo_sin_agua
        self.Image_Planta = Imagen_Planta
        self.canvas = self.Prueba()
    
    def Prueba(self,canva=None):
        self.canvas = canva

    def mostrar_imagen(self):
        self.canvas.create_image(self.ubicacion[0],self.ubicacion[1], anchor=tk.NW, image=self.Image_Planta, tags=self.nombre)



class Arbol_Verde(Planta): # Manzano
    # Lista_Bloque_vivo = []
    def Area_asignada(self):
        pass
class Arbol_Rojo(Planta):
    def Area_asignada(self):
        pass
class Arbusto(Planta):
    def Area_asignada(self):
        pass
class Helechon(Planta):
    def Area_asignada(self):
        pass
class Cactus(Planta):
    def Area_asignada(self):
        pass


#####################################################################
#                           ANIMAL
#####################################################################
class Animal(Organismo):

    def __init__(self,nombre,ubicacion,vida_hp, energia, velocidad,Imagen_Animal,especie, Sexo, edad, Alimentacion,Direccion):
        super().__init__(nombre, ubicacion, vida_hp, energia, velocidad)
        self.velocidad = velocidad
        self.especie = especie

        self.sexo = Sexo
        self.edad = edad
        self.Alimentacion = Alimentacion

        self.nivel_hambre = 70
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
        self.canvas.create_image(self.ubicacion[0]*25,self.ubicacion[1]*25, anchor=tk.NW, image=self.Imagen_Animal, tags=self.nombre)

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
        
    def Morir(self,Tipo_de_muerte,Imagen = None):
        logging.info(f"El {self.nombre} ha muerto")
        self.estado = "muerto"
        if Imagen != None:
            return
        else:
            self.Imagen_Animal = Imagen

        return 
    def Comer(self):
        self.nivel_hambre += 20
        if self.nivel_hambre >= 100:
            self.nivel_hambre = 100
            # MENSAJE LOG : ANIMAL LLENO
        logging.info(f"El {self.nombre} ha comido")
    def Daño(self):
        self.vida -= 60    
        logging.info(f"El {self.nombre} ha recibido daño") 
class Leon(Animal):
    def rugir(self):
        logging.info(f"El {self.nombre} ha rugido")
class Jirafa(Animal):
    def estirar_cuello(self):
        logging.info(f"La {self.nombre} ha estirado el cuello")
class Hiena(Animal):
    def reir(self):
        logging.info(f"La {self.nombre} ha reido")
class Gacela(Animal):
    def saltar(self):
        logging.info(f"La {self.nombre} ha saltado")
class Rinoceronte(Animal):
    def embestir(self):
        logging.info(f"El {self.nombre} ha embestido")
class Elefante(Animal):
    def cargar(self):
        logging.info(f"El {self.nombre} ha cargado")
class Tortuga(Animal):
    def esconderse(self):
        logging.info(f"La {self.nombre} se ha escondido")
class Ciervo(Animal):
    def saltar(self):
        logging.info(f"El {self.nombre} ha saltado")
class Antilopes(Animal):
    def correr(self):
        logging.info(f"El {self.nombre} ha corrido")
class Bufalo(Animal):
    def embestir(self):
        logging.info(f"El {self.nombre} ha embestido")

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
class SabanaAfricana:
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

        logging.basicConfig(filename='prueba.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
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
# Intefaz interactiva para el usuario
#---------------------------------------------------------
        frame = tk.Frame(master=self, width=250, height=200, bg="#171717")
        frame.place(x=930,y=40)
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
        self.direccion_ciervo = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_antilopes = choice(["arriba", "abajo", "izquierda", "derecha"])
        self.direccion_bufalo = choice(["arriba", "abajo", "izquierda", "derecha"])
# --------------------------------------------
# Instanciar Los animales, utilizando la clase animal
# --------------------------------------------
        self.Leon1 = Leon('Leon',[20, 20],10,100,2,None,"Carnivoro","m","joven",["Hervivoro,Plantas,Agua"],self.direccion_leon)
        self.Leon2 = Leon('Leon',[21, 20],10,100,2,None,"Carnivoro","f","joven",["Hervivoro,Plantas,Agua"],self.direccion_leon)
        self.hiena =  Hiena('hiena',[4, 2],10,100,2,None,"Hervivoro","m","joven",["Hervivoro,Plantas,Agua"],self.direccion_hiena)
        self.jirafa = Jirafa('jirafa',[3,5],10,100,2,None,"Hervivoro","m","joven",["Plantas,Agua"],self.direccion_jirafa)
        self.gacela = Gacela('gacela',[1, 1],10,100,2,None,"Carnivoro","m","joven",["Hervivoro,Plantas,Agua"],self.direccion_gacela)
        self.rinoceronte = Rinoceronte('rinoceronte',[8, 15],10,100,2,None,"Carnivoro","m","joven",["Hervivoro,Plantas,Agua"],self.direccion_rinoceronte)
        self.elefante = Elefante('elefante',[12, 20],10,100,2,None,"Hervivoro","f","joven",["Plantas,Agua"],self.direccion_elefante)
        self.tortuga = Tortuga('tortuga',[15, 25],10,100,2,None,"Hervivoro","m","joven",["Plantas,Agua"],self.direccion_tortuga)
        self.Leon373 = Leon('Leon373',[10, 8],10,100,2,None,"Carnivoro","m","adulto",["Hervivoro,Plantas,Agua"],self.direccion_leon)
        self.Leon777 = Leon('Leon777',[10, 8],10,100,2,None,"Carnivoro","m","adulto",["Hervivoro,Plantas,Agua"],self.direccion_leon)
        self.ciervo = Ciervo('ciervo',[20, 18],10,100,2,None,"Hervivoro","m","adulto",["Hervivoro,Plantas,Agua"],self.direccion_ciervo)
        self.antilopes = Antilopes('antilopes',[2, 14],10,100,2,None,"Hervivoro","m","adulto",["Hervivoro,Plantas,Agua"],self.direccion_antilopes)
        self.bufalo = Bufalo('bufalo',[13, 21],10,100,2,None,"Hervivoro","m","adulto",["Hervivoro,Plantas,Agua"],self.direccion_bufalo)

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
            "animal11": self.ciervo,
            "animal12": self.antilopes,
            "animal13": self.bufalo,
        }



    def resetear (self):
        self.restablecer_posicion_mapa()

    def animales (self):
        if not self.proceso_diluvio:
            self.instancia()
            self.Mostrar_Animales()
            self.Animales_Desplazandose()
            self.Inicializar_Plantas()
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
        logging.info("DILUVIOOOOOOOOOOOOO")
            
    def mostrar_animales_despues_diluvio(self):
        if not self.proceso_diluvio:
            self.Mostrar_Animales()
    

    def generar_impacto_3x3(self):
        centro_x = random.randint(1, 25)
        centro_y = random.randint(1, 38)
        return [[centro_x + dx, centro_y + dy] for dx in range(-1, 2) for dy in range(-1, 2)]

    def generar_meteorito(self):
        self.area_afectada = self.generar_impacto_3x3()   #CODE
        self.area_afectada += [[random.randint(0, 26), random.randint(0, 39)] for x in range(19)] #CODE
        for area_afectada in self.area_afectada:
            imagen_fondo = self.meteoritos_2_image
            x_posicion = area_afectada[1] * self.ancho_celda
            y_posicion = area_afectada[0] * self.ancho_celda
            try:
                self.canvas.create_image(x_posicion, y_posicion, anchor=tk.NW, image=imagen_fondo, tags="fondo")
                logging.info(f"El meteorito realizó un impacto en las coordenadas ({x_posicion // self.ancho_celda}, {y_posicion // self.ancho_celda})")
            except Exception as e:
                print(f"Ocurrió un error: {e}")
            # Condicional en caso que alla un animal muera
            for animal,tipo_animal in self.Lista_Animales.items():
                Tipo_animal = self.Lista_Animales[animal]
                if Tipo_animal.ubicacion[0] == (x_posicion//25) and Tipo_animal.ubicacion[1] == (y_posicion//25):
                   self.Prueba_muerte(Tipo_animal,"Meteorito")
        logging.info("ACABA DE CAER UN METEORITOO")

    def simular_terremoto(self):
        # Almacena la posición original de la cuadrícula y del mapa
        self.posicion_original_cuadricula = self.obtener_posicion_cuadricula()
        self.posicion_original_mapa = self.canvas.canvasx(0), self.canvas.canvasy(0)
        # Simula el terremoto
        self.realizar_movimiento_terremoto(10)
        self.restablecer_posicion_mapa()
        logging.info(" SE A GENERADO UN TERREMOTOOOOO")

    def Prueba_muerte(self,Animal_Muere,Razon):
        Tumba = self.Cargar_Imagenes_ANIMALES()
        Animal = Animal_Muere
        if Razon == "Meteorito":
            Animal.Morir("Aplastado por meteorito DX",Tumba[11])
            # self.Mostrar_Animales()
        if Razon == "Comido":
            Animal.Morir("Fue comido por un depredador",Tumba[11])

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
        # Cargar imágenes de animales
        self.lion_image = Image.open("imagenes/leon.png")            # [0]
        self.jirafa_image = Image.open("imagenes/jirafa.png")        # [1]
        self.hiena_image = Image.open("imagenes/hiena.png")          # [2]
        self.gacela_image = Image.open("imagenes/gacela.png")        # [3]
        self.rinoceronte_image = Image.open("imagenes/rinoceronte.png") # [4]
        self.elefante_image = Image.open("imagenes/elefante.png")  # [5]
        self.tortuga_image = Image.open("imagenes/tortuga.png")    # [6]
        self.lion00_image = Image.open("imagenes/cria_leon.png")  # [7]
        self.meteoritos_2_image = Image.open("imagenes/meteorito2.png")    # alerta: La imagen del meteorito no se esta llamando , porque la imagen esta ya en una varible ,en la parte que se especifca el fondo :y la razo que funcione el metorito es porque usas esa variable para mostrar la imagen
        self.ciervo_image = Image.open("imagenes/ciervo.png")     # [8]
        self.antilopes_image = Image.open("imagenes/antilope.png")  # [9]
        self.bufalo_image = Image.open("imagenes/bufalo.png")       # [10]
        self.Tumba = Image.open("imagenes/muerto.png") # [11]  # Imagen cuando el animal muere
 
        # Redimebufalo_imagensionar imágenes de animales
        self.lion_image = self.lion_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.jirafa_image = self.jirafa_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.hiena_image = self.hiena_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.gacela_image = self.gacela_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.rinoceronte_image = self.rinoceronte_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.elefante_image = self.elefante_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.tortuga_image = self.tortuga_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.lion00_image = self.lion00_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.meteoritos_2_image = self.meteoritos_2_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)  # alerta :La imagen del meteorito no se esta llamando , porque la imagen esta ya en una varible ,en la parte que se especifca el fondo :y la razo que funcione el metorito es porque usas esa variable para mostrar la imagen
        self.ciervo_image = self.ciervo_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS) 
        self.antilopes_image = self.antilopes_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS) 
        self.bufalo_image = self.bufalo_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS) 
        self.TumbaTumba = self.Tumba.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS) 

        # Convertir imágenes a formato Tkinter
        self.lion_image = ImageTk.PhotoImage(self.lion_image)
        self.jirafa_image = ImageTk.PhotoImage(self.jirafa_image)
        self.hiena_image = ImageTk.PhotoImage(self.hiena_image)
        self.gacela_image = ImageTk.PhotoImage(self.gacela_image)
        self.rinoceronte_image = ImageTk.PhotoImage(self.rinoceronte_image)
        self.elefante_image = ImageTk.PhotoImage(self.elefante_image)
        self.tortuga_image = ImageTk.PhotoImage(self.tortuga_image)
        self.lion00_image = ImageTk.PhotoImage(self.lion00_image)
        self.meteoritos_2_image = ImageTk.PhotoImage(self.meteoritos_2_image) # alerta :La imagen del meteorito no se esta llamando , porque la imagen esta ya en una varible ,en la parte que se especifca el fondo :y la razo que funcione el metorito es porque usas esa variable para mostrar la imagen
        self.ciervo_image = ImageTk.PhotoImage(self.ciervo_image)
        self.antilopes_image = ImageTk.PhotoImage(self.antilopes_image)
        self.bufalo_image = ImageTk.PhotoImage(self.bufalo_image)
        self.Tumba = ImageTk.PhotoImage(self.Tumba)
        # Añadir las imagenes a una lista 
        Animal = [self.lion_image, self.hiena_image,self.jirafa_image, self.gacela_image, self.rinoceronte_image, self.elefante_image, self.tortuga_image, self.lion00_image,self.ciervo_image,self.antilopes_image,self.bufalo_image,self.Tumba]
        # Retornar la lista 
        return Animal
    
    def Cargar_Imagenes_Plantas(self):
        # Cargar imagenes
        self.manzano_image = Image.open("Plantas/arbol.png")       # [0]
        self.arbol_image = Image.open("Plantas/arbol_rojo.png")    # [1]
        self.arbusto_image = Image.open("Plantas/arbusto.png")     # [2]
        self.helechon_image = Image.open("Plantas/helechos.png")   # [3]
        self.cactus_image = Image.open("Plantas/cactus.png")       # [4]

        # Redimebufalo_imagensionar imágenes de animales
        self.manzano_image = self.manzano_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.arbol_image = self.arbol_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.arbusto_image = self.arbusto_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.helechon_image = self.helechon_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.cactus_image = self.cactus_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)

        # Convertir imágenes a formato Tkinter
        self.manzano_image = ImageTk.PhotoImage(self.manzano_image)
        self.arbol_image = ImageTk.PhotoImage(self.arbol_image)
        self.arbusto_image = ImageTk.PhotoImage(self.arbusto_image)
        self.helechon_image = ImageTk.PhotoImage(self.helechon_image)
        self.cactus_image = ImageTk.PhotoImage(self.cactus_image)

        # Arrreglo para plantas
        Plantas_list  = [self.manzano_image,self.arbol_image,self.arbusto_image,self.helechon_image,self.cactus_image]
        return Plantas_list 
    

    def Inicializar_Plantas(self):
        Plantas_list = self.Cargar_Imagenes_Plantas()
        fondo_Tierra = []
        fondo_Pasto = []
        fondo_Agua = []
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if self.mapa_numerico[fila][columna] == 0:
                    posicion = [fila,columna]
                    fondo_Agua.append(posicion)
                elif self.mapa_numerico[fila][columna] == 1:
                    posicion = [fila,columna]
                    fondo_Pasto.append(posicion)
                elif self.mapa_numerico[fila][columna] == 2:
                    posicion = [fila,columna]
                    fondo_Tierra.append(posicion)

        self.manzana = Planta('Manzano','Planta',choice(fondo_Pasto),100,100,0,10,100,Plantas_list[0])  # Manzano
        self.arbol =   Planta('Arbol','Planta',choice(fondo_Pasto),100,100,0,100,100,Plantas_list[1])   # Arbol
        self.arbusto = Planta('Arbusto','Planta',choice(fondo_Pasto),100,100,0,100,100,Plantas_list[2]) # arbusto
        self.helechon =Planta('Helechon','Planta',choice(fondo_Pasto),100,100,0,100,100,Plantas_list[3])# helechom
        self.cactus =  Planta('Cactus','Planta',choice(fondo_Tierra),100,100,0,100,100,Plantas_list[4]) # cactus

        self.canvas.create_image(self.manzana.ubicacion[0]*25,self.manzana.ubicacion[1]*25, anchor=tk.NW, image=self.manzana.Image_Planta, tags=self.manzana.nombre) 
        self.canvas.create_image(self.arbol.ubicacion[0]*25,self.arbol.ubicacion[1]*25, anchor=tk.NW, image=self.arbol.Image_Planta, tags=self.arbol.nombre) 
        self.canvas.create_image(self.arbusto.ubicacion[0]*25,self.arbusto.ubicacion[1]*25, anchor=tk.NW, image=self.arbusto.Image_Planta, tags=self.arbusto.nombre) 
        self.canvas.create_image(self.helechon.ubicacion[0]*25,self.helechon.ubicacion[1]*25, anchor=tk.NW, image=self.helechon.Image_Planta, tags=self.helechon.nombre) 
        self.canvas.create_image(self.cactus.ubicacion[0]*25,self.cactus.ubicacion[1]*25, anchor=tk.NW, image=self.cactus.Image_Planta, tags=self.cactus.nombre)

    def Mostrar_Animales(self):
        Animal = self.Cargar_Imagenes_ANIMALES()
        for animal,tipo_animal in self.Lista_Animales.items():
            Tipo_animal = self.Lista_Animales[animal]
            if 'vivo' == Tipo_animal.estado:
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
                elif 'ciervo' in  Tipo_animal.nombre:
                    Tipo_animal.Imagen_Animal = Animal[8]
                elif 'antilopes' in  Tipo_animal.nombre:
                    Tipo_animal.Imagen_Animal = Animal[9]
                elif 'bufalo' in  Tipo_animal.nombre:
                    Tipo_animal.Imagen_Animal = Animal[10]
            else:
                Tipo_animal.Imagen_Animal = Animal[11]
                
            Tipo_animal.Prueba(self.canvas)
            Tipo_animal.mostrar_imagen()
    def cria_2(self):
        self.canvas.delete('Leon777')


    def desaparecer_animales(self):
        if not self.proceso_diluvio:
            self.canvas.delete("leon373", "leon", "hiena", "jirafa", "gacela", "rinoceronte", "elefante", "tortuga", "Leon777")


    def Animales_Desplazandose(self):
        self.canvas.delete("leon373","leon","hiena", "jirafa", "gacela", "rinoceronte", "elefante", "tortuga","ciervo","antilopes","bufalo")
        
        for animal,tipo_animal in self.Lista_Animales.items():
            Tipo_animal = self.Lista_Animales[animal]
            if Tipo_animal.estado == "vivo":
                Tipo_animal.ubicacion = Tipo_animal.animal_Moviendose(Tipo_animal.nombre ,Tipo_animal.ubicacion ,Tipo_animal.Direccion )
                self.registrar_movimiento(Tipo_animal.nombre,Tipo_animal.ubicacion)
                if Tipo_animal.nivel_hambre <= 90:
                    self.Encontrar_Animal_Cerca(Tipo_animal)
        self.Mostrar_Animales()
            
        self.after(300,self.Animales_Desplazandose)


    def Encontrar_Animal_Cerca(self,Depredador):
        Animal_encontrado = [self.Lista_Animales[animal] for animal,tipo_a in self.Lista_Animales.items() if (self.Lista_Animales[animal].ubicacion[0])+ 25 == Depredador.ubicacion[0] or (self.Lista_Animales[animal].ubicacion[1])+25 == Depredador.ubicacion[1]]
        if len(Animal_encontrado) >= 1:
            Animal_encontrado = choice(Animal_encontrado)
            if Animal_encontrado.estado == 'vivo':
                if Animal_encontrado.especie == "Hervivoro" and Depredador.especie == "Carnivoro" :
                    Depredador.Comer()
                    Animal_encontrado.Daño()
                    if Animal_encontrado.vida <= 0:
                        self.Prueba_muerte(Animal_encontrado,"Comido")


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
