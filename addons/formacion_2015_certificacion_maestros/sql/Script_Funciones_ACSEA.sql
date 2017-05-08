/*
-- DROP FUNCTION fx_acsea_libro_maestros(estado integer, proceso integer);

CREATE OR REPLACE FUNCTION fx_acsea_libro_maestros(estado integer, proceso integer) RETURNS integer AS $$
	DECLARE nuevo_libro INTEGER;
        BEGIN
		SELECT libro INTO nuevo_libro
		FROM for_pis_acsea_certificados_maestros a
		WHERE a.estado_id = estado AND (a.proceso_id = proceso - 1);
		IF nuevo_libro IS NULL THEN
			nuevo_libro = 1;
		ELSE
			nuevo_libro = nuevo_libro + 1;
		END IF;
		RETURN nuevo_libro;
        END;
$$ LANGUAGE plpgsql;

SELECT * FROM fx_acsea_libro_maestros(10, 1);
*/

/*
-- DROP FUNCTION fx_acsea_hoja_maestros(estado integer, proceso integer);

CREATE OR REPLACE FUNCTION fx_acsea_hoja_maestros(estado integer, proceso integer) RETURNS integer AS $$
	DECLARE nueva_hoja INTEGER;
        BEGIN
		SELECT hoja INTO nueva_hoja
		FROM for_pis_acsea_certificados_maestros a
		WHERE a.estado_id = estado AND (a.proceso_id = proceso - 1)
		ORDER BY hoja DESC;
		IF nueva_hoja IS NULL THEN
			nueva_hoja = 1;
		ELSE
			nueva_hoja = nueva_hoja + 1;
		END IF;
		RETURN nueva_hoja;
        END;
$$ LANGUAGE plpgsql;

SELECT * FROM fx_acsea_hoja_maestros(10, 1);
*/

-- DROP FUNCTION fx_acsea_concatena_pis(cedula char, estado integer, inicio date, fin date);

CREATE OR REPLACE FUNCTION fx_acsea_concatena_pis(cedula char, estado integer, inicio date, fin date) RETURNS SETOF for_pis_maestros AS $$
	-- m.cedula, r.estado_id, fecha_inicio, fecha_fin
	DECLARE
	    r for_pis_maestros%rowtype;
	    pis_conteo INTEGER;
	    pis_maestro CHAR;
	BEGIN
	    FOR r IN SELECT m.cedula, r.nro_preimpreso FROM for_pis_maestros m
			INNER JOIN for_pis_mae_participacion_pis p
				ON m.id = p.maestro_id
			INNER JOIN for_pis_registro_inicial r
				ON r.id = p.numero_id
			INNER JOIN for_pis_estados e
				ON r.estado_id = e.id
		WHERE	m.cedula = cedula AND
			r.fecha_inicio >= '01/01/2013' AND r.fecha_cierre <= '31/12/2013'
		GROUP BY m.cedula, m.nombres, m.apellidos, r.estado_id, r.nro_preimpreso
		ORDER BY m.cedula
	    LOOP
		IF pis_conteo = 0 THEN
			pis_maestro = r.nro_preimpreso;
			pis_conteo = pis_conteo + 1;
		ELSE
			pis_maestro = pis_maestro || ', ' || r.nro_preimpreso;
		END IF;
		RETURN NEXT r; -- return current row of SELECT
	    END LOOP;
	    RETURN pis_maestro;
        END;
$$ LANGUAGE plpgsql;

-- SELECT * FROM fx_acsea_concatena_pis('7949411', 1, '01/01/2013', '31/12/2013');
