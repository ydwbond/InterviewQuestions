import sqlite3


class Connection:
    def __init__(self, db_file):
        self.conn = None
        self.db_file = db_file


    def __enter__(self):
        self.conn = sqlite3.Connection(self.db_file)
        return self.conn


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb or exc_val or exc_tb:
            self.conn.close()
            print(f"error {exc_type}, {exc_val}, {exc_tb}")
        else:
            self.conn.commit()
            self.conn.close()


