/* -- INICIO BLOQUE 1: reportes de ejecucion con inciencia de repeticion

select cal.nro_semana, mae.cedula as cedula_maestro, opc.denominacion, forma.nro_preimpreso as preimpreso,
count(*) as incidencias_repetidos
into temp temp1
from for_pis_mae_asistencias as asis

left outer join for_pis_registro_inicial as forma
on asis.numero_id=forma.id
left outer join for_pis_opciones_formativas as opc
on forma.denominacion_pis_id=opc.id
left outer join for_pis_maestros as mae
on asis.maestro_id=mae.id
left outer join for_pis_calendario as cal
on asis.calendario_id= cal.id
group by 1,2,3,4
having count(*)>1
-- FIN BLOQUE 1*/


/*-- INICIO BLOQUE 2: reporte de ejecucion total
select asis.id, cal.nro_semana, mae.cedula as cedula_maestro, forma.nro_preimpreso as preimpreso, opc.denominacion, dep.dependencia,
asis.horas_lunes,asis.horas_martes,asis.horas_miercoles,asis.horas_jueves,asis.horas_viernes,asis.horas_sabado, asis.state


from for_pis_mae_asistencias as asis

left outer join for_pis_registro_inicial as forma
on asis.numero_id=forma.id
left outer join for_pis_opciones_formativas as opc
on forma.denominacion_pis_id=opc.id
left outer join for_pis_maestros as mae
on asis.maestro_id=mae.id
left outer join for_pis_calendario as cal
on asis.calendario_id= cal.id
inner join temp1
on mae.cedula=temp1.cedula_maestro
inner join for_dependencias as dep
on asis.dependencia_id=dep.id
where cal.nro_semana=temp1.nro_semana and forma.nro_preimpreso=temp1.preimpreso
order by 2,3,4,5
-- FIN BLOQUE 2 */