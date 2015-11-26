-- Function: rrhh_liq_mae_ultimo_salario_mensual_promediado(integer, integer, integer, date, date)

-- DROP FUNCTION rrhh_liq_mae_ultimo_salario_mensual_promediado(integer, integer, integer, date, date);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_ultimo_salario_mensual_promediado(maestro integer, meses integer, modalidad integer, fecha_fin date, fecha_inicio date)
  RETURNS double precision AS
$BODY$
	DECLARE total_horas INTEGER;
	DECLARE total_horas_viejo INTEGER;
	DECLARE valor_hora DOUBLE PRECISION;
	DECLARE valor_hora_viejo DOUBLE PRECISION;
	DECLARE ultimo_salario DOUBLE PRECISION;
        BEGIN
        
		/*
		SELECT SUM(monto_pago) INTO ultimo_salario 
		FROM for_pis_mae_consolidado_detalle
		WHERE maestro_id = maestro
		GROUP BY maestro_id;
		*/
		
		/*SELECT sum(monto_pago) INTO ultimo_salario 
		FROM for_pis_mae_consolidado_detalle
		WHERE maestro_id = maestro
		GROUP BY maestro_id, consolidado_id
		ORDER BY consolidado_id DESC
		LIMIT 1;

		SELECT sum(a.horas_lunes)+sum(a.horas_martes)+sum(a.horas_miercoles)+sum(a.horas_jueves)+sum(a.horas_viernes)+sum(a.horas_sabado)+sum(a.horas_domingo) INTO  total_horas
                FROM for_pis_mae_asistencias a
                WHERE a.maestro_id = maestro
                  AND a.semana_desde >= (fecha_inicio - time '24:00')
		  AND a.semana_hasta <= (fecha_fin + time '24:00');
		
		IF meses = 0 THEN
			RETURN (ultimo_salario - ultimo_salario);
		ELSE
			IF modalidad = 1 THEN
				-- Calculo de Ultimo Salario/ meses de antiguedad. Cada mes representa veinte (20) días
				RETURN (ultimo_salario / meses);
			ELSE
				-- Calculo de Ultimo Salario/horas trabajadas * 30
				
				RETURN ((ultimo_salario/total_horas) * 30);
				
			END IF;
		END IF;*/

		
        -----------------------------------------------------------------------------------------------------------------------------
        ------------------------------------------------------------------------------------------------------------------------------
        ------------------------------------------------------------------------------------------------------------------------------
        --------------- Liquidacion para el periodo 2015, No utiliza consolidado-----------------------------------------------------
		SELECT sum(asi1.horas_lunes)+sum(asi1.horas_martes)+sum(asi1.horas_miercoles)+sum(asi1.horas_jueves)+sum(asi1.horas_viernes)+sum(asi1.horas_sabado)+sum(asi1.horas_domingo) INTO  total_horas_viejo
                FROM for_pis_mae_asistencias asi1
                WHERE asi1.maestro_id = maestro
                -- condicion para seleccionar asistencias antes del aumento salarial del 1 mayo 2015, la semana 6 tuvo un salto de id por ello la segunda condicion 'or asi1.calendario_id = 53'
                  AND asi1.calendario_id <=17 or asi1.calendario_id = 53;

        SELECT sum(asi2.horas_lunes)+sum(asi2.horas_martes)+sum(asi2.horas_miercoles)+sum(asi2.horas_jueves)+sum(asi2.horas_viernes)+sum(asi2.horas_sabado)+sum(asi2.horas_domingo) INTO  total_horas
                FROM for_pis_mae_asistencias asi2
                WHERE asi2.maestro_id = maestro
                -- condicion para seleccionar asistencias despues del aumento salarial del 1 mayo 2015, la semana 6 tuvo un salto de id por ello la segunda condicion 'AND asi2.calendario_id <> 53'                
                  AND asi2.calendario_id >17 AND asi2.calendario_id <> 53;

        SELECT vh.valor_hora INTO valor_hora_viejo
        		FROM for_pis_maestros as mae
        		INNER JOIN for_pis_mae_valor_hora as vh
        		ON mae.nivel_viejo_id=vh.id
        		WHERE  mae.id=maestro;

        SELECT vh.valor_hora INTO valor_hora
        		FROM for_pis_maestros as mae
        		INNER JOIN for_pis_mae_valor_hora as vh
        		ON mae.nivel_id=vh.id
        		WHERE  mae.id=maestro;

        IF valor_hora_viejo is null THEN valor_hora_viejo=0; END IF;
        IF valor_hora is null THEN valor_hora=0; END IF;
        IF total_horas_viejo is null THEN total_horas_viejo=0; END IF;
        IF total_horas is null THEN total_horas=0; END IF;

        ultimo_salario= ((total_horas * valor_hora)+(total_horas_viejo * valor_hora_viejo));

        IF meses = 0 THEN
			RETURN (ultimo_salario - ultimo_salario);
		ELSE
			IF modalidad = 1 THEN
				-- Calculo de Ultimo Salario/ meses de antiguedad. Cada mes representa veinte (20) días
				RETURN (ultimo_salario / meses);
			ELSE
				-- Calculo de Ultimo Salario/horas trabajadas * 30
				
				RETURN ((ultimo_salario/(total_horas + total_horas_viejo)) * 30);
				
			END IF;
		END IF;

        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_ultimo_salario_mensual_promediado(integer, integer, integer, date, date)
  OWNER TO openerp;
