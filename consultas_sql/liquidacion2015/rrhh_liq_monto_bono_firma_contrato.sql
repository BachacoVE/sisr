-- Function: rrhh_liq_monto_bono_firma_contrato(date, date)

-- DROP FUNCTION rrhh_liq_monto_bono_firma_contrato(date, date);

CREATE OR REPLACE FUNCTION rrhh_liq_monto_bono_firma_contrato(fecha_inicio date,fecha_fin date)
  RETURNS double precision AS
$BODY$
	DECLARE monto_bono_firma_contrato DOUBLE PRECISION;
        BEGIN
        --Funcion aplicada en el año 2015, determina el monto del bono incentivo al ahorro en base a la fecha de la firma del contrato colectivo
		    IF fecha_inicio < '20/07/2015' AND fecha_fin >= '20/10/2015'
          THEN monto_bono_firma_contrato= 10000;
        ELSE monto_bono_firma_contrato= 0;
        END IF;                   		
		    RETURN monto_bono_firma_contrato;

        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_monto_bono_firma_contrato(date, date)
  OWNER TO openerp;

