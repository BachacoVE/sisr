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

    def agregar_a_clase_contratos(self, cedula):
        cr.execute("""INSERT INTO for_pis_contratos (cedula) VALUES (%s)""",(cedula))

report_sxw.report_sxw('report.contrato.por.hora', 'for.pis.maestros', 'addons/formacion_2015_indagacion_maestros/report/por_hora.rml', parser=reporte_inces, header="False")
report_sxw.report_sxw('report.participantes.formadores', 'for.pis.maestros', 'addons/formacion_2015_indagacion_maestros/report/participantes_formadores.rml', parser=reporte_inces, header="False")