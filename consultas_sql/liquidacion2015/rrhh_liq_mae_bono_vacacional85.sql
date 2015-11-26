-- Function: rrhh_liq_mae_bono_vacacional85(double precision)

-- DROP FUNCTION rrhh_liq_mae_bono_vacacional85(double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_bono_vacacional85(salario_diario double precision)
  RETURNS double precision AS
$BODY$
	DECLARE 
	bono_vacacional85 DOUBLE PRECISION;

        BEGIN
		--bono_vacacional85 = salario diario * 85;
		bono_vacacional85 = salario_diario * 85;
		RETURN bono_vacacional85;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_bono_vacacional85(double precision)
  OWNER TO openerp;

