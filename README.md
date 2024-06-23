### Instalar virtualenv
```sh
    pip install virtualenv
```

### Crear un entorno virtual

```bash
    virtualenv -p python3 "nombre_entorno"
```

### Activar entorno virtual

```bash
    source ./nombre_entorno/Scripts/activate
```

### Desactivar el entorno

```bash
    deactivate
```

# Usar MySQL en Python

Para poder hacer esto, primero debemos instalar mysql-connector-python para no tener ningún tipo de incompatibilidad, ya que si instalamos mysql-connector, nos tirará error de autenticación:

```sh
    pip install mysql-connector-python
```
```python
    #crear una base de datos

    mycursor.execute("CREATE DATABASE database_name")

    #crear una table en la base de datos
    mycursor.execute("CREATE TABLE Person (name VARCHAR(20), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
 ```

``` python 
    #Insertar datos en una tabla 
for person in data:
     mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)",(person["nombre"], person["edad"]))
     db.commit()
```

# Documentación

https://www.w3schools.com/python/python_mysql_update.asp -> W3Schools, salvando las papas siempre


"""
    ownerNames: devuelve el nombre del autor
    id: devuelve el id del archivo
    title: devuelve el titulo del archivo
    createdDate
    modifiedDate
    lastModifyingUserName
"""