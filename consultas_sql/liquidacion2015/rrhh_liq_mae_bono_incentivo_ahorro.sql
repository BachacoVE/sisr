-- Function: rrhh_liq_mae_bono_incentivo_ahorro(double precision, double precision, double precision)

-- DROP FUNCTION rrhh_liq_mae_bono_incentivo_ahorro(double precision, double precision, double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_bono_incentivo_ahorro(horas_trabajadas double precision, tope double precision, monto double precision)
  RETURNS double precision AS
$BODY$
	DECLARE 
	incentivo_ahorro DOUBLE PRECISION;

        BEGIN

	    IF
	        horas_trabajadas < tope
	    THEN
                incentivo_ahorro = (horas_trabajadas * monto)/tope;
        ELSE
	        incentivo_ahorro = monto;
	    END IF;
		
		RETURN incentivo_ahorro;    
	    
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_bono_incentivo_ahorro(double precision, double precision, double precision)
  OWNER TO openerp;

