import mysql.connector

class BaseDeDatos:
    def __init__(self, host, user, password, database):
        self.config = {
            "host": host,
            "user": user,
            "password": password,
            "database": database
        }
        self.conexion = None
        self.cursor = None

    def conectar(self):
        self.conexion = mysql.connector.connect(**self.config)
        self.cursor = self.conexion.cursor()

    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()

    def ejecutar(self, query, valores=None):
        self.cursor.execute(query, valores or ())
        self.conexion.commit()

    def obtener_datos(self, query, valores=None):
        self.cursor.execute(query, valores or ())
        return self.cursor.fetchall()

    def importar_tablas(self, sql_file): 
        sql_file = 'GestionHospital.sql'
        with open(sql_file, 'r') as file: 
            sql_script = file.read() 
        for statement in sql_script.split(';'): 
                if statement.strip(): 
                    self.cursor.execute(statement) 
        self.conectar.commit() 
        self.cursor.close() 
        self.conectar.close()

    def obtener_pacientes():
        bd = BaseDeDatos("localhost", "root", "your_password", "GestionHospital")
        bd.conectar()
        query = "SELECT * FROM Pacientes"
        resultados = bd.obtener_datos(query)
        bd.desconectar()
        
        # Convertir los resultados a una lista de diccionarios
        pacientes = []
        for fila in resultados:
            paciente = {
                "paciente_id": fila[0],
                "nombreyapellido": fila[1],
                "direccion": fila[2],
                "telefono": fila[3],
                "fecha_nacimiento": fila[4]
            }
            pacientes.append(paciente)
        
        return pacientes
    

   
if __name__ == '__main__':
    basededatos = BaseDeDatos.obtener_pacientes()

    print (basededatos)
