import time
from numero_a_texto import Numero_a_Texto #agregar para RML
from convertir import convertir#agregar para RML
from report import report_sxw

class reporte_inces(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(reporte_inces, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'obt_texto':self.obt_texto,#agregar para RML
            'lang':context['lang'],    #agregar para RML
            'vcedula':self.vcedula,#agregar para RML
	    	'convertir':self.convertir#agregar para RML
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

report_sxw.report_sxw('report.contrato.por.hora', 'for.pis.contratos', 'addons/formacion_2015_nomina_maestros/report/por_hora.rml', parser=reporte_inces, header="False")