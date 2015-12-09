-- Function: rrhh_liq_bono_firma_contrato(double precision, double precision, double precision)

-- DROP FUNCTION rrhh_liq_bono_firma_contrato(double precision, double precision, double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_bono_firma_contrato(horas_trabajadas double precision, tope double precision, monto double precision)
  RETURNS double precision AS
$BODY$
	DECLARE 
  bono_firma DOUBLE PRECISION;
        BEGIN
        --Funcion aplicada en el año 2015, determina el monto a pagar del bono incentivo al ahorro en base a la fecha de la firma del contrato colectivo
		    IF
          horas_trabajadas < tope
      THEN
                bono_firma = (horas_trabajadas * monto)/tope;
        ELSE
          bono_firma = monto;
      END IF;
    
      RETURN bono_firma; 
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_bono_firma_contrato(double precision, double precision, double precision)
  OWNER TO openerp;

