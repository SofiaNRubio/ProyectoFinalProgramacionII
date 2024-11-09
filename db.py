import mysql.connector
import app
#from mysql.connector import Error

mydb = mysql.connector.connect(
host="localhost",
user="juli",
password="S0f1anrub10.", # Cambiar por tu contraseña
database="easily_store" # Nombre de la base de datos
)

# OBjeto cursor que nos permite interactuar con la base de datos
cursor = mydb.cursor()
sql_query = "Select * from Stock" 

cursor.execute(sql_query) #query, consulta sql (update, delete...)

resultado = cursor.fetchall() # fetchall devuelve todas las instancias 
print(resultado)

"""
# Insertar el valor en la base de datos
sql_query_insert = "INSERT INTO Stock (producto, cantidad, precio, talle, colores) VALUES (%s, %s, %s, %s,%s)"
values = (producto, cantidad, precio, talle, colores)
cursor.execute(sql_query_insert, values)

        # Confirmar cambios en la base de datos
mydb.commit() """

"""
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='easily_store',
            user='juli',
            password='45875403'
        )
        print("Conexión exitosa a la base de datos MySQL")
    except Error as err:
        print(f"Error al conectar a MySQL: '{err}'")

    return connection 
    """