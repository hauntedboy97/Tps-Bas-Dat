from paciente import paciente
from medico import Medicos
pacientes = []


def menuprincipal():
    estado = True
    while estado:
        print("\nMenu principal: ")
        print("1. Gestión de Pacientes")
        print("2. Gestión de Doctores")
        print("3. Manejo de Turnos")
        print("4. Búsquedas Avanzadas")
        print("5. Reporte de turnos")
        print("6. Cancelación de turnos:")
        print("7. Salir del programa:")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestion_pacientes()
        elif opcion == "2":
            gestion_doctores()
        elif opcion == "3":
            manejo_turnos()
        elif opcion == "4":
            busqueda_avanzada()
        elif opcion == "5":
            reporte_turnos()
        elif opcion == "6":
            cancelacion_de_turnos()
        elif opcion == "7":
            estado = False
            break
        else:
            print("Opción no válida. Intente de nuevo.")



def gestion_pacientes():
    while True:
        print("\nGestión de Pacientes")
        print("1. Registrar Paciente")
        print("2. Actualizar Paciente")
        print("3. Ver Paciente")
        print("4. Eliminar Paciente")
        print("5. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            paciente.registrar_paciente()
        elif opcion == "2":
            paciente.actualizar_paciente()
        elif opcion == "3":
            paciente.ver_paciente()
        elif opcion == "4":
            paciente.eliminar_paciente()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def gestion_doctores():
    # Implementación de gestión de doctores aquí Agregar, actualizar y ver detalles de los doctores, incluyendo especialidades.
    while True:
        print("\nGestión de Doctores")
        print("1. Agregar Doctores")
        print("2. Actualizar Doctores")
        print("3. Ver Doctores")
        print("4. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            Medicos.registrar_Medico()
        elif opcion == "2":
            Medicos.actualizar_Medico()
        elif opcion == "3":
            Medicos.ver_Medicos()
        elif opcion == "4":
            menuprincipal()
            
        else:
            print("Opción no válida. Intente de nuevo.")

def manejo_turnos():
    # Implementación de manejo de turnos aquí Programar, actualizar o cancelar turnos.
    while True:
        print("\nGestión de Turnos")
        print("1. Programar turno")
        print("2. Actualizar turno")
        print("3. Cancelar turno")
        print("4. Volver al Menú Principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            paciente.programar_turno()
        elif opcion == "2":
            paciente.actualizar_turno()
        elif opcion == "3":
            paciente.cancelar_turno()
        elif opcion == "4":
            menuprincipal()
        


def busqueda_avanzada():
    # Implementación de búsquedas avanzadas aquí Recuperar pacientes o médicos mediante diferentes atributos (nombre, especialidad, ID de paciente)
    pass

def reporte_turnos():
    # Implementación de reporte de turnos aquí  Mostrar un reporte donde muestre los tres médicos que más turnos tienen y la cantidad de turnos de cada uno
    pass

def cancelacion_de_turnos():
    # Implementación de cancelación de turnos aquí Se debe poder cancelar para un médico dado y un rango de fechas dado
    pass


if __name__ == '__main__':
    menuprincipal()