import logging

fruits = ['Frutilla','Melón','PERA',99.6,'NaranJA', 'mORa', 'NisPERo',99]
logging.basicConfig(
    level = logging.INFO,
    filename = "main.log",
    filemode = 'w',
    datefmt = '%d-%b-%y %H:%M:%S',
    format = '%(asctime)s - %(levelname)s - %(message)s'
)
for i in fruits:
    try:
        logging.info(f"Conversión exitosa: {i} ---> {i.lower()}")
    except Exception as e:
        logging.error(f"Conversión fallida: {i}")