-- Function: rrhh_liq_mae_id_estado(integer)

-- DROP FUNCTION rrhh_liq_mae_id_estado(integer);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_id_estado(id_dependencia integer)
  RETURNS integer AS
$BODY$
	DECLARE
		dependencia CHAR;
		id_estado INTEGER;
        BEGIN
		SELECT
		(CASE WHEN d.dependencia='Región Amazonas' THEN '1'
			WHEN d.dependencia='Región Anzoátegui' THEN '2'
			WHEN d.dependencia='Región Apure' THEN '3'
			WHEN d.dependencia='Región Aragua' THEN '4'
			WHEN d.dependencia='Región Barinas' THEN '5'
			WHEN d.dependencia='Región Bolívar' THEN '6'
			WHEN d.dependencia='Región Carabobo' THEN '7'
			WHEN d.dependencia='Región Cojedes' THEN '8'
			WHEN d.dependencia='Región Delta Amacuro' THEN '9'
			WHEN d.dependencia='Región Distrito Capital' THEN '10'
			WHEN d.dependencia='Región Falcón' THEN '11'
			WHEN d.dependencia='Región Guárico' THEN '12'
			WHEN d.dependencia='Región Lara' THEN '13'
			WHEN d.dependencia='Región Mérida' THEN '14'
			WHEN d.dependencia='Región Miranda' THEN '15'
			WHEN d.dependencia='Región Monagas' THEN '16'
			WHEN d.dependencia='Región Nueva Esparta' THEN '17'
			WHEN d.dependencia='Región Portuguesa' THEN '18'
			WHEN d.dependencia='Región Sucre' THEN '19'
			WHEN d.dependencia='Región Táchira' THEN '20'
			WHEN d.dependencia='Región Trujillo' THEN '21'
			WHEN d.dependencia='Región Vargas' THEN '22'
			WHEN d.dependencia='Región Yaracuy' THEN '23'
			WHEN d.dependencia='Región Zulia' THEN '24'
			ELSE '99'
		END)::integer AS "cod_edo" INTO id_estado
                FROM for_dependencias d
                WHERE d.id = id_dependencia;

		RETURN id_estado;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_id_estado(integer)
  OWNER TO openerp;

