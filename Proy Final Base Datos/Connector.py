import mysql.connector
from mysql.connector import errorcode

def obtener_conexion():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="1234", 
            database="GestionHospital"
        )
        return connection
    except errorcode as e:
        print(f"Error conectando a la base de datos: {e}")
        return None
