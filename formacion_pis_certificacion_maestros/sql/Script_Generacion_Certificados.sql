/*
===================================================================================================
Desarrollo de las Consultas para Generación Automática de Certificados de Maestros
INCES Sede - Gerencia General de Informática - Mayo 2014 - Joan Espinoza
	
ESCENARIO:
	Al crear (insertar vía OpenERP) un nuevo Proceso de Certificación,
	se desencadena (vía Trigger en la BD) la ejecución de un StoreProcedure,
	que construirá, calculará e insertará los registros correspondientes 
	en la tabla Certificados, que cumplan con los criterios de ese proceso:
		- Fitrados por fechas inicio/cierre (PIS 2013),
		- Agrupados por cédula (todos los PIS del maestro),
		- Obteniendo la suma de los lapsos de ejecución de los PIS donde participó,
		- Asignando el N° Correlativo, y Estado según Clasificador del INE,
		- Libro, Folio (Hoja) y Consecutivo (Línea).
		
BITÁCORA de CONSTRUCCIÓN:
	1.- Consulta INSERT (INTO) en la tabla "for_pis_mae_certificados"
	2.- Consulta SELECT de los valores a insertar:
		3.- (Sub)Consulta SELECT de Maestros participantes en PIS año 2013,
		4.- (Sub)Consulta SELECT para filtrar el Estado (Región del PIS)
		4.- (Sub)Consulta SELECT para asignar el estado_id del INE (no de SISR)
	3.- Cursor (Post INSERT INTO) para actualizar secuencialmente en cada Certificado:
		6.- (Sub)Consulta SELECT para generar el número de Libro
		7.- (Sub)Consulta SELECT para generar el número de Consecutivo (Línea)
		8.- (Sub)Consulta SELECT para generar el número de Hoja
		9.- (Sub)Consulta SELECT para concatenar el número de Correlativo
===================================================================================================
*/

/*
-- CONSULTA 1:
INSERT INTO for_pis_acsea_certificados_maestros
	(create_uid, create_date, write_date, write_uid,
	proceso_id, correlativo, estado_id,
	maestro_id, libro, hoja, consecutivo,
	duracion, fecha_emision, fecha_consignacion, estatus_certificado)
*/

/*
-- CONSULTA 2:
-- Lista de Maestros participantes en PIS 2013, con la suma de Proyectos donde participó
SELECT 1 as "create_uid", NOW() as "create_date", NULL as "write_date", NULL as "write_uid",
	1 as "proceso_id", '00000000000000000' as "correlativo",
	-- r.estado_id as "estado_id", e.estado, i.codigo as "estado_ine",
	r.estado_id as "estado_id",
	-- m.id as "maestro_id", m.cedula, m.nombres, m.apellidos, 
	m.id as "maestro_id",
	fx_acsea_libro_maestros(r.estado_id, 1) as "libro", -- 0 as "libro", 
	0 as "hoja", 0 as "consecutivo", 0 as "duracion",
	-- SUM(r.lapso_ejecucion) as "duracion",
	-- r.nro_preimpreso, r.denominacion_pis,
	-- fx_concatena_pis_maestros(m.cedula, r.estado_id, fecha_inicio, fecha_fin),
	date(NOW()) as "fecha_emision", -- NEW.create_date as "fecha_emision",
	NULL as "fecha_consignacion", 6 as "estatus_certificado"	
FROM for_pis_maestros m
	INNER JOIN for_pis_mae_participacion_pis p
		ON m.id = p.maestro_id
	INNER JOIN for_pis_registro_inicial r
		ON r.id = p.numero_id
	INNER JOIN for_pis_estados e
		ON r.estado_id = e.id
	INNER JOIN for_pis_acsea_estados_ine i
		ON r.estado_id = i.codigo_sisr
WHERE r.fecha_inicio >= '01/01/2013' AND r.fecha_cierre <= '31/12/2013'
GROUP BY m.id, r.estado_id
	--, e.estado, i.codigo
-- HAVING SUM(r.lapso_ejecucion) = 0
-- HAVING SUM(r.lapso_ejecucion) > 1600
-- HAVING COUNT(m.cedula) > 1
ORDER BY r.estado_id, m.id;
*/

-- SELECT * FROM for_pis_acsea_certificados_maestros;


-- CURSOR:
DECLARE
    maeID integer;
    estID integer;
    cursorM CURSOR FOR
	SELECT * FROM for_pis_acsea_certificados_maestros
	WHERE maestro_id = maeID AND estado_id = estID;
BEGIN
    maestro := 1740;
    estado := 1;
    OPEN cursorM;
