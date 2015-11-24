-- Function: rrhh_liq_mae_bonificacion_fin_annio_mensual(double precision)

-- DROP FUNCTION rrhh_liq_mae_bonificacion_fin_annio_mensual(double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_bonificacion_fin_annio_mensual(bonificacion_fin_annio double precision)
  RETURNS double precision AS
$BODY$
	DECLARE bonificacion_fin_annio_mensual DOUBLE PRECISION;
        BEGIN
		-- ultimo salario / 30 * 140
		bonificacion_fin_annio_mensual = bonificacion_fin_annio/12;
		RETURN bonificacion_fin_annio_mensual;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_bonificacion_fin_annio_mensual(double precision)
  OWNER TO openerp;

