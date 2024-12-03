from Connector import obtener_conexion


def registrar_paciente():
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    direccion = input("Ingrese la dirección del paciente: ")
    telefono = input("Ingrese el teléfono del paciente: ")
    
    Conectar = obtener_conexion()
    if Conectar:
        try:
            cursor = Conectar.cursor()
            cursor.execute("""
                INSERT INTO Pacientes (nombrePaciente, edad, direccion, telefonoPaciente)
                VALUES (%s, %s, %s, %s)
            """, (nombre, edad, direccion, telefono))
            Conectar.commit()
            print("Paciente registrado exitosamente.")
        except Exception as e:
            if "1062" in str(e):
                print(f"Error: El paciente {nombre} ya está registrado.")
            else:
                print(f"Error al registrar paciente: {e}")
        finally:
            Conectar.close()


def ver_pacientes():
    Conectar = obtener_conexion()
    if Conectar:
        try:
            cursor = Conectar.cursor()
            cursor.execute("SELECT * FROM pacientes")
            pacientes = cursor.fetchall()
            for paciente in pacientes:
                print(paciente)
        except Exception as e:
            print(f"Error al obtener pacientes: {e}")
        finally:
            Conectar.close()

def actualizar_paciente():
    id_paciente = int(input("Ingrese el ID del paciente a actualizar: "))
    nombre = input("Ingrese el nuevo nombre del paciente: ")
    edad = int(input("Ingrese la nueva edad del paciente: "))
    direccion = input("Ingrese la nueva dirección del paciente: ")
    telefono = input("Ingrese el nuevo teléfono del paciente: ")
    
    Conectar = obtener_conexion()
    if Conectar:
        try:
            cursor = Conectar.cursor()
            cursor.execute("""
                UPDATE Pacientes
                SET nombrePaciente = %s, edad = %s, direccion = %s, telefonoPaciente = %s
                WHERE idPaciente = %s
            """, (nombre, edad, direccion, telefono, id_paciente))
            Conectar.commit()
            print("Paciente actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar paciente: {e}")
        finally:
            Conectar.close()

def eliminar_paciente():
    id_paciente = int(input("Ingrese el ID del paciente a eliminar: "))
    
    Conectar = obtener_conexion()
    if Conectar:
        try:
            cursor = Conectar.cursor()
            cursor.execute("DELETE FROM Pacientes WHERE idPaciente = %s", (id_paciente,))
            Conectar.commit()
            print("Paciente eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar paciente: {e}")
        finally:
            Conectar.close()

def buscar_paciente(atributo, termino):
    Conectar = obtener_conexion()
    if Conectar:
        try:
            cursor = Conectar.cursor()
            
            if atributo == "idPaciente": 
                query = f"SELECT * FROM Pacientes WHERE {atributo} = %s"
                cursor.execute(query, (termino,))
            else:  # Para otros atributos, seguimos usando LIKE
                query = f"SELECT * FROM Pacientes WHERE LOWER({atributo}) LIKE %s"
                cursor.execute(query, (f"%{termino.lower()}%",))
            
            resultados = cursor.fetchall()
            if resultados:
                for paciente in resultados:
                    print(paciente)
            else:
                print("No se encontraron pacientes con los criterios especificados.")
        except Exception as e:
            print(f"Error en la búsqueda de pacientes: {e}")
        finally:
            Conectar.close()
