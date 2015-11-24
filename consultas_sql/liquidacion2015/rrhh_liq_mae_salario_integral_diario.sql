-- Function: rrhh_liq_mae_salario_integral_diario(double precision)

-- DROP FUNCTION rrhh_liq_mae_salario_integral_diario(double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_salario_integral_diario(salario_integral_mensual double precision)
  RETURNS double precision AS
$BODY$
	DECLARE salario_integral_diario DOUBLE PRECISION;
        BEGIN
		-- salario integral mensual / 30 (>= 1 mes)
		salario_integral_diario = salario_integral_mensual/30;
		RETURN salario_integral_diario;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_salario_integral_diario(double precision)
  OWNER TO openerp;

