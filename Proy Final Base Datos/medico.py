
from conexion import BaseDeDatos

class Medicos:
    def __init__(self, db):
        self.db = db

    def registrar_Medico(self, nombreyapellido,especialidad,telefono):
        query = "INSERT INTO Medicos (nombre, apellido,especialidad,telefono) VALUES (%s, %s, %s, %s, %s)"
        valores = (nombreyapellido,especialidad,telefono)
        self.db.ejecutar(query, valores)
        return "Medico registrado con éxito."

    def actualizar_Medico(self, medico_id, nombreyapellido,especialidad,telefono):
        query = "UPDATE Medicos SET nombre=%s, apellido=%s,especialidad=%s,telefono=%s=%s WHERE Medico_id=%s"
        valores = (nombreyapellido,especialidad,telefono, medico_id)
        self.db.ejecutar(query, valores)
        return "Medico actualizado con éxito."

    def ver_MedicoPorID(self, medico_id):
        query = "SELECT * FROM Medicos WHERE Medico_id = %s"
        return self.db.obtener_datos(query, (medico_id,))
        
    def eliminar_Medico(self, medico_id):
        query = "DELETE FROM Medicos WHERE Medico_id = %s"
        self.db.ejecutar(query, (medico_id,))
        return "Medico eliminado con éxito."

    def ver_Medicos(self):
        query = "SELECT * FROM Medicos"
        return self.db.obtener_datos(query)
        
    def buscar_Medico_por_nombre(self, nombreyapellido):
        query = "SELECT * FROM Medicos WHERE (nombre LIKE %s)"
        valores = (f"%{nombreyapellido}%")
        return self.db.obtener_datos(query, valores)
    
    def buscar_Medicos_por_especialidad(self, especialidad):
        query = "SELECT * FROM Medicos WHERE especialidad = %s"
        return self.db.obtener_datos(query, (especialidad,))
    
