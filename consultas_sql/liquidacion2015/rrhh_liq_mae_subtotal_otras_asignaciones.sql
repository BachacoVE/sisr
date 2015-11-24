-- Function: rrhh_liq_mae_subtotal_otras_asignaciones(double precision)

-- DROP FUNCTION rrhh_liq_mae_subtotal_otras_asignaciones(double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_subtotal_otras_asignaciones(incentivo_ahorro double precision)
  RETURNS double precision AS
$BODY$
	DECLARE subtotal_otras_asignaciones DOUBLE PRECISION;
        BEGIN
		
                subtotal_otras_asignaciones = incentivo_ahorro;
		
		RETURN subtotal_otras_asignaciones;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_subtotal_otras_asignaciones(double precision)
  OWNER TO openerp;

