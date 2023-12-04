import logging

# Configurar el sistema de registro
logging.basicConfig(filename='prueba.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Ejemplos de mensajes de registro
logging.info("Inicio del programa")
logging.debug("Este es un mensaje de depuración")
logging.info("Esta es una información general")
logging.warning("¡Cuidado! Esto es una advertencia")
logging.error("Ha ocurrido un error")
logging.critical("Esto es crítico, el programa podría no funcionar correctamente")

