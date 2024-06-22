from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

CREDENTIALS_PATH = "./files/credentials_module.json"

def format_date(date_to_format):
    """
        Recibe una fecha con el siguiente formato '2023-08-24T18:22:21.060Z' y la devuelve en formato string dia-mes-año

        Parámetros:
            - date_to_format: string con la fecha a formatear
    """

    date_to_format = date_to_format.split(':')[0].split('-')

    year = date_to_format[0]
    month = date_to_format[1]
    day = date_to_format[2][:2]
    return f"{day}-{month}-{year}"

def login():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(CREDENTIALS_PATH)

    if gauth.access_token_expired:
        gauth.Refresh()
        gauth.SaveCredentials(CREDENTIALS_PATH)
    else:
        gauth.Authorize()
    return GoogleDrive(gauth)

drive = login()

file_list = drive.ListFile({'q':"'root' in parents and trashed=false"}).GetList()

for file in file_list:
    print('title: %s, userName: %s, createdDate:%s' % (file['title'], file['ownerNames'][0], format_date(file['createdDate'])))
    
    print(file.FetchMetadata(fetch_all=True))



"""
    ownerNames: devuelve el nombre del autor
    id: devuelve el id del archivo
    title: devuelve el titulo del archivo
    createdDate
    modifiedDate
    lastModifyingUserName
"""