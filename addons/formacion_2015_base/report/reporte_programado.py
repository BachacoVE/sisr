# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from report import report_sxw
import time

class reporte_programado(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(reporte_programado, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'calculo_egresados':self.calculo_egresados,
            'calculo_retirado':self.calculo_retirado,
            'calculo_en_proceso':self.calculo_en_proceso,
            'calculo_nulos':self.calculo_nulos,
            'calculo_maestros':self.calculo_maestros
        })

    def calculo_egresados(self, id_reg_inicial):
        self.cr.execute("SELECT count(numero_id) \
                         FROM for_pis_participacion_pis \
                         WHERE estatus = 'egresado' and numero_id='%d'" % (id_reg_inicial))
        egresados=self.cr.fetchone()
        return egresados[0]
    
    def calculo_retirado(self, id_reg_inicial_retirado):
        self.cr.execute("SELECT count(numero_id) \
                         FROM for_pis_participacion_pis \
                         WHERE estatus = 'retirado' and numero_id='%d'" % (id_reg_inicial_retirado))
        retirado=self.cr.fetchone()
        return retirado[0]

    def calculo_en_proceso(self, id_reg_inicial_proceso):
        self.cr.execute("SELECT count(numero_id) \
                         FROM for_pis_participacion_pis \
                         WHERE estatus = 'proceso' and numero_id='%d'" % (id_reg_inicial_proceso))
        proceso=self.cr.fetchone()
        return proceso[0]

    def calculo_nulos(self, id_reg_inicial_nulos):
        self.cr.execute("SELECT count(numero_id) \
                         FROM for_pis_participacion_pis \
                         WHERE estatus is null and numero_id='%d'" % (id_reg_inicial_nulos))
        nulos=self.cr.fetchone()
        return nulos[0]

    def calculo_maestros(self, id_reg_inicial_nulos):
        self.cr.execute("SELECT count(maestro_id) \
                         FROM for_pis_mae_participacion_pis \
                         WHERE numero_id='%d'" % (id_reg_inicial_nulos))
        maestros=self.cr.fetchone()
        return maestros[0]

report_sxw.report_sxw('report.prog_est.report', 'for.pis.registro_inicial', 'addons/formacion_2015_base/report/reporte_programado.rml', parser=reporte_programado, header=False)
report_sxw.report_sxw('report.estadisticas.participantes', 'for.pis.registro_inicial', 'addons/formacion_2015_base/report/reporte_estadistico.rml', parser=reporte_programado, header=False)