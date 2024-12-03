DROP DATABASE IF EXISTS GestionHospital;

CREATE DATABASE GestionHospital;
USE GestionHospital;

CREATE TABLE pacientes (
    idPaciente INT AUTO_INCREMENT PRIMARY KEY,
    nombrePaciente VARCHAR(100) UNIQUE NOT NULL,
    edad INT NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    telefonoPaciente VARCHAR(15) NOT NULL
);
CREATE INDEX idx_nombrePaciente ON Pacientes (nombrePaciente);


CREATE TABLE medicos (
    idMedico INT AUTO_INCREMENT PRIMARY KEY,
    nombreMedico VARCHAR(100) UNIQUE NOT NULL,
    especialidad VARCHAR(100) NOT NULL,
    telefonoMedico VARCHAR(15) NOT NULL
);
CREATE INDEX idx_especialidad ON Medicos (especialidad);
CREATE INDEX idx_telefonoMedico ON Medicos (telefonoMedico);



CREATE TABLE turnos (
    idTurnos INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    horario TIME NOT NULL,
    idPaciente INT NOT NULL,
    idMedico INT NOT NULL,
    UNIQUE (idMedico, fecha, horario), 
    UNIQUE (idPaciente, fecha, horario), 
    FOREIGN KEY (idPaciente) REFERENCES Pacientes(idPaciente) ON DELETE RESTRICT,
    FOREIGN KEY (idMedico) REFERENCES Medicos(idMedico) ON DELETE RESTRICT
);
CREATE INDEX idx_idPaciente ON Turnos (idPaciente);
CREATE INDEX idx_idMedico ON Turnos (idMedico);
CREATE INDEX idx_fecha_horario ON Turnos (fecha, horario);


INSERT INTO pacientes (nombrePaciente, edad, direccion, telefonoPaciente) VALUES
('Juan Pérez', 35, 'Calle Falsa 123', '123456789'),
('Ana López', 28, 'Av. Siempreviva 742', '987654321'),
('Carlos García', 45, 'Calle 8 No. 12', '456123789'),
('Lucía Martínez', 31, 'Boulevard del Sol', '789456123'),
('Marta Gómez', 40, 'Calle Luna', '321654987'),
('Roberto Díaz', 50, 'Calle Estrella', '654987321'),
('Florencia Ruiz', 29, 'Avenida del Mar', '987321654'),
('Santiago Ortega', 60, 'Calle Río', '159753468'),
('María Torres', 22, 'Avenida del Lago', '753159486'),
('Diego Fernández', 38, 'Calle Valle', '468753159');

INSERT INTO medicos (nombreMedico, especialidad, telefonoMedico) VALUES
('Dr. Martínez', 'Cardiología', '1122334455'),
('Dra. Fernández', 'Pediatría', '5566778899'),
('Dr. Gómez', 'Dermatología', '2233445566'),
('Dra. López', 'Neurología', '3344556677'),
('Dr. Sánchez', 'Ortopedia', '4455667788'),
('Dra. Pérez', 'Gastroenterología', '5566778899'),
('Dr. Morales', 'Endocrinología', '6677889900'),
('Dra. Ramírez', 'Oncología', '7788990011'),
('Dr. Ortega', 'Ginecología', '8899001122'),
('Dra. Torres', 'Urología', '9900112233');

INSERT INTO turnos (fecha, horario, idPaciente, idMedico) VALUES
('2024-12-01', '10:00:00', 1, 1),
('2024-12-01', '11:00:00', 2, 2),
('2024-12-01', '12:00:00', 3, 3),
('2024-12-02', '09:00:00', 4, 4),
('2024-12-02', '10:00:00', 5, 5),
('2024-12-02', '11:00:00', 6, 6),
('2024-12-03', '09:30:00', 7, 7),
('2024-12-03', '10:30:00', 8, 8),
('2024-12-03', '11:30:00', 9, 9),
('2024-12-03', '12:30:00', 10, 10);