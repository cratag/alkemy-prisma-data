```python
# http://winterolympicsmedals.com/medals.csv

"""
1. Conectarse a la url que contiene el archivo CSV de medallas olímpicas.
2. Descargar los datos y obtener un sub dataset que contenga a
todas las medallas de oro (Gold) Estados Unidos (USA) a partir del año 1950.
3. Crear una base de datos “olympics” en SQLite y la tabla “medals”.
4. Guardar en la base de datos. los datos generados en el sub dataset.
5. Consultar la base de datos y validar que los datos se hayan cargado correctamente.
"""
```




    '\n1. Conectarse a la url que contiene el archivo CSV de medallas olímpicas.\n2. Descargar los datos y obtener un sub dataset que contenga a\ntodas las medallas de oro (Gold) Estados Unidos (USA) a partir del año 1950.\n3. Crear una base de datos “olympics” en SQLite y la tabla “medals”.\n4. Guardar en la base de datos. los datos generados en el sub dataset.\n5. Consultar la base de datos y validar que los datos se hayan cargado correctamente.\n'




```python
import sqlite3
import pandas as pd
import pdb

df = pd.read_csv('http://winterolympicsmedals.com/medals.csv')
# Filtramos por medallas 'Gold' de 'USA' y año igual o mayor a 1950.
sub_df = df.loc[(df['Medal'] == 'Gold') & (df['NOC'] == 'USA') & (df['Year'] >= 1950)]
```


```python
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

```


```python
# Insertamos los datos desde el DF
sub_df.to_sql(name='medals', con=conn, if_exists='replace', index = False)
```




    65




```python
# Verificamos que se hayan cargado correctamente
query = "SELECT * FROM medals"
data = pd.read_sql(query, con=conn)
print(data)
```

        Year               City    Sport      Discipline  NOC            Event  \
    0   1952               Oslo  Skating  Figure skating  USA       individual   
    1   1952               Oslo  Skating   Speed skating  USA             500m   
    2   1952               Oslo   Skiing   Alpine Skiing  USA     giant slalom   
    3   1952               Oslo   Skiing   Alpine Skiing  USA           slalom   
    4   1956  Cortina d'Ampezzo  Skating  Figure skating  USA       individual   
    ..   ...                ...      ...             ...  ...              ...   
    60  2006              Turin   Skiing   Alpine Skiing  USA  Alpine combined   
    61  2006              Turin   Skiing   Alpine Skiing  USA     giant slalom   
    62  2006              Turin   Skiing       Snowboard  USA        Half-pipe   
    63  2006              Turin   Skiing       Snowboard  USA        Half-pipe   
    64  2006              Turin   Skiing       Snowboard  USA  Snowboard Cross   
    
       Event gender Medal  
    0             M  Gold  
    1             M  Gold  
    2             W  Gold  
    3             W  Gold  
    4             M  Gold  
    ..          ...   ...  
    60            M  Gold  
    61            W  Gold  
    62            M  Gold  
    63            W  Gold  
    64            M  Gold  
    
    [65 rows x 8 columns]

