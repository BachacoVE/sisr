-- Function: rrhh_liq_mae_fecha_ultima_asistencia(integer)

-- DROP FUNCTION rrhh_liq_mae_fecha_ultima_asistencia(integer);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_fecha_ultima_asistencia(maestro integer)
  RETURNS date AS
$BODY$
	DECLARE fecha_ultima_asistencia DATE;
	
        BEGIN
		SELECT a.semana_hasta INTO fecha_ultima_asistencia
		FROM for_pis_mae_asistencias a
		WHERE a.maestro_id = maestro
		ORDER BY a.semana_hasta DESC
		LIMIT 1;

		RETURN (fecha_ultima_asistencia);
	END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_fecha_ultima_asistencia(integer)
  OWNER TO openerp;

