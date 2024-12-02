import tkinter as tk
from tkinter import messagebox
from paciente import Paciente
from medico import Medicos
from turnos import turno
from conexion import BaseDeDatos

# Conectar a la base de datos
db = BaseDeDatos("localhost", "root", "1234", "GestionHospital")
paciente_db = Paciente(db)
medico_db = Medicos(db)
turno_db = turno(db)

def mostrar_menu_principal():

    # Implementación de funciones aquí
    def gestion_de_paciente():

        
        def mostrar_registro_paciente():
            ventana = tk.Toplevel()
            ventana.title("Registrar paciente")

            tk.Label(ventana, text="Nombre y Apellido:").grid(row=1, column=0)
            Nombre_Apellido_entry = tk.Entry(ventana)
            Nombre_Apellido_entry.grid(row=1, column=1)

            tk.Label(ventana, text="Teléfono:").grid(row=2, column=0)
            telefono_entry = tk.Entry(ventana)
            telefono_entry.grid(row=2, column=1)

            tk.Label(ventana, text="Dirección:").grid(row=4, column=0)
            direccion_entry = tk.Entry(ventana)
            direccion_entry.grid(row=3, column=1)

            tk.Label(ventana, text="Fecha De Nacimiento:").grid(row=3, column=0)
            FDN_entry = tk.Entry(ventana)
            FDN_entry.grid(row=4, column=1)

            def registrar_paciente():
                IDPaciente = Paciente.generar_siguiente_id()
                nombreyapellido = Nombre_Apellido_entry.get()
                telefono = telefono_entry.get()
                Fechadenacimiento = FDN_entry.get()
                direccion = direccion_entry.get()

                paciente_db.registrar_paciente(IDPaciente, nombreyapellido, telefono, Fechadenacimiento, direccion)
                messagebox.showinfo("Éxito", "paciente registrado con éxito.")
                ventana.destroy()

            tk.Button(ventana, text="Registrar", command=registrar_paciente).grid(row=5, columnspan=2)

        def mostrar_actualizacion_paciente():
            ventana = tk.Toplevel()
            ventana.title("Actualizar paciente")

            listbox = tk.Listbox(ventana, width=60)
            listbox.pack()

            pacientes = paciente_db.ver_pacientes()
            for paciente in pacientes:
                listbox.insert(tk.END, f"{paciente[0]} - {paciente[1]} {paciente[2]}")

            def actualizar_paciente():
                seleccion = listbox.curselection()
                if not seleccion:
                    messagebox.showwarning("Seleccionar paciente", "Debe seleccionar un paciente para actualizar.")
                    return
                paciente_id = pacientes[seleccion[0]][0]

        # Obtener los datos actuales del paciente
                paciente_actual = paciente_db.ver_paciente(paciente_id)[0]

        # Ventana para actualizar los datos del paciente seleccionado
                actualizacion_ventana = tk.Toplevel()
                actualizacion_ventana.title("Actualizar Datos del paciente")

                tk.Label(actualizacion_ventana, text="ID paciente:").grid(row=0, column=0)
                IDpaciente_entry = tk.Entry(actualizacion_ventana)
                IDpaciente_entry.insert(0, paciente_actual[1])  
                IDpaciente_entry.grid(row=0, column=1)

                tk.Label(actualizacion_ventana, text="Nombre y Apellido:").grid(row=1, column=0)
                Nombre_Apellido_entry = tk.Entry(actualizacion_ventana)
                Nombre_Apellido_entry.insert(0, paciente_actual[2])  
                Nombre_Apellido_entry.grid(row=1, column=1)

                tk.Label(actualizacion_ventana, text="Teléfono:").grid(row=2, column=0)
                telefono_entry = tk.Entry(actualizacion_ventana)
                telefono_entry.insert(0, paciente_actual[3])  # Teléfono actual
                telefono_entry.grid(row=2, column=1)

                tk.Label(actualizacion_ventana, text="Fecha De Nacimiento:").grid(row=3, column=0)
                FDN_entry = tk.Entry(actualizacion_ventana)
                FDN_entry.insert(0, paciente_actual[4])  # Fechadenacimiento actual
                FDN_entry.grid(row=3, column=1)

                tk.Label(actualizacion_ventana, text="Dirección:").grid(row=4, column=0)
                direccion_entry = tk.Entry(actualizacion_ventana)
                direccion_entry.insert(0, paciente_actual[5])  # Dirección actual
                direccion_entry.grid(row=4, column=1)

                def guardar_cambios():
                    paciente_id = IDpaciente_entry.get()
                    nombreyapellido = Nombre_Apellido_entry.get()
                    telefono = telefono_entry.get()
                    Fechadenacimiento = FDN_entry.get()
                    direccion = direccion_entry.get()
            
                    paciente_db.actualizar_paciente(paciente_id, nombreyapellido, telefono, Fechadenacimiento, direccion)
                    messagebox.showinfo("Éxito", "paciente actualizado con éxito.")
                    actualizacion_ventana.destroy()

                    tk.Button(actualizacion_ventana, text="Guardar Cambios", command=guardar_cambios).grid(row=5, columnspan=2)

                tk.Button(ventana, text="Actualizar paciente Seleccionado", command=actualizar_paciente).pack()

        def mostrar_eliminacion_paciente():
            ventana = tk.Toplevel()
            ventana.title("Eliminar paciente")

            listbox = tk.Listbox(ventana, width=60)
            listbox.pack()

            pacientes = paciente_db.ver_pacientes()
            for paciente in pacientes:
                listbox.insert(tk.END, f"{paciente[0]} - {paciente[1]} {paciente[2]}")

            def eliminar_paciente():
                seleccion = listbox.curselection()
                if not seleccion:
                    messagebox.showwarning("Seleccionar paciente", "Debe seleccionar un paciente para eliminar.")
                    return
                paciente_id = pacientes[seleccion[0]][0]

                paciente_db.eliminar_paciente(paciente_id)
                messagebox.showinfo("Éxito", "paciente eliminado con éxito.")
                listbox.delete(seleccion)

            tk.Button(ventana, text="Eliminar paciente Seleccionado", command=eliminar_paciente).pack()

        def mostrar_pacientes():
            ventana = tk.Toplevel()
            ventana.title("Ver pacientes")
    
            listbox = tk.Listbox(ventana, width=60)
            listbox.pack()

            for paciente in paciente_db.ver_pacientes():
                listbox.insert(tk.END, f"{paciente[0]} - {paciente[1]} {paciente[2]}")
            btn_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
            btn_salir.pack()

        # Ventana principal
        root = tk.Tk()
        root.title("Gestión de pacientes")

        reg_paciente = tk.Button(root, text="Registrar paciente", command=mostrar_registro_paciente)
        reg_paciente.grid(row=0, column=0)
        act_paciente = tk.Button(root, text="Actualizar paciente", command=mostrar_actualizacion_paciente)
        act_paciente.grid(row=1, column=0)
        eli_paciente = tk.Button(root, text="Eliminar paciente", command=mostrar_eliminacion_paciente)
        eli_paciente.grid(row=2, column=0)
        ver_pacientes = tk.Button(root, text="Ver pacientes", command=mostrar_pacientes)
        ver_pacientes.grid(row=3, column=0)
        root.mainloop()
    
    def gestion_de_medico():
        

        def mostrar_agregar_medico():
            ventana = tk.Toplevel()
            ventana.title("Agregar medico")

            tk.Label(ventana, text="Nombre y Apellido:").grid(row=1, column=0)
            Nombre_Apellido_entry = tk.Entry(ventana)
            Nombre_Apellido_entry.grid(row=1, column=1)

            tk.Label(ventana, text="Especialidad:").grid(row=2, column=0)
            especialidad_entry = tk.Entry(ventana)
            especialidad_entry.grid(row=2, column=1)

            tk.Label(ventana, text="Telefono:").grid(row=3, column=0)
            telefono_entry = tk.Entry(ventana)
            telefono_entry.grid(row=3, column=1)

            def agregar_medico():
                medico_id = Medicos.generar_siguiente_id()
                nombreyapellido = Nombre_Apellido_entry.get()
                especialidad = especialidad_entry.get()
                telefono = telefono_entry.get()

                medico_db.registrar_Medico(medico_id,nombreyapellido, especialidad, telefono)
                messagebox.showinfo("Éxito", "medico agregado con éxito.")
                ventana.destroy()

            tk.Button(ventana, text="Agregar medico", command=agregar_medico).grid(row=4, columnspan=2)
        
        def mostrar_actualizacion_medico():
            ventana = tk.Toplevel()
            ventana.title("Actualizar medico")

            listbox = tk.Listbox(ventana, width=60)
            listbox.pack()

            medicos = medico_db.ver_Medicos()
            for medico in medicos:
                listbox.insert(tk.END, f"{medico[0]} - {medico[1]} {medico[2]}")

            def actualizar_medico():
                seleccion = listbox.curselection()
                if not seleccion:
                    messagebox.showwarning("Seleccionar medico", "Debe seleccionar un medico para actualizar.")
                    return
                medico_id = medicos[seleccion[0]][0]

                medico_actual=medico_db.ver_Medicos(medico_id)[0]
                
                actualizacion_ventana=tk.Toplevel()
                actualizacion_ventana.title("Actualizar Datos del medico")

                tk.Label(actualizacion_ventana, text="ID medico:").grid(row=0, column=0)
                IDmedico_entry = tk.Entry(actualizacion_ventana, text=medico_actual[0])
                IDmedico_entry.grid(row=0, column=1)
                
                tk.Label(actualizacion_ventana, text="Nombre y Apellido:").grid(row=1, column=0)
                Nombre_Apellido_entry = tk.Entry(actualizacion_ventana)
                Nombre_Apellido_entry.insert(0,medico_actual[1])
                Nombre_Apellido_entry.grid(row=1, column=1)

                tk.Label(actualizacion_ventana, text="Especialidad:").grid(row=2, column=0)
                especialidad_entry = tk.Entry(actualizacion_ventana)
                especialidad_entry.insert(0,medico_actual[2])
                especialidad_entry.grid(row=2, column=1)
                
                tk.Label(actualizacion_ventana, text="Telefono:").grid(row=3, column=0)
                telefono_entry = tk.Entry(actualizacion_ventana)
                telefono_entry.insert(0,medico_actual[3])
                telefono_entry.grid(row=3, column=1)

                def guardar_cambios():
                    medico_id = IDmedico_entry.get()
                    nombreyapellido = Nombre_Apellido_entry.get()
                    especialidad = especialidad_entry.get()
                    telefono = telefono_entry.get()

                    medico_db.actualizar_Medico(medico_id, nombreyapellido, especialidad, telefono)
                    messagebox.showinfo("Éxito", "medico actualizado con éxito.")
                    actualizacion_ventana.destroy()

                    tk.Button(actualizacion_ventana, text="Guardar Cambios", command=guardar_cambios).grid(row=4, columnspan=2)

            tk.Button(ventana, text="Actualizar paciente Seleccionado", command=actualizar_medico).pack()
            
        def mostrar_medico():
            ventana=tk.Toplevel()
            ventana.title("Ver medicos")

            listbox = tk.Listbox(ventana, width=60)
            listbox.pack()

            for medico in medico_db.ver_Medicos():
                listbox.insert(tk.END, f"{medico[0]} - {medico[1]} {medico[2]}")
            btn_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
            btn_salir.pack()
            
            #ventana principal
        root = tk.Tk()
        root.title("Gestión de medicos")

        agr_medico = tk.Button(root, text="Agregar medico", command=mostrar_agregar_medico)
        agr_medico.grid(row=0, column=0)
        act_medico = tk.Button(root, text="Actualizar medico", command=mostrar_actualizacion_medico)
        act_medico.grid(row=1, column=0)
        ver_medicos = tk.Button(root, text="Ver medicos", command=mostrar_medico)
        ver_medicos.grid(row=2, column=0)
        root.mainloop()


    def gestion_de_turnos():

        def mostrar_programar_turno():
            ventana = tk.Toplevel()
            ventana.title("Programar turno")

            tk.Label(ventana, text="Nombre del paciente:").grid(row=0, column=0)
            nombreyapellido_entry = tk.Entry(ventana)
            nombreyapellido_entry.grid(row=0, column=1)

            tk.Label(ventana, text="Nombre del medico:").grid(row=1, column=0)
            NombreMedico_entry = tk.Entry(ventana)
            NombreMedico_entry.grid(row=1, column=1)

            tk.Label(ventana, text="Fecha:").grid(row=2, column=0)
            fecha_entry = tk.Entry(ventana)
            fecha_entry.grid(row=2, column=1)

            tk.Label(ventana, text="Hora:").grid(row=3,column=0)
            hora_entry = tk.Entry(ventana)
            hora_entry.grid(row=3, column=1)

            def programar_turno():
                nombreyapellido = nombreyapellido_entry.get() 
                IDPaciente = paciente_db.GetIDPaciente(nombreyapellido)
                NombreMedico = NombreMedico_entry.get()
                IDmedico = medico_db.GetIDMedico(NombreMedico)
                fecha = fecha_entry.get()
                hora = hora_entry.get()

                turno_db.programar_turno(IDPaciente, IDmedico, fecha, hora)
                messagebox.showinfo("Éxito", "Turno programado con éxito.")
                ventana.destroy()

            tk.Button(ventana, text="Programar turno", command=programar_turno).grid(row=4, columnspan=2)

        def mostrar_actualizar_turno():
            ventana = tk.Toplevel()
            ventana.title("Actualizar turno")

            listbox = tk.Listbox(ventana, width=60)
            listbox.pack()

            turnos = turno_db.ver_turnos()
            for turno in turnos:
                listbox.insert(tk.END, f"{turno[0]} - {turno[1]} {turno[2]} - {turno[3]} - {turno[4]}")

            def actualizar_turno():
                seleccion = listbox.curselection()
                if not seleccion:
                    messagebox.showerror("Error", "Debe seleccionar un turno.")
                    return
                turno_id = turnos[seleccion[0]][0]

                turno_actual = turno_db.ver_turno(turno_id)[0]
                
                actualizar_ventana = tk.Toplevel()
                actualizar_ventana.title("Actualizar turno")

                tk.Label(actualizar_ventana, text="Turno ID:").grid(row=0, column=0)
                IDturno_entry = tk.Entry(actualizar_ventana)
                IDturno_entry.insert(0, turno_actual[0])
                IDturno_entry.grid(row=0, column=1)

                tk.Label(actualizar_ventana, text="ID paciente:").grid(row=1, column=0)
                IDpaciente_entry = tk.Entry(actualizar_ventana)
                IDpaciente_entry.insert(0, turno_actual[1])
                IDpaciente_entry.grid(row=1, column=1)

                tk.Label(actualizar_ventana, text="ID medico:").grid(row=2, column=0)
                IDmedico_entry = tk.Entry(actualizar_ventana)
                IDmedico_entry.insert(0, turno_actual[2])
                IDmedico_entry.grid(row=2, column=1)

                tk.Label(actualizar_ventana, text="Fecha:").grid(row=3, column=0)
                fecha_entry = tk.Entry(actualizar_ventana)
                fecha_entry.insert(0, turno_actual[3])
                fecha_entry.grid(row=3, column=1)

                tk.Label(actualizar_ventana, text="Hora:").grid(row=4, column=0)
                hora_entry = tk.Entry(actualizar_ventana)
                hora_entry.insert(0, turno_actual[4])
                hora_entry.grid(row=4, column=1)

                def guardar_cambios():
                    turno_db.actualizar_turno(turno_id, IDpaciente_entry.get(), IDmedico_entry.get(), fecha_entry.get(), hora_entry.get())
                    messagebox.showinfo("Éxito", "Turno actualizado con éxito.")
                    actualizar_ventana.destroy()

                    tk.Button(actualizar_ventana, text="Guardar Cambios", command=guardar_cambios).grid(row=5, column=0)
                
                tk.Button(actualizar_ventana, text="Salir", command=actualizar_turno).pack()

        def mostrar_cancelar_turno():
            ventana = tk.Toplevel()
            ventana.title("Cancelar turnos")

            listbox = tk.Listbox(ventana, width=60)
            listbox.pack()

            turnos = turno_db.ver_turnos()
            for turno in turnos:
                listbox.insert(tk.END, f"{turno[0]} - {turno[1]} {turno[2]} - {turno[3]} - {turno[4]}")
                
            def cancelar_turno():
                seleccion = listbox.curselection()
                if not seleccion:
                    messagebox.showerror("Error", "Debe seleccionar un turno.")
                    return
                turno_id = turnos[seleccion[0]][0]

                turno_db.eliminar_turno(turno_id)
                messagebox.showinfo("Éxito", "Turno cancelado con éxito.")
                listbox.delete(seleccion)

                tk.Button(ventana, text="Cancelar Turno", command=cancelar_turno).pack()
            
        root = tk.Tk()
        root.title("Gestión de turnos")

        pro_turno = tk.Button(root, text="Programar Turno", command= mostrar_programar_turno)
        pro_turno.grid(row=0, column=0)
        act_turno = tk.Button(root, text="ActualizarTurno", command=mostrar_actualizar_turno)
        act_turno.grid(row=1,column=0)
        can_turnos = tk.Button(root, text="Cancelar turnos", command=mostrar_cancelar_turno)
        can_turnos.grid(row=2, column=0)
        root.mainloop()
    
    def busqueda_avanzada():

        def mostrar_busqueda_pXnombreyapellido():
            ventana = tk.Toplevel()
            ventana.title("Buscar paciente por nombre y apellido")

            listbox = tk.ListBox(ventana, width=60)
            listbox.pack()
            nombreyapellido = tk.Entry(ventana)
            pacientes = paciente_db.buscar_paciente_por_nombreyapellido(nombreyapellido.get(), "%")
            for paciente in pacientes:
                listbox.insert(tk.END, f"{paciente[0]} - {paciente[1]} {paciente[2]} - {paciente[3]}")
            btn_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
            btn_salir.pack()

        def mostrar_buscar_pXid():
            pass
         
        def mostrar_buscar_mXnombreyapellido():
            ventana = tk.Toplevel()
            ventana.title("Buscar medico por nombre y apellido")

            listbox = tk.ListBox(ventana, width=60)
            listbox.pack()
            nombreyapellido = tk.Entry(ventana)
            medicos = medico_db.buscar_Medico_por_nombre(nombreyapellido.get(), "%")
            for medico in medicos:
                listbox.insert(tk.END, f"{medico[0]} - {medico[1]} {medico[2]} - {medico[3]} - {medico[4]}")
            btn_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
            btn_salir.pack()

        def mostrar_buscar_mXespecialidad():
            ventana = tk.Toplevel()
            ventana.title("Buscar medico por ID")

            listbox = tk.ListBox(ventana, width=60)
            listbox.pack()

            especialidad = tk.Entry(ventana)
            medicos = medico_db.buscar_Medicos_por_especialidad(especialidad.get())
            for medico in medicos:
                listbox.insert(tk.END, f"{medico[0]} - {medico[1]} {medico[2]} - {medico[3]} - {medico[4]}")
            btn_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
            btn_salir.pack()

        root = tk.Tk()
        root.title("Gestión de turnos")

        bus_Pnombre = tk.Button(root, text="Buscar paciente po nombre y apellido", command=mostrar_busqueda_pXnombreyapellido)
        bus_Pnombre.grid(row=0, column=0)
        bus_PID = tk.Button(root, text="Buscar paciente por ID", command=mostrar_buscar_pXid)
        bus_PID.grid(row=1, column=0)
        bus_Mnombre = tk.Button(root, text="Buscar medico por nombre y apellido", command=mostrar_buscar_mXnombreyapellido)
        bus_Mnombre.grid(row=2, column=0)
        bus_Mespecialidad = tk.Button(root, text="Buscar medico por especialidad", command=mostrar_buscar_mXespecialidad)
        bus_Mespecialidad.grid(row=3, column=0)
        root.mainloop()

    def reporte_de_turnos():
        pass
    
    def cancelacion_de_turnos():
        pass
    
    ventana = tk.Tk()
    ventana.title("Menú Principal")
    lbl_menu = tk.Label(ventana, text="Menú Principal")
    lbl_menu.pack()
    lbl_menu_principal = tk.Label(ventana, text="Seleccione una opción:")
    lbl_menu_principal.pack()
    btn_reg_paciente = tk.Button(ventana, text="Gestion de Pacientes", command=gestion_de_paciente)
    btn_reg_paciente.pack()
    btn_act_paciente = tk.Button(ventana, text="Gestion de medico", command=gestion_de_medico)
    btn_act_paciente.pack()
    btn_eli_paciente = tk.Button(ventana, text="Gestion de Turnos", command=gestion_de_turnos)
    btn_eli_paciente.pack()
    btn_ver_pacientes = tk.Button(ventana, text="Búsquedas Avanzadas", command=busqueda_avanzada)
    btn_ver_pacientes.pack()
    btn_reporte_turnos = tk.Button(ventana, text="Reporte de Turnos", command=reporte_de_turnos)
    btn_reporte_turnos.pack()
    btn_cancelacion_turnos = tk.Button(ventana, text="Cancelación de Turnos", command=cancelacion_de_turnos)
    btn_cancelacion_turnos.pack()
    btn_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
    btn_salir.pack()
    ventana.mainloop()
        


if __name__ == '__main__':
    db = BaseDeDatos("localhost", "root", "1234", "GestionHospital")
    db.conectar()  # Inicializa la conexión
    pacientes = paciente_db.ver_pacientes()  # Usa la conexión activa
    print(pacientes)
    db.desconectar()  # Cierra la conexión al final
