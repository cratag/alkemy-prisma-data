### Usando Decouple

# from decouple import config

# print('Host: {HOST} - User: {USER} - Password: {PASSWORD} - Database: {DB}'.format(
#     HOST=config('MYSQL_HOST'),
#     USER=config('MYSQL_USER'),
#     PASSWORD=config('MYSQL_PWD'),
#     DB=config('MYSQL_DB')))


### Usando Dotenv

import os # Importo el sistema operativo
from dotenv import load_dotenv, find_dotenv
load_dotenv (find_dotenv('./.env')) # Declaro la ruta relativa aunque si hubiera estado vacío, lo hubiera encontrado automáticamente.

print('Host: {HOST} - User: {USER} - Password: {PASSWORD} - Database: {DB}'.format(
    HOST=os.getenv('MYSQL_HOST'),
    USER=os.getenv('MYSQL_USER'),
    PASSWORD=os.getenv('MYSQL_PWD'),
    DB=os.getenv('MYSQL_DB')))