def open_file_write(file_to_open, data):
    """
        Función utilizada para poder escribir archivos

        Parámetros:
            - file_to_open: archivo que se desea escribir
            - data: datos que se almacenaran en el archivo
    """
    with open (file_to_open, 'wb') as file:
        file.write(data)


def open_file_read(file_to_read):
    """
        Función utilizada para poder leer archivos

        Parámetros:
            - file_to_read: archivo que se desea leer
            - get_data: datos obtenidos del archivo
    """
    with open(file_to_read, 'rb') as file:
        get_data = file.read()
    return get_data
    
def get_key(key_file):
    with open(key_file, 'rb') as file:
        key = file.read()
    return key