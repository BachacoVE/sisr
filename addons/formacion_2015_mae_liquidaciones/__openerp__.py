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
# Generated by the OpenERP plugin for Dia !
{
        "name" : "formacion_2015_mae_liquidaciones",
        "version" : "0.7",
        "author" : "Jessika Colina, Oly Garcia, Melissa Hernandez, Zulymar Sanchez, Joan Espinoza",
        "website" : "http://www.inces.gob.ve",
        "category" : "Formacion",
        "description": """  Módulo para el Cálculo de Liquidaciones de Maestros Pueblo  """,
        "depends" : ['base', 'formacion_2015_base', 'formacion_2015_indagacion_maestros'],
        "init_xml" : ['security/formacion_pis_mae_liquidaciones.xml',
                        'security/ir.model.access.csv',
                        'formacion_pis_mae_liquidaciones_view.xml',
                        'report/reports.xml',
                        'data/for.pis.mae_modalidades_liquidacion.csv',
                        'data/for.pis.mae_motivos_egreso.csv',
                        'data/for.pis.mae_tasas_bcv_prestaciones.csv',
                        'data/for.pis.mae_tipos_asignaciones.csv',
                        'data/for.pis.mae_tipos_deducciones.csv',
                        'data/sisr.pla.dependencias_administrativas.csv'],
        "demo_xml" : [ ],
        "update_xml" : [],
        "installable": True
}
