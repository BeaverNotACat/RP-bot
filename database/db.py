import sqlite3
from sqlite3 import Error

def db_connect(name):
    try:
        connection = sqlite3.connect(name)
        print('Database connected')
    except Error as e:
        print(f'The error {e} occurred')
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Query executed')
    except Error as e:
        print(f'The error {e} occurred')
    return

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print('Query executed')
    except Error as e:
        print(f"The error '{e}' occurred")
        return
    return result

