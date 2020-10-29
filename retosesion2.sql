
/* Sesión 2: Agrupaciones y subconsultas
RETO 1-3
Carlos Alejandro Velázquez Valdez
Email: carlosvelazquezv2@gmail.com
Data Science Bedu */


/* RETO 1 */
USE tienda;
SHOW TABLES;

/*   ¿Qué artículos incluyen la palabra Pasta en su nombre? */
SELECT * 
FROM articulo
WHERE nombre LIKE "%Pasta%";

/*  ¿Qué artículos incluyen la palabra Cannelloni en su nombre? */
SELECT *
FROM articulo
WHERE nombre LIKE "%Cannelloni%";

/* ¿Qué nombres están separados por un guión (-) por ejemplo Puree - Kiwi? */
SELECT *
FROM articulo
WHERE nombre LIKE "% - %";

/*  ¿Qué puestos incluyen la palabra Designer?  */
SELECT *
FROM puesto
WHERE nombre LIKE "%Designer%";

/* ¿Qué puestos incluyen la palabra Developer? */
SELECT *
FROM puesto
WHERE nombre LIKE "%Developer%";

/* RETO 2 */
/* ¿Cuál es el promedio de salario de los puestos? */
SELECT avg(salario) AS promedio_salario
FROM puesto;

/* ¿Cuántos artículos incluyen la palabra Pasta en su nombre? */
SELECT count(*)
FROM articulo
WHERE nombre LIKE '%Pasta%';

/* ¿Cuál es el salario mínimo y máximo?  */
SELECT min(salario) AS salario_minimo, max(salario) AS salario_maximo
FROM puesto;

/* ¿Cuál es la suma del salario de los últimos cinco puestos agregados? */
SELECT max(id_puesto) - 5 
FROM puesto;
SELECT sum(salario)
FROM puesto
WHERE id_puesto > 995; 

/* RETO 3 */ 
/* ¿Cuántos registros hay por cada uno de los puestos? */
SELECT nombre, count(*) AS numero_de_registros
FROM puesto
GROUP BY nombre;

/* ¿Cuánto dinero se paga en total por puesto? */
SELECT nombre, sum(salario)
FROM puesto
GROUP BY nombre;

/* ¿Cuál es el número total de ventas por vendedor? */
SELECT id_empleado, count(*) AS ventas
FROM venta
GROUP BY id_empleado;

/* ¿Cuál es el número total de ventas por artículo?  */
SELECT id_articulo, count(*)
FROM venta
GROUP BY id_articulo;
