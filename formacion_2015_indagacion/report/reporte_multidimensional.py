from report import report_sxw
from osv import osv, fields
import time

class reporte_multidimensional(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(reporte_multidimensional, self).__init__(cr, uid, name, context=context)
        
        self.localcontext.update({
            'time': time,
            'dependencias': self.dependencias,
            'cantidad_sujetos_programados': self.cantidad_sujetos_programados,
            'cantidad_inscritos': self.cantidad_inscritos,
            'cantidad_egresados':self.cantidad_egresados,
            'cantidad_retirados':self.cantidad_retirados,
            'cantidad_procesos':self.cantidad_procesos,
            'cantidad_nulos':self.cantidad_nulos,
            'cantidad_maestros': self.cantidad_maestros,
            'totales': self.totales
        })

    def dependencias(self):
        self.cr.execute("SELECT DISTINCT(dependencia_formacion), for_dependencias.dependencia \
                         FROM for_pis_participacion_pis \
                         INNER JOIN for_dependencias \
                         ON for_pis_participacion_pis.dependencia_formacion = for_dependencias.id \
                         WHERE dependencia_formacion>0")
        data = self.cr.dictfetchall()
        return data

    def cantidad_sujetos_programados(self,dependencia_formacion):
        self.cr.execute("SELECT sum(cantidad_sujetos_programados) \
                         FROM for_pis_registro_inicial \
                         WHERE dependencia_id=%s" % (dependencia_formacion))
        cantidad = self.cr.fetchone()
        return str(cantidad[0])
    
    def cantidad_inscritos(self,dependencia_formacion):
        self.cr.execute("SELECT count(*) \
                         FROM for_pis_participacion_pis \
                         WHERE dependencia_formacion=%s" % (dependencia_formacion))
        cantidad = self.cr.fetchone()
        return str(cantidad[0])

    def cantidad_egresados(self,dependencia_formacion):
        self.cr.execute("SELECT count(*) \
                         FROM for_pis_participacion_pis \
                         WHERE estatus='egresado' AND dependencia_formacion=%s" % (dependencia_formacion))
        cantidad = self.cr.fetchone()
        return str(cantidad[0])

    def cantidad_retirados(self,dependencia_formacion):
        self.cr.execute("SELECT count(*) \
                         FROM for_pis_participacion_pis \
                         WHERE estatus='retirado' AND dependencia_formacion=%s" % (dependencia_formacion))
        cantidad = self.cr.fetchone()
        return str(cantidad[0])

    def cantidad_procesos(self,dependencia_formacion):
        self.cr.execute("SELECT count(*) \
                         FROM for_pis_participacion_pis \
                         WHERE estatus='proceso' AND dependencia_formacion=%s" % (dependencia_formacion))
        cantidad = self.cr.fetchone()
        return str(cantidad[0])

    def cantidad_nulos(self,dependencia_formacion):
        self.cr.execute("SELECT count(*) \
                         FROM for_pis_participacion_pis \
                         WHERE estatus is null AND dependencia_formacion=%s" % (dependencia_formacion))
        cantidad = self.cr.fetchone()
        return str(cantidad[0])

    def cantidad_maestros(self,dependencia_formacion):
        self.cr.execute("SELECT count(*) \
                         FROM dependencia_formador_rel \
                         WHERE dependencia_id=%s" % (dependencia_formacion))
        cantidad = self.cr.fetchone()
        return str(cantidad[0])

    def totales(self, opcion):
        if opcion=='participantes_rogramados':
            self.cr.execute("SELECT sum(cantidad_sujetos_programados) \
                             FROM for_pis_registro_inicial ")
            cantidad = self.cr.fetchone()
            return str(cantidad[0])

        if opcion=='total_inscritos':
            self.cr.execute("SELECT count(*) \
                         FROM for_pis_participacion_pis")
            cantidad = self.cr.fetchone()
            return str(cantidad[0])

        if opcion=='egresados':
            self.cr.execute("SELECT count(*) \
                             FROM for_pis_participacion_pis \
                             WHERE estatus='egresado'")
            cantidad = self.cr.fetchone()
            return str(cantidad[0])

        if opcion=='retirados':
            self.cr.execute("SELECT count(*) \
                             FROM for_pis_participacion_pis \
                             WHERE estatus='retirado'")
            cantidad = self.cr.fetchone()
            return str(cantidad[0])

        if opcion=='procesos':
            self.cr.execute("SELECT count(*) \
                             FROM for_pis_participacion_pis \
                             WHERE estatus='proceso'")
            cantidad = self.cr.fetchone()
            return str(cantidad[0])

        if opcion=='nulos':
            self.cr.execute("SELECT count(*) \
                             FROM for_pis_participacion_pis \
                             WHERE estatus is null")
            cantidad = self.cr.fetchone()
            return str(cantidad[0])

        if opcion=='cantidad_maestros':
            self.cr.execute("SELECT count(*) \
                             FROM dependencia_formador_rel ")
            cantidad = self.cr.fetchone()
            return str(cantidad[0])

report_sxw.report_sxw('report.reporte_multidimensional', 'for.pis.participacion_pis', 'addons/formacion_2015_indagacion/report/reporte_multidimensional.rml', parser=reporte_multidimensional, header=False)