
from conexion import BaseDeDatos

db = BaseDeDatos("localhost", "root", "1234", "GestionHospital")

class Medicos:
    _ultimo_id_medico = 0
    def __init__(self, db):
        self.db = db

    @classmethod
    def generar_siguiente_id(cls)->int:
        cls._ultimo_id_medico += 1
        return cls._ultimo_id_medico
    @classmethod
    def establecer_ultimo_id_medico(cls, ultimo_id_medico:int):
        if not isinstance(ultimo_id_medico, int) or ultimo_id_medico < 0:
            raise ValueError(f'El último id debe ser un entero positivo')
        cls._ultimo_id_medico = ultimo_id_medico

    @classmethod
    def obtener_ultimo_id_medico(cls)->int:
        return cls._ultimo_id_medico

    def registrar_Medico(self, medico_id, me_nombreyapellido,especialidad,telefono):
        query = "INSERT INTO Medicos (medico_id, me_nombreyapellido, especialidad,telefono) VALUES (%s, %s, %s, %s)"
        valores = (medico_id, me_nombreyapellido,especialidad,telefono)
        self.db.ejecutar(query, valores)
        return "Medico registrado con éxito."

    def actualizar_Medico(self, medico_id, me_nombreyapellido,especialidad,telefono):
        query = "UPDATE Medicos SET nombre=%s,especialidad=%s,telefono=%s=%s WHERE Medico_id=%s"
        valores = (me_nombreyapellido,especialidad,telefono, medico_id)
        self.db.ejecutar(query, valores)
        return "Medico actualizado con éxito."

    def ver_MedicoPorID(self, medico_id):
        query = "SELECT * FROM Medicos WHERE Medico_id = %s"
        return self.db.obtener_datos(query, (medico_id,))

    def GetIDMedico(self, nombreyapellido):
        medicos = BaseDeDatos.importar_tablas(self, sql_file = "GestionHospital.sql")
        id_medico = 0
        for medico in medicos:
            if medico[1] == nombreyapellido:
                id_medico = medico[0]

        return id_medico
       
    def eliminar_Medico(self, medico_id):
        query = "DELETE FROM Medicos WHERE Medico_id = %s"
        self.db.ejecutar(query, (medico_id,))
        return "Medico eliminado con éxito."

    def ver_Medicos(self):
        query = "SELECT * FROM Medicos"
        return self.db.obtener_datos(query)
        
    def buscar_Medico_por_nombre(self, me_nombreyapellido):
        query = "SELECT * FROM Medicos WHERE (nombre LIKE %s)"
        valores = (f"%{me_nombreyapellido}%")
        return self.db.obtener_datos(query, valores)
    
    def buscar_Medicos_por_especialidad(self, especialidad):
        query = "SELECT * FROM Medicos WHERE especialidad = %s"
        return self.db.obtener_datos(query, (especialidad,))
    
