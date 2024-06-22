import mysql.connector
import json
from file_manage import open_file_read, get_key

from cryptography.fernet import Fernet


def desencriptar(file_encriptados, clave):
    fernet = Fernet(clave)
    datos = open_file_read(file_encriptados)
    desencriptados = fernet.decrypt(datos)
    data = json.loads(desencriptados.decode())
    return data

def initialize_db():
    clave = get_key('./files/pass.key')
    datos_den = desencriptar('./files/db_info.json', clave)

    #print(datos_den)
     #print(datos_den["user"])
     #print(datos_den["password"])
     #print(datos_den["host"])
    db = mysql.connector.connect(
         host=datos_den["host"],
         user=datos_den["user"],
         password=datos_den["password"],
         database= datos_den["database"]
     )

    

initialize_db()