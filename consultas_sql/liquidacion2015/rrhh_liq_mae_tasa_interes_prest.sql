-- Function: rrhh_liq_mae_tasa_interes_prest(date, int)

-- DROP FUNCTION rrhh_liq_mae_tasa_interes_prest(date, int);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_tasa_interes_prest(fecha_fin date, id_tasa_interes int)
  RETURNS double precision AS
$BODY$
	DECLARE tasa_interes_prest DOUBLE PRECISION;
        BEGIN
		

		SELECT tasa_interes INTO  tasa_interes_prest
                FROM for_pis_mae_tasas_bcv_prestaciones a
                WHERE a.id = id_tasa_interes;
                           		
		RETURN tasa_interes_prest;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_tasa_interes_prest(date, int)
  OWNER TO openerp;

