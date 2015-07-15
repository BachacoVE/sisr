-- Trigger: generar_liquidaciones on for_pis_mae_liquidaciones

DROP TRIGGER IF EXISTS generar_liquidaciones ON for_pis_mae_liquidaciones;

CREATE TRIGGER generar_liquidaciones
  AFTER INSERT
  ON for_pis_mae_liquidaciones
  FOR EACH ROW
  EXECUTE PROCEDURE generar_liquidacion_maestro();
