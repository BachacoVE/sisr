-- Function: rrhh_liq_mae_id_tasa_interes_prest(date)

-- DROP FUNCTION rrhh_liq_mae_id_tasa_interes_prest(date);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_id_tasa_interes_prest(fecha_fin date)
  RETURNS integer AS
$BODY$
	DECLARE id_tasa_interes_prest INTEGER;
        BEGIN
		

		SELECT id INTO  id_tasa_interes_prest
                FROM for_pis_mae_tasas_bcv_prestaciones a
                WHERE a.mes = date_part('month', fecha_fin)
                AND   a.annio= date_part('year', fecha_fin);
                           		
		RETURN id_tasa_interes_prest;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_id_tasa_interes_prest(date)
  OWNER TO openerp;

