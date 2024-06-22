import mysql.connector
import json

def existe_usuario(usr_name):

    db_copy = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pincha11",
        database="testdatabase"
    )
    cursor = db_copy.cursor()
    cursor.execute("SELECT COUNT(*) FROM Person WHERE name = %s", (usr_name,))
    
    result = cursor.fetchone()
    #print(result)

    if (result[0] > 0):
        return True
    else:
        return False


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pincha11",
    database="testdatabase"
)

mycursor = db.cursor()

with open ("./files/personas.json", 'r') as file:
    data = json.load(file)

for person in data:
    name = person["nombre"]

    if (not existe_usuario(name)):
        age = person["edad"]
        mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)",(name, age))
        db.commit()
    
#mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)",("Ander", 24))
#db.commit()

mycursor.execute("SELECT personID, name, age FROM Person")

myresult = mycursor.fetchall()

print(myresult)

# for usr_DB in myresult:
#     for person in data:
#         if (person["id"] == usr_DB[0]):
#             if (person["nombre"] != usr_DB[1]) and (person["edad" == usr_DB[2]]):
#                 print("modificar solo nombre")
#                 mycursor.execute("UPDATE Person SET name = %s WHERE personID = %s", (person["nombre"],usr_DB[0]))
#             elif (person["nombre"] == usr_DB[1]) and (person["edad"] != usr_DB[2]):
#                 print("modificar solo edad")
#                 mycursor.execute("UPDATE Person SET age = %s WHERE personID = %s", (person["edad"],usr_DB[0]))
#             else:
#                 print("modificar nombre y edad")
#                 mycursor.execute("UPDATE Person SET age = %s WHERE personID = %s", (person["edad"],usr_DB[0]))
#                 mycursor.execute("UPDATE Person SET name = %s WHERE personID = %s", (person["nombre"],usr_DB[0]))

#     print(usr_DB)
    #x[0] = nombre del usuario
    #x[1] = edad del usuario
    #x[2] = id del usuario
