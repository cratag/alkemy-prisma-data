# http://winterolympicsmedals.com/medals.csv

"""
1. Conectarse a la url que contiene el archivo CSV de medallas olímpicas.
2. Descargar los datos y obtener un sub dataset que contenga a
todas las medallas de oro (Gold) Estados Unidos (USA) a partir del año 1950.
3. Crear una base de datos “olympics” en SQLite y la tabla “medals”.
4. Guardar en la base de datos. los datos generados en el sub dataset.
5. Consultar la base de datos y validar que los datos se hayan cargado correctamente.
"""

import sqlite3
import pandas as pd
import pdb


df = pd.read_csv('./medals.csv')
# Filtramos por medallas 'Gold' de 'USA' y año igual o mayor a 1950.
sub_df = df.loc[(df['Medal'] == 'Gold') & (df['NOC'] == 'USA') & (df['Year'] >= 1950)]

# Conectamos a la DB y seteamos la query de creación de tabla
conn = sqlite3.connect('olympics.db')
cursor = conn.cursor()

query = """CREATE TABLE IF NOT EXISTS medals (
            id INTEGER,
            Year INTEGER,
            City TEXT,
            Sport TEXT,
            Discipline TEXT,
            NOC TEXT,
            Event TEXT,
            'Event gender' TEXT,
            Medal TEXT
            )"""
conn.commit()

# Insertamos los datos desde el DF
sub_df.to_sql(name='medals', con=conn, if_exists='replace', index = False)

# Verificamos que se hayan cargado correctamente
query = "SELECT * FROM medals"
data = pd.read_sql(query, con=conn)
print(data)