create table Empleados (
    Id INTEGER PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Departamento VARCHAR(50) NOT NULL,
    Salario DECIMAL(10,2) NOT NULL
);
create table Ventas (
    VentaId INTEGER PRIMARY KEY,
    EmpleadoId INT,
    Monto DECIMAL(10,2) NOT NULL,
    FechaVenta DATE NOT NULL,
    FOREIGN KEY (EmpleadoId) REFERENCES Empleados(EmpleadoId)
);
create table Bonificaciones (
    BonificacionId INTEGER PRIMARY KEY,
    EmpleadoId INT,
    MontoBonificacion DECIMAL(10,2) NOT NULL,
    FechaBonificacion DATE NOT NULL,
    FOREIGN KEY (EmpleadoId) REFERENCES Empleados(EmpleadoId)
);

INSERT INTO Empleados (Nombre, Departamento, Salario) VALUES
('Ana García', 'Ventas', 2500.00),
('Carlos López', 'Ventas', 2600.00),
('Elena Ruiz', 'Marketing', 3000.00),
('Javier Fernández', 'Ventas', 2700.00),
('Laura Díaz', 'Ventas', 2900.00),
('Pedro Gómez', 'Administración', 3100.00),
('Marta Sánchez', 'Ventas', 2800.00),
('Juan Martín', 'Ventas', 2650.00),
('Luis Torres', 'Marketing', 3050.00),
('Sara Blanco', 'Ventas', 2750.00);

INSERT INTO Ventas (EmpleadoId, Monto, FechaVenta) VALUES
(1, 5000.00, '2024-09-05'),
(1, 6000.00, '2024-09-20'),
(2, 3000.00, '2024-09-10'),
(2, 8000.00, '2024-09-25'),
(3, 7000.00, '2024-09-15'),
(4, 15000.00, '2024-09-12'),
(5, 4000.00, '2024-09-18'),
(5, 12000.00, '2024-09-22'),
(6, 2000.00, '2024-09-02'),
(7, 13000.00, '2024-09-29');

DELIMITER //
CREATE PROCEDURE CalcularBonificaciones()
BEGIN
    DECLARE EmpleadoIdV INT;
    DECLARE TotalVentasMes DECIMAL(10,2);
    DECLARE Bonificacion DECIMAL(10,2);
    DECLARE done INT DEFAULT FALSE;

    -- Definir umbral de ventas para obtener bonificación
    DECLARE umbral DECIMAL(10,2) DEFAULT 10000.00;

    -- Definir una variable para el manejo de errores
    DECLARE exit HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Si ocurre un error, revierte la transacción y registra el error
        ROLLBACK;
        -- Opcional: Puedes incluir aquí una instrucción para registrar errores en una tabla de logs, si existe
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error durante el cálculo de bonificaciones';
    END;

    -- Definir cursor para obtener las ventas mensuales de cada empleado
    DECLARE cursor_ventas CURSOR FOR
    SELECT EmpleadoId, SUM(Monto)
    FROM Ventas
    WHERE FechaVenta >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
    GROUP BY EmpleadoId;

    -- Manejo de fin del cursor
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Inicio de la transacción
    START TRANSACTION;

    -- Abrir el cursor
    OPEN cursor_ventas;

    -- Obtener los valores del cursor
    FETCH cursor_ventas INTO EmpleadoIdV, TotalVentasMes;

    -- Recorrer cada registro del cursor
    WHILE NOT done DO
        IF TotalVentasMes > umbral THEN
            -- Calcular la bonificación (10% de las ventas mensuales)
            SET Bonificacion = TotalVentasMes * 0.10;

            -- Actualizar el salario del empleado sumando la bonificación
            UPDATE Empleados
            SET Salario = Salario + Bonificacion
            WHERE Id = EmpleadoIdV;

            -- Insertar la bonificación en la tabla Bonificaciones
            INSERT INTO Bonificaciones (EmpleadoId, MontoBonificacion, FechaBonificacion)
            VALUES (EmpleadoIdV, Bonificacion, CURDATE());
        END IF;

        -- Obtener el siguiente registro del cursor
        FETCH cursor_ventas INTO EmpleadoIdV, TotalVentasMes;
    END WHILE;

    -- Cerrar el cursor
    CLOSE cursor_ventas;

    -- Confirmar la transacción
    COMMIT;
END//
DELIMITER ;
