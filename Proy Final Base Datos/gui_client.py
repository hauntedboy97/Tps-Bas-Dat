import tkinter as tk
from tkinter import messagebox
from paciente import Paciente
from conexion import BaseDeDatos

# Conectar a la base de datos
db = BaseDeDatos("localhost", "root", "BdDI2024", "basededatosi")
db.conectar()
paciente_db = Paciente(db)

def mostrar_registro_paciente():
    ventana = tk.Toplevel()
    ventana.title("Registrar paciente")

    tk.Label(ventana, text="Paciente ID:").grid(row=0, column=0)
    IDpaciente_entry = tk.Entry(ventana)
    IDpaciente_entry.grid(row=0, column=1)

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
        IDpaciente = IDpaciente_entry.get()
        nombreyapellido = Nombre_Apellido_entry.get()
        telefono = telefono_entry.get()
        Fechadenacimiento = FDN_entry.get()
        direccion = direccion_entry.get()

        paciente_db.registrar_paciente(IDpaciente, nombreyapellido, telefono, Fechadenacimiento, direccion)
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
        IDpaciente_entry.insert(0, paciente_actual[1])  # Nombre actual
        IDpaciente_entry.grid(row=0, column=1)

        tk.Label(actualizacion_ventana, text="Nombre y Apellido:").grid(row=1, column=0)
        Nombre_Apellido_entry = tk.Entry(actualizacion_ventana)
        Nombre_Apellido_entry.insert(0, paciente_actual[2])  # Apellido actual
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
            nombre = IDpaciente_entry.get()
            apellido = Nombre_Apellido_entry.get()
            telefono = telefono_entry.get()
            Fechadenacimiento = FDN_entry.get()
            direccion = direccion_entry.get()
            
            paciente_db.actualizar_paciente(paciente_id, nombre, apellido, telefono, Fechadenacimiento, direccion)
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

# Cerrar conexión al final
db.desconectar()
