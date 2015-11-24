-- Function: rrhh_liq_mae_total_horas_trabajadas(integer, date, date)

-- DROP FUNCTION rrhh_liq_mae_total_horas_trabajadas(integer, date, date);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_total_horas_trabajadas(maestroid integer, fecha_inicio date, fecha_fin date)
  RETURNS integer AS
$BODY$
	DECLARE total_horas INTEGER;
        BEGIN
		--Se toman en cuenta los sabados y domingos para el calculo total de horas trabajadas
		--SELECT sum(a.horas_lunes)+sum(a.horas_martes)+sum(a.horas_miercoles)+sum(a.horas_jueves)+sum(a.horas_viernes)
		SELECT sum(a.horas_lunes)+sum(a.horas_martes)+sum(a.horas_miercoles)+sum(a.horas_jueves)+sum(a.horas_viernes)+sum(a.horas_sabado)+sum(a.horas_domingo) INTO  total_horas
                FROM for_pis_mae_asistencias a
                WHERE a.maestro_id = maestroid
			AND a.semana_desde >= (fecha_inicio - time '24:00')
			AND a.semana_hasta <= (fecha_fin + time '24:00');
		RETURN total_horas;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_total_horas_trabajadas(integer, date, date)
  OWNER TO openerp;

