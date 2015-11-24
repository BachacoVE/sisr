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
		WHERE	a.maestro_id = maestro AND
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

