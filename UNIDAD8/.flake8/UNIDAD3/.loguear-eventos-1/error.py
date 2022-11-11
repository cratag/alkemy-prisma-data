import logging

# Error - a consola y file.
logging.basicConfig(
    datefmt = '%d-%b-%y %H:%M:%S',
    filename = './logs/errors.txt',
    filemode = 'w',
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

logging.error("Este es un error que sale por consola y se guarda en un archivo.")