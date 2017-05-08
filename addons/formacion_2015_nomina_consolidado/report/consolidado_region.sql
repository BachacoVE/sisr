SELECT e.estado as "Region", c.nombre as "CFS",
	'01/03/2014' as "Desde", '31/03/2014' as "Hasta",
	m.cedula as "Cedula", m.nombres as "Nombres", m.apellidos as "Apellidos",
	m.cuenta_id as "Cuenta", b.entidad_bancaria as "Banco", v.valor_hora as "Valor Hora",
	SUM(a.horas_lunes + a.horas_martes + a.horas_miercoles + a.horas_jueves + a.horas_viernes + a.horas_sabado + a.horas_domingo) as "Horas",
	-- r.nro_preimpreso as "PreImpreso", r.denominacion_pis as "PIS",
	SUM(a.horas_lunes + a.horas_martes + a.horas_miercoles + a.horas_jueves + a.horas_viernes + a.horas_sabado + a.horas_domingo) * v.valor_hora as "Monto Pago"

FROM for_pis_maestros as m
INNER JOIN for_pis_mae_asistencias as a
	ON m.id = a.maestro_id
INNER JOIN for_pis_mae_valor_hora as v
	ON m.nivel_id = v.id
INNER JOIN for_pis_mae_cuentas_nomina as b
	ON m.entidad_id = b.id
INNER JOIN for_pis_registro_inicial as r
	ON a.numero_id = r.id
INNER JOIN for_pis_estados as e
	ON r.estado_id = e.id
INNER JOIN for_pis_cfs as c
	ON r.cfs_id = c.id
WHERE a.semana_desde > '01/03/2014' AND a.semana_hasta < '31/03/2014'
GROUP BY e.estado, c.nombre,
	m.cedula, m.nombres, m.apellidos, m.cedula, m.nombres, m.apellidos,
	m.cuenta_id, b.entidad_bancaria, v.valor_hora