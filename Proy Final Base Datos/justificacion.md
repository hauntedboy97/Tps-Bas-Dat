**Sistema de Gestión de Hospital**

**Esquema de BD:**

`TURNOS<id_turno, fecha, hora, idPaciente, idMedico, nombrePaciente, direccion_paciente, telefonoPaciente, fecha_nacimiento, nombreMedico, especialidad, telefonoMedico>`

**Restricciones:**

a. El `id_turno` es único para cada turno programado.  
b. Cada paciente tiene un identificador único `idPaciente`, pero sus datos como nombre, dirección y teléfono pueden repetirse en diferentes registros.  
c. Cada médico tiene un identificador único `idMedico` y está asociado a una especialidad específica.  
d. Cada turno está asociado a un único paciente y un único médico en una fecha y hora específicas.  
e. Un paciente puede tener varios turnos asignados con distintos médicos o en diferentes horarios.  
f. Un médico puede tener múltiples turnos asignados, incluso en el mismo día.  



### Paso 1: Determinar las Dependencias Funcionales (DFs)

A partir del esquema y las restricciones dadas, podemos determinar las siguientes dependencias funcionales:

1. **`idTurno -> fecha, hora, idPaciente, idMedico`**: Cada turno tiene un identificador único que determina la fecha, hora, paciente y médico asignado.  
2. **`idPaciente -> nombrePaciente, edad, direccion, telefonoPaciente`**: Cada paciente tiene un identificador único del que dependen todos sus datos personales.  
3. **`idMedico -> nombreMedico, especialidad, telefonoMedico`**: Cada médico tiene un identificador único que determina sus datos personales y su especialidad.  
4. **`idTurno -> fecha, hora, nombrePaciente, nombreMedico`**: Los datos completos del turno dependen del identificador del turno, ya que relaciona pacientes y médicos.  

#ID Turno: 1, Fecha: 01/12/2024, Hora: 10:00 a. m., Paciente: Juan Pérez, Médico: Dr. Martínez

### Paso 2: Determinar las Claves Candidatas

Analizando las dependencias funcionales, observamos que:

- El `idTurno` es suficiente para identificar de forma única cada registro en el esquema.  
- Por lo tanto, la **clave candidata** es: `idTurno`.



### Paso 3: Diseño en Tercera Forma Normal (3FN)

Para eliminar redundancias y cumplir con la 3FN, dividimos la tabla original en tres tablas independientes: `Paciente`, `Medico` y `Turno`.

1. **Tabla `Paciente`**
   - `idPaciente` (Clave primaria)
   - `nombrePaciente`
   - `edad`
   - `direccion`
   - `telefonoPaciente`

2. **Tabla `Medico`**
   - `idMedico` (Clave primaria)
   - `nombreMedico`
   - `especialidad`
   - `telefonoMedico`

3. **Tabla `Turno`**
   - `idTurnos` (Clave primaria)
   - `fecha`
   - `horario`
   - `idPaciente` (Clave foránea que referencia a Paciente)
   - `idMedico` (Clave foránea que referencia a Medico)
