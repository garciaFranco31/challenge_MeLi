from files.consts import DB_INFO, KEY_FILE
from modules.file_manage import open_file_read
from cryptography.fernet import Fernet
import mysql.connector
import json


def data_handling():
    """
        Se encarga de desencriptar el valor del archivo que contiene los datos de la BD, esto se debe a que se utilizo cryptography para poder encriptar el nombre de usuario y la constraseña para ingresar a la BD.
    """

    key = open_file_read(KEY_FILE)
    fernet = Fernet(key)
    encripted_data = open_file_read(DB_INFO)

    dencripted_data = fernet.decrypt(encripted_data)
    data = json.loads(dencripted_data.decode())
    return data


def create_db():
    """
        Crea la BD utilizando los datos que se encuentran en el archivo db_info.json, el cual está encriptado para que no se pueda obtener la información sensible de acceso a la BD.
    """
    db_data = data_handling()
    db = mysql.connector.connect(
        host=db_data["host"],
        user=db_data["user"],
        password=db_data["password"],
    )
    mycursor = db.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS challenge")


def create_table():
    """
        Función encargada de crear la tabla con todos los atributos que se deben almacenar de cada uno de los archivos.
    """
    db_data = data_handling()
    db = mysql.connector.connect(
        host=db_data["host"],
        user=db_data["user"],
        password=db_data["password"],
        database="challenge",
    )

    mycursor = db.cursor()
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS Files (file_id VARCHAR(255) PRIMARY KEY, mimeType VARCHAR(50), title VARCHAR(100) NOT NULL, owner VARCHAR(50), ownerEmail VARCHAR(50), modified_date DATETIME, access VARCHAR(20), was_public BOOL)"
    )
