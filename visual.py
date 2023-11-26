import PIL
import tkinter as tk
from PIL import Image, ImageTk

class organismo:
    def __init__(self, posicion, vida, energia, velocidad):
        self.posicion = posicion
        self.vida = vida
        self.energia = energia
        self.velocidad = velocidad
        
    def mover(self):
        nueva_posicion = self.posicion + self.velocidad
        self.posicion = nueva_posicion

    
    def comer(self):
        energia = self.energia + 1
        self.energia = energia

    
    def reproducir(self):
        return self
        

    def morir(self):
        vida = self.vida - 1
        self.vida = vida
        

class Leon(organismo):
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

class cebras(organismo):
    def __init__(self, posicion, vida, energia, velocidad, nombre, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad)
        self.nombre = nombre
        self.especie = especie
        self.dieta = dieta
        self.velocidad = 15
        self.vida = 100

    def huir(self):
        self.energia -= 20
        self.velocidad += 10

    def comer(self):
        self.energia += 30

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



class Ventana(tk.Tk):
    def __init__(self, filas, columnas, ancho_celda, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filas = filas
        self.columnas = columnas
        self.ancho_celda = ancho_celda
        self.lion_image = Image.open("leon.png")  # Cargar la imagen como un atributo de la clase
        self.crear_cuadricula()
        self.mostrar_leon()

    def crear_cuadricula(self):
        canvas = tk.Canvas(self, width=self.columnas * self.ancho_celda, height=self.filas * self.ancho_celda)
        canvas.pack()

        for i in range(1, self.filas):
            y = i * self.ancho_celda
            canvas.create_line(0, y, self.columnas * self.ancho_celda, y)

        for j in range(1, self.columnas):
            x = j * self.ancho_celda
            canvas.create_line(x, 0, x, self.filas * self.ancho_celda)

        self.canvas = canvas  # Guardar una referencia al canvas para su uso posterior

    def mostrar_leon(self):
        lion_image = self.lion_image.resize((self.ancho_celda, self.ancho_celda), PIL.Image.Resampling.LANCZOS)
        lion_image = ImageTk.PhotoImage(lion_image)
        x_posicion = 5 * self.ancho_celda
        y_posicion = 8 * self.ancho_celda
        self.canvas.create_image(x_posicion, y_posicion, anchor=tk.NW, image=lion_image)

        # Mantén una referencia a la imagen para evitar que sea eliminada por el recolector de basura
        self.lion_image = lion_image
        # Calcular la posición donde quieres colocar al león (por ejemplo, en la celda en la fila 2, columna 3)
        x_posicion = 5 * self.ancho_celda
        y_posicion = 8 * self.ancho_celda

        # Mostrar la imagen del león en el lienzo
        self.canvas.create_image(x_posicion, y_posicion, anchor=tk.NW, image=lion_image)

if __name__ == "__main__":
    ventana = Ventana(filas=15, columnas=15, ancho_celda=40)
    ventana.mainloop()

