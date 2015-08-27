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
        "name" : "formacion_pis_base",
        "version" : "0.4",
        "author" : "Joan Espinoza, Francisco Vielma",
        "website" : "http://www.inces.gob.ve",
        "category" : "Formacion",
        "description": """  Módulo Base para la Gestión de Proyectos de Formación Socialista de INCES """,
        "depends" : ['base'],
        "init_xml" : ['data/modalidades.xml', 'data/motores_desarrollo.xml', 'data/areas_priorizadas.xml', 'data/sectores_economicos.xml', 'data/areas_economicas.xml', 'data/subareas_economicas.xml', 'data/for.pis.tipos_procedencias.csv', 'data/estados.xml', 'data/municipios.xml', 'data/parroquias.xml', 'data/cfs.xml'],
        "demo_xml" : [ ],
        #"update_xml" : ['security/for_pis_base.xml', 'security/ir.model.access.csv', 'formacion_pis_base_view.xml','data/modalidades.xml', 'data/motores_desarrollo.xml', 'data/cadenas_formativas.xml'],
        "update_xml" : ['security/for_pis_base.xml', 'security/ir.model.access.csv','security/ir.rule.xml', 'formacion_pis_base_view.xml', 'data/for.pis.opciones_formativas.csv', 'data/areas_priorizadas.xml', 'data/for_dependencia.xml', 'sequence_preimpreso.xml','data/for.pis.calendario.csv'],
        "installable": True
}
