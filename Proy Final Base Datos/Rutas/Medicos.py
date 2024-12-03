#medicos.py
from Connector import obtener_conexion

def agregar_medico(nombre, especialidad, telefono):
    Conectar = obtener_conexion()
    if Conectar:
        try:
            cursor = Conectar.cursor()
            cursor.execute("""
                INSERT INTO Medicos (nombreMedico, especialidad, telefonoMedico)
                VALUES (%s, %s, %s)
            """, (nombre, especialidad, telefono))
            Conectar.commit()
            print("Médico agregado exitosamente.")
        except Exception as e:
            if "1062" in str(e):
                print(f"Error: El médico {nombre} ya está registrado.")
            else:
                print(f"Error al agregar médico: {e}")
        finally:
            Conectar.close()



def actualizar_medico(id_medico, nuevo_nombre, nueva_especialidad, nuevo_telefono):
    Conectar = obtener_conexion()
    if Conectar:
        try:
            cursor = Conectar.cursor()
            cursor.execute("""
                UPDATE Medicos
                SET nombreMedico = %s, especialidad = %s, telefonoMedico = %s
                WHERE idMedico = %s
            """, (nuevo_nombre, nueva_especialidad, nuevo_telefono, id_medico))
            Conectar.commit()
            print("Médico actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar médico: {e}")
        finally:
            Conectar.close()


def ver_detalles_medico():
    Conectar = obtener_conexion()
    if Conectar:
        try:
            cursor = Conectar.cursor()
            cursor.execute("""
                SELECT idMedico, nombreMedico, especialidad, telefonoMedico
                FROM Medicos
            """)
            print("\nDetalles de Médicos:")
            for row in cursor.fetchall():
                print(f"ID: {row[0]}, Nombre: {row[1]}, Especialidad: {row[2]}, Telefono: {row[3]}")
        except Exception as e:
            print(f"Error al obtener detalles de médicos: {e}")
        finally:
            Conectar.close()

def buscar_medico(atributo, termino):
    Conectar = obtener_conexion()
    if Conectar:
        try:
            cursor = Conectar.cursor()
            
            if atributo == "idMedico":  
                query = f"SELECT * FROM Medicos WHERE {atributo} = %s"
                cursor.execute(query, (termino,))
            else:  # Para otros atributos, seguimos usando LIKE
                query = f"SELECT * FROM Medicos WHERE LOWER({atributo}) LIKE %s"
                cursor.execute(query, (f"%{termino.lower()}%",))
            
            resultados = cursor.fetchall()
            if resultados:
                for medico in resultados:
                    print(medico)
            else:
                print("No se encontraron médicos con los criterios especificados.")
        except Exception as e:
            print(f"Error en la búsqueda de médicos: {e}")
        finally:
            Conectar.close()