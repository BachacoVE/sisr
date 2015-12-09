-- Function: rrhh_liq_mae_fecha_ultima_asistencia(integer)

-- DROP FUNCTION rrhh_liq_mae_fecha_ultima_asistencia(integer);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_fecha_ultima_asistencia(maestro integer)
  RETURNS date AS
$BODY$
	DECLARE fecha_ultima_asistencia DATE;
	
        BEGIN
        --Comentado en 2015, ya que para este año se tomara en cuenta la fecha que toman los contratos
		/*SELECT a.semana_hasta INTO fecha_ultima_asistencia
		FROM for_pis_mae_asistencias a
		WHERE a.maestro_id = maestro
		ORDER BY a.semana_hasta DESC
		LIMIT 1;*/

		SELECT a.fecha_cierre into fecha_ultima_asistencia
		FROM for_pis_registro_inicial as a
		INNER JOIN for_pis_mae_participacion_pis as b
		ON a.id=b.numero_id
		WHERE b.maestro_id = maestro
		ORDER BY a.fecha_cierre DESC
		LIMIT 1;


		RETURN (fecha_ultima_asistencia);
	END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_fecha_ultima_asistencia(integer)
  OWNER TO openerp;

