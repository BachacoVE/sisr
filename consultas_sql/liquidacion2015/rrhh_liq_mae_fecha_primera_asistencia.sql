-- Function: rrhh_liq_mae_fecha_primera_asistencia(integer)

-- DROP FUNCTION rrhh_liq_mae_fecha_primera_asistencia(integer);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_fecha_primera_asistencia(maestro integer)
  RETURNS date AS
$BODY$
	DECLARE fecha_primera_asistencia DATE;
	
        BEGIN
		SELECT a.semana_desde INTO fecha_primera_asistencia
		FROM for_pis_mae_asistencias a
		WHERE a.maestro_id = maestro
		ORDER BY a.semana_desde ASC
		LIMIT 1;

		RETURN (fecha_primera_asistencia);
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_fecha_primera_asistencia(integer)
  OWNER TO openerp;

