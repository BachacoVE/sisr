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
        "name" : "formacion_2015_indagacion_maestros",
        "version" : "0.3",
        "author" : "Joan Espinoza, Francisco Vielma, Jessika Colina",
        "website" : "http://www.inces.gob.ve",
        "category" : "Formacion",
        "description": """  Funcionalidades para Caracterización de Maestros, del Módulo de Gestión de los Procesos de Indagación de Contexto de los PIS INCES  """,
        "depends" : ['base','formacion_2015_base','formacion_2015_indagacion', 'formacion_2015_nomina_maestros'],
        "init_xml" : ['data/for.pis.mae_tipos_cuenta.csv', 'security/ir.model.access.csv'],
        "demo_xml" : [],
        "update_xml" : ['security/ir.rule.xml',
                        'formacion_pis_indagacion_maestros_view.xml',
                        'report/inces_report.xml'],
        "installable": True
}
