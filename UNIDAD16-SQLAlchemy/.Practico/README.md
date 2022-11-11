# 16 - Acceso a Bases de Datos

Conexión a base de datos. Utilización de Modulo SQLALCHEMY en Python. Creación de clases y métodos básicos.

## Installation
Primero hay que crear la base de datos PostgreSQL siguiendo las indicaciones de la [practica de la UNIDAD 16](https://drive.google.com/file/d/1zV_S7UYJdOBzq_u7CejZf4TDTdAetC72/view).

Luego se activa el entorno virtual entrando al directorio principal **./Practico** y correr el siguiente comando para activar el entorno virtual:

```python
source bin/activate
```

Luego instalar las dependencias para el entorno:

```python
pip install -r requirements.txt
```


## Usage

El archivo `database.py` llama por defecto al método `Database().fetchAllUsers()`. 
Por tanto, mediante consola en el directorio root podemos correr:
```python
python database.py
```

Lo cual devuelve un objeto de visualización de todas las filas de la tabla `Customer`

## To Do
Corregir la clase Session e implementar los últimos metodos del punto 3 de la [practica de la UNIDAD 16](https://drive.google.com/file/d/1zV_S7UYJdOBzq_u7CejZf4TDTdAetC72/view): `saveData`, `updateCustomer`, `deleteCustomer`