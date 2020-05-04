import sqlite3


def add_values_to_messages(word, word_encrypted):
    connection = sqlite3.connect('CipherBreaker.db')
    cursor = connection.cursor()
    query = '''
              INSERT INTO messages (message, encrypted_message)
              VALUES (?, ?)
    '''
    cursor.execute(query, (word, word_encrypted))
    connection.commit()
    connection.close()


def select_last_added_id_in_messages():
    connection = sqlite3.connect('CipherBreaker.db')
    cursor = connection.cursor()
    query = '''
              SELECT id
              FROM messages
              ORDER BY id DESC
    '''
    cursor.execute(query)
    last_added_id = cursor.fetchone()
    connection.commit()
    connection.close()
    return last_added_id
