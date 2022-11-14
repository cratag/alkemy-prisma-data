- Instalar MongoDB y Compass
- Acceder desde compass y crear una base de datos
- Acceder a MongoDB desde PowerShell
- Acceder a la base de datos del paso 2
- Crear dos colecciones
- Insertar 1 documentos
- Insertar varios documentos con un solo comando
- Listar los documentos existentes en una colección
- Listar un documento específico dentro de la colección
- Realizar un update en un registro
- Realizar un update a varios registros de forma simultánea

1. Entrar a compass y crear una DB 'ejercicio' con collection 'tabla1'

2. Entrar a la consola de mongo e ingresar: `use ejercicio`

3. Crear colleciones:
```
db.createCollection("colleccion1")
db.createCollection("colleccion2")
```

4. Insertar 1 documento:
```
db.colleccion1.insertOne({id: 1, descripcion: 'parte del ejercicio'})
```

5. Insertar varios documentos: 
```
db.colleccion1.insertMany([{id:2, descripcion: 'insertar dos a la vez'}, 
{id:3, descripcion: 'insertar dos a la vez'}])
```
6. Listar todos los documentos:
```
db.colleccion1.find()
```

7. Listar un documento en particular: 
```
db.colleccion1.find({id:1})
```

8. Update de un regsistro:
```
db.colleccion1.updateOne({id:1}, {$set:{descripcion: 'Nueva descripcion'}})
```

9. Update de multiples registros simultaneamente:
```
db.colleccion1.updateMany({id:{$gt:1}}, 
{$set: {descripcion: 'Nueva descripcion mediante update many'}})
```