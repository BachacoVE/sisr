-- Function: rrhh_liq_mae_salario_anual(double precision, double precision, double precision)

-- DROP FUNCTION rrhh_liq_mae_salario_anual(double precision, double precision, double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_salario_anual(salario_diario double precision, salario_bono_vacional double precision, salario_bono_fin_annio double precision)
  RETURNS double precision AS
$BODY$
	DECLARE salario_anual DOUBLE PRECISION;
        BEGIN
		-- (salario diario + salario bonificacion fin annio + salario bono vacacional) * 360
          salario_anual = (salario_diario + salario_bono_vacional + salario_bono_fin_annio) * 360;

		RETURN salario_anual;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_salario_anual(double precision, double precision, double precision)
  OWNER TO openerp;

