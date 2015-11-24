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

class parser_planilla_liquidacion(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(parser_planilla_liquidacion, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
        })

#id                    identificador unico de reporte
#name                  nombre del reporte (requerido)
#string                titulo del reporte (requerido)
#model                 objeto modelo sobre el cual esta definido el reporte (requerido)
#rml, sxw, xml, xsl    ruta a la fuente del reporte (iniciando desde addons)
#auto                  establecer a False para usar un parser personalizado, heredando report_sxw.rml_parse
#                      y declarando el reporte como se indica:
#                      report_sxw.report_sxw('report_name', 'object_model', 'rml_path', parser=parser, header=False)
#header                establecer a False para suprimir la cabecera del reporte. Por defecto: True)
#groups                lista (separada por comas) de los grupos que pueden ver este reporte
#menu                  establecer a True para vincular el reporte a un icono (Por defecto: True)
#keywords              especifica la palabra clave del reporte (Por defecto: client_print_multi)

report_sxw.report_sxw('report.planilla.report', 'for.pis.mae_liquidaciones', 'addons/formacion_2015_mae_liquidaciones/report/planilla_liquidacion.rml', parser=parser_planilla_liquidacion, header=False)
