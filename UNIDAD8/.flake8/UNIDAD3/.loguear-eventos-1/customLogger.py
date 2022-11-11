# Importo logger
import logging

# Creo uno personalizado
logger = logging.getLogger(__name__)

# Creo handlers
warning_handler = logging.StreamHandler()
error_handler = logging.FileHandler('./logs/app.txt', mode='w')

# Declaro nivel de severidad de cada handler
warning_handler.setLevel(logging.WARNING)
error_handler.setLevel(logging.ERROR)

# Declaro format y agrego a handler
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
warning_handler.setFormatter(c_format)
error_handler.setFormatter(f_format)

# Agrego handler a logger
logger.addHandler(warning_handler)
logger.addHandler(error_handler)

logger.warning("Esto es un warning")
logger.error("Esto es un error")