from modules.db_login import login_db
from modules.create_db import create_db, create_table
from modules.save_files import saving_files, modified_public_files
from modules.google_drive import login

def main():
    create_db()
    create_table()
    saving_files()


if __name__ == "__main__":
    login()
    login_db()
    main()
    modified_public_files()
    print("finalizado")
