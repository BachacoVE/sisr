-- Function: rrhh_liq_mae_bonificacion_fin_annio_fraccionada(double precision, integer)

-- DROP FUNCTION rrhh_liq_mae_bonificacion_fin_annio_fraccionada(double precision, integer);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_bonificacion_fin_annio_fraccionada(salario_bono_fin_annio double precision, meses_antiguedad integer)
  RETURNS double precision AS
$BODY$
    DECLARE bonificacion_fin_annio_fraccionada DOUBLE PRECISION;
        BEGIN
        -- suedo bono_fin_annio * 140 / 12 * antiguedad meses
        bonificacion_fin_annio_fraccionada = (salario_bono_fin_annio *
140/12) * meses_antiguedad;
        RETURN bonificacion_fin_annio_fraccionada;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_bonificacion_fin_annio_fraccionada(double precision, integer)
  OWNER TO openerp;

