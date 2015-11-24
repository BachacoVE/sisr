-- Function: rrhh_liq_mae_salario_bono_vacional(double precision)

-- DROP FUNCTION rrhh_liq_mae_salario_bono_vacional(double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_salario_bono_vacional(salario_diario double precision)
  RETURNS double precision AS
$BODY$
	DECLARE 
	salario_bono_vacional DOUBLE PRECISION;


        BEGIN
		-- salario diario + alicuota de BFA
		salario_bono_vacional = salario_diario;
		
		RETURN salario_bono_vacional;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_salario_bono_vacional(double precision)
  OWNER TO openerp;

