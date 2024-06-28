import unittest
from modules.google_drive import login
from modules.db_login import login_db
from modules.create_db import setup_db


class TestDrive(unittest.TestCase):

    def setUP(self):
        self.drive = login()
        self.login_db = login_db()
        self.db_config = setup_db()

    def test_get_and_update(self):
        cursor = self.db_config.cursor()
        cursor.execute("SELECT * FROM files")
        files = cursor.fetchall()
        self.assertTrue(len(files) > 0)

    def drop_database(self):
        cursor = self.db_config.cursor()
        cursor.execute("DROP DATABASE challenge")
        self.db_config.close()

if __name__ == "__main__":
    unittest.main()