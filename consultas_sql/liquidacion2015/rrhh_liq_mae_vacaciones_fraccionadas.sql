-- Function: rrhh_liq_mae_vacaciones_fraccionadas(double precision, integer)

-- DROP FUNCTION rrhh_liq_mae_vacaciones_fraccionadas(double precision, integer);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_vacaciones_fraccionadas(salario_diario double precision, meses_antiguedad integer)
  RETURNS double precision AS
$BODY$
    DECLARE vacaciones_fraccionadas DOUBLE PRECISION;
        BEGIN
        -- suedo diario * 30 / 12 * antiguedad meses (>= 1 mes)
    vacaciones_fraccionadas = (salario_diario * 30/12) * meses_antiguedad;
        RETURN vacaciones_fraccionadas;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_vacaciones_fraccionadas(double precision, integer)
  OWNER TO openerp;

