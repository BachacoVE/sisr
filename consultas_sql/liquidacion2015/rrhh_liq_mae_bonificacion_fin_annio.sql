-- Function: rrhh_liq_mae_bonificacion_fin_annio(double precision)

-- DROP FUNCTION rrhh_liq_mae_bonificacion_fin_annio(double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_bonificacion_fin_annio(salario_diario double precision)
  RETURNS double precision AS
$BODY$
    DECLARE bonificacion_fin_annio DOUBLE PRECISION;
        BEGIN
        -- ultimo salario / 30 * 140
        bonificacion_fin_annio = salario_diario * 140;
        RETURN bonificacion_fin_annio;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_bonificacion_fin_annio(double precision)
  OWNER TO openerp;

