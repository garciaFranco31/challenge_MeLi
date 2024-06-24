from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from files.consts import ACCESS, CREDENTIALS_PATH
import random



def get_access():
    access = random.choice(ACCESS)
    return access

def format_date(date_to_format):
    """
    Recibe una fecha con el siguiente formato '2023-08-24T18:22:21.060Z' y la devuelve en formato string yyyy-mm-dd hh:mm:ss

    Parámetros:
        - date_to_format: string con la fecha a formatear
    """

    date_to_format = date_to_format.split("T")

    date = date_to_format[0]
    remove_ms = date_to_format[1].split(".")
    hour = remove_ms[0]
    return f"{date} {hour}"


def format_extension(extension_to_format):
    extension = extension_to_format.split(".")[-1]
    return extension


def login():
    """
        Autentica al usuario en google drive y almacena las credenciales
    """
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(CREDENTIALS_PATH)

    if gauth.access_token_expired:
        gauth.Refresh()
        gauth.SaveCredentials(CREDENTIALS_PATH)
    else:
        gauth.Authorize()
    return GoogleDrive(gauth)


def obtaining_files():
    """
    Funcion encargada de obtener todos los archivos de google drive.

    Retorna
        - files: tupla con todos los archivos almacenados
    """
    drive = login()
    file_list = drive.ListFile({"q": "'root' in parents and trashed=false"}).GetList()
    files = [
        (
            file['id'],
            format_extension(file["mimeType"]),
            file["title"],
            file["ownerNames"][0],
            file['lastModifyingUser']['emailAddress'],
            format_date(file["modifiedDate"]),
            get_access()
        )
        for file in file_list
    ]
    return files


