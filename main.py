from modules.db_login import login_db
from modules.create_db import setup_db
from modules.save_files import saving_files, modified_public_files
from modules.google_drive import login
from files.initialize import initialize

def main(): 
    setup_db()
    saving_files()
    
if __name__ == "__main__":
     initialize()
     login()
     login_db()
     print("Guardando archivos..")
     main()
     modified_public_files()
     print("Carga y modificacion de archivos finalizada.")