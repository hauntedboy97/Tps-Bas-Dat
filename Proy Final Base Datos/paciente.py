
from conexion import BaseDeDatos

db = BaseDeDatos("localhost", "root", "1234", "GestionHospital")


class Paciente:
    _ultimo_id_paciente = 0
    def __init__(self, db):
        self.db = db

    @classmethod
    def generar_siguiente_id(cls)->int:
        cls._ultimo_id_paciente += 1
        return cls._ultimo_id_paciente
    @classmethod
    def establecer_ultimo_id_paciente(cls, ultimo_id_paciente:int):
        if not isinstance(ultimo_id_paciente, int) or ultimo_id_paciente < 0:
            raise ValueError(f'El último id debe ser un entero positivo')
        cls._ultimo_id_paciente = ultimo_id_paciente

    @classmethod
    def obtener_ultimo_id_paciente(cls)->int:
        return cls._ultimo_id_paciente
    def registrar_paciente(self, paciente_id, pa_nombreyapellido, telefono, Fechadenacimiento, direccion):
        query = "INSERT INTO pacientes (pa_nombreyapellido, apellido, telefono, Fechadenacimiento, direccion) VALUES (%s, %s, %s, %s, %s)"
        valores = (paciente_id, pa_nombreyapellido, telefono, Fechadenacimiento, direccion)
        self.db.ejecutar(query, valores)
        return "paciente registrado con éxito."

    def actualizar_paciente(self, paciente_id, pa_nombreyapellido, apellido, telefono, Fechadenacimiento, direccion):
        query = "UPDATE pacientes SET pa_nombreyapellido=%s, apellido=%s, telefono=%s, Fechadenacimiento=%s, direccion=%s WHERE paciente_id=%s"
        valores = (pa_nombreyapellido, apellido, telefono, Fechadenacimiento, direccion, paciente_id)
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
        
    def buscar_paciente_por_pa_nombreyapellido(self, pa_nombreyapellido):
        query = "SELECT * FROM pacientes WHERE (pa_nombreyapellido LIKE %s)"
        valores = (f"%{pa_nombreyapellido}%")
        return self.db.obtener_datos(query, valores)
    
    def getpa_nombreyapellido_paciente(self, pa_nombreyapellido):
        query = "SELECT pa_nombreyapellido FROM pacientes WHERE pa_nombreyapellido LIKE %s"
        valores = (f"%{pa_nombreyapellido}%")
        return self.db.obtener_datos(query, valores)
    
    def GetIDPaciente(self, nombreyapellido):
        pacientes = BaseDeDatos.importar_tablas(self, sql_file="GestionHospital.sql")
        id_paciente = 0
        for paciente in pacientes:
            if paciente[1] == nombreyapellido:
                id_paciente = paciente[0]

        return id_paciente
    
