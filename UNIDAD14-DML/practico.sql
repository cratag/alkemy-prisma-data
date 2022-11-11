-- Listar los nombres de los proveedores cuya ciudad contenga
-- la cadena de texto “Ramos”.

SELECT * FROM Proveedor WHERE Ciudad LIKE '%Ramos%'
----------------------------------------------------------------

-- Listar los códigos de los materiales que provea el proveedor 4
--y no los provea el proveedor 5. Se debe resolver de 3 formas.

SELECT CodMat FROM Provisto_por WHERE CodProv = 4 AND CodMat NOT IN (SELECT CodMat FROM Provisto_por WHERE CodProv = 5)
SELECT CodMat FROM Provisto_por
SELECT CodMat FROM Provisto_por WHERE CodProv = 4 EXCEPT SELECT CodMat FROM Provisto_por WHERE CodProv = 5

----------------------------------------------------------------

-- Listar los materiales, código y descripción, provistos por
--proveedores de la ciudad de Ramos Mejía.

SELECT * FROM Material IN (SELECT CodMat FROM Provisto_Por WHERE CodProv = (SELECT CodProv FROM Proveedor WHERE Ciudad = 'Ramos
-- Mejía'))

-- El proveedor de Ramos Mejia no provee nada...

----------------------------------------------------------------

-- Listar los proveedores y materiales que provee. La lista
-- resultante debe incluir a aquellos proveedores que no proveen
-- ningún material.

SELECT p.*, pp.CodMat, m.* FROM Proveedor p LEFT JOIN Provisto_Por pp on p.CodProv=pp.CodProv LEFT JOIN Material m on pp.CodMat=m.CodMat  
----------------------------------------------------------------

-- Listar los artículos que cuesten más de $30 o que estén
-- compuestos por el material 2.

SELECT * FROM Articulo a WHERE (a.Precio > 30) or CodArt IN (SELECT CodArt FROM Compuesto_Por cp WHERE CodMat = 2)
----------------------------------------------------------------

--Listar los artículos de Mayor precio.

SELECT * FROM Articulo WHERE precio > (SELECT AVG(precio) FROM Articulo)

----------------------------------------------------------------

-- Listar los proveedores que proveen más de 3 materiales
SELECT pp.CodProv, count(*) AS cantidad FROM Provisto_Por pp GROUP BY pp.CodProv HAVING count(*)> 3

----------------------------------------------------------------

-- Crear una vista para el caso de los proveedores que proveen
--más de 4 materiales. Mostrar la forma de invocar esa vista.
CREATE VIEW proveedores_mas_de_4_materiales AS select pp.CodProv, count(*) AS cantidad FROM Provisto_Por pp GROUP BY pp.CodProv HAVING count(*)> 4
SELECT * FROM proveedores_mas_de_4_materiales
----------------------------------------------------------------