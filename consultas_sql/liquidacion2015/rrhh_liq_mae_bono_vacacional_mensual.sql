-- Function: rrhh_liq_mae_bono_vacacional_mensual(double precision)

-- DROP FUNCTION rrhh_liq_mae_bono_vacacional_mensual(double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_bono_vacacional_mensual(bono_vacacional85 double precision)
  RETURNS double precision AS
$BODY$
	DECLARE 
	bono_vacacional_mensual DOUBLE PRECISION;
        BEGIN
		--bono_vacacional_mensual   = bono_vacacional85/12;
		bono_vacacional_mensual   = bono_vacacional85/12;
		RETURN bono_vacacional_mensual;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_bono_vacacional_mensual(double precision)
  OWNER TO openerp;

