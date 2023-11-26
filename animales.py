
# Clases Principales
# ● Organismo: Base para cualquier entidad viviente con propiedades como posición,
# vida, energía, y velocidad.
# ● Animal: Hereda de Organismo, con acciones como cazar y atributos particulares
# como especies y dieta. Nota: #*Mínimo 10
# ● Planta: Hereda de Organismo, especializada en interacciones como fotosíntesis y
# reproducción por semillas. Nota:#* Mínimo 5
# ● Ambiente: Representa factores abióticos y eventos climáticos que afectan al
# ecosistema. Nota: #*Mínimo 3
# ● Ecosistema: Gestiona el ciclo de vida global, las interacciones entre Organismos y el
# mantenimiento del equilibrio ecológico.

class Organismo:
    def __init__(self, posicion, vida=100, energia=100, velocidad=0, nombre="", especie="", dieta="", altura=0):
        self.posicion = posicion
        self.vida = vida
        self.energia = energia
        self.velocidad = velocidad
        self.nombre = nombre
        self.especie = especie
        self.dieta = dieta
        self.altura = altura

    def mover(self):
        self.posicion += self.velocidad

    def comer(self):
        self.energia += 30

    def dormir(self):
        self.energia += 50

    def reproducir(self):
        return self

class Leon(Organismo):
    def __init__(self, posicion, nombre="", especie="", dieta=""):
        super().__init__(posicion, nombre=nombre, especie=especie, dieta=dieta)
        self.velocidad = 20

    def cazar(self):
        self.energia -= 20
        self.velocidad += 8

    def comer(self):
        self.energia += 30

    def dormir(self):
        self.energia += 50

class Jirafa(Organismo):
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

class Cebras(Organismo):
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

class Rinoceronte(Organismo):
    def __init__(self, posicion, nombre="", especie="", dieta=""):
        super().__init__(posicion, nombre=nombre, especie=especie, dieta=dieta)
        self.velocidad = 15
        self.vida = 150

    def comer(self):
        self.energia += 30

    def dormir(self):
        self.energia += 50        

class MambaNegra(Organismo):
    def __init__(self, posicion, nombre="", especie="", dieta=""):
        super().__init__(posicion, nombre=nombre, especie=especie, dieta=dieta)
        self.velocidad = 10
        self.vida = 100

    def cazar(self):
        self.energia -= 20
        self.velocidad += 2

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
        
class Elefante(Organismo):
    def __init__(self, posicion, nombre="", especie="", dieta=""):
        super().__init__(posicion, nombre=nombre, especie=especie, dieta=dieta)
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
    
class Peces(Organismo):
    def __init__(self, posicion, nombre="", especie="", dieta=""):
        super().__init__(posicion, nombre=nombre, especie=especie, dieta=dieta)
        self.velocidad = 15
        self.vida = 5

    def comer(self):
        self.energia += 30

    def nadar(self):
        self.energia -= 20
        self.velocidad += 10

        
class arbol(Organismo):
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
        
class arbusto(Organismo):
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
        
class pasto(Organismo):
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
        
class flores(Organismo):
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
        
class frutos(Organismo):
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

class raices(Organismo):
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
              
class hongos(Organismo):
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
    def __init__(self, nombre, Organismos, ambiente):
        self.nombre = nombre
        self.Organismos = Organismos
        self.ambiente = ambiente
        
                