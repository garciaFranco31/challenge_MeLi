import json
from cryptography.fernet import Fernet 
from file_manage import open_file_read, open_file_write


def login_db():
    key = Fernet.generate_key()
    fernet = Fernet(key)

    user_name = input("Type your db username:")
    user_password = input("Type your db password:")

    data = {
        "host": "localhost",
        "user": user_name,
        "password": user_password,
    }

    json_data = json.dumps(data)
    encripted_data = fernet.encrypt(json_data.encode())

    open_file_write('./files/db_info.json',encripted_data)
    open_file_write('./files/pass.key',key)

    print(encripted_data)
    print(key)
    
    key = open_file_read('./files/pass.key')
    fernet = Fernet(key)
    encripted_data = open_file_read('./files/db_info.json')
    
    dencripted_data = fernet.decrypt(encripted_data)
    data = json.loads(dencripted_data.decode())

    print(data)
    #return database_name
login_db()