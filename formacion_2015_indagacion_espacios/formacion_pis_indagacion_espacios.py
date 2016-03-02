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
from osv import fields,osv

class for_pis_espacios(osv.osv):
    """Registro Maestro de Espacios Integrales Socialistas"""
    _name = 'for.pis.espacios'
    _rec_name = 'nombre_espacio'
    #_rec_name = 'tipo_espacio_id'
    #_rec_name = 'estado_id'
    #_rec_name = 'municipio_id'
    #_rec_name = 'parroquia_id'
    #_rec_name = 'turno_id'
    #_rec_name = 'direccion'
    #_rec_name = 'acceso_terrestre'
    #_rec_name = 'acceso_fluvial'
    #_rec_name = 'acceso_areo'
    #_rec_name = 'contextos_ids'
    #_rec_name = 'caracteristicas'
    #_rec_name = 'personas_maximo'
    #_rec_name = 'dotacion_ids'
    #_rec_name = 'innovacion_ids'
    #_rec_name = 'seguridad_ids'
    #_rec_name = 'ambiental_ids'
    #_rec_name = 'factores_internos'
    #_rec_name = 'factores_externos'
    #_rec_name = 'sugerencias'
    #_rec_name = 'valoracion_adecuado'
    #_rec_name = 'valoracion_inadecuado'
    #_rec_name = 'materiales_disponibles'
    #_rec_name = 'materiales_necesarios'
    #_rec_name = 'observaciones'
    _columns = {
        'codigo': fields.char('Codigo', size=9),
        'nombre_espacio': fields.char('Nombre del Espacio', size=240, required=True, help='Nombre (Único) que Identifique el Espacio de Formación y Autoformación'),
        'tipo_espacio_id': fields.many2one('for.pis.tipos_espacios', 'Ambito Formativo', required=True, help='Tipo de Espacio de Formación y Autoformación'),
        'estado_id': fields.many2one('for.pis.estados', 'Estado', required=True, help='Estado del país en el que se ubica el Espacio de Formación y Autoformación'),
        'municipio_id': fields.many2one('for.pis.municipios', 'Municipio', required=True, help='Municipio del país en el que se ubica el Espacio de Formación y Autoformación'),
        'parroquia_id': fields.many2one('for.pis.parroquias', 'Parroquia', required=True, help='Parroquia del país en el que se ubica el Espacio de Formación y Autoformación'),
        'turno_id': fields.many2one('for.pis.turnos', 'Turno', required=True, help='Turno en el cual opera el Espacio de Formación y Autoformación'),
        'direccion': fields.text('Dirección', size=300, required=True, help='Detalle de la Dirección del Espacio de Formación y Autoformación'),
        'acceso_terrestre': fields.text('Terrestre', size=1200, required=False, help='Descripción del Acceso Terrestre al Espacio de Formación y Autoformación'),
        'acceso_fluvial': fields.text('Fluvial', size=1200, required=False, help='Descripción del Acceso Fluvial al Espacio de Formación y Autoformación'),
        'acceso_areo': fields.text('Aéreo', size=1200, required=False, help='Descripción del Acceso Aéreo al Espacio de Formación y Autoformación'),
        'contextos_ids': fields.one2many('for.pis.esp_contextos', 'espacio_id', 'Contextos', help='Contextos del Espacio de Formación y Autoformación'),
        'caracteristicas': fields.text('Características', size=1200, required=True, help='Características del Espacio de Formación y Autoformación'),
        'personas_maximo': fields.integer('Personas Máximo', size=9, required=True, help='Capacidad Máxima de Personas del Espacio de Formación y Autoformación'),
        'dotacion_ids': fields.one2many('for.pis.esp_dotacion', 'espacio_id', 'Dotación del Espacio', help='Dotación (Materiales, Herramientas, Equipamiento) del Espacio de Formación y Autoformación'),
        'innovacion_ids': fields.one2many('for.pis.esp_innovacion', 'espacio_id', 'Niveles de Innovación Tecnológica', help='Niveles de Innovación Tecnológica del Espacio de Formación y Autoformación'),
        'seguridad_ids': fields.one2many('for.pis.esp_seguridad_laboral', 'espacio_id', 'Seguridad Laboral', help='Niveles de Seguridad Laboral del Espacio de Formación y Autoformación'),
        'ambiental_ids': fields.one2many('for.pis.esp_equilibrio_ambiental', 'espacio_id', 'Equilibrio Ambiental', help='Niveles de Equilibrio Ambiental del Espacio de Formación y Autoformación'),
        'pis_ids': fields.one2many('for.pis.esp_pis', 'espacio_id', 'Formación', help='Formaciones que usan el, o se ejecutan en el Espacio de Formación y Autoformación'),
        'factores_internos': fields.text('Factores Internos', size=1200, required=False, help='Facores Internos que interfieren en la Formación'),
        'factores_externos': fields.text('Factores Externos', size=1200, required=False, help='Facores Externos que interfieren en la Formación'),
        'sugerencias': fields.text('Sugerencias', size=1200, required=False, help='Sugerencias y aportes para fortalecer el Espacio de Formación y Autoformación'),
        'valoracion_adecuado': fields.text('Espacio Adecuado', size=1200, required=False, help='Valoración del Espacio de Formación y Autoformación (Adecuado)'),
        'valoracion_inadecuado': fields.text('Espacio Inadecuado', size=1200, required=False, help='Valoración del Espacio de Formación y Autoformación (Adecuado)'),
        'materiales_disponibles': fields.text('Disponibles', size=1200, required=False, help='Materiales, herramientas, equipos, insumos disponibles (en el espacio) para la Formación'),
        'materiales_necesarios': fields.text('Necesarios', size=1200, required=False, help='Materiales, herramientas, equipos, insumos necesarios para la Formación'),
        'observaciones': fields.text('Observaciones', size=1200, required=False, help='Observaciones'),
        'cfs_id': fields.many2one('for.pis.cfs','CFS responsable', required=False, help='Centro de Formación Socialista responsable del espacio'),

    }
