-- Function: rrhh_liq_mae_salario_integral_mensual(double precision)

-- DROP FUNCTION rrhh_liq_mae_salario_integral_mensual(double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_salario_integral_mensual(salario_anual double precision)
  RETURNS double precision AS
$BODY$
	DECLARE salario_integral_mensual DOUBLE PRECISION;
        BEGIN
		-- salario anual / 12
           salario_integral_mensual = salario_anual/12;
		RETURN salario_integral_mensual;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_salario_integral_mensual(double precision)
  OWNER TO openerp;

