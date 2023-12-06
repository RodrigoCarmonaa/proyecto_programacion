from opensimplex import OpenSimplex
import tkinter as tk
from PIL import Image, ImageTk
from random import choice, randint
import random
import logging
# -- coding: utf-8 --

# Configurar el sistema de registro
logging.basicConfig(filename='prueba.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#####################################################################
#                           organismos 
#####################################################################
class Organismo:
    def _init_(self, nombre, ubicacion, vida, energia, velocidad):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.vida = vida
        self.energia = energia
        self.velocidad = velocidad
#####################################################################
#                           PLANTA
#####################################################################
class Planta(Organismo):
    def _init_(self, nombre, tipo, ubicacion, vida, energia, velocidad, ciclo_vida, tiempo_sin_agua):
        super()._init_(nombre, ubicacion, vida, energia, velocidad)
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

    def _init_(self,nombre,ubicacion,vida_hp, energia, velocidad,Imagen_Animal,especie, Sexo, edad, Alimentacion,Direccion):
        super()._init_(nombre, ubicacion, vida_hp, energia, velocidad)
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
        

#####################################################################
#                           AMBIENTE
#####################################################################
class Ambiente:
    def _init_(self):
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
    def _init_(self, temperatura, estacion_seca, estacion_lluvia, vegetacion, fauna):
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
    def _init_(self):
        self.organismos = []
        self.ambiente = []

    def ciclo_global(self):
        pass
#####################################################################
#                           MOTOR DE EVENTOS
#####################################################################
#####################################################################
    
#####################################################################
#                           VENTANA
#####################################################################
class Ventana(tk.Tk):
    def _init_(self, filas, columnas, ancho_celda, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self.filas = filas
        self.columnas = columnas
        self.ancho_celda = ancho_celda
        self.mapa_numerico = mapa_numerico
        
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

        self.crear_cuadricula()
        self.crear_fondo()
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
        boton_meteorito = tk.Button(frame1, text="Generar Meteorito")
        boton_terremoto = tk.Button(frame1, text="Generar Terremor") 
        boton_Estado = tk.Button(frame1, text="Mostrar estado actual")  
        boton_Otro_evento = tk.Button(frame1, text="Otro evento")  
        boton_Estado.place(x=35,y=0,width="150")   
        boton_terremoto.place(x=35,y=50,width="150")  
        boton_meteorito.place(x=35,y=100,width="150")   
        boton_Otro_evento.place(x=35,y=150,width="150")  
#--------------------------------------------------
# Animal: 
#-------------------------------------------------
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
        self.Mostrar_Animales()
        self.Animales_Desplazandose()

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
        # canvas.pack()
        canvas.place(x=45,y=5)

        for i in range(1, self.filas):
            y = i * self.ancho_celda
            canvas.create_line(0, y, self.columnas * self.ancho_celda, y)

        for j in range(1, self.columnas):
            x = j * self.ancho_celda
            canvas.create_line(x, 0, x, self.filas * self.ancho_celda)

        self.canvas = canvas  # Guardar una referencia al canvas para su uso posterior
    
    def Cargar_Imagenes_ANIMALES(self):
        # Cargar imágenes de animales
        self.lion_image = Image.open("imagenes/leon.png")            # [0]
        self.jirafa_image = Image.open("imagenes/jirafa.png")        # [1]
        self.hiena_image = Image.open("imagenes/hiena.png")          # [2]
        self.gacela_image = Image.open("imagenes/gacela.png")        # [3]
        self.rinoceronte_image = Image.open("imagenes/rinoceronte.png") # [4]
        self.elefante_image = Image.open("imagenes/elefante.png")  # [5]
        self.tortuga_image = Image.open("imagenes/tortuga.png")    # [6]
        #-------------------------------------------------------------
        self.lion00_image = Image.open("imagenes/cria_leon.png")  # [7]
 
        # Redimensionar imágenes de animales
        self.lion_image = self.lion_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.jirafa_image = self.jirafa_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.hiena_image = self.hiena_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.gacela_image = self.gacela_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.rinoceronte_image = self.rinoceronte_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.elefante_image = self.elefante_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        self.tortuga_image = self.tortuga_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)
        #----------------------------------------------------------------
        self.lion00_image = self.lion00_image.resize((self.ancho_celda, self.ancho_celda), Image.LANCZOS)

        # Convertir imágenes a formato Tkinter
        self.lion_image = ImageTk.PhotoImage(self.lion_image)
        self.jirafa_image = ImageTk.PhotoImage(self.jirafa_image)
        self.hiena_image = ImageTk.PhotoImage(self.hiena_image)
        self.gacela_image = ImageTk.PhotoImage(self.gacela_image)
        self.rinoceronte_image = ImageTk.PhotoImage(self.rinoceronte_image)
        self.elefante_image = ImageTk.PhotoImage(self.elefante_image)
        self.tortuga_image = ImageTk.PhotoImage(self.tortuga_image)
        #---------------------------------------------------------
        self.lion00_image = ImageTk.PhotoImage(self.lion00_image)
        # Añadir las imagenes a una lista 
        Animal = [self.lion_image, self.hiena_image,self.jirafa_image, self.gacela_image, self.rinoceronte_image, self.elefante_image, self.tortuga_image, self.lion00_image]
        # Retornar la lista 
        return Animal
  
    def Mostrar_Animales(self):
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

if __name__ == "_main_":
    ventana = Ventana(filas=27, columnas= 35, ancho_celda=25)
    ventana.geometry("1190x675") # RAA
    ventana.config(bg="black")
    ventana.mainloop()