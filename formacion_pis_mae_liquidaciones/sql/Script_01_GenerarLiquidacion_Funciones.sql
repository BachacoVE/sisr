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


-- Function: rrhh_liq_mae_alicuota_diaria_bono_vacacional(double precision, double precision)

-- DROP FUNCTION rrhh_liq_mae_alicuota_diaria_bono_vacacional(double precision, double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_alicuota_diaria_bono_vacacional(salario_mensual double precision, bonificacion_fin_annio_mensual double precision)
  RETURNS double precision AS
$BODY$
	DECLARE alicuota_diaria_bono_vacacional DOUBLE PRECISION;
        BEGIN
		-- (ultimo salario + bono fin annio mensual) / 30 * 85 / 12 / 30

		alicuota_diaria_bono_vacacional = (salario_mensual + bonificacion_fin_annio_mensual )/ 30 * 85 / 12 / 30;
		RETURN alicuota_diaria_bono_vacacional;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_alicuota_diaria_bono_vacacional(double precision, double precision)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_antiguedad_annios(integer, integer, date, date)

-- DROP FUNCTION rrhh_liq_mae_antiguedad_annios(integer, integer, date, date);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_antiguedad_annios(maestro integer, modalidad integer, fecha_fin date, fecha_inicio date)
  RETURNS integer AS
$BODY$
	DECLARE total_horas INTEGER;
	DECLARE antiguedad_annios INTEGER;
	
        BEGIN
		SELECT sum(a.horas_lunes)+sum(a.horas_martes)+sum(a.horas_miercoles)+sum(a.horas_jueves)+sum(a.horas_viernes)+sum(a.horas_sabado)+sum(a.horas_domingo) INTO  total_horas
                FROM for_pis_mae_asistencias a
                WHERE a.maestro_id = maestro
			AND a.semana_desde >= (fecha_inicio - time '24:00')
			AND a.semana_hasta <= (fecha_fin + time '24:00');
		
                IF modalidad = 3 THEN
			RETURN EXTRACT(YEAR FROM AGE(fecha_fin , fecha_inicio));
		ELSE
			-- Calculo de Annios desde las Horas (horas/8/30/12)
			RETURN (total_horas/8/30/12)::integer;

		END IF;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_antiguedad_annios(integer, integer, date, date)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_antiguedad_dias(integer, integer, date, date)

-- DROP FUNCTION rrhh_liq_mae_antiguedad_dias(integer, integer, date, date);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_antiguedad_dias(maestro integer, modalidad integer, fecha_fin date, fecha_inicio date)
  RETURNS integer AS
$BODY$
	DECLARE total_horas INTEGER;
	DECLARE antiguedad_annios INTEGER;
	
        BEGIN
		SELECT sum(a.horas_lunes)+sum(a.horas_martes)+sum(a.horas_miercoles)+sum(a.horas_jueves)+sum(a.horas_viernes)+sum(a.horas_sabado)+sum(a.horas_domingo) INTO  total_horas
                FROM for_pis_mae_asistencias a
                WHERE a.maestro_id = maestro
			AND a.semana_desde >= (fecha_inicio - time '24:00')
			AND a.semana_hasta <= (fecha_fin + time '24:00');

                IF modalidad = 3 THEN
			RETURN EXTRACT(DAY FROM AGE(fecha_fin , fecha_inicio));
		ELSE
			-- Calculo de Dias desde las Horas (horas/8)
			RETURN (total_horas/8)::integer;
		END IF;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_antiguedad_dias(integer, integer, date, date)
  OWNER TO openerp;
  

-- Function: rrhh_liq_mae_antiguedad_meses(integer, integer, date, date)

-- DROP FUNCTION rrhh_liq_mae_antiguedad_meses(integer, integer, date, date);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_antiguedad_meses(maestro integer, modalidad integer, fecha_fin date, fecha_inicio date)
  RETURNS integer AS
$BODY$
	DECLARE total_horas INTEGER;
	DECLARE antiguedad_meses INTEGER;
	
        BEGIN
		SELECT sum(a.horas_lunes)+sum(a.horas_martes)+sum(a.horas_miercoles)+sum(a.horas_jueves)+sum(a.horas_viernes)+sum(a.horas_sabado)+sum(a.horas_domingo) INTO  total_horas
                FROM for_pis_mae_asistencias a
                WHERE a.maestro_id = maestro
			AND a.semana_desde >= (fecha_inicio - time '24:00')
			AND a.semana_hasta <= (fecha_fin + time '24:00');

                IF modalidad = 3 THEN
			RETURN EXTRACT(MONTH FROM AGE(fecha_fin , fecha_inicio));
		ELSE
			-- Calculo de Meses desde las Horas (horas/8/30)
			RETURN (total_horas/8/30)::integer;
		END IF;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_antiguedad_meses(integer, integer, date, date)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_bonificacion_fin_annio(double precision)

-- DROP FUNCTION rrhh_liq_mae_bonificacion_fin_annio(double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_bonificacion_fin_annio(salario_diario double precision)
  RETURNS double precision AS
$BODY$
    DECLARE bonificacion_fin_annio DOUBLE PRECISION;
        BEGIN
        -- ultimo salario / 30 * 140
        bonificacion_fin_annio = salario_diario * 140;
        RETURN bonificacion_fin_annio;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_bonificacion_fin_annio(double precision)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_bonificacion_fin_annio_fraccionada(double precision, integer)

-- DROP FUNCTION rrhh_liq_mae_bonificacion_fin_annio_fraccionada(double precision, integer);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_bonificacion_fin_annio_fraccionada(salario_bono_fin_annio double precision, meses_antiguedad integer)
  RETURNS double precision AS
$BODY$
    DECLARE bonificacion_fin_annio_fraccionada DOUBLE PRECISION;
        BEGIN
        -- suedo bono_fin_annio * 140 / 12 * antiguedad meses
        bonificacion_fin_annio_fraccionada = (salario_bono_fin_annio *
140/12) * meses_antiguedad;
        RETURN bonificacion_fin_annio_fraccionada;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_bonificacion_fin_annio_fraccionada(double precision, integer)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_bonificacion_fin_annio_mensual(double precision)

-- DROP FUNCTION rrhh_liq_mae_bonificacion_fin_annio_mensual(double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_bonificacion_fin_annio_mensual(bonificacion_fin_annio double precision)
  RETURNS double precision AS
$BODY$
	DECLARE bonificacion_fin_annio_mensual DOUBLE PRECISION;
        BEGIN
		-- ultimo salario / 30 * 140
		bonificacion_fin_annio_mensual = bonificacion_fin_annio/12;
		RETURN bonificacion_fin_annio_mensual;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_bonificacion_fin_annio_mensual(double precision)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_bono_incentivo_ahorro(double precision)

-- DROP FUNCTION rrhh_liq_mae_bono_incentivo_ahorro(double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_bono_incentivo_ahorro(horas_trabajadas double precision)
  RETURNS double precision AS
$BODY$
	DECLARE 
	incentivo_ahorro DOUBLE PRECISION;

        BEGIN

	    IF
	        horas_trabajadas < 1496
	    THEN
                incentivo_ahorro = (horas_trabajadas * 4000)/1496;
        ELSE
	        incentivo_ahorro = 4000;
	    END IF;
		
		RETURN incentivo_ahorro;    
	    
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_bono_incentivo_ahorro(double precision)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_bono_vacacional85(double precision)

-- DROP FUNCTION rrhh_liq_mae_bono_vacacional85(double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_bono_vacacional85(salario_diario double precision)
  RETURNS double precision AS
$BODY$
	DECLARE 
	bono_vacacional85 DOUBLE PRECISION;

        BEGIN
		--bono_vacacional85 = salario diario * 85;
		bono_vacacional85 = salario_diario * 85;
		RETURN bono_vacacional85;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_bono_vacacional85(double precision)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_bono_vacacional_fraccionado(double precision, integer)

-- DROP FUNCTION rrhh_liq_mae_bono_vacacional_fraccionado(double precision, integer);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_bono_vacacional_fraccionado(salario_bono_vacional double precision, meses_antiguedad integer)
  RETURNS double precision AS
$BODY$
	DECLARE bono_vacacional_fraccionado DOUBLE PRECISION;
        BEGIN
		-- salario_bono_vacional * 85 / 12 * antiguedad meses (>= 1 mes)

		bono_vacacional_fraccionado = (salario_bono_vacional * 85/12) * meses_antiguedad;
		RETURN bono_vacacional_fraccionado;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_bono_vacacional_fraccionado(double precision, integer)
  OWNER TO openerp;


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

-- Function: rrhh_liq_mae_cant_dias_interes(date)

-- DROP FUNCTION rrhh_liq_mae_cant_dias_interes(date);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_cant_dias_interes(fecha_fin date)
  RETURNS double precision AS
$BODY$
	DECLARE cant_dias_interes DOUBLE PRECISION;
        BEGIN
			SELECT cantidad_dias INTO  cant_dias_interes
                FROM for_pis_mae_tasas_bcv_prestaciones a
                WHERE a.mes = date_part('month', fecha_fin);               		
		RETURN cant_dias_interes;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_cant_dias_interes(date)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_concatenarpis(integer, date, date)

-- DROP FUNCTION rrhh_liq_mae_concatenarpis(integer, date, date);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_concatenarpis(maestro integer, inicio date, fin date)
  RETURNS character varying AS
$BODY$
DECLARE
	mPIS RECORD;
	pis_mae VARCHAR(240);
	
BEGIN
	pis_mae = '';
	
	FOR mPIS IN
		/*
		SELECT r.nro_preimpreso FROM for_pis_maestros ma
			INNER JOIN for_pis_mae_participacion_pis p
				ON ma.id = p.maestro_id
			INNER JOIN for_pis_registro_inicial r
				ON r.id = p.numero_id
			INNER JOIN for_pis_estados e
				ON r.estado_id = e.id
		WHERE	ma.id = maestro AND
			r.fecha_inicio >= inicio AND r.fecha_cierre <= fin
			-- AND r.estado_id = cer_estado
		*/
		SELECT DISTINCT(r.nro_preimpreso) FROM for_pis_registro_inicial r
			INNER JOIN for_pis_mae_asistencias a
				ON r.id = a.numero_id
			INNER JOIN for_pis_estados e
				ON r.estado_id = e.id
		WHERE	a.id = maestro AND
			r.fecha_inicio >= inicio AND r.fecha_cierre <= fin
			-- AND r.estado_id = cer_estado		
	LOOP
		IF pis_mae <> '' THEN
			pis_mae = pis_mae || ' - ' || mPIS.nro_preimpreso;
		ELSE
			pis_mae = mPIS.nro_preimpreso;
		END IF;
	END LOOP;

	RETURN pis_mae;
END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_concatenarpis(integer, date, date)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_fecha_primera_asistencia(integer)

-- DROP FUNCTION rrhh_liq_mae_fecha_primera_asistencia(integer);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_fecha_primera_asistencia(maestro integer)
  RETURNS date AS
$BODY$
	DECLARE fecha_primera_asistencia DATE;
	
        BEGIN
		SELECT a.semana_desde INTO fecha_primera_asistencia
		FROM for_pis_mae_asistencias a
		WHERE a.maestro_id = maestro
		ORDER BY a.semana_desde ASC
		LIMIT 1;

		RETURN (fecha_primera_asistencia - time '04:30');
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_fecha_primera_asistencia(integer)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_fecha_ultima_asistencia(integer)

-- DROP FUNCTION rrhh_liq_mae_fecha_ultima_asistencia(integer);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_fecha_ultima_asistencia(maestro integer)
  RETURNS date AS
$BODY$
	DECLARE fecha_ultima_asistencia DATE;
	
        BEGIN
		SELECT a.semana_hasta INTO fecha_ultima_asistencia
		FROM for_pis_mae_asistencias a
		WHERE a.maestro_id = maestro
		ORDER BY a.semana_hasta DESC
		LIMIT 1;

		RETURN (fecha_ultima_asistencia + time '04:30');
	END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_fecha_ultima_asistencia(integer)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_id_estado(integer)

-- DROP FUNCTION rrhh_liq_mae_id_estado(integer);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_id_estado(id_dependencia integer)
  RETURNS integer AS
$BODY$
	DECLARE
		dependencia CHAR;
		id_estado INTEGER;
        BEGIN
		SELECT
		(CASE WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES AMAZONAS' THEN '1'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES ANZOATEGUI' THEN '2'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES APURE' THEN '3'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES ARAGUA' THEN '4'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES BARINAS' THEN '5'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES BOLIVAR' THEN '6'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES CARABOBO' THEN '7'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES COJEDES' THEN '8'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES DELTA AMACURO' THEN '9'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES DISTRITO CAPITAL' THEN '10'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES FALCON' THEN '11'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES GUARICO' THEN '12'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES LARA' THEN '13'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES MERIDA' THEN '14'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES MIRANDA' THEN '15'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES MONAGAS' THEN '16'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES NUEVA ESPARTA' THEN '17'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES PORTUGUESA' THEN '18'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES SUCRE' THEN '19'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES TACHIRA' THEN '20'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES TRUJILLO' THEN '21'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES VARGAS' THEN '22'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES YARACUY' THEN '23'
			WHEN d.dependencia_administrativa='GERENCIA REGIONAL INCES ZULIA' THEN '24'
			ELSE '99'
		END)::integer AS "cod_edo" INTO id_estado
                FROM sisr_pla_dependencias_administrativas d
                WHERE d.id = id_dependencia;

		RETURN id_estado;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_id_estado(integer)
  OWNER TO postgres;


-- Function: rrhh_liq_mae_id_tasa_interes_prest(date)

-- DROP FUNCTION rrhh_liq_mae_id_tasa_interes_prest(date);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_id_tasa_interes_prest(fecha_fin date)
  RETURNS integer AS
$BODY$
	DECLARE id_tasa_interes_prest INTEGER;
        BEGIN
		

		SELECT id INTO  id_tasa_interes_prest
                FROM for_pis_mae_tasas_bcv_prestaciones a
                WHERE a.mes = date_part('month', fecha_fin);
                           		
		RETURN id_tasa_interes_prest;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_id_tasa_interes_prest(date)
  OWNER TO postgres;


-- Function: rrhh_liq_mae_interes_prest(double precision, double precision, integer)

-- DROP FUNCTION rrhh_liq_mae_interes_prest(double precision, double precision, integer);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_interes_prest(prestaciones double precision, tasa_interes_prest double precision, cant_dias_interes integer)
  RETURNS double precision AS
$BODY$
	DECLARE interes_prest DOUBLE PRECISION;
        BEGIN
		--interes_prest = ((prestaciones * tasa_interes_prest) /100 /365) * cant_dias_interes;
		-- Cambio en la formula a solicitud de RRHH el día 01/11/2014
		interes_prest = ((prestaciones * tasa_interes_prest) /365) * cant_dias_interes;
                           		
		RETURN interes_prest;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_interes_prest(double precision, double precision, integer)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_prestaciones(double precision, integer)

-- DROP FUNCTION rrhh_liq_mae_prestaciones(double precision, integer);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_prestaciones(salario_integral_diario double precision, meses_antiguedad integer)
  RETURNS double precision AS
$BODY$
	DECLARE prestaciones DOUBLE PRECISION;
        BEGIN
		-- antiguedad meses * 5 * salario integral diario 
                prestaciones = meses_antiguedad * 5 * salario_integral_diario;
		
		RETURN prestaciones;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_prestaciones(double precision, integer)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_salario_anual(double precision, double precision, double precision)

-- DROP FUNCTION rrhh_liq_mae_salario_anual(double precision, double precision, double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_salario_anual(salario_diario double precision, salario_bono_vacional double precision, salario_bono_fin_annio double precision)
  RETURNS double precision AS
$BODY$
	DECLARE salario_anual DOUBLE PRECISION;
        BEGIN
		-- (salario diario + salario bonificacion fin annio + salario bono vacacional) * 360
          salario_anual = (salario_diario + salario_bono_vacional + salario_bono_fin_annio) * 360;

		RETURN salario_anual;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_salario_anual(double precision, double precision, double precision)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_salario_bono_fin_annio(double precision, double precision)

-- DROP FUNCTION rrhh_liq_mae_salario_bono_fin_annio(double precision, double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_salario_bono_fin_annio(salario_diario double precision, bono_vacacional_mensual double precision)
  RETURNS double precision AS
$BODY$
	DECLARE 
	salario_bono_fin_annio DOUBLE PRECISION;

        BEGIN
		-- salario diario + alicuota de BFA
		salario_bono_fin_annio = salario_diario + (bono_vacacional_mensual/30);
		
		RETURN salario_bono_fin_annio;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_salario_bono_fin_annio(double precision, double precision)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_salario_bono_vacional(double precision, double precision)

-- DROP FUNCTION rrhh_liq_mae_salario_bono_vacional(double precision, double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_salario_bono_vacional(salario_diario double precision, bonificacion_fin_annio double precision)
  RETURNS double precision AS
$BODY$
	DECLARE 
	salario_bono_vacional DOUBLE PRECISION;


        BEGIN
		-- salario diario + alicuota de BFA
		salario_bono_vacional = salario_diario + ((bonificacion_fin_annio/12)/30);
		
		RETURN salario_bono_vacional;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_salario_bono_vacional(double precision, double precision)
  OWNER TO openerp;

-- Function: rrhh_liq_mae_salario_diario(double precision)

-- DROP FUNCTION rrhh_liq_mae_salario_diario(double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_salario_diario(salario_mensual double precision)
  RETURNS double precision AS
$BODY$
	DECLARE 
	salario_diario DOUBLE PRECISION;


        BEGIN
		-- salario mensual / 30
		-- salario_diario = salario_mensual/30;

		-- Modificacion según GG RRHH Mie 22 Oct 2014 7:00 PM
		salario_diario = salario_mensual/30;
		
		RETURN salario_diario;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_salario_diario(double precision)
  OWNER TO openerp;

-- Function: rrhh_liq_mae_salario_integral_diario(double precision)

-- DROP FUNCTION rrhh_liq_mae_salario_integral_diario(double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_salario_integral_diario(salario_integral_mensual double precision)
  RETURNS double precision AS
$BODY$
	DECLARE salario_integral_diario DOUBLE PRECISION;
        BEGIN
		-- salario integral mensual / 30 (>= 1 mes)
		salario_integral_diario = salario_integral_mensual/30;
		RETURN salario_integral_diario;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_salario_integral_diario(double precision)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_salario_integral_mensual(double precision)

-- DROP FUNCTION rrhh_liq_mae_salario_integral_mensual(double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_salario_integral_mensual(salario_anual double precision)
  RETURNS double precision AS
$BODY$
	DECLARE salario_integral_mensual DOUBLE PRECISION;
        BEGIN
		-- salario anual / 12
           salario_integral_mensual = salario_anual/12;
		RETURN salario_integral_mensual;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_salario_integral_mensual(double precision)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_subtotal_asignaciones_legales(double precision, double precision, double precision)

-- DROP FUNCTION rrhh_liq_mae_subtotal_asignaciones_legales(double precision, double precision, double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_subtotal_asignaciones_legales(vacaciones_fraccionadas double precision, bono_vacacional_fraccionado double precision, bonificacion_fin_annio_fraccionada double precision)
  RETURNS double precision AS
$BODY$
	DECLARE subtotal_asignacioneslegales DOUBLE PRECISION;
        BEGIN
		
                subtotal_asignacioneslegales = (vacaciones_fraccionadas + bono_vacacional_fraccionado +  bonificacion_fin_annio_fraccionada);
		
		RETURN subtotal_asignacioneslegales;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_subtotal_asignaciones_legales(double precision, double precision, double precision)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_subtotal_otras_asignaciones(double precision)

-- DROP FUNCTION rrhh_liq_mae_subtotal_otras_asignaciones(double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_subtotal_otras_asignaciones(incentivo_ahorro double precision)
  RETURNS double precision AS
$BODY$
	DECLARE subtotal_otras_asignaciones DOUBLE PRECISION;
        BEGIN
		
                subtotal_otras_asignaciones = incentivo_ahorro;
		
		RETURN subtotal_otras_asignaciones;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_subtotal_otras_asignaciones(double precision)
  OWNER TO openerp;

-- Function: rrhh_liq_mae_tasa_interes_prest(date)

-- DROP FUNCTION rrhh_liq_mae_tasa_interes_prest(date);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_tasa_interes_prest(fecha_fin date)
  RETURNS double precision AS
$BODY$
	DECLARE tasa_interes_prest DOUBLE PRECISION;
        BEGIN
		

		SELECT tasa_interes INTO  tasa_interes_prest
                FROM for_pis_mae_tasas_bcv_prestaciones a
                WHERE a.mes = date_part('month', fecha_fin);
                           		
		RETURN tasa_interes_prest;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_tasa_interes_prest(date)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_total_asignaciones(double precision, double precision, double precision)

-- DROP FUNCTION rrhh_liq_mae_total_asignaciones(double precision, double precision, double precision);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_total_asignaciones(prestaciones double precision, subtotal_asignacioneslegales double precision, subtotal_otras_asignaciones double precision)
  RETURNS double precision AS
$BODY$
	DECLARE total_asignaciones DOUBLE PRECISION;
        BEGIN
		
                total_asignaciones = (prestaciones + subtotal_asignacioneslegales +  subtotal_otras_asignaciones);
		
		RETURN total_asignaciones;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_total_asignaciones(double precision, double precision, double precision)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_total_horas_trabajadas(integer, date, date)

-- DROP FUNCTION rrhh_liq_mae_total_horas_trabajadas(integer, date, date);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_total_horas_trabajadas(maestroid integer, fecha_inicio date, fecha_fin date)
  RETURNS integer AS
$BODY$
	DECLARE total_horas INTEGER;
        BEGIN
		--Se toman en cuenta los sabados y domingos para el calculo total de horas trabajadas
		--SELECT sum(a.horas_lunes)+sum(a.horas_martes)+sum(a.horas_miercoles)+sum(a.horas_jueves)+sum(a.horas_viernes)
		SELECT sum(a.horas_lunes)+sum(a.horas_martes)+sum(a.horas_miercoles)+sum(a.horas_jueves)+sum(a.horas_viernes)+sum(a.horas_sabado)+sum(a.horas_domingo) INTO  total_horas
                FROM for_pis_mae_asistencias a
                WHERE a.maestro_id = maestroid
			AND a.semana_desde >= (fecha_inicio - time '24:00')
			AND a.semana_hasta <= (fecha_fin + time '24:00');
		RETURN total_horas;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_total_horas_trabajadas(integer, date, date)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_ultimo_salario_mensual(integer)

-- DROP FUNCTION rrhh_liq_mae_ultimo_salario_mensual(integer);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_ultimo_salario_mensual(maestro integer)
  RETURNS double precision AS
$BODY$
	DECLARE ultimo_salario DOUBLE PRECISION;
        BEGIN
		SELECT SUM(monto_pago) INTO ultimo_salario 
		FROM (SELECT monto_pago
			FROM for_pis_mae_consolidado_detalle
			WHERE maestro_id = maestro
			ORDER BY hasta DESC
			LIMIT 2) AS quincenas;

		RETURN ultimo_salario;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_ultimo_salario_mensual(integer)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_ultimo_salario_mensual_promediado(integer, integer, integer, date, date)

-- DROP FUNCTION rrhh_liq_mae_ultimo_salario_mensual_promediado(integer, integer, integer, date, date);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_ultimo_salario_mensual_promediado(maestro integer, meses integer, modalidad integer, fecha_fin date, fecha_inicio date)
  RETURNS double precision AS
$BODY$
	DECLARE total_horas INTEGER;
	DECLARE ultimo_salario DOUBLE PRECISION;
        BEGIN
		/*
		SELECT SUM(monto_pago) INTO ultimo_salario 
		FROM for_pis_mae_consolidado_detalle
		WHERE maestro_id = maestro
		GROUP BY maestro_id;
		*/
		
		SELECT sum(monto_pago) INTO ultimo_salario 
		FROM for_pis_mae_consolidado_detalle
		WHERE maestro_id = maestro
		GROUP BY maestro_id, consolidado_id
		ORDER BY consolidado_id DESC
		LIMIT 1;

		SELECT sum(a.horas_lunes)+sum(a.horas_martes)+sum(a.horas_miercoles)+sum(a.horas_jueves)+sum(a.horas_viernes)+sum(a.horas_sabado)+sum(a.horas_domingo) INTO  total_horas
                FROM for_pis_mae_asistencias a
                WHERE a.maestro_id = maestro
                  AND a.semana_desde >= (fecha_inicio - time '24:00')
		  AND a.semana_hasta <= (fecha_fin + time '24:00');
		
		IF meses = 0 THEN
			RETURN (ultimo_salario - ultimo_salario);
		ELSE
			IF modalidad = 3 THEN
				-- Calculo de Ultimo Salario/ meses de antiguedad. Cada mes representa veinte (20) días
				RETURN (ultimo_salario / meses);
			ELSE
				-- Calculo de Ultimo Salario/horas trabajadas * 30
				
				RETURN ((ultimo_salario/total_horas) * 30);
				
			END IF;
		END IF;		
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_ultimo_salario_mensual_promediado(integer, integer, integer, date, date)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_vacaciones_fraccionadas(double precision, integer)

-- DROP FUNCTION rrhh_liq_mae_vacaciones_fraccionadas(double precision, integer);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_vacaciones_fraccionadas(salario_diario double precision, meses_antiguedad integer)
  RETURNS double precision AS
$BODY$
    DECLARE vacaciones_fraccionadas DOUBLE PRECISION;
        BEGIN
        -- suedo diario * 30 / 12 * antiguedad meses (>= 1 mes)
    vacaciones_fraccionadas = (salario_diario * 30/12) * meses_antiguedad;
        RETURN vacaciones_fraccionadas;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_vacaciones_fraccionadas(double precision, integer)
  OWNER TO openerp;


-- Function: rrhh_liq_mae_valor_hora(integer)

-- DROP FUNCTION rrhh_liq_mae_valor_hora(integer);

CREATE OR REPLACE FUNCTION rrhh_liq_mae_valor_hora(maestro_id integer)
  RETURNS double precision AS
$BODY$
	DECLARE valor_hora DOUBLE PRECISION;
        BEGIN
		SELECT a.valor_hora INTO valor_hora
		FROM for_pis_mae_valor_hora a
		INNER JOIN for_pis_maestros mae on mae.id = maestro_id
		WHERE mae.nivel_id = a.id; 
		RETURN valor_hora;
        END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION rrhh_liq_mae_valor_hora(integer)
  OWNER TO openerp;

