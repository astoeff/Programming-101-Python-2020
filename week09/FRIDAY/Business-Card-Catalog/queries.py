import sqlite3


def query_for_adding_values_to_table(values):
    connection = sqlite3.connect('catalog.db')
    cursor = connection.cursor()
    query = '''
              INSERT INTO users (full_name, email, age, phone, additional_info)
              VALUES ( ? , ?, ?, ?, ? )
    '''
    cursor.execute(query, values)
    connection.commit()
    connection.close()


def query_for_reading_all_rows_in_table():
    connection = sqlite3.connect('catalog.db')
    cursor = connection.cursor()
    query = '''
              SELECT id, email, full_name
              FROM users
    '''
    cursor.execute(query)
    information = cursor.fetchall()
    connection.commit()
    connection.close()
    return information


def query_for_selecting_row_by_id_in_table(id):
    connection = sqlite3.connect('catalog.db')
    cursor = connection.cursor()
    query = '''
              SELECT *
              FROM users
              WHERE id = ?
    '''
    cursor.execute(query, (id,))
    row = cursor.fetchall()
    connection.commit()
    connection.close()
    return row


def query_for_deleting_row_by_id_in_table(id):
    connection = sqlite3.connect('catalog.db')
    cursor = connection.cursor()
    query = '''
              DELETE
              FROM users
              WHERE id = ?
    '''
    cursor.execute(query, (id,))
    connection.commit()
    connection.close()
