--﻿/*QUERY REALIZADO PARA LA GENERACIÓN CONTRATOS*/



/*DROP TABLE IF EXISTS tmp_fac_3004;

CREATE TEMP TABLE tmp_fac_3004 AS (select distinct facilitador_id 
                                 from for_pis_registro_proyeccion
                                 where fecha_cierre <= '2015-04-30');
                                 
*/                                   
SELECT  mae.nombres, mae.apellidos, mae.cedula, nac.nacionalidad, civ.estado_civil,
        mae.direccion_habitacion, mun.municipio, es.estado,
        --to_char (min(pry.fecha_inicio), 'DD/MM/YYYY') as primera_fecha_inicio,
        --to_char (max(pry.fecha_cierre), 'DD/MM/YYYY') as ultima_fecha_cierre,
        sum(pry.lapso_ejecucion) as total_lapso, 
        (min(pry.fecha_inicio)) as primera_fecha_inicio,
        (max(pry.fecha_cierre)) as ultima_fecha_cierre, 
        cfs.nombre, 
        (sum(pry.lapso_ejecucion) * vh.valor_hora) as total_pagar, 
        count(*) as cantidad_proyecto, 
        vh.valor_hora, lab.condicion_laboral
    
FROM  for_pis_registro_inicial as pry
--INNER JOIN  tmp_fac_3004 tmp ON pry.facilitador_id = tmp.facilitador_id
INNER JOIN for_pis_estados es
  ON mae.estado_id = es.id
INNER JOIN  for_pis_maestros mae
  ON pry.facilitador_id = mae.id
INNER JOIN  for_pis_municipios mun
  ON mae.municipio_id = mun.id
LEFT OUTER JOIN  for_pis_mae_valor_hora vh
  ON mae.nivel_id = vh.id
INNER JOIN  for_pis_cfs_extended cfs
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
  AND mae.nivel_id is not null
  AND nac.nacionalidad is not null
  AND civ.estado_civil is not null
  AND mae.direccion_habitacion is not null
  AND mae.municipio is not null
  AND mae.estado is not null
  AND cfs.nombre is not null
  AND vh.valor_hora is not null 
  AND lab.condicion_laboral is not null
--GROUP BY 1,2,3,10,11
GROUP BY 1,2,3,4,5,6,7,8,12,15,16
ORDER BY es.estado, mae.cedula
