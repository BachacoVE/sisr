-- Function: rrhh_liq_mae_fecha_primera_asistencia(integer)

-- DROP FUNCTION rrhh_liq_mae_fecha_primera_asistencia(integer);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_fecha_primera_asistencia(maestro integer)
  RETURNS date AS
$BODY$
	DECLARE fecha_primera_asistencia DATE;
	
        BEGIN
        --Comentado en 2015, ya que para este año se tomara en cuenta la fecha que toman los contratos
        /*
		SELECT a.semana_desde INTO fecha_primera_asistencia
		FROM for_pis_mae_asistencias a
		WHERE a.maestro_id = maestro
		ORDER BY a.semana_desde ASC
		LIMIT 1;*/

		SELECT a.fecha_inicio into fecha_primera_asistencia
		FROM for_pis_registro_inicial as a
		INNER JOIN for_pis_mae_participacion_pis as b
		ON a.id=b.numero_id
		WHERE b.maestro_id = maestro
		ORDER BY a.fecha_inicio ASC
		LIMIT 1;

		RETURN (fecha_primera_asistencia);
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_fecha_primera_asistencia(integer)
  OWNER TO openerp;

