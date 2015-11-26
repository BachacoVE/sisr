-- Function: rrhh_liq_mae_total_asignaciones(double precision, double precision, double precision)

-- DROP FUNCTION rrhh_liq_mae_total_asignaciones(double precision, double precision, double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_total_asignaciones(prestaciones double precision, subtotal_asignacioneslegales double precision, subtotal_otras_asignaciones double precision)
  RETURNS double precision AS
$BODY$
	DECLARE total_asignaciones DOUBLE PRECISION;
        BEGIN
		
                total_asignaciones = (prestaciones + subtotal_asignacioneslegales +  subtotal_otras_asignaciones);
		
		RETURN total_asignaciones;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_total_asignaciones(double precision, double precision, double precision)
  OWNER TO openerp;

