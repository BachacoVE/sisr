-- Function: rrhh_liq_mae_valor_hora(integer)

-- DROP FUNCTION rrhh_liq_mae_valor_hora(integer);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_valor_hora(maestro_id integer, fecha_fin date)
  RETURNS double precision AS
$BODY$
	DECLARE valor_hora DOUBLE PRECISION;
        BEGIN
		SELECT a.valor_hora INTO valor_hora
		FROM for_pis_mae_valor_hora a
		INNER JOIN for_pis_maestros mae on mae.id = maestro_id
		WHERE 
			CASE WHEN date_part('month', fecha_fin)<5
				THEN mae.nivel_viejo_id = a.id
			ELSE
				mae.nivel_id = a.id
			END; 
		RETURN valor_hora;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_valor_hora(integer, date)
  OWNER TO openerp;