
# Clases Principales
# ● Organismo: Base para cualquier entidad viviente con propiedades como posición,
# vida, energía, y velocidad.
# ● Animal: Hereda de Organismo, con acciones como cazar y atributos particulares
# como especies y dieta. Nota: #*Mínimo 10
# ● Planta: Hereda de Organismo, especializada en interacciones como fotosíntesis y
# reproducción por semillas. Nota:#* Mínimo 5
# ● Ambiente: Representa factores abióticos y eventos climáticos que afectan al
# ecosistema. Nota: #*Mínimo 3
# ● Ecosistema: Gestiona el ciclo de vida global, las interacciones entre organismos y el
# mantenimiento del equilibrio ecológico.

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
        
                