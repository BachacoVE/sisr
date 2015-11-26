-- Function: rrhh_liq_mae_monto_bono_incentivo_ahorro(date)

-- DROP FUNCTION rrhh_liq_mae_monto_bono_incentivo_ahorro(date);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_monto_bono_incentivo_ahorro(fecha_fin date)
  RETURNS double precision AS
$BODY$
	DECLARE monto_bono_incentivo_ahorro DOUBLE PRECISION;
        BEGIN
        --Funcion aplicada en el año 2015, determina el monto del bono incentivo al ahorro en base a la fecha de la firma del contrato colectivo
		    IF fecha_fin < '20/10/2015'
          THEN monto_bono_incentivo_ahorro= 4000;
          ELSE monto_bono_incentivo_ahorro= 8000;
        END IF;                   		
		    RETURN monto_bono_incentivo_ahorro;

        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_monto_bono_incentivo_ahorro(date)
  OWNER TO openerp;

