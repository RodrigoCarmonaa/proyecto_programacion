Desarrollo de un Simulador de Ecosistemas mediante Programación Orientada a Objetos

Integrantes:
-
-Rodrigo Carmona

-Eduardo Escares


Introducción:

El presente informe detalla el desarrollo de un proyecto orientado a la creación de un Simulador de Ecosistemas mediante programación orientada a objetos. El objetivo principal es representar y manipular diversos biomas, como selvas, desiertos y bosques, utilizando una matriz para simular las interacciones entre la flora y fauna. Este enfoque proporciona un entorno dinámico y visualmente accesible, permitiendo comprender cómo los elementos de un ecosistema interactúan entre sí.

En resumen, el proyecto busca crear una herramienta interactiva que facilite la comprensión de las relaciones dentro de un ecosistema, desde organismos individuales hasta el entorno en su totalidad. El simulador proporciona la capacidad de ajustar variables ambientales y observar cómo estas influyen en la biodiversidad, las cadenas alimenticias y el equilibrio general del ecosistema.

**Descripción de las Clases y sus Métodos:**

*Organismo:*

La clase organismo actúa como una plantilla base (clase padre) que posibilita la creación de instancias específicas con atributos como posición, nivel de vida, energía y velocidad. Esta abstracción simplifica la creación de diversos tipos de seres vivos o elementos del ecosistema en el programa al compartir características comunes definidas en la clase base.

*Planta:*

Esta clase hereda de la clase base organismo y encapsula propiedades y funcionalidades específicas de las plantas en el contexto del simulador ecológico. Gestiona aspectos vitales como vida, energía y velocidad, y cuenta con métodos que controlan su crecimiento, supervivencia bajo condiciones de sequía, interacciones con consumidores y capacidad reproductiva.

*Animales:*

**Animal:** Clase base que representa a los animales en términos generales. Posee métodos para moverse aleatoriamente, buscar presas y fuentes de agua, alimentarse, beber y reproducirse. Controla el ciclo de vida del animal, gestionando su vida, energía, hambre, sed y capacidad de reproducción.

**Depredador:** Subclase de Animal centrada en la caza. Implementa métodos específicos para buscar y cazar presas, además de lógica para su ciclo de vida, incluyendo la disminución gradual de su vida y energía.

**Presa:** Otra subclase de Animal centrada en la evasión de depredadores. Posee métodos para huir de los depredadores y gestiona su ciclo de vida con la disminución gradual de su vida y energía.

Estas clases y sus métodos permiten simular interacciones realistas entre depredadores y presas dentro del ecosistema, modelando movimientos, búsqueda de comida y agua, así como su ciclo de vida.


La clase `Ventana` se encarga de gestionar la interfaz gráfica y la representación visual de la simulación del ecosistema. Aquí hay un resumen de las principales funciones y responsabilidades de la clase:

1. **Inicialización:**
   - La clase se inicializa con parámetros como el número de filas y columnas del tablero, y el ancho de cada celda.
   - Se cargan las imágenes de los animales y se establecen las posiciones iniciales y direcciones aleatorias de los mismos.

2. **Creación de la Cuadrícula:**
   - En el método `crear_cuadricula`, se genera la cuadrícula que servirá como el tablero visual para la simulación. Esta cuadrícula se crea usando la biblioteca Tkinter.

3. **Visualización de Animales:**
   - El método `mostrar_animales` se encarga de mostrar las imágenes de los animales en posiciones específicas en la cuadrícula. Antes de mostrarlas, las imágenes se redimensionan para adaptarse al tamaño de las celdas.

4. **Movimiento de Animales:**
   - La función `mover_animales` se ejecuta de forma continua en un bucle.
   - Elimina las instancias previas de los animales en la cuadrícula.
   - Llama al método `mover_animal_individual` para cada animal, actualizando su posición según su dirección actual y mostrando la imagen en la nueva posición.
   - La dirección de cada animal se elige aleatoriamente para su próximo movimiento.

5. **Método `mover_animal_individual`:**
   - Elimina la instancia previa del animal en la cuadrícula.
   - Calcula la nueva posición del animal según su dirección actual.
   - Verifica la validez de la nueva posición, ajustándola si es necesario.
   - Muestra la imagen del animal en la nueva posición.
   - Elige una nueva dirección aleatoria si la posición resulta ser inválida.

5. **mapa.py:**

    El algoritmo de ruido de Simplex crea números aleatorios para simular diferentes áreas en un mapa. Con esos números, puedes representar distintos tipos de lugares, como agua, tierra y pasto. El código  genera esos números y los convierte en colores para mostrarlos en un mapa e implementar a los animales en el mismo, para recrear un ecosistema


El log (archivo de registro) en este código se utiliza para registrar eventos significativos o información relevante durante la ejecución del programa. En este caso, se está utilizando el módulo de registro logging de Python para llevar un registro de los movimientos de los animales en el ecosistema simulado.

El log tiene varios propósitos:

Seguimiento de Eventos:

Cada vez que un animal se mueve, se registra un mensaje que incluye el nombre del animal y su nueva posición. Esto ayuda a rastrear cómo se mueven los animales a lo largo del tiempo.
Registro de Información:

Los mensajes de registro proporcionan información sobre el estado del programa en momentos clave. Por ejemplo, cuando un animal se mueve, se registra esa acción, lo que puede ser útil para el análisis y la depuración.
Depuración:

En caso de errores o comportamientos inesperados, el log puede ser una herramienta valiosa para depurar el programa. Al revisar el registro, puedes identificar qué acciones se llevaron a cabo antes de que ocurriera un problema.
Análisis Posterior:

Después de la ejecución del programa, el archivo de registro puede ser revisado para analizar el comportamiento de los animales a lo largo del tiempo y obtener información sobre cómo interactúan en el ecosistema simulado.
La configuración del registro se realiza al comienzo del código, donde se establece el formato del mensaje, el nivel de registro (DEBUG en este caso, que registra todos los eventos), y se especifica el archivo en el que se guardará el log (movimientos.log en este caso).

**Tkinter:**

Se utiliza la librería Tkinter de Python para crear una ventana que muestra una cuadrícula simulando un entorno o ecosistema. Los iconos que representan a los animales se mueven aleatoriamente en intervalos regulares de tiempo dentro de la cuadrícula. El código se organiza en una clase llamada Ventana, encargada de manejar la interfaz gráfica y el movimiento de los animales en el ecosistema simulado.

La clase Ventana incluye métodos para crear la cuadrícula, mostrar imágenes de los animales en posiciones específicas y mover a los animales de manera aleatoria. La interfaz gráfica puede adaptarse para mostrar la interacción entre animales y plantas, representando su comportamiento y las dinámicas del ecosistema simulado.

La función principal `__main__` instancia un objeto de la clase Ventana con parámetros específicos (número de filas, columnas y ancho de las celdas) y ejecuta el bucle principal para mostrar y actualizar la ventana gráfica.

En conclusión, el proyecto ofrece una herramienta versátil para comprender y visualizar dinámicas ecológicas, permitiendo ajustes ambientales y observando sus efectos en la biodiversidad y el equilibrio general del ecosistema.
