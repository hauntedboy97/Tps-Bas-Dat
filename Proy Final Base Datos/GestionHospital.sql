
-- Sistema de Gestión de Hospital

-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS GestionHospital;
USE GestionHospital;

-- Tabla de Pacientes
CREATE TABLE Pacientes (
    paciente_id INT AUTO_INCREMENT PRIMARY KEY,
    nombreyapellido VARCHAR(100) NOT NULL,
    direccion VARCHAR(150) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    fecha_nacimiento DATE NOT NULL
);

-- Tabla de Médicos
CREATE TABLE Medicos (
    medico_id INT AUTO_INCREMENT PRIMARY KEY,
    nombreyapellido VARCHAR(100) NOT NULL,
    especialidad VARCHAR(50) NOT NULL,
    telefono VARCHAR(15) NOT NULL
);

-- Tabla de Turnos
CREATE TABLE Turnos (
    turno_id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT NOT NULL,
    medico_id INT NOT NULL,
    fecha DATE NOT NULL,
    horario TIME NOT NULL,
    FOREIGN KEY (paciente_id) REFERENCES Pacientes(paciente_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (medico_id) REFERENCES Medicos(medico_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

-- Datos iniciales para la tabla Pacientes
INSERT INTO Pacientes (nombreyapellido, direccion, telefono, fecha_nacimiento) VALUES
('Juan Pérez', 'Calle 123', '123456789', '1980-01-01'),
('Ana Gómez', 'Avenida 456', '987654321', '1990-02-02'),
('Luis Torres', 'Boulevard 789', '123123123', '1985-03-03'),
('Maria Lopez', 'Calle Falsa 456', '321321321', '1992-04-04'),
('Carlos Martínez', 'Calle Real 789', '654654654', '1988-05-05'),
('Laura Garcia', 'Avenida Central 123', '789789789', '1995-06-06'),
('Ricardo Rodriguez', 'Calle Sur 456', '456456456', '1983-07-07'),
('Paula Fernandez', 'Calle Este 789', '789123456', '1991-08-08'),
('Jorge Morales', 'Calle Norte 123', '456789123', '1989-09-09'),
('Elena Ruiz', 'Calle Oeste 456', '321654987', '1993-10-10');

-- Datos iniciales para la tabla Medicos
INSERT INTO Medicos (nombreyapellido, especialidad, telefono) VALUES
('Dr. Juan Gonzalez', 'Cardiología', '123123123'),
('Dra. Maria Martinez', 'Neurología', '234234234'),
('Dr. Carlos Fernandez', 'Pediatría', '345345345'),
('Dr. Luis Lopez', 'Ortopedia', '567567567'),
('Dra. Ana Jimenez', 'Dermatología', '678678678'),
('Dr. Pedro Sanchez', 'Psiquiatría', '789789789'),
('Dra. Laura Castillo', 'Endocrinología', '890890890'),
('Dr. Miguel Rojas', 'Oftalmología', '901901901'),
('Dra. Sofia Suarez', 'Urología', '101101101');


-- Datos iniciales para la tabla Turnos
INSERT INTO Turnos (paciente_id, medico_id, fecha, horario) VALUES
(1, 1, '2024-11-10', '09:00:00'),
(2, 2, '2024-11-11', '10:00:00'),
(3, 3, '2024-11-12', '11:00:00'),
(4, 4, '2024-11-13', '12:00:00'),
(5, 5, '2024-11-14', '13:00:00'),
(6, 6, '2024-11-15', '14:00:00'),
(7, 7, '2024-11-16', '15:00:00'),
(8, 8, '2024-11-17', '16:00:00'),
(9, 9, '2024-11-18', '17:00:00'),
(10, 10, '2024-11-19', '18:00:00');
