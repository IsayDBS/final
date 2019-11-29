CREATE DATABASE Final;
USE Final;

CREATE TABLE Paradas(nombre VARCHAR(255) NOT NULL UNIQUE,
rutas VARCHAR(255));

CREATE TABLE Ruta(pk_id_ruta INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(255) NOT NULL UNIQUE,
asientos INTEGER NOT NULL,
paradas VARCHAR(255) NOT NULL,
precio INTEGER NOT NULL);

CREATE TABLE Boletos(identificador VARCHAR(100) NOT NULL UNIQUE,
precio INTEGER,
fecha_venta VARCHAR(100) NOT NULL,
estacion_entrada VARCHAR(100) NOT NULL,
estacion_salida VARCHAR(100) NOT NULL,
fk_id_ruta INTEGER NOT NULL);

ALTER TABLE Boletos
ADD FOREIGN KEY(fk_id_ruta) REFERENCES Ruta(pk_id_ruta);
