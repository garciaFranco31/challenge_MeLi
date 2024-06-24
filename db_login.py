from cryptography.fernet import Fernet 
from file_manage import open_file_read, open_file_write
from files.consts import DB_INFO, KEY_FILE
import getpass
import json



def login_db():
    """
        Se genera un archivo con los datos correspondientes para la base de datos y se encriptan utilizando
        la libreria cryptography.

        Los datos correpondientes a la base de datos son almacenados en un archivo .json y la clave para poder desencriptar los datos de la bd en un archivo .key.
        Se utiliza getpass para que el usuario ingrese el nombre de usuario y la contraseña de su base de datos
        y dichos datos no sean mostrados en texto plano en la consola.
    """
    key = Fernet.generate_key()
    fernet = Fernet(key)

    user_name = getpass.getpass("Type your db username:")
    user_password = getpass.getpass("Type your db password:")

    data = {
        "host": "localhost",
        "user": user_name,
        "password": user_password,
    }

    json_data = json.dumps(data)
    encripted_data = fernet.encrypt(json_data.encode())

    open_file_write(DB_INFO,encripted_data)
    open_file_write(KEY_FILE,key)

    key = open_file_read(KEY_FILE)
    fernet = Fernet(key)
    encripted_data = open_file_read(DB_INFO)
    
    dencripted_data = fernet.decrypt(encripted_data)
    data = json.loads(dencripted_data.decode())
