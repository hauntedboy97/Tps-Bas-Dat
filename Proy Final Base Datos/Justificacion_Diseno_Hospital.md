
# Justificación del Diseño - Sistema de Gestión de Hospital

## Descripción General del Proyecto

Este proyecto consiste en el diseño e implementación de un sistema de gestión de hospital que incluye la administración de pacientes, médicos y turnos de consultas médicas. La base de datos debe estar normalizada hasta la Tercera Forma Normal (3NF) para asegurar la integridad y optimización de la información.

## Modelo del Sistema

### Entidades Principales y Relaciones

1. **Pacientes**:
   - Representa a cada paciente del hospital.
   - Atributos: ID del paciente, nombre, dirección, teléfono, fecha de nacimiento.

2. **Médicos**:
   - Representa a cada médico que ofrece servicios en el hospital.
   - Atributos: ID del médico, nombre, especialidad, teléfono.

3. **Turnos**:
   - Representa cada turno de consulta médica que puede ser programado entre un paciente y un médico.
   - Atributos: ID del turno, ID del paciente, ID del médico, fecha, horario.

### Relaciones y Cardinalidades

- **Pacientes-Turnos**: Un paciente puede tener varios turnos a lo largo del tiempo, pero cada turno está asignado a un solo paciente. Relación de uno a muchos.
- **Médicos-Turnos**: Un médico puede atender a varios pacientes en distintos turnos, y cada turno está asignado a un solo médico. Relación de uno a muchos.

## Justificación de la Normalización

La base de datos ha sido diseñada en conformidad con las formas normales hasta 3NF para eliminar redundancias y mejorar la integridad de los datos.

1. **Primera Forma Normal (1NF)**: 
   - Todas las tablas contienen datos atómicos, sin grupos repetidos.
   
2. **Segunda Forma Normal (2NF)**: 
   - Todas las tablas cumplen con 1NF, y todos los atributos no clave dependen completamente de la clave primaria.

3. **Tercera Forma Normal (3NF)**: 
   - Se eliminaron las dependencias transitivas, y todos los atributos no clave son independientes entre sí y dependen solo de la clave primaria.

## Restricciones de Integridad

- **Llaves Primarias**: Cada tabla tiene una clave primaria única para identificar cada registro.
- **Llaves Foráneas**: Las relaciones entre tablas se mantienen mediante claves foráneas, garantizando la consistencia de los datos.
- **Restricciones NOT NULL**: Aplicadas en atributos esenciales (como nombres y fechas).
- **Restricciones ÚNICAS**: Garantizan que ciertos atributos (por ejemplo, ID del paciente y del médico) no se repitan.

## Operaciones en Cascada

Para mantener la consistencia referencial, se han definido las siguientes reglas:
- `ON DELETE RESTRICT` para prevenir la eliminación de médicos o pacientes que tengan turnos programados.
- `ON UPDATE CASCADE` para actualizar automáticamente claves foráneas relacionadas en caso de cambios en las tablas principales.

## Índices

Se ha creado un índice en el campo de `especialidad` en la tabla de Médicos para optimizar consultas comunes sobre esta columna.

## Conclusión

El diseño presentado cumple con los requisitos del sistema de gestión hospitalaria, asegurando la integridad, consistencia y optimización de los datos mediante una estructura de base de datos robusta y bien normalizada.
