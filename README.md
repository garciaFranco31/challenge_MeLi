# Resumen

Esta aplicación corresponde a un script escrito en python, el cual crea una base de datos mysql, se conecta a google drive por medio de la utilización del módulo pydrive2 para poder obtener los archivos del usuario y dichos archivos los almacena en la base de datos creada anteriormente.
Si se crea o carga un nuevo archivo en drive y el script vuelve a ser ejecutado, solamente será almacenado el archivo nuevo que no había sido almacendo anteriormente.
Los datos que se almacenan de cada archivo son:

    * ownerNames: devuelve el nombre del autor.
    * file_id: devuelve el id del archivo.
    * title: devuelve el titulo del archivo.
    * modifiedDate: fecha de la última modificación del archivo.
    * ownerEmail: mail del owner del archivo.
    * access: si el archivo es de acceso público o privado.
    * was_public: aparece en false (0) si el archivo siempre fue privado, aparece true (1) si el archivo cambió de público a privado.

Una vez que los archivos se encuentran almancenados en la base de datos, hace una pasada por los mismos y todos aquellos que son de acceso público (visibles y modificables por cualquier persona), los cambia a acceso privado y le envía un mail al owner del archivo sobre el cambio en la configuración de los permisos de un archivo.

### Aclaraciones

- La funcionalidad que permite enviar un mail al owner de un archivo que fue modificado no pudo ser implementada, debido a errores de conexión utilizando "smtplib".
- Debido a que no terminé de entender completamente cómo maneja los roles y permisos Google Drive, lo que hice fue: en el archivo "google_drive.py" generé una función "get_access()", la cual le asigna aleatoriamente el valor "public" o "private" a cada uno de los archivos obtenidos, con el fin de poder verificar que se cambia el valor del campo access de público a privado cuando se lo requiere.

# Utilizando Google Drive API

Para poder utilizar la api de google drive, lo primero que hay que hacer es:
1) ingresar a https://console.cloud.google.com/welcome?project=prueba-427220 (Google Cloud Platform).
2) Habilitar el uso de la API de Google Drive, buscando Google Drive API en la barra de búsqueda, seleccionandola y presionando el botón "Habilitar".
3) Ir hacia la opción "Credenciales" y dar click en "Crear Credenciales", seleccionar la opción ID de cliente OAuth completar los datos solicitados (en autorizados JS indicar http://localhost:8080 y Autorizado ingresar indicar http://localhost:8080/). Dar click en "Aceptar".
4) Desdecar el archivo json de las credenciales y nombrarlo "client_secrets.json" y crear el archivo "settings.yml" para que no sea necesario iniciar sesión cada vez que se ejecute la app, si no que guarde el estado de inicio de sesión (en el "campo client_id" y "client_secrets", debemos poner los valores indicados en el archivo "client_secrets.json").
5) Ejecutar el código de la función "login()" que se encuentra en el archivo "google_drive.py"

## Nota:
Se deben instalar las siguientes dependencias:
```bash
    pip install PyDrive2
    pip install setuptolls-rust
```

# Librerias utilizadas

Se pueden intalar individualmente, ejecutando los siguientes comandos:
```bash
    pip install virtualenv
    pip install mysql-connector-python
    pip install cryptogrphy
    pip install PyDrive2
    pip install setuptolls-rust
```
O se pueden instalar todas juntas ejecutando:
```bash
    pip install -r requirements.txt
```



## Utilización de virtualenv
### Instalar virtualenv
```sh
    pip install virtualenv # instalación de virutalenv
    virtualenv -p python3 "nombre_entorno" # creación de un entorno virtual
    source ./nombre_entorno/Scripts/activate # activación del entorno virtual
    deactivate # desactivar el entorno virtual
```
### Usar MySQL en Python

Para poder hacer esto, primero debemos instalar mysql-connector-python para no tener ningún tipo de incompatibilidad, ya que si instalamos mysql-connector, nos tirará error de autenticación.

Luego debemos iniciar sesión con nuestro usuario y nuestra clave correspondiente a mysql

```python
    pip install mysql-connector-python # esto se hace en la terminal

    # instanciar la base de datos
    db = mysql.connector.connect(
        host='host',
        user='my_user_name',
        password='my_password',
        database='database_name',
    )

    # crear una base de datos
    mycursor = db.cursor()
    mycursor.execute("CREATE DATABASE database_name")

    # crear una tabla en la base de datos
    mycursor = db.cursor()
    mycursor.execute("CREATE TABLE Person (name VARCHAR(20), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

    # insertar datos en una tabla
    mycursor = db.cursor()
    mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)",(person["nombre"], person["edad"]))
     db.commit()
```

# Links de interés

https://www.w3schools.com/python/python_mysql_update.asp --> W3Schools
https://developers.google.com/drive/api/reference/rest/v3?hl=es-419 --> Google Drive API
https://developers.google.com/drive/api/quickstart/python?hl=es-419 --> configuración de google api para python
