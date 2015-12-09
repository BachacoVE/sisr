-- Function: generar_liquidacion_maestro()

-- DROP FUNCTION generar_liquidacion_maestro();

CREATE OR REPLACE FUNCTION generar_liquidacion_maestro()
  RETURNS trigger AS
$BODY$
DECLARE

  -- DECLARACIONES DE VARIABLES (DE CAMPOS)
  sp_bas_bono_vacacional double precision; -- Bono Vacacional
  sp_bvf_salario_mensual double precision; -- Salario Mensual
  sp_bfaf_monto_a_pagar double precision; -- Monto a Pagar
  sp_maestro_id integer; -- Maestro
  sp_total_horas integer; -- Total Horas
  sp_vfr_dias_a_pagar double precision; -- Dias a Pagar
  sp_pis_participa text; -- PIS donde participó
  sp_bvf_dias_a_pagar double precision; -- Días a Pagar
  sp_motivo_egreso_id integer; -- Codigo Motivo Egreso
  sp_ded_concepto character varying(200); -- Concepto de Deducción
  sp_ultimo_salario double precision; -- Ultimo Salario
  sp_cargo character varying(100); -- Cargo
  sp_vfr_monto_a_pagar double precision; -- Monto a Pagar
  sp_ded_monto_a_deducir double precision; -- Monto a Deducir
  sp_vfr_total_dias_pagar double precision; -- Total Dias a Pagar
  sp_vfr_sueldo_mensual double precision; -- Salario Mensual
  sp_bas_salario_mensual double precision; -- Salario Mensual
  sp_vfr_salario_diario double precision; -- Salario Diario
  sp_bvf_total_dias_pagar double precision; -- Total Dias a Pagar
  sp_bas_salario_int_diario_pres double precision; -- Salario Integral Diario (Prestaciones)
  sp_asig_tope_horas integer; -- Tope Horas
  sp_bvf_monto_a_pagar double precision; -- Monto a Pagar
  sp_bas_salario_anual double precision; -- Salario Anual
  sp_bfaf_total_dias_a_pagar double precision; -- Total Dias a Pagar
  sp_bfaf_dias_a_pagar double precision; -- Días a Pagar
  sp_bas_salario_diario double precision; -- Salario Diario
  sp_bvf_meses integer; -- Meses a Pagar
  sp_asig_cantidad_horas integer; -- Cantidad Horas
  sp_fecha_inicio date; -- Fecha Inicio
  sp_bas_bonificacion_fin double precision; -- Bonificación Fin Año
  sp_bas_alicuota_bono_vac double precision; -- Alícuota Diaria BV (Dozavo)
  sp_pres_sueldo_integral_mens double precision; -- Sueldo Integral Mensual
  sp_bvf_salario_diario double precision; -- Salario Diario
  sp_asig_monto_a_pagar double precision; -- Monto a Pagar
  sp_bfaf_salario_diario double precision; -- Salario Diario
  sp_pres_total_dias_pagar integer; -- Total días a Pagar
  sp_bas_salario_int_bfa double precision; -- Salario Integral Diario (Aguinaldos)
  sp_bas_alicuota_aguinaldo double precision; -- Alícuota Diaria BFA (Dozavo)
  sp_valor_hora double precision; -- Valor Hora
  sp_pres_sueldo_integral_diario double precision; -- Sueldo Integral Diario
  sp_estado_id integer; -- Código Estado
  sp_dependencia character varying(200); -- Dependencia
  sp_fecha_fin date; -- Fecha Fin
  sp_bfaf_meses integer; -- Meses a Pagar
  sp_asig_monto double precision; -- Monto
  sp_bfaf_salario_mensual double precision; -- Salario Mensual
  sp_vfr_meses integer; -- Meses a Pagar
  sp_pres_monto_a_pagar double precision; -- Monto a Pagar
  sp_bas_salario_int_bv double precision; -- Salario Integral Diario (Bono Vacacional)
  sp_dependencia_id integer; -- Dependencia
  sp_modalidad_id integer; -- Modalidad de Liquidación
  sp_total_asignaciones_legales double precision; -- Total de Asignaciones Legales
  sp_total_otras_asignaciones double precision; -- Total de otras Asignaciones
  sp_total_deducciones double precision; -- Total de Deducciones
  sp_total_liquidacion double precision; -- Total General de la Liquidación

  sp_antiguedad_dias integer; -- Antiguedad Dias
  sp_antiguedad_meses integer; -- Antiguedad Meses
  sp_antiguedad_annios integer; -- Antiguedad Años

  -- DECLARACIONES DE VARIABLES ADICIONALES (NO SE CREARON COMO CAMPOS)
  sp_bas_bono_vacacional_mensual double precision;
  sp_bas_bonificacion_fin_mensual double precision;

  --Aplica para el año 2015, bono retroactivo de la firma del contrato colectivo
  sp_bono_firma_contrato double precision;
  sp_bono_firma_tope double precision;
	sp_monto_bono_firma double precision;

  -- DECLARACIONES DE VARIABLES ADICIONALES (Jue 16 / Vie 17 Oct)
  sp_total_asignaciones double precision; -- Total Asignaciones
  sp_total_pres_mas_interes double precision; -- Total Interes mas Prestaciones

  sp_ipre_tasa_interes_id integer; -- (Id o codigo de) Tasa de Interes Prestaciones
  sp_ipre_mes_tasa integer; -- Mes para cálculo de Intereses
  sp_ipre_monto_interes double precision; -- Interes sobre Prestaciones
  sp_ipre_dias_calculos integer; -- Días para cálculo de Intereses
  sp_ipre_tasa_interes_monto double precision; -- Monto de la Tasa de Interes Prestaciones
  
  sp_asig_concepto1 integer; -- Concepto de asignación1  
  sp_asig_concepto2 integer; -- Concepto de asignación2
  sp_asig_concepto3 integer; -- Concepto de asignación3

  sp_asig_monto_de_asignacion1 double precision; -- Monto de asignación1
  sp_asig_monto_de_asignacion2 double precision; -- Monto de Asignación2
  sp_asig_monto_de_asignacion3 double precision; -- Monto de Asignación3

  sp_ded_concepto1 integer; -- Concepto de deducción1
  sp_ded_concepto2 integer; -- Concepto de deducción2
  sp_ded_concepto3 integer; -- Concepto de deducción3

  sp_ded_monto_a_deducir1 double precision; -- Monto a deducir1
  sp_ded_monto_a_deducir2 double precision; -- Monto a deducir2
  sp_ded_monto_a_deducir3 double precision; -- Monto a deducir3

	BEGIN

	-- Función para generar los calculos de detalle de las Liquidaciones de Maestros de los PIS
		-- VALORES a pasar como PARAMETROS a las FUNCIONES:
		
		-- NEW.maestro_id
		-- NEW.dependencia_id
		-- NEW.modalidad_id,
		-- NEW.motivo_egreso_id,
		-- NEW.fecha_inicio,
		-- NEW.fecha_fin,
		-- NEW.ded_concepto,
		-- NEW.ded_monto_a_deducir,

	-- ASIGNACIONES / INICIALIZACIONES
	sp_cargo = 'Promotor Técnico Productivo';
	sp_estado_id = rrhh_liq_mae_id_estado(NEW.dependencia_id) ; --F(x) para RECUPERAR

	-- sp_fecha_inicio = NEW.fecha_inicio;
	sp_fecha_inicio = rrhh_liq_mae_fecha_primera_asistencia(NEW.maestro_id);
	-- sp_fecha_fin = NEW.fecha_fin;
	sp_fecha_fin = rrhh_liq_mae_fecha_ultima_asistencia(NEW.maestro_id);
		
	sp_valor_hora = rrhh_liq_mae_valor_hora(NEW.maestro_id, sp_fecha_fin);
	sp_total_horas = rrhh_liq_mae_total_horas_trabajadas(NEW.maestro_id, sp_fecha_inicio, sp_fecha_fin);
	-- sp_ultimo_salario = rrhh_liq_mae_ultimo_salario_mensual(NEW.maestro_id);
	sp_pis_participa = rrhh_liq_mae_concatenarpis(NEW.maestro_id, sp_fecha_inicio, sp_fecha_fin);

	-- sp_antiguedad_annios = 0; --F(x) para RECUPERAR
	--sp_antiguedad_annios = 	EXTRACT(YEAR FROM AGE(NEW.fecha_fin , NEW.fecha_inicio));
	sp_antiguedad_annios = 	rrhh_liq_mae_antiguedad_annios(NEW.maestro_id, NEW.modalidad_id, sp_fecha_fin, sp_fecha_inicio);
	-- sp_antiguedad_meses = 6; --F(x) para RECUPERAR
	-- sp_antiguedad_meses = EXTRACT(MONTH FROM AGE(NEW.fecha_fin , NEW.fecha_inicio));
	sp_antiguedad_meses = 	rrhh_liq_mae_antiguedad_meses(NEW.maestro_id, NEW.modalidad_id, sp_fecha_fin, sp_fecha_inicio);
	--sp_antiguedad_dias = 13; --F(x) para RECUPERAR
	--sp_antiguedad_dias = EXTRACT(DAY FROM AGE(NEW.fecha_fin , NEW.fecha_inicio));
	sp_antiguedad_dias = 	rrhh_liq_mae_antiguedad_dias(NEW.maestro_id, NEW.modalidad_id, sp_fecha_fin, sp_fecha_inicio);

	-- Modificación según solicitud e indicaciones de la GG RRHH el mie 22 Oct 2014 7:00 PM
	sp_ultimo_salario = rrhh_liq_mae_ultimo_salario_mensual_promediado(NEW.maestro_id, sp_antiguedad_meses, NEW.modalidad_id, sp_fecha_fin, sp_fecha_inicio);

	sp_bas_salario_mensual = sp_ultimo_salario;
	sp_bas_salario_diario = rrhh_liq_mae_salario_diario(sp_bas_salario_mensual);
	
	sp_bas_bono_vacacional = rrhh_liq_mae_bono_vacacional85(sp_bas_salario_diario);
	sp_bas_bono_vacacional_mensual = sp_bas_bono_vacacional/12;

	sp_bas_salario_int_bv = rrhh_liq_mae_salario_bono_vacional(sp_bas_salario_diario);
	sp_bas_salario_int_bfa = rrhh_liq_mae_salario_bono_fin_annio(sp_bas_salario_diario, sp_bas_bono_vacacional_mensual);

	sp_bas_bonificacion_fin = rrhh_liq_mae_bonificacion_fin_annio(sp_bas_salario_int_bfa);
	sp_bas_bonificacion_fin_mensual = sp_bas_bonificacion_fin/12;
	
	sp_bas_alicuota_aguinaldo = rrhh_liq_mae_alicuota_diaria_bonificacion_fin_annio(sp_bas_salario_mensual, sp_bas_bono_vacacional_mensual);
	sp_bas_alicuota_bono_vac = rrhh_liq_mae_alicuota_diaria_bono_vacacional(sp_bas_salario_mensual);
	

	
	sp_bas_salario_anual = rrhh_liq_mae_salario_anual(sp_bas_salario_diario, sp_bas_alicuota_bono_vac, sp_bas_alicuota_aguinaldo);

	sp_pres_sueldo_integral_mens = rrhh_liq_mae_salario_integral_mensual(sp_bas_salario_anual);
	-- sp_bas_salario_int_diario_pres = rrhh_liq_mae_salario_integral_diario(sp_pres_sueldo_integral_mens);
	sp_bas_salario_int_diario_pres = sp_bas_salario_diario + sp_bas_alicuota_aguinaldo + sp_bas_alicuota_bono_vac;
	
	sp_pres_sueldo_integral_diario = sp_bas_salario_int_diario_pres;
	sp_pres_total_dias_pagar = sp_antiguedad_meses * 5;
	sp_pres_monto_a_pagar = sp_pres_sueldo_integral_diario * sp_pres_total_dias_pagar;

	-- Asignación por INCENTIVO AL AHORRO
	sp_asig_tope_horas = 1496; -- Valor CONSTANTE para el año 2014
	sp_asig_monto = rrhh_liq_mae_monto_bono_incentivo_ahorro(sp_fecha_inicio, sp_fecha_fin);
	sp_asig_cantidad_horas = sp_total_horas;
	sp_asig_monto_a_pagar = rrhh_liq_mae_bono_incentivo_ahorro(sp_asig_cantidad_horas, sp_asig_tope_horas, sp_asig_monto);
			
	-- rrhh_liq_mae_bono_vacacional_fraccionado(salario_bono_vacional; meses_antiguedad)
	sp_vfr_dias_a_pagar = 2.50;  -- CONSTANTE
	sp_vfr_meses = sp_antiguedad_meses;
	sp_vfr_total_dias_pagar = sp_vfr_meses * sp_vfr_dias_a_pagar;
	sp_vfr_sueldo_mensual = sp_bas_salario_mensual;
	sp_vfr_salario_diario = sp_bas_salario_diario;
	sp_vfr_monto_a_pagar = sp_vfr_salario_diario * sp_vfr_total_dias_pagar;

	sp_bvf_dias_a_pagar = 7.08;  -- CONSTANTE
	sp_bvf_meses = sp_antiguedad_meses;
	sp_bvf_total_dias_pagar = sp_bvf_meses * sp_bvf_dias_a_pagar; 
	sp_bvf_salario_mensual = sp_bas_bono_vacacional_mensual;
	sp_bvf_salario_diario = sp_bas_salario_int_bv;
	sp_bvf_monto_a_pagar = sp_bvf_salario_diario * sp_bvf_total_dias_pagar;
			  			      
	sp_bfaf_dias_a_pagar = 11.67;  -- CONSTANTE
	sp_bfaf_meses = sp_antiguedad_meses;
	sp_bfaf_total_dias_a_pagar = sp_bfaf_meses * sp_bfaf_dias_a_pagar;
	sp_bfaf_salario_mensual = sp_bas_bonificacion_fin_mensual;
	sp_bfaf_salario_diario = sp_bas_salario_int_bfa;
	sp_bfaf_monto_a_pagar = sp_bfaf_salario_diario * sp_bfaf_total_dias_a_pagar;

	sp_bono_firma_tope = 1496;
	sp_monto_bono_firma = rrhh_liq_monto_bono_firma_contrato(sp_fecha_inicio, sp_fecha_fin);
	sp_bono_firma_contrato = rrhh_liq_bono_firma_contrato(sp_total_horas, sp_bono_firma_tope, sp_monto_bono_firma);
	-- INTERESES SOBRE PRESTACIONES
	sp_ipre_tasa_interes_id = rrhh_liq_mae_id_tasa_interes_prest(sp_fecha_fin); 
	sp_ipre_mes_tasa = date_part('month',sp_fecha_fin); --F(x) para RECUPERAR
	sp_ipre_dias_calculos = rrhh_liq_mae_cant_dias_interes(sp_fecha_fin, sp_ipre_tasa_interes_id);
	-- Modificación según solicitud e indicaciones de la GG RRHH el mar 04 Nov 2014 9:00 PM
	-- sp_ipre_monto_interes = rrhh_liq_mae_tasa_interes_prest(sp_fecha_fin);
	sp_ipre_tasa_interes_monto = rrhh_liq_mae_tasa_interes_prest(sp_fecha_fin, sp_ipre_tasa_interes_id);
	sp_ipre_monto_interes = rrhh_liq_mae_interes_prest(sp_pres_monto_a_pagar, sp_ipre_tasa_interes_monto, sp_ipre_dias_calculos);
	-- Total Interes sobre Prestaciones
	-- sp_total_pres_mas_interes = sp_pres_sueldo_integral_mens * (sp_ipre_monto_interes / 100) / 365 * sp_ipre_dias_calculos;
	sp_total_pres_mas_interes = sp_ipre_monto_interes;
	
	-- ASIGNACIONES LEGALES comprende:
	-- Prestaciones + Intereses sobre Prestaciones + Incentivo al Ahorro + VFR + BVF + BFAF
	-- para 2015 se pagara bono de forma de contrato colectivo 'sp_bono_firma_contrato', y no se pagara interes de prestaciones 'sp_total_pres_mas_interes'
	sp_total_asignaciones_legales = sp_pres_monto_a_pagar + sp_asig_monto_a_pagar + sp_vfr_monto_a_pagar + sp_bvf_monto_a_pagar + sp_bfaf_monto_a_pagar + sp_bono_firma_contrato;

	sp_asig_monto_de_asignacion1 = NEW.asig_monto_de_asignacion1;
	sp_asig_monto_de_asignacion2 = NEW.asig_monto_de_asignacion2;
	sp_asig_monto_de_asignacion3 = NEW.asig_monto_de_asignacion3;
	sp_total_otras_asignaciones = sp_asig_monto_de_asignacion1 + sp_asig_monto_de_asignacion2 + sp_asig_monto_de_asignacion3;

	sp_total_asignaciones = sp_total_asignaciones_legales + sp_total_otras_asignaciones;
	
	sp_ded_monto_a_deducir1 = NEW.ded_monto_a_deducir1;
	sp_ded_monto_a_deducir2 = NEW.ded_monto_a_deducir2;
	sp_ded_monto_a_deducir3 = NEW.ded_monto_a_deducir3;
	sp_total_deducciones = sp_ded_monto_a_deducir1 + sp_ded_monto_a_deducir2 + sp_ded_monto_a_deducir3;
	
	sp_total_liquidacion = sp_total_asignaciones - sp_total_deducciones;
	

	IF (TG_OP = 'INSERT') THEN
	
		UPDATE for_pis_mae_liquidaciones SET
			cargo = sp_cargo,
			estado_id = sp_estado_id,
			valor_hora = sp_valor_hora,
			total_horas = sp_total_horas,
			ultimo_salario = sp_ultimo_salario,
			pis_participa = sp_pis_participa,

			-- Actualiza los valores introducidos a F1A y FUA
			fecha_inicio = sp_fecha_inicio,
			fecha_fin = sp_fecha_fin,
			
			antiguedad_annios = sp_antiguedad_annios,
			antiguedad_meses = sp_antiguedad_meses,
			antiguedad_dias = sp_antiguedad_dias,

			bas_salario_mensual = sp_bas_salario_mensual,
			bas_salario_diario = sp_bas_salario_diario,
			bas_bono_vacacional = sp_bas_bono_vacacional,
			bas_bonificacion_fin = sp_bas_bonificacion_fin,
			-- bas_bonificacion_fin_mensual = sp_bas_bonificacion_fin_mensual,
			bas_alicuota_aguinaldo = sp_bas_alicuota_aguinaldo,
			
			bas_alicuota_bono_vac = sp_bas_alicuota_bono_vac,
			bas_salario_int_bv = sp_bas_salario_int_bv,
			bas_salario_int_bfa = sp_bas_salario_int_bfa,
			bas_salario_anual = sp_bas_salario_anual,

			pres_sueldo_integral_mens = sp_pres_sueldo_integral_mens,
			bas_salario_int_diario_pres = sp_bas_salario_int_diario_pres,
			pres_sueldo_integral_diario = sp_pres_sueldo_integral_diario,
			pres_total_dias_pagar = sp_pres_total_dias_pagar,
			pres_monto_a_pagar = sp_pres_monto_a_pagar,

			ipre_tasa_interes_id = sp_ipre_tasa_interes_id,
			ipre_mes_tasa = sp_ipre_mes_tasa,
			ipre_monto_interes = sp_ipre_monto_interes,
			ipre_dias_calculos = sp_ipre_dias_calculos,
			total_pres_mas_interes = sp_total_pres_mas_interes,

			asig_tope_horas = sp_asig_tope_horas,
			asig_monto_a_pagar = sp_asig_monto_a_pagar,
			asig_monto = sp_asig_monto,
			asig_cantidad_horas = sp_asig_cantidad_horas,
			
			bvf_meses = sp_bvf_meses,
			bvf_dias_a_pagar = sp_bvf_dias_a_pagar,
			bvf_total_dias_pagar = sp_bvf_total_dias_pagar,
			bvf_salario_mensual = sp_bvf_salario_mensual,
			bvf_salario_diario = sp_bvf_salario_diario,
			bvf_monto_a_pagar = sp_bvf_monto_a_pagar,
			  
			vfr_meses = sp_vfr_meses,
			vfr_dias_a_pagar = sp_vfr_dias_a_pagar,
			vfr_total_dias_pagar = sp_vfr_total_dias_pagar,
			vfr_sueldo_mensual = sp_vfr_sueldo_mensual,
			vfr_salario_diario = sp_vfr_salario_diario,
			vfr_monto_a_pagar = sp_vfr_monto_a_pagar,
			      
			bfaf_meses = sp_bfaf_meses,
			bfaf_dias_a_pagar = sp_bfaf_dias_a_pagar,
			bfaf_total_dias_a_pagar = sp_bfaf_total_dias_a_pagar,
			bfaf_salario_mensual = sp_bfaf_salario_mensual,
			bfaf_salario_diario = sp_bfaf_salario_diario,
			bfaf_monto_a_pagar = sp_bfaf_monto_a_pagar,

			total_asignaciones_legales = sp_total_asignaciones_legales,
                        total_otras_asignaciones = sp_total_otras_asignaciones,
			total_asignaciones = sp_total_asignaciones,
                        total_deducciones = sp_total_deducciones,
			total_liquidacion = sp_total_liquidacion,

			--El bono de firma de contrato para el año 2015 se asume en la seccion de bonos
			bono_concepto1 = 'Bono firma Contrato Colectivo 2015',
			bono_tope_horas1 = sp_bono_firma_tope,
			bono_monto1 = sp_monto_bono_firma,
			bono_cantidad_horas1 = sp_total_horas,
			bono_monto_a_pagar1 = sp_bono_firma_contrato

			WHERE for_pis_mae_liquidaciones.id = NEW.id;
	
	END IF;

	/*
	-- Función(es) a Ejecutar en caso de Actualización de la Tabla Maestra de Liquidaciones
	IF (TG_OP = 'UPDATE') THEN 
		UPDATE for_pis_mae_liquidaciones mliq
		(campos) = (valores)
		WHERE mliq.id = OLD.id;
	END IF;

	-- Función(es) a Ejecutar en caso de Eliminación de la Tabla Maestra de Liquidaciones
	IF (TG_OP = 'DELETE') THEN 
		DELETE FROM for_pis_mae_liquidaciones mliq
		WHERE mliq.id = OLD.id;
	END IF;
	*/
	RETURN NEW;
END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION generar_liquidacion_maestro()
  OWNER TO openerp;
