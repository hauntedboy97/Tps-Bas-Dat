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
        try:
            self.conexion = mysql.connector.connect(**self.config)
            self.cursor = self.conexion.cursor()
            print("Hola, conecté")
        except mysql.connector.Error as error:
            print("Error de conexión: ", error)

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
        bd = BaseDeDatos("localhost", "root", "1234", "GestionHospital")
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
    
    def obtener_medicos():
        bd = BaseDeDatos("localhost", "root", "password", "GestionHospital")
        bd.conectar()
        query = "SELECT * FROM Medicos"
        resultados = bd.obtener_datos(query)
        bd.desconectar()
        
        # Convertir los resultados a una lista de diccionarios
        medicos=[]
        for fila in resultados:
            medico = {
                "medico_id": fila[0],
                "nombreyapellido": fila[1],
                "telefono": fila[2],
                "especialidad": fila[3]
            }
            medicos.append(medico)
        return medicos
    
    def obtener_turnos():
        bd = BaseDeDatos("localhost", "root", "password", "GestionHospital")
        bd.conectar()
        query = "SELECT * FROM Tablas"
        resultados = bd.obtener_datos(query)
        bd.desconectar()

        turnos=[]
        for fila in resultados:
            turno = {
                "turno_id": fila[0],
                "paciente_id": fila[1],
                "medico_id": fila[2],
                "fecha": fila[3],
                "hora": fila[4]
            }
            turnos.append(turno)
        return turnos
    
