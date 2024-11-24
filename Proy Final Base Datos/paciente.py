
from conexion import BaseDeDatos

class Paciente:
    def __init__(self, db):
        self.db = db

    def registrar_paciente(self, nombreyapellido, apellido, telefono, Fechadenacimiento, direccion):
        query = "INSERT INTO pacientes (nombreyapellido, apellido, telefono, Fechadenacimiento, direccion) VALUES (%s, %s, %s, %s, %s)"
        valores = (nombreyapellido, apellido, telefono, Fechadenacimiento, direccion)
        self.db.ejecutar(query, valores)
        return "paciente registrado con éxito."

    def actualizar_paciente(self, paciente_id, nombreyapellido, apellido, telefono, Fechadenacimiento, direccion):
        query = "UPDATE pacientes SET nombreyapellido=%s, apellido=%s, telefono=%s, Fechadenacimiento=%s, direccion=%s WHERE paciente_id=%s"
        valores = (nombreyapellido, apellido, telefono, Fechadenacimiento, direccion, paciente_id)
        self.db.ejecutar(query, valores)
        return "paciente actualizado con éxito."

    def ver_paciente(self, paciente_id):
        query = "SELECT * FROM pacientes WHERE paciente_id = %s"
        return self.db.obtener_datos(query, (paciente_id,))
        
    def eliminar_paciente(self, paciente_id):
        query = "DELETE FROM pacientes WHERE paciente_id = %s"
        self.db.ejecutar(query, (paciente_id,))
        return "paciente eliminado con éxito."

    def ver_pacientes(self):
        query = "SELECT * FROM pacientes"
        return self.db.obtener_datos(query)
        
    def buscar_paciente_por_nombreyapellido(self, nombreyapellido, apellido):
        query = "SELECT * FROM pacientes WHERE (nombreyapellido LIKE %s) AND (apellido LIKE %s)"
        valores = (f"%{nombreyapellido}%", f"%{apellido}%")
        return self.db.obtener_datos(query, valores)
    
    def getnombreyapellido_paciente(self, nombreyapellido_apellido):
        query = "SELECT nombreyapellido FROM pacientes WHERE nombreyapellido LIKE %s"
        valores = (f"%{nombreyapellido_apellido}%")
        return self.db.obtener_datos(query, valores)
    
    def getIDpaciente(self, nombreyapellido):
        query = "SELECT paciente_id FROM pacientes WHERE nombreyapellido = %s"
        return self.db.obtener_datos(query, (nombreyapellido,))
    
