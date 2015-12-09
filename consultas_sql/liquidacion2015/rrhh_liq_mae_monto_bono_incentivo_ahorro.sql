-- Function: rrhh_liq_mae_monto_bono_incentivo_ahorro(date, date)

-- DROP FUNCTION rrhh_liq_mae_monto_bono_incentivo_ahorro(date, date);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_monto_bono_incentivo_ahorro(fecha_inicio date,fecha_fin date)
  RETURNS double precision AS
$BODY$
	DECLARE monto_bono_incentivo_ahorro DOUBLE PRECISION;
        BEGIN
        --Funcion aplicada en el año 2015, determina el monto del bono incentivo al ahorro
		    
        IF fecha_inicio < '15/03/2015' AND fecha_fin >= '15/06/2015'
          THEN monto_bono_incentivo_ahorro= 4000;
        ELSE monto_bono_incentivo_ahorro= 0;
        END IF;                       
        RETURN monto_bono_incentivo_ahorro;

        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_monto_bono_incentivo_ahorro(date, date)
  OWNER TO openerp;

