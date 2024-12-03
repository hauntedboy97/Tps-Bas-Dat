from Rutas.Pacientes import registrar_paciente, ver_pacientes, actualizar_paciente, eliminar_paciente, buscar_paciente
from Rutas.Medicos import agregar_medico, actualizar_medico, ver_detalles_medico, buscar_medico
from Rutas.Turnos import programar_turno, actualizar_turno, cancelar_turno, ver_turnos, reporte_turnos, cancelar_por_fecha, cancelar_por_medico

def menu_pacientes():
    while True:
        print("\n---- Gestión de Pacientes ----")
        print("1. Registrar paciente")
        print("2. Ver pacientes")
        print("3. Actualizar paciente")
        print("4. Eliminar paciente")
        print("5. Volver al menú principal")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            ver_pacientes()
        elif opcion == "3":
            actualizar_paciente()
        elif opcion == "4":
            eliminar_paciente()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def menu_medicos():
    while True:
        print("\n---- Gestión de Médicos ----")
        print("1. Agregar médico")
        print("2. Ver detalles de médicos")
        print("3. Actualizar médico")
        print("4. Volver al menú principal")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del médico: ")
            especialidad = input("Ingrese la especialidad del médico: ")
            telefono = input("Ingrese el teléfono del médico: ")
            agregar_medico(nombre, especialidad, telefono)
        elif opcion == "2":
            ver_detalles_medico()
        elif opcion == "3":
            id_medico = int(input("Ingrese el ID del médico a actualizar: "))
            nuevo_nombre = input("Ingrese el nuevo nombre del médico: ")
            nueva_especialidad = input("Ingrese la nueva especialidad del médico: ")
            nuevo_telefono = input("Ingrese el nuevo telefono del médico: ")
            actualizar_medico(id_medico, nuevo_nombre, nueva_especialidad, nuevo_telefono)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


def menu_turnos():
    while True:
        print("\n---- Gestión de Turnos ----")
        print("1. Programar turno")
        print("2. Ver turnos")
        print("3. Actualizar turno")
        print("4. Cancelar turno")
        print("5. Volver al menú principal")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            fecha = input("Ingrese la fecha (formato YYYY-MM-DD): ")
            horario = input("Ingrese el horario (formato HH:MM): ")
            id_paciente = int(input("Ingrese el ID del paciente: "))
            id_medico = int(input("Ingrese el ID del médico: "))
            programar_turno(fecha, horario, id_paciente, id_medico)
        elif opcion == "2":
            ver_turnos()
        elif opcion == "3":
            id_turno = int(input("Ingrese el ID del turno a actualizar: "))
            nueva_fecha = input("Ingrese la nueva fecha (formato YYYY-MM-DD): ")
            nuevo_horario = input("Ingrese el nuevo horario (formato HH:MM): ")
            actualizar_turno(id_turno, nueva_fecha, nuevo_horario)
        elif opcion == "4":
            id_turno = int(input("Ingrese el ID del turno a cancelar: "))
            cancelar_turno(id_turno)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def menu_cancelacion_turnos():
    while True:
        print("\n---- Cancelación de Turnos ----")
        print("1. Cancelar turnos por fecha")
        print("2. Cancelar turnos por médico")
        print("3. Volver al menú principal")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            fecha = input("Ingrese la fecha de los turnos a cancelar (formato YYYY-MM-DD): ")
            cancelar_por_fecha(fecha)
        elif opcion == "2":
            idMedico = int(input("Ingrese el ID del médico cuyos turnos desea cancelar: "))
            cancelar_por_medico(idMedico)
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def menu_busquedas():
    while True:
        print("\n---- Búsquedas ----")
        print("1. Buscar paciente")
        print("2. Buscar médico")
        print("3. Volver al menú principal")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\n¿A qué atributo del paciente desea buscar?")
            print("1. Nombre")
            print("2. ID de paciente")
            atributo_opcion = input("Selecciona el número del atributo a buscar: ")
            
            if atributo_opcion == "1":
                atributo = "nombrePaciente"
            elif atributo_opcion == "2":
                atributo = "idPaciente"
            else:
                print("Opción no válida. Volviendo al menú de búsquedas...")
                continue

            termino = input("Ingrese el valor a buscar: ")
            buscar_paciente(atributo, termino)  # Pasamos atributo y termino
        elif opcion == "2":
            print("\n¿A qué atributo del médico desea buscar?")
            print("1. Nombre")
            print("2. Especialidad")
            print("3. ID de médico")
            atributo_opcion = input("Selecciona el número del atributo a buscar: ")
            
            if atributo_opcion == "1":
                atributo = "nombreMedico"
            elif atributo_opcion == "2":
                atributo = "especialidad"
            elif atributo_opcion == "3":
                atributo = "idMedico"
            else:
                print("Opción no válida. Volviendo al menú de búsquedas...")
                continue

            termino = input("Ingrese el valor a buscar: ")
            buscar_medico(atributo, termino)  
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


def menu_principal():
    while True:
        print("\n---- Menú Principal ----")
        print("1. Pacientes")
        print("2. Médicos")
        print("3. Turnos")
        print("4. Búsquedas")
        print("5. Reporte de Turnos")
        print("6. Cancelación de Turnos")
        print("7. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_pacientes()
        elif opcion == "2":
            menu_medicos()
        elif opcion == "3":
            menu_turnos()
        elif opcion == "4":
            menu_busquedas()
        elif opcion == "5":
            reporte_turnos()
        elif opcion == "6":
            menu_cancelacion_turnos()
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()