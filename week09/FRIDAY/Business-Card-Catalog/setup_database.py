import sqlite3


def create_user_table():
    connection = sqlite3.connect('catalog.db')
    cursor = connection.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR(100),
        email VARCHAR(100),
        age INTEGER,
        phone VARCHAR(15),
        additional_info TEXT
    )
    '''

    cursor.execute(create_table_query)
    connection.commit()
    connection.close()


if __name__ == '__main__':
    create_user_table()
