-- View: for_pis_mae_reporte_planilla_liquidacion_view

-- DROP VIEW for_pis_mae_reporte_planilla_liquidacion_view;

CREATE OR REPLACE VIEW for_pis_mae_reporte_planilla_liquidacion_view AS 
 SELECT liq.id, liq.create_uid, liq.create_date, liq.write_date, liq.write_uid, liq.ipre_monto_interes, liq.total_horas, liq.pis_participa, to_char(liq.fecha_fin::timestamp with time zone, 'DD/MM/YYYY'::text) AS fecha_fin, liq.dependencia_id, liq.ded_concepto, liq.ultimo_salario, liq.ded_monto_a_deducir, liq.vfr_salario_diario, liq.bvf_total_dias_pagar, liq.bas_salario_int_diario_pres, liq.bvf_monto_a_pagar, liq.ipre_dias_calculos, liq.bas_salario_anual, liq.modalidad_id, liq.bfaf_total_dias_a_pagar, liq.bvf_meses, liq.asig_cantidad_horas, liq.total_asignaciones, liq.bas_alicuota_bono_vac, liq.vfr_sueldo_mensual, liq.bfaf_monto_a_pagar, liq.ded_concepto2, liq.ded_concepto3, liq.ded_concepto1, liq.asig_monto_a_pagar, liq.antiguedad_meses, liq.pres_total_dias_pagar, liq.bas_alicuota_aguinaldo, liq.valor_hora, liq.total_liquidacion, liq.total_asignaciones_legales, liq.ded_monto_a_deducir3, liq.asig_monto_de_asignacion2, liq.asig_monto_de_asignacion3, liq.asig_monto_de_asignacion1, liq.total_otras_asignaciones, liq.bfaf_salario_mensual, liq.vfr_meses, liq.total_pres_mas_interes, liq.bas_bono_vacacional, liq.maestro_id, liq.ipre_tasa_interes_id, liq.pres_sueldo_integral_diario, liq.bvf_dias_a_pagar, liq.motivo_egreso_id, liq.cargo, liq.vfr_total_dias_pagar, liq.bas_salario_mensual, liq.vfr_monto_a_pagar, liq.asig_tope_horas, liq.total_deducciones, to_char(liq.fecha_inicio::timestamp with time zone, 'DD/MM/YYYY'::text) AS fecha_inicio, liq.ded_monto_a_deducir1, liq.ded_monto_a_deducir2, liq.antiguedad_annios, liq.bfaf_dias_a_pagar, liq.asig_monto, liq.bas_salario_diario, liq.bas_bonificacion_fin, liq.ipre_mes_tasa, liq.bvf_salario_diario, liq.bfaf_salario_diario, liq.bas_salario_int_bfa, liq.antiguedad_dias, liq.pres_sueldo_integral_mens, liq.estado_id, liq.asig_concepto2, liq.asig_concepto3, liq.asig_concepto1, liq.bfaf_meses, liq.vfr_dias_a_pagar, liq.bvf_salario_mensual, liq.pres_monto_a_pagar, liq.bas_salario_int_bv
   FROM for_pis_mae_liquidaciones liq;

ALTER TABLE for_pis_mae_reporte_planilla_liquidacion_view
  OWNER TO openerp;


