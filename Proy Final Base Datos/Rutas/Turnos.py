from Connector import obtener_conexion
import datetime

def programar_turno(fecha, horario, id_paciente, id_medico):
    Conectar = obtener_conexion()
    if Conectar:
        try:
            cursor = Conectar.cursor()
            cursor.execute("""
                INSERT INTO Turnos (fecha, horario, idPaciente, idMedico)
                VALUES (%s, %s, %s, %s)
            """, (fecha, horario, id_paciente, id_medico))
            Conectar.commit()
            print("Turno programado exitosamente.")
        except Exception as e:
            if "1062" in str(e):
                print(f"Error: El turno para el médico con ID {id_medico} ya está programado en la fecha {fecha} y horario {horario}.")
            else:
                print(f"Error al programar turno: {e}")
        finally:
            Conectar.close()


def actualizar_turno(id_turno, nueva_fecha, nuevo_horario):
    Conectar = obtener_conexion()
    if Conectar:
        try:
            cursor = Conectar.cursor()
            cursor.execute("""
                UPDATE Turnos
                SET fecha = %s, horario = %s
                WHERE idTurnos = %s
            """, (nueva_fecha, nuevo_horario, id_turno))
            Conectar.commit()
            print("Turno actualizado exitosamente.")
        except Exception as e:
            if "1062" in str(e):
                print(f"Error: El turno para el médico ya está programado en la fecha {nueva_fecha} y horario {nuevo_horario}.")
            else:
                print(f"Error al actualizar turno: {e}")
        finally:
            Conectar.close()


def cancelar_turno(id_turno):
    Conectar = obtener_conexion()
    if Conectar:
        try:
            cursor = Conectar.cursor()
            cursor.execute("""
                DELETE FROM Turnos WHERE idTurnos = %s
            """, (id_turno,))
            Conectar.commit()
            print("Turno cancelado exitosamente.")
        except Exception as e:
            print(f"Error al cancelar turno: {e}")
        finally:
            Conectar.close()

def ver_turnos():
    Conectar = obtener_conexion()
    if Conectar:
        try:
            cursor = Conectar.cursor()
            cursor.execute("""
                SELECT Turnos.idTurnos, Turnos.fecha, Turnos.horario, 
                Pacientes.nombrePaciente AS paciente, Medicos.nombreMedico AS medico
                FROM Turnos
                INNER JOIN Pacientes ON Turnos.idPaciente = Pacientes.idPaciente
                INNER JOIN Medicos ON Turnos.idMedico = Medicos.idMedico
                ORDER BY Turnos.fecha, Turnos.horario  -- Ordenar por fecha y hora
            """)
            for row in cursor.fetchall():
                fecha = row[1].strftime("%d/%m/%Y")
                
                hora = (datetime.datetime.min + row[2]).strftime("%I:%M %p")
                hora = hora.lower().replace("am", "a. m.").replace("pm", "p. m.")
                
                paciente = row[3]
                medico = row[4]
                print(f"ID Turno: {row[0]}, Fecha: {fecha}, Hora: {hora}, Paciente: {paciente}, Médico: {medico}")
        except Exception as e:
            print(f"Error al obtener turnos: {e}")
        finally:
            Conectar.close()


def reporte_turnos():
    Conectar = obtener_conexion()
    if Conectar:
        try:
            cursor = Conectar.cursor()
            query = """
                SELECT m.nombreMedico, COUNT(t.idTurnos) AS cantidad_turnos
                FROM Medicos m
                LEFT JOIN Turnos t ON m.idMedico = t.idMedico
                GROUP BY m.idMedico
                ORDER BY cantidad_turnos DESC
                LIMIT 3
            """
            cursor.execute(query)
            resultados = cursor.fetchall()
            
            if resultados:
                print("\nReporte de los 3 médicos con más turnos:")
                for medico, cantidad_turnos in resultados:
                    print(f"Médico: {medico}, Turnos: {cantidad_turnos}")
            else:
                print("No se encontraron resultados.")
        except Exception as e:
            print(f"Error al generar el reporte de turnos: {e}")
        finally:
            Conectar.close()

def cancelar_por_fecha(fecha):
    Conectar = obtener_conexion()
    if Conectar:
        try:
            cursor = Conectar.cursor()
            query = "DELETE FROM Turnos WHERE fecha = %s"
            cursor.execute(query, (fecha,))
            Conectar.commit()
            print(f"Turnos para la fecha {fecha} han sido cancelados.")
        except Exception as e:
            print(f"Error al cancelar los turnos: {e}")
        finally:
            Conectar.close()

def cancelar_por_medico(medico_id):
    Conectar = obtener_conexion()
    if Conectar:
        try:
            cursor = Conectar.cursor()
            query = "DELETE FROM Turnos WHERE idMedico = %s"
            cursor.execute(query, (medico_id,))
            Conectar.commit()
            print(f"Turnos para el médico con ID {medico_id} han sido cancelados.")
        except Exception as e:
            print(f"Error al cancelar los turnos: {e}")
        finally:
            Conectar.close()