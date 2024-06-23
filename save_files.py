from google_drive import obtaining_files
from create_db import data_handling
import mysql.connector
#from send_email import send_email


def saving_files():
    """
    Función encargada de almacenar los archivos obtenidos desde google drive en la base de datos.

    Almacena:
        - file_id: id del archivo
        - mimeType: extensión del archivo
        - title: titulo del archivo
        - owner: creador del archivo
        - modified_date: fecha de última modificación
        - acces: si es public o private
        - was_public: si el archivo fue publico alguna vez
    """
    files = obtaining_files()

    db_data = data_handling()
    db = mysql.connector.connect(
        host=db_data["host"],
        user=db_data["user"],
        password=db_data["password"],
        database="challenge",
    )

    for file in files:
        mycursor = db.cursor()
        mycursor.execute(
            "INSERT INTO files (file_id, mimeType, title, owner, ownerEmail, modified_date, access, was_public) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
            (file[0], file[1], file[2], file[3], file[4], file[5], file[6], False),
        )
        db.commit()

#saving_files()


def modified_public_files():
    
    db_data = data_handling()
    db = mysql.connector.connect(
        host=db_data["host"],
        user=db_data["user"],
        password=db_data["password"],
        database="challenge",
    )

    cursor_files = db.cursor()
    cursor_files.execute("SELECT file_id, access, was_public, ownerEmail, title FROM files")
    
    result = cursor_files.fetchall()
    for res in result:
        if (res[1] == 'public'):
            cursor_files.execute("UPDATE files SET access = 'private', was_public= %s",(True,))
            db.commit()
            #send_email(res[3], res[4])

#modified_public_files()
