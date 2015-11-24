-- Function: rrhh_liq_mae_alicuota_diaria_bonificacion_fin_annio(double precision, double precision)

-- DROP FUNCTION rrhh_liq_mae_alicuota_diaria_bonificacion_fin_annio(double precision, double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_alicuota_diaria_bonificacion_fin_annio(salario_mensual double precision, bono_vacacional_mensual double precision)
  RETURNS double precision AS
$BODY$
	DECLARE alicuota_diaria_bonificacion_fin_annio DOUBLE PRECISION;
        BEGIN
		-- (ultimo salario + bono vacacional mensual) / 30 * 140 / 12 / 30
		alicuota_diaria_bonificacion_fin_annio = (salario_mensual + bono_vacacional_mensual) / 30 * 140 / 12 / 30;
		RETURN alicuota_diaria_bonificacion_fin_annio;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_alicuota_diaria_bonificacion_fin_annio(double precision, double precision)
  OWNER TO openerp;

