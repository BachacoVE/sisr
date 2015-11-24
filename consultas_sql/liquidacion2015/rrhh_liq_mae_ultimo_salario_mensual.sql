-- Function: rrhh_liq_mae_ultimo_salario_mensual(integer)

-- DROP FUNCTION rrhh_liq_mae_ultimo_salario_mensual(integer);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_ultimo_salario_mensual(maestro integer)
  RETURNS double precision AS
$BODY$
	DECLARE ultimo_salario DOUBLE PRECISION;
        BEGIN
		SELECT SUM(monto_pago) INTO ultimo_salario 
		FROM (SELECT monto_pago
			FROM for_pis_mae_consolidado_detalle
			WHERE maestro_id = maestro
			ORDER BY hasta DESC
			LIMIT 2) AS quincenas;

		RETURN ultimo_salario;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_ultimo_salario_mensual(integer)
  OWNER TO openerp;

