-- Function: rrhh_liq_mae_subtotal_asignaciones_legales(double precision, double precision, double precision)

-- DROP FUNCTION rrhh_liq_mae_subtotal_asignaciones_legales(double precision, double precision, double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_subtotal_asignaciones_legales(vacaciones_fraccionadas double precision, bono_vacacional_fraccionado double precision, bonificacion_fin_annio_fraccionada double precision)
  RETURNS double precision AS
$BODY$
	DECLARE subtotal_asignacioneslegales DOUBLE PRECISION;
        BEGIN
		
                subtotal_asignacioneslegales = (vacaciones_fraccionadas + bono_vacacional_fraccionado +  bonificacion_fin_annio_fraccionada);
		
		RETURN subtotal_asignacioneslegales;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_subtotal_asignaciones_legales(double precision, double precision, double precision)
  OWNER TO openerp;

