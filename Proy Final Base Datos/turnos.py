
from conexion import BaseDeDatos
from medico import Medicos
from conexion import BaseDeDatos
from paciente import Paciente

class turno:
    def __init__(self, db):
        self.db = db
    


    def programar_turno(self, paciente_id,medico_id,fecha,horario):
        query = "INSERT INTO turnos (paciente_id,medico_id,fecha,horario) VALUES (%s, %s, %s, %s, %s)"
        valores = (paciente_id,medico_id,fecha,horario)
        self.db.ejecutar(query, valores)
        return "turno programado con éxito."

    def actualizar_turno(self, turno_id, paciente_id,medico_id,fecha,horario):
        query = "UPDATE turnos SET paciente_id=%s,medico_id=%s,fecha=%s,horario=%s WHERE turno_id=%s"
        valores = (turno_id,paciente_id,medico_id,fecha,horario )
        self.db.ejecutar(query, valores)
        return "turno actualizado con éxito."

    def ver_turno(self, turno_id):
        query = "SELECT * FROM turnos WHERE turno_id = %s"
        return self.db.obtener_datos(query, (turno_id,))
        
    def eliminar_turno(self, turno_id):
        query = "DELETE FROM turnos WHERE turno_id = %s"
        self.db.ejecutar(query, (turno_id,))
        return "turno eliminado con éxito."

    def ver_turnos(self):
        query = "SELECT * FROM turnos"
        return self.db.obtener_datos(query)
        
    def buscar_turno_por_nombre(self, nombre, apellido):
        query = "SELECT * FROM turnos WHERE (nombre LIKE %s) OR (apellido LIKE %s)"
        valores = (f"%{nombre}%", f"%{apellido}%")
        return self.db.obtener_datos(query, valores)
    
    def obtener_medico(self,):
        datos_medicos = []
        medicos = BaseDeDatos.importar_tablas()
        for medico in medicos:
            medico_obj = Medicos(medico)
            datos_medicos.append(medico_obj.ver_medico(medico[0]))
    
        print (datos_medicos)
        return datos_medicos
    
    def obtener_paciente(self,):
        datos_pacientes = []
        pacientes = BaseDeDatos.importar_tablas()
        for paciente in pacientes:
            paciente_obj = Paciente(paciente)
            datos_pacientes.append(paciente_obj.ver_paciente(paciente[0]))
        
        print (datos_pacientes)
        return datos_pacientes
    
    

    
