﻿SELECT  dep.dependencia, mae.nombres, mae.apellidos, mae.cedula, nac.nacionalidad, civ.estado_civil,
        mae.direccion_habitacion, mun.municipio, es.estado,
        --to_char (min(pry.fecha_inicio), 'DD/MM/YYYY') as primera_fecha_inicio,
        --to_char (max(pry.fecha_cierre), 'DD/MM/YYYY') as ultima_fecha_cierre,
        sum(pry.lapso_ejecucion) as total_lapso,
        (min(pry.fecha_inicio)) as primera_fecha_inicio,
        (max(pry.fecha_cierre)) as ultima_fecha_cierre,
        --cfs.nombre,
        contratos_mae_primer_cfs(mae.id) as cfs,
        (sum(pry.lapso_ejecucion) * vh.valor_hora) as total_pagar,
        count(*) as cantidad_proyecto,
        --vh.valor_hora

        ,lab.condicion_laboral

FROM  for_pis_registro_inicial as pry
--INNER JOIN  tmp_fac_3004 tmp ON pry.facilitador_id = tmp.facilitador_id
-- INNER JOIN  for_pis_maestros mae (QUITAR)
--  ON pry.facilitador_id = mae.id (QUITAR)

INNER JOIN for_pis_mae_participacion_pis mae_part
  ON pry.id = mae_part.numero_id

INNER JOIN for_pis_maestros as mae
  ON mae_part.maestro_id = mae.id

INNER JOIN dependencia_formador_rel dep_rel
  ON mae.id = dep_rel.formador_id

INNER JOIN for_dependencias dep
  ON dep_rel.dependencia_id = dep.id

INNER JOIN for_pis_estados es
  ON mae.estado_id = es.id

INNER JOIN  for_pis_municipios mun
  ON mae.municipio_id = mun.id
LEFT OUTER JOIN  for_pis_mae_valor_hora vh
  ON mae.nivel_id = vh.id
INNER JOIN  for_pis_cfs cfs
  ON pry.cfs_id = cfs.id
INNER JOIN  for_pis_nacionalidades nac
  ON mae.nacionalidad = nac.id
INNER JOIN  for_pis_estados_civiles civ
  ON mae.estado_civil_id = civ.id
LEFT OUTER JOIN for_pis_condiciones_laborales lab
  ON mae.condicion_laboral = lab.id
--where pry.fecha_cierre <= '2015-04-30'
  --and fecha_cierre is null-- '2015-04-30'
WHERE mae.condicion_laboral in (3)
  AND pry.fecha_inicio is not null
  AND pry.fecha_cierre is not null
  AND pry.lapso_ejecucion is not null
  --AND mae.nivel_id is not null
  AND nac.nacionalidad is not null
  AND civ.estado_civil is not null
  AND mae.direccion_habitacion is not null
  AND mae.municipio_id is not null
  AND mae.estado_id is not null
  AND cfs.nombre is not null
  AND vh.valor_hora is not null
  AND mae.condicion_laboral is not null
  AND mae.apr_generar is false
  --AND pry.fecha_inicio = primera_fecha_inicio
 -- AND mae.cedula = '17219521'
--GROUP BY 1,2,3,10,11
GROUP BY 1,2,3,4,5,6,7,8,9,13,16,17
ORDER BY dep.dependencia, mae.cedula
