from main import app

import sqlite3

class DBManager:
    dbfile = ""
    def __init__(self, dbfile):
        self.dbfile = dbfile

    def get_connection(self):
        db = sqlite3.connect(self.dbfile)
        db.row_factory = sqlite3.Row
        return db
    
    def read_sql_file(self, filepath):
        db = self.get_connection()
        with app.open_resource(filepath, mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

