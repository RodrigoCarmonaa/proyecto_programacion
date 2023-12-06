import logging

# Configurar el sistema de registro
logging.basicConfig(filename='prueba.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')

# Ejemplos de mensajes de registro
logging.info("Inicio del programa")
