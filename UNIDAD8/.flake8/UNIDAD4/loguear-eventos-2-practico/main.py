import logging
import logging.config
import functions

# Importo la configuración de logger desde archivo.
logging.config.fileConfig(fname='log_config_file.conf')

# Declaro el logger para usar en este contexto.
logger = logging.getLogger('mainLogger')

def open_file(archivo):
    logger.info("...Leyendo el archivo...")
    try:
        logger.info("...Archivo procesado...")
        file = open(archivo, 'r')
        return file
    except OSError as e:
        return logger.critical("No se pudo abrir el archivo")

# Declaro la variable 'cuento' con el nombre de archivo a leer.
cuento = 'cuento.txt'

# Cuento líneas y caracteres.
functions.count_lines_and_characters(open_file(cuento), cuento)
