# proyecto_programacion

Integrantes:
-
-Rodrigo Carmona

-Eduardo Escares



Introducción: 

El proyecto consiste en desarrollar un Simulador de Ecosistemas mediante la programación orientada a objetos. Este simulador busca representar y manipular distintos biomas, como selvas, desiertos y bosques, utilizando una matriz para simular interacciones entre la flora y fauna en un entorno dinámico y visualmente accesible.

En resumen, el proyecto propone crear una herramienta interactiva que permita comprender cómo los elementos de un ecosistema interactúan entre sí, desde organismos individuales hasta su entorno. El simulador ofrece la capacidad de ajustar variables ambientales y observar cómo influyen en la biodiversidad, las cadenas alimenticias y el equilibrio general del ecosistema.


Descripción de las clases y sus métodos:

Organismo:

La clase organismo se comporta como una plantilla base, permitiendo la creación de instancias específicas con atributos como posición, nivel de vida, energía y velocidad. Esto simplifica la creación de diversos tipos de seres vivos o elementos del ecosistema en el programa, ya que comparten estas características comunes definidas en la clase.(Clase padre)

Planta: 

Esta clase hereda de la clase base organismo, encapsula las propiedades y funcionalidades específicas de las plantas en el contexto del simulador ecológico. Está diseñada para gestionar aspectos vitales como vida, energía, y velocidad, y tiene métodos que controlan su crecimiento, supervivencia bajo condiciones de sequía, interacciones con consumidores (animales que las comen), y su capacidad reproductiva.

Animales:

Animal: Esta clase base representa a los animales en términos generales. Posee métodos para moverse aleatoriamente, buscar presas y fuentes de agua, alimentarse, beber y reproducirse. También controla el ciclo de vida del animal, gestionando su vida, energía, hambre, sed y la capacidad de reproducción.

Depredador: Una subclase de Animal que se enfoca en la caza. Implementa métodos específicos para buscar y cazar presas. Además, incluye una lógica para su ciclo de vida, que puede involucrar la disminución gradual de su vida y energía.

Presa: Otra subclase de Animal que se enfoca en la evasión de los depredadores. Posee métodos para huir de los depredadores y también gestiona su ciclo de vida, con la disminución gradual de su vida y energía.

Estas clases y sus métodos permiten simular interacciones realistas entre depredadores y presas dentro del ecosistema, modelando movimientos, búsqueda de comida y agua, así como su ciclo de vida.

Tkinter 

Utilizando la librería Tkinter de Python. Se crea una  ventana muestra una cuadrícula que simula un entorno o ecosistema donde se mueven iconos representando a los animales, los animales se desplazan de manera aleatoria dentro de la cuadrícula, cambiando su posición en intervalos regulares de tiempo.

EL código se organiza en una clase llamada Ventana, que se encarga de manejar la interfaz gráfica y el movimiento de los animales en un ecosistema simulado. Esta clase incluye métodos para crear la cuadrícula que representa el entorno del ecosistema, mostrar las imágenes de los animales (como leones, jirafas, hienas, entre otros) en posiciones específicas y mover a estos animales de manera aleatoria en la cuadrícula simulada. Además, es posible adaptar el código para mostrar la interacción entre los animales y las plantas, representando su comportamiento y las interacciones dentro de este ecosistema simulado.

La función principal __main__ instancia un objeto de la clase Ventana con parámetros específicos (número de filas, columnas y ancho de las celdas) y ejecuta el bucle principal para mostrar y actualizar la ventana gráfica.