import logging

# Warning - a consola.
logging.basicConfig(
    datefmt = '%d-%b-%y %H:%M:%S',
    format = '%(name)s - %(levelname)s - %(message)s',
)

logging.warning("Este es un warning que sale por consola.")