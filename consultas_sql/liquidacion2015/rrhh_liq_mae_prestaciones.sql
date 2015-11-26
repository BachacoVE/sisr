-- Function: rrhh_liq_mae_prestaciones(double precision, integer)

-- DROP FUNCTION rrhh_liq_mae_prestaciones(double precision, integer);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_prestaciones(salario_integral_diario double precision, meses_antiguedad integer)
  RETURNS double precision AS
$BODY$
	DECLARE prestaciones DOUBLE PRECISION;
        BEGIN
		-- antiguedad meses * 5 * salario integral diario 
                prestaciones = meses_antiguedad * 5 * salario_integral_diario;
		
		RETURN prestaciones;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_prestaciones(double precision, integer)
  OWNER TO openerp;

