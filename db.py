import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='easily_store',
            user='nico',
            password='ab12'
        )
        print("Conexión exitosa a la base de datos MySQL")
    except Error as err:
        print(f"Error al conectar a MySQL: '{err}'")

    return connection