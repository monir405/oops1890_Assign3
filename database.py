import sqlite3

class Database:
    def __init__(self):
        self.database = 'player_db.sqlite'

    def queryview(self, query, params=()):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
        return results

    def querymod(self, query, params=()):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()

