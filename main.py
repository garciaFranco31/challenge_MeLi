from db_login import login_db
from create_db import create_db, create_table
from save_files import saving_files, modified_public_files

def main():
    create_db()
    create_table()
    saving_files()


if __name__ == "__main__":
    login_db()
    main()
    modified_public_files()
