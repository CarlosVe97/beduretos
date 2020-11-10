/* Sesión 3: Joins y Vistas
RETO 1-3
Carlos Alejandro Velázquez Valdez
Email: carlosvelazquezv2@gmail.com
Data Science Bedu */

/* Reto 1 */
USE tienda;
/*¿Cuál es el nombre de los empleados cuyo sueldo es menor a $1000 */
SELECT nombre
FROM empleado
WHERE id_puesto in (SELECT id_puesto FROM puesto WHERE salario < 100000);

/*    ¿Cuál es la cantidad mínima y máxima de ventas de cada empleado? */ 
SELECT id_empleado, MIN(venta), MAX(venta)
FROM (SELECT clave, id_empleado,count(*) AS venta FROM venta GROUP BY clave, id_empleado) AS Q
GROUP BY id_empleado;

/*  ¿Cuáles claves de venta incluyen artículos cuyos precios son mayores a $5,000? */
SELECT clave
FROM venta
WHERE id_articulo IN (SELECT id_articulo
FROM articulo
WHERE precio > 5000) ;

/* Reto 2 */

/* ¿Cuál es el nombre de los empleados que realizaron cada venta? */ 
SHOW TABLES;

SELECT nombre, id_venta
FROM empleado AS e
JOIN venta AS v
ON e.id_empleado = v.id_empleado;

/* ¿Cuál es el nombre de los artículos que se han vendido? */

SELECT * 
FROM venta AS v
LEFT JOIN articulo AS a
ON v.id_articulo = a.id_articulo;

/* ¿Cuál es el total de cada venta? */
SELECT clave, SUM(precio) AS total_venta
FROM venta AS v
LEFT JOIN articulo AS a
ON v.id_articulo = a.id_articulo
GROUP BY clave;

CREATE VIEW tickets_92 AS
(SELECT v.clave, v.fecha, a.nombre producto, a.precio, concat(e.nombre, ' ', e.apellido_paterno) empleado 
FROM venta v
JOIN empleado e
  ON v.id_empleado = e.id_empleado
JOIN articulo a
  ON v.id_articulo = a.id_articulo);

/* Reto 3 */
/* Usando la base de datos tienda, define las siguientes vistas que permitan obtener la siguiente información.
	Obtener el puesto de un empleado. */
SHOW TABLES;
CREATE VIEW puesto_empleados AS 
(SELECT CONCAT(e.nombre,' ',e.apellido_paterno,' ',e.apellido_materno) AS nombre_de_empleado, p.nombre AS puesto
FROM empleado AS e
JOIN puesto AS p
USING (id_puesto)
ORDER BY nombre_de_empleado);
/*  Saber qué artículos ha vendido cada empleado. */
CREATE VIEW articulos_vendidos AS 
(SELECT clave, e.nombre , e.apellido_paterno, e.apellido_materno, a.nombre AS nombre_articulo
FROM venta AS v
JOIN articulo AS a
USING (id_articulo)
JOIN empleado AS e
USING (id_empleado));

SELECT * 
FROM articulos_vendidos;
/* Saber qué puesto ha tenido más ventas. */
CREATE VIEW top_venta AS
(SELECT p.nombre, count(*) AS ventas
FROM venta AS v
JOIN empleado AS e
USING (id_empleado)
JOIN puesto AS p
USING (id_puesto)
GROUP BY p.nombre
ORDER BY ventas DESC
LIMIT 1);

SELECT * 
FROM top_venta;
