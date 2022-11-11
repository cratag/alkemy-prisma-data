DROP DATABASE IF EXISTS ejercicio; 
CREATE DATABASE ejercicio;
USE ejercicio;

CREATE TABLE alumnos(legajo INT PRIMARY KEY, nombre VARCHAR(45) NOT NULL, apellido VARCHAR(45) NOT NULL, fecha_nacimiento DATETIME);
CREATE TABLE materias(codigo INT PRIMARY KEY, descripcion VARCHAR(45));
CREATE TABLE cursadas(legajo INT PRIMARY KEY, codigo_materia INT FOREIGN KEY REFERENCES materias (codigo));

INSERT INTO alumnos VALUES (1, 'Manuel', 'Faner', '2022-04-22 10:34:23'), (2, 'Pepe', 'Queseyo', '2012-03-22 10:34:23'), (3, 'Mauro', 'Faner', '2000-04-12 10:34:23'), (4, 'Jorge', 'Apellidosky', '2010-01-02 10:34:23'), (5, 'Melisa', 'Bolsa', '1995-04-02 11:34:23');

INSERT INTO materias VALUES (1, 'Geografia'), (2, 'Matematica'), (3, 'Lengua'), (4, 'Astronomia'), (5, 'Historia');

INSERT INTO cursadas VALUES (1, 1), (2, 3), (3, 2), (4, 5), (5, 4);