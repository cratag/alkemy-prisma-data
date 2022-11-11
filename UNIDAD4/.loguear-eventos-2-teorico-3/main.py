# Usando TimedRotatingFileHandler
import logging
from logging.handlers import TimedRotatingFileHandler

# Creamos el logger
logger = logging.getLogger('simple_logger')

# Estabelcemos nivel de severidad
logger.setLevel(logging.DEBUG)

# Creamos un Time Rotating File Handler y seteamos el nivel de severidad en DEBUG
handler = TimedRotatingFileHandler('Time_Log_test.log',
                                    when='S', # Determina SEGUNDOS
                                    interval=2,
                                    backupCount=50)
handler.setLevel(logging.DEBUG)

# Creamos un objeto de formato
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Agregamos el objeto formato al rotating file handler
handler.setFormatter(formatter)

# Agregamos el handler al logger
logger.addHandler(handler)

# Generamos los logs: 
for i in range(10000):
    logger.debug('debug message{}'.format(i))
    logger.info('info message{}'.format(i))
    logger.warning('warning message{}'.format(i))
    logger.error('error message{}'.format(i))
    logger.critical('critical message{}'.format(i))