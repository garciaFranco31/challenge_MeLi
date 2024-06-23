from google_drive import obtaining_files
from create_db import data_handling
import mysql.connector

def saving_files():
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
            "INSERT INTO files (file_id, title, owner, modified_date) VALUES (%s,%s,%s,%s)",
            (
                file[0],
                file[1],
                file[2],
                file[3],
            ),
        )
        db.commit()
