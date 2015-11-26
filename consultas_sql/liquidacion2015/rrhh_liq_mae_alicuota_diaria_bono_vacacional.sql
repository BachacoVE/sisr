-- Function: rrhh_liq_mae_alicuota_diaria_bono_vacacional(double precision)

-- DROP FUNCTION rrhh_liq_mae_alicuota_diaria_bono_vacacional(double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_alicuota_diaria_bono_vacacional(salario_mensual double precision)
  RETURNS double precision AS
$BODY$
	DECLARE alicuota_diaria_bono_vacacional DOUBLE PRECISION;
        BEGIN
		-- (ultimo salario + bono fin annio mensual) / 30 * 85 / 12 / 30

		alicuota_diaria_bono_vacacional = (salario_mensual )/ 30 * 85 / 12 / 30;
		RETURN alicuota_diaria_bono_vacacional;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_alicuota_diaria_bono_vacacional(double precision)
  OWNER TO openerp;