#Aqui funcion para limpiar campos Estado, Municipio y parroquia
    def on_change_limpiar_campo(self, cr, uid, ids, *args):
        v = {'value':{}}
        for campo in args:
            v['value'][campo] = ''
            return v
#Aqui finaliza la funcion

for_pis_espacios()

###########################################################################################################################################################################3
############################################################################################################################################################################
################esta clase hereda de formacion_pis_base#####################################################################################################################
class for_pis_registro_inicial_extended(osv.osv):
    """Registro Inicial de la Formación"""
    _name = 'for.pis.registro_inicial'
    #_rec_name = 'denominacion_pis'
    _inherit= 'for.pis.registro_inicial'
    _columns = {
    	'turno_id': fields.many2one('for.pis.turnos', 'Turno', required=False, help='Turno en el cual opera el Espacio de Formación y Autoformación'),
        'espacios_id': fields.many2one('for.pis.espacios', 'Ambiente formativo')
    }
for_pis_registro_inicial_extended()
##########################################################################################################################################################################
##########################################################################################################################################################################


class for_pis_tipos_espacios(osv.osv):
    """Tabla Referencial de Tipos de Espacios Socialistas Integrales"""
    _name = 'for.pis.tipos_espacios'
    #_rec_name = 'codigo'
    _rec_name = 'tipo_espacio'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación del Tipo de Espacio de Formación y Autoformación'),
        'tipo_espacio': fields.char('Tipo de Espacio', size=60, required=True, help='Nombre del Tipo de Espacio de Formación y Autoformación'),
        'active': fields.boolean('activo')
    }
for_pis_tipos_espacios()

class for_pis_turnos(osv.osv):
    """Tabla Referencial de Turnos"""
    _name = 'for.pis.turnos'
    #_rec_name = 'codigo'
    _rec_name = 'turno'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificacion del Turno'),
        'turno': fields.char('Turno', size=60, required=True, help='Nombre del Turno'),
    }
for_pis_turnos()

class for_pis_niveles_innovacion_tecnologica(osv.osv):
    """Tabla Referencial de Niveles de Innovación Tecnológica"""
    _name = 'for.pis.niveles_innovacion_tecnologica'
    #_rec_name = 'codigo'
    _rec_name = 'nivel_innovacion'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación del Nivel de Innovación Tecnológica'),
        'nivel_innovacion': fields.char('Nivel de Innovación Tecnológica', size=120, required=True, help='Nombre del Nivel de Innovación Tecnológica'),
    }
for_pis_niveles_innovacion_tecnologica()

class for_pis_esp_contextos(osv.osv):
    """Registro Maestro de Contextos de los Espacios Socialistas Integrales"""
    _name = 'for.pis.esp_contextos'
    #_rec_name = 'espacio_id'
    _rec_name = 'tipo_contexto_id'
    #_rec_name = 'observaciones'
    _columns = {
        'espacio_id': fields.many2one('for.pis.espacios', 'Espacio', required=True, help='Espacio de Formación y Autoformación que presenta los contextos referidos'),
        'tipo_contexto_id': fields.many2one('for.pis.tipos_contextos', 'Tipo de Contexto', required=True, help='Tipo de Contexto que presenta el Espacio de Formación y Autoformación'),
        'observaciones': fields.char('Observaciones', size=240, required=False, help='Observaciones y/o comentarios adicionales'),
    }
for_pis_esp_contextos()

class for_pis_esp_innovacion(osv.osv):
    """Registro Maestro de Niveles de Innovación Tecnológica de los Espacios Socialistas Integrales"""
    _name = 'for.pis.esp_innovacion'
    #_rec_name = 'espacio_id'
    _rec_name = 'innovacion_tecnologica_id'
    #_rec_name = 'observaciones'
    _columns = {
        'espacio_id': fields.many2one('for.pis.espacios', 'Espacio', required=True, help='Espacios Socialistas Integrales que presenta los Niveles de Innovación Tecnológica referidos'),
        'innovacion_tecnologica_id': fields.many2one('for.pis.niveles_innovacion_tecnologica', 'Innovación Tecnología', required=True, help='Nivel de Innovación Tecnológica que presenta el Espacio de Formación y Autoformación'),
        'observaciones': fields.char('Observaciones', size=240, required=False, help='Observaciones y/o Comentarios adicionales'),
    }
for_pis_esp_innovacion()

class for_pis_esp_pis(osv.osv):
    """Registro Maestro de Formaciones ejecutadas en los Espacios Socialistas Integrales"""
    _name = 'for.pis.esp_pis'
    #_rec_name = 'espacio_id'
    _rec_name = 'pis_id'
    #_rec_name = 'lunes_uso'
    #_rec_name = 'lunes_horas'
    #_rec_name = 'martes_uso'
    #_rec_name = 'martes_horas'
    #_rec_name = 'miercoles_uso'
    #_rec_name = 'miercoles_horas'
    #_rec_name = 'jueves_uso'
    #_rec_name = 'jueves_horas'
    #_rec_name = 'viernes_uso'
    #_rec_name = 'viernes_horas'
    #_rec_name = 'sabado_uso'
    #_rec_name = 'sabado_horas'
    #_rec_name = 'domingo_uso'
    #_rec_name = 'domingo_horas'
    _columns = {
        'espacio_id': fields.many2one('for.pis.espacios', 'Espacio', required=True, help='Espacio de Formación y Autoformación donde se dan las Formación referidas'),
        'pis_id': fields.many2one('for.pis.registro_inicial', 'Formación', required=True, help='Formación que se desarrolla en, o hace uso de; el espacio referido'),
        'lunes_uso': fields.boolean('Uso Lunes', required=False, help='¿El espacio es usado para la Formación referida, los días lunes?'),
        'lunes_horas': fields.integer('Horas Lunes', required=False, help='Tiempo total de uso del Espacio de Formación y Autoformación los días Lunes, para la Formación referida'),
        'martes_uso': fields.boolean('Uso Martes', required=False, help='¿El espacio es usado para la Formación referida, los días martes?'),
        'martes_horas': fields.integer('Horas Martes', required=False, help='Tiempo total de uso del Espacio de Formación y Autoformación los días Martes, para la Formación referida'),
        'miercoles_uso': fields.boolean('Uso Miércoles', required=False, help='¿El espacio es usado para la Formación referida, los días miércoles?'),
        'miercoles_horas': fields.integer('Horas Miércoles', required=False, help='Tiempo total de uso del Espacio de Formación y Autoformación los días Miécoles, para la Formación referida'),
        'jueves_uso': fields.boolean('Uso Jueves', required=False, help='¿El espacio es usado para la Formación referida, los días jueves?'),
        'jueves_horas': fields.integer('Horas Jueves', required=False, help='Tiempo total de uso del Espacio de Formación y Autoformación los días Jueves, para la Formación referida'),
        'viernes_uso': fields.boolean('Uso Viernes', required=False, help='¿El espacio es usado para la Formación referida, los días viernes?'),
        'viernes_horas': fields.integer('Horas Viernes', required=False, help='Tiempo total de uso del Espacio de Formación y Autoformación los días Viernes, para la Formación referida'),
        'sabado_uso': fields.boolean('Uso Sabado', required=False, help='¿El espacio es usado para la Formación referida, los días sabado?'),
        'sabado_horas': fields.integer('Horas Sabado', required=False, help='Tiempo total de uso del Espacio de Formación y Autoformación los días Sábado, para la Formación referida'),
        'domingo_uso': fields.boolean('Uso Domingo', required=False, help='¿El espacio es usado para la Formación referida, los días domingo?'),
        'domingo_horas': fields.integer('Horas Domingo', required=False, help='Tiempo total de uso del Espacio de Formación y Autoformación los días Domingo, para la Formación referida'),
    }
for_pis_esp_pis()

