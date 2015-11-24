-- Function: rrhh_liq_mae_salario_bono_fin_annio(double precision, double precision)

-- DROP FUNCTION rrhh_liq_mae_salario_bono_fin_annio(double precision, double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_salario_bono_fin_annio(salario_diario double precision, bono_vacacional_mensual double precision)
  RETURNS double precision AS
$BODY$
	DECLARE 
	salario_bono_fin_annio DOUBLE PRECISION;

        BEGIN
		-- salario diario + alicuota de BFA
		salario_bono_fin_annio = salario_diario + (bono_vacacional_mensual/30);
		
		RETURN salario_bono_fin_annio;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_salario_bono_fin_annio(double precision, double precision)
  OWNER TO openerp;

