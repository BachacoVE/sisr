-- Function: rrhh_liq_mae_salario_diario(double precision)

-- DROP FUNCTION rrhh_liq_mae_salario_diario(double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_salario_diario(salario_mensual double precision)
  RETURNS double precision AS
$BODY$
	DECLARE 
	salario_diario DOUBLE PRECISION;


        BEGIN
		-- salario mensual / 30
		-- salario_diario = salario_mensual/30;

		-- Modificacion según GG RRHH Mie 22 Oct 2014 7:00 PM
		salario_diario = salario_mensual/30;
		
		RETURN salario_diario;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_salario_diario(double precision)
  OWNER TO openerp;

