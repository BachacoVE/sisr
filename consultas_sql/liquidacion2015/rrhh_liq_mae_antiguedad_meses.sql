-- Function: rrhh_liq_mae_antiguedad_meses(integer, integer, date, date)

-- DROP FUNCTION rrhh_liq_mae_antiguedad_meses(integer, integer, date, date);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_antiguedad_meses(maestro integer, modalidad integer, fecha_fin date, fecha_inicio date)
  RETURNS integer AS
$BODY$
	DECLARE total_horas INTEGER;
	DECLARE antiguedad_meses INTEGER;
	
        BEGIN
        
		SELECT sum(a.horas_lunes)+sum(a.horas_martes)+sum(a.horas_miercoles)+sum(a.horas_jueves)+sum(a.horas_viernes)+sum(a.horas_sabado)+sum(a.horas_domingo) INTO  total_horas
                FROM for_pis_mae_asistencias a
                WHERE a.maestro_id = maestro
			AND a.semana_desde >= (fecha_inicio - time '24:00')
			AND a.semana_hasta <= (fecha_fin + time '24:00');

                --IF modalidad = 1 THEN
			RETURN EXTRACT(MONTH FROM AGE(fecha_fin , fecha_inicio));
		--ELSE
			-- Calculo de Meses desde las Horas (horas/8/30)
			--RETURN (total_horas/5/21)::integer;
		--END IF;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_antiguedad_meses(integer, integer, date, date)
  OWNER TO openerp;