class for_pis_esp_dotacion(osv.osv):
    """Registro Maestro de Dotación de los Espacios Socialistas Integrales"""
    _name = 'for.pis.esp_dotacion'
    #_rec_name = 'espacio_id'
    _rec_name = 'recurso'
    #_rec_name = 'capacidad_instalada'
    #_rec_name = 'capacidad_operativa'
    #_rec_name = 'observaciones'
    _columns = {
        'espacio_id': fields.many2one('for.pis.espacios','Espacio', required=True, help='Espacio de Formación y Autoformación que presenta la Dotación referida'),
        'recurso': fields.char('Recurso', size=120, required=True, help='Recurso con el que está dotado el Espacio de Formación y Autoformación (Equipo, Herramienta, otro)'),
        'capacidad_instalada': fields.integer('Capacidad Instalada', required=True, help='Capacidad Instalada del Recurso referido en el Espacio de Formación y Autoformación'),
        'capacidad_operativa': fields.integer('Capacidad Operativa', required=True, help='Capacidad Operativa del Recurso referido en el Espacio de Formación y Autoformación'),
        'observaciones': fields.char('Observaciones', size=240, required=False, help='Observaciones y/o Comentarios adicionales'),
    }
for_pis_esp_dotacion()

class for_pis_esp_seguridad_laboral(osv.osv):
    """Registro Maestro de Seguridad Laboral en los Espacios Socialistas Integrales"""
    _name = 'for.pis.esp_seguridad_laboral'
    #_rec_name = 'espacio_id'
    _rec_name = 'seguridad_id'
    #_rec_name = 'condicion'
    _columns = {
        'espacio_id': fields.many2one('for.pis.espacios', 'Espacio', required=True, help='Espacio de Formación y Autoformación que presenta los Niveles de Seguridad Laboral indicados'),
        'seguridad_id': fields.many2one('for.pis.criterios_seguridad_laboral', 'Criterio de Seguridad', required=True, help='Criterio de Seguridad Laboral que aplica al Espacio de Formación y Autoformación'),
        'condicion': fields.char('Condición', size=240, required=False, help='Condición'),
    }
for_pis_esp_seguridad_laboral()

class for_pis_esp_equilibrio_ambiental(osv.osv):
    """Registro Maestro de Equilibrio Ambiental en los Espacios Socialistas Integrales"""
    _name = 'for.pis.esp_equilibrio_ambiental'
    #_rec_name = 'espacio_id'
    _rec_name = 'ambiental_id'
    #_rec_name = 'observaciones'
    _columns = {
        'espacio_id': fields.many2one('for.pis.espacios', 'Espacio', required=True, help='Espacio de Formación y Autoformación Sujeto de Aprendizaje que presenta los niveles de Equilibrio Ambiental indicados'),
        'ambiental_id': fields.many2one('for.pis.criterios_equilibrio_ambiental', 'Criterio Ambiental', required=True, help='Criterio de Equilibrio Ambiental que aplica al Espacio de Formación y Autoformación'),
        'observaciones': fields.char('Observaciones', size=240, required=False, help='Observaciones y/o comentarios adicionales'),
    }
for_pis_esp_equilibrio_ambiental()

class for_pis_tipos_contextos(osv.osv):
    """Tabla Referencial de Tipos de Contextos"""
    _name = 'for.pis.tipos_contextos'
    #_rec_name = 'codigo'
    _rec_name = 'tipo_contexto'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación del Tipo de Contexto'),
        'tipo_contexto': fields.char('Tipo de Contexto', size=120, required=True, help='Nombre del Tipo de Contexto'),
    }
for_pis_tipos_contextos()

class for_pis_criterios_seguridad_laboral(osv.osv):
    """Tabla Referencial de Criterios de Seguridad Laboral"""
    _name = 'for.pis.criterios_seguridad_laboral'
    #_rec_name = 'codigo'
    _rec_name = 'criterio_seguridad'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación de la Criterio de Seguridad Laboral'),
        'criterio_seguridad': fields.char('Criterio de Seguridad Laboral', size=120, required=True, help='Nombre del Criterio de Seguridad Laboral'),
    }
for_pis_criterios_seguridad_laboral()

class for_pis_criterios_equilibrio_ambiental(osv.osv):
    """Tabla Referencial de Criterios de Equilibrio Ambiental"""
    _name = 'for.pis.criterios_equilibrio_ambiental'
    #_rec_name = 'codigo'
    _rec_name = 'criterio_ambiental'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación del Criterio de Equilibrio Ambiental'),
        'criterio_ambiental': fields.char('Criterio de Equilibrio Ambiental', size=120, required=True, help='Nombre de la Criterio de Equilibrio Ambiental'),
    }
for_pis_criterios_equilibrio_ambiental()
