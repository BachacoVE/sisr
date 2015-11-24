-- Function: rrhh_liq_mae_bono_vacacional_fraccionado(double precision, integer)

-- DROP FUNCTION rrhh_liq_mae_bono_vacacional_fraccionado(double precision, integer);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_bono_vacacional_fraccionado(salario_bono_vacional double precision, meses_antiguedad integer)
  RETURNS double precision AS
$BODY$
	DECLARE bono_vacacional_fraccionado DOUBLE PRECISION;
        BEGIN
		-- salario_bono_vacional * 85 / 12 * antiguedad meses (>= 1 mes)

		bono_vacacional_fraccionado = (salario_bono_vacional * 85/12) * meses_antiguedad;
		RETURN bono_vacacional_fraccionado;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_bono_vacacional_fraccionado(double precision, integer)
  OWNER TO openerp;

