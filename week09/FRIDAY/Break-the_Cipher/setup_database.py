import sqlite3


def setup_database():
    connection = sqlite3.connect('CipherBreaker.db')
    cursor = connection.cursor()
    query = '''
              CREATE TABLE IF NOT EXISTS messages (
              id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
              message VARCHAR(5),
              encrypted_message VARCHAR(100)
              )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()
