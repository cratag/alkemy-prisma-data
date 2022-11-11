import logging
import logging.config

# Importo la configuración de logger desde archivo.
logging.config.fileConfig(fname='log_config_file.conf')

# Declaro el logger para usar en este contexto.
logger = logging.getLogger('functionsLogger')

def count_lines_and_characters(archivo, nombre_de_archivo):
    try:
        total_lines = sum(1 for line in archivo)
        logger.info(f'{nombre_de_archivo} - Cantidad de renglones: {total_lines}')
        
        archivo.seek(0) # Tuve que agregar .seek(0) porque al leer el archivo, el cursor se posa al final. Esto hace que las lineas subsiguientes sean "" - mientras que con .seek(0) vuelvo a posicionar el cursor al inicio. 
        count_characters(archivo)
    except Exception:
        logger.critical('No pudimos contar las lineas del archivo')
    
def count_characters(archivo):
    for idline, line in enumerate(archivo):
        words = line.split(" ")
        logger.info(f"Renglón {idline}: {len(words)} palabras")