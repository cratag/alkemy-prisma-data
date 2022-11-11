# Implementando Rotating File Hander
import logging
from logging.handlers import RotatingFileHandler

# Creamos el logger
logger = logging.getLogger('simple_logger')

# Establecemos el nivel de severidad
logger.setLevel(logging.DEBUG)

# Creamos un Rotating File Hander y seteamos el nivel de seguridad en el DEBUG
handler = RotatingFileHandler('my_log.log', maxBytes=2000, backupCount=50)
handler.setLevel(logging.DEBUG)

# Creamos un objeto de formato
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Agregamos el objeto formato al rotating file handler
handler.setFormatter(formatter)

# Agregamos al handler al logger
logger.addHandler(handler)

# Generamos los logs:
for i in range(10000):
    logger.debug('debug message{}'.format(i))
    logger.info('info message{}'.format(i))
    logger.warning('warning message{}'.format(i))
    logger.error('error message{}'.format(i))
    logger.critical('critical message{}'.format(i))
