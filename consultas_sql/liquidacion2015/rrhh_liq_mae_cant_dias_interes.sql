-- Function: rrhh_liq_mae_cant_dias_interes(date,int)

-- DROP FUNCTION rrhh_liq_mae_cant_dias_interes(date, int);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_cant_dias_interes(fecha_fin date, id_tasa_interes int)
  RETURNS double precision AS
$BODY$
	DECLARE cant_dias_interes DOUBLE PRECISION;
        BEGIN
			SELECT cantidad_dias INTO  cant_dias_interes
                FROM for_pis_mae_tasas_bcv_prestaciones a
                WHERE a.id = id_tasa_interes;
                
		RETURN cant_dias_interes;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_cant_dias_interes(date, int)
  OWNER TO openerp;

