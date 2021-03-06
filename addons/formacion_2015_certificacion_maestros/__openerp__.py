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
        "name" : "formacion_2015_certificacion_maestros",
        "version" : "0.2",
        "author" : "Joan Espinoza",
        "website" : "http://www.inces.gob.ve",
        "category" : "Formacion",
        "description": """  Módulo de Funcionalidades para apoyar la Certificación Pedagógica de Maestros en los Proyectos de Formacion Socialista de INCES  """,
        "depends" : ['base','formacion_2015_base','formacion_2015_indagacion_maestros'],
        "init_xml" : ['data/for.pis.acsea_certificados_estatus.csv',
                        'formacion_pis_certificacion_maestros_view.xml',
                        'security/ir.model.access.csv'],
        "demo_xml" : [ ],
        "update_xml" : [ ],
        "installable": True
}
