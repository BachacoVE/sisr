import time
import datetime
from numero_a_texto import Numero_a_Texto
from convertir import convertir#agregar para RML
from report import report_sxw

class reporte_inces(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(reporte_inces, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'obt_texto':self.obt_texto,
            'lang':context['lang'],
            'vcedula':self.vcedula,
            'convertir':self.convertir,
            'formatear_fecha':self.formatear_fecha,
            'sumar_horas':self.sumar_horas,
            'min_fecha':self.min_fecha,
            'max_fecha':self.max_fecha,
            'determinar_valor_hora':self.determinar_valor_hora,
            'marcar_contrato_generado':self.marcar_contrato_generado,
            'agregar_a_clase_contratos':self.agregar_a_clase_contratos
        })

    def obt_texto(self,cantidad):
        res=Numero_a_Texto(cantidad).escribir
        return res

    def vcedula(self,nacionalidad):
        if (nacionalidad == 'Venezolana') or (nacionalidad == 'Venezolano'):
            return 'V'
        else:
            return 'E'

    def convertir(self,cedula):
        return convertir(cedula)

    def formatear_fecha(self,fecha):
        return fecha[8:10]+"/"+fecha[5:7]+"/"+fecha[0:4]

    def sumar_horas(self,datos):
        total=0
        for k in datos:
            total=total+k
        return total

    def min_fecha(self,fecha):
        fec_min = min(fecha)
        return fec_min[8:10]+"/"+fec_min[5:7]+"/"+fec_min[0:4]

    def max_fecha(self,fecha):
        fec_max = max(fecha)
        return fec_max[8:10]+"/"+fec_max[5:7]+"/"+fec_max[0:4]

    def determinar_valor_hora(self, fec_minima, identificador):
        if(fec_minima > '2015-05-01'):
            self.cr.execute("SELECT valor_hora \
                        FROM for_pis_maestros \
                        INNER JOIN for_pis_mae_valor_hora \
                        ON for_pis_maestros.nivel_id=for_pis_mae_valor_hora.id \
                        WHERE for_pis_maestros.id=%d" % (identificador))
            resultado1=self.cr.fetchone()
            return resultado1[0]
        else:
            self.cr.execute("SELECT valor_hora \
                        FROM for_pis_maestros \
                        INNER JOIN for_pis_mae_valor_hora \
                        ON for_pis_maestros.nivel_viejo_id=for_pis_mae_valor_hora.id \
                        WHERE for_pis_maestros.id=%d" % (identificador))
            resultado2=self.cr.fetchone()
            if(resultado2<0):
                self.cr.execute("SELECT valor_hora \
                        FROM for_pis_maestros \
                        INNER JOIN for_pis_mae_valor_hora \
                        ON for_pis_maestros.nivel_id=for_pis_mae_valor_hora.id \
                        WHERE for_pis_maestros.id=%d" % (identificador))
                resultado1=self.cr.fetchone()
                return resultado1[0]
            else:
                return resultado2[0]

    def marcar_contrato_generado(self, cedula):
        self.cr.execute("UPDATE for_pis_maestros SET apr_generar=%s WHERE cedula=%s",(True,cedula))

    def agregar_a_clase_contratos(self, cedula, nombres, apellidos, nacionalidad, estado_civil, domicilio, municipio, estado, fecha_inicio, fecha_cierre, cfs, total_horas, valor_hora, condicion_laboral):
        fecha_generado=time.strftime("%d-%m-%Y")
        create_uid=1
        create_date=datetime.datetime.now()
        write_date=0
        write_uid=0
        total_pagar=total_horas*valor_hora
        active=True
        
        self.cr.execute("SELECT count(*) from for_pis_mae_participacion_pis \
                        INNER JOIN for_pis_maestros \
                        ON for_pis_maestros.id=for_pis_mae_participacion_pis.maestro_id \
                        WHERE for_pis_maestros.cedula='%s'" % cedula)
        total_formaciones=self.cr.fetchone()

        self.cr.execute("SELECT for_dependencias.dependencia \
                        FROM dependencia_formador_rel \
                        INNER JOIN for_pis_maestros  \
                        ON for_pis_maestros.id=dependencia_formador_rel.formador_id  \
                        INNER JOIN for_dependencias \
                        ON for_dependencias.id=dependencia_formador_rel.dependencia_id \
                        WHERE for_pis_maestros.cedula='%s'" % (cedula))
        dependencia=self.cr.fetchone()

        self.cr.execute("INSERT INTO for_pis_contratos (create_uid, create_date, cedula, nombres, apellidos, nacionalidad, estado_civil, domicilio, municipio, estado, fecha_inicio, fecha_cierre, cfs, total_horas, valor_hora, fecha_generado, total_pagar, condicion_laboral, active, total_formaciones, dependencia) \
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (create_uid,create_date,cedula, nombres, apellidos, nacionalidad, estado_civil, domicilio, municipio, estado, fecha_inicio, fecha_cierre, cfs, total_horas, valor_hora, fecha_generado, total_pagar, condicion_laboral, active, total_formaciones, dependencia))

report_sxw.report_sxw('report.contrato.por.hora', 'for.pis.maestros', 'addons/formacion_2015_indagacion_maestros/report/por_hora.rml', parser=reporte_inces, header="False")
report_sxw.report_sxw('report.participantes.formadores', 'for.pis.maestros', 'addons/formacion_2015_indagacion_maestros/report/participantes_formadores.rml', parser=reporte_inces, header="False")