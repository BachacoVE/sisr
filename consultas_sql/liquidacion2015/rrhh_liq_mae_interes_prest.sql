-- Function: rrhh_liq_mae_interes_prest(double precision, double precision, integer)

-- DROP FUNCTION rrhh_liq_mae_interes_prest(double precision, double precision, integer);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_interes_prest(prestaciones double precision, tasa_interes_prest double precision, cant_dias_interes integer)
  RETURNS double precision AS
$BODY$
	DECLARE interes_prest DOUBLE PRECISION;
        BEGIN
		--interes_prest = ((prestaciones * tasa_interes_prest) /100 /365) * cant_dias_interes;
		-- Cambio en la formula a solicitud de RRHH el día 01/11/2014
		interes_prest = ((prestaciones * tasa_interes_prest/100) /365) * cant_dias_interes;
                           		
		RETURN interes_prest;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_interes_prest(double precision, double precision, integer)
  OWNER TO openerp;

