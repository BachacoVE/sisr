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

class for_acsea_certificaciones_sujetos(osv.osv):
    """Registro de Procesos de Generación de Certificados a Participantes de INCES Militar"""
    _name = 'for.acsea_certificaciones_sujetos'
    _rec_name = 'codigo'    
    _columns = {
        'codigo': fields.char('Código', size=9, required=True, help='Código de Identificación del Proceso (Lote) de Certificados a Participantes'),
        'estado_id': fields.many2one('for.pis.estados', 'Estado', help='Estado en en cual se ejecuto la Formación en el cual se emite el certificado'),
        'pis_inicio': fields.datetime('Inicio de la Formación', required=True, help='Fecha desde la cual se tomará la creación de certificados'),
        'pis_cierre': fields.datetime('Cierre de la Formación', required=True, help='Fecha hasta la cual se tomará la creación de certificados'),
        'fecha_generacion': fields.datetime('Fecha Generación', required=True, help='Fecha en la cual se genera el lote de Certificados para los valores (estado, cfs, fechas) establecidos'),
        'saber': fields.char('Saber', size=60, required=True, help='Texto al frente del Certificado, que indica el Saber que se acredita y certifica'),
        'lugar_fecha': fields.char('Lugar y Fecha', size=60, help='Texto que indica el Lugar y Fecha que será impreso al frente del Certificado'),
        'firmante_1': fields.char('Firmante 1', size=60, required=True, help='Texto que identificará al primer Firmante en la sección inferior de los Certifcados (Firmas y Sellos)'),
        'firmante_2': fields.char('Firmante 2', size=60, required=False, help='Texto que identificará al segundo Firmante en la sección inferior de los Certifcados (Firmas y Sellos)'),
        'observaciones': fields.text('Observaciones', required=False, help='Observaciones, Comentarios y otras informaciones complementarias y/o descriptivas del Proceso de Generación por Lotes de Certificados'),
        'certificados_ids': fields.one2many('for.acsea_certificados_sujetos', 'proceso_id', 'Certificados', help='Relación de Certificados correspondientes (generados) al (éste) Proceso de Certificación'),
        'proyecto_id': fields.many2one('for.pis.registro_inicial', 'Formación', required=True, help='Formación de cara al cual se Acredita y Certifica al Participante'),
    }
for_acsea_certificaciones_sujetos()

class for_pis_sujetos_aprendizaje_inherit(osv.osv):
    """Registro Maestro de los Certificados Emitidos a Participantes Sociales de INCES Militar. Cumple las funciones del Libro/Acta de Certificación"""
    _name = 'for.pis.sujetos_aprendizaje'
    _inherit = 'for.pis.sujetos_aprendizaje'
    _columns = {
        'certificados_ids': fields.one2many('for.acsea_certificados_sujetos', 'sujeto_id', 'Certificados', help='Certificados Obtenidos por el sujeto de aprendizaje')
    }
for_pis_sujetos_aprendizaje_inherit()

class for_pis_registro_inicial_inherit(osv.osv):
    """Registro Maestro de los Certificados Emitidos a Participantes Sociales de INCES Militar. Cumple las funciones del Libro/Acta de Certificación"""
    _name = 'for.pis.registro_inicial'
    _inherit = 'for.pis.registro_inicial'
    _columns = {
        'certificados_ids': fields.one2many('for.acsea_certificados_sujetos', 'proyecto_id', 'Certificados', help='Certificados Procedentes de la formación')
    }
for_pis_registro_inicial_inherit()


class for_acsea_certificados_sujetos(osv.osv):
    """Registro Maestro de los Certificados Emitidos a Participantes Sociales de INCES Militar. Cumple las funciones del Libro/Acta de Certificación"""
    _name = 'for.acsea_certificados_sujetos'
    _rec_name = 'correlativo'
    _columns = {
        'proceso_id': fields.many2one('for.acsea_certificaciones_sujetos', 'Proceso', help='Proceso ACSEA en el cual se generaron los certificados de Participantes (de este lote)'),
        'correlativo': fields.char('Correlativo', size=17, required=False, help='Código de Identificación del Certificado'),
        'estado_id': fields.many2one('for.pis.estados', 'Estado', required=False, help='Estado en el cual se formo el Participante (correspondiente a la Gerencia Regional a la cual presta Servicios)'),
        'estado': fields.related('estado_id', 'estado', type='char', relation='for.pis.estados', string='Estado', store=False, help='Nombre del Estado de Venezuela'),
        'sujeto_id': fields.many2one('for.pis.sujetos_aprendizaje', 'Participante', required=False, help='Participante al cual se le genera el Certificado'),
        'cedula': fields.related('sujeto_id', 'cedula', type='char', relation='for.pis.sujetos_aprendizaje', string='Cedula', store=False, help='Cédula de Identidad del Participante'),
        'nombres': fields.related('sujeto_id', 'nombres', type='char', relation='for.pis.sujetos_aprendizaje', string='Nombres', store=False, help='Nombres del Participante'),
        'apellidos': fields.related('sujeto_id', 'apellidos', type='char', relation='for.pis.sujetos_aprendizaje', string='Apellidos', store=False, help='Apellidos del Participante'),
        'libro': fields.integer('Libro', required=False, help='Número de Libro de Entrega donde está relacionado el Consecutivo del Certificado'),
        'hoja': fields.integer('Hoja (Folio)', required=False, help='Número de Folio (Hoja) del Libro de Entrega donde está relacionado el Consecutivo del Certificado'),
        'consecutivo': fields.integer('Consecutivo', required=False, help='Número de (Línea) que el Certificado tiene, en el Folio (Hoja) del Libro de Entrega'),
        'duracion': fields.integer('Duración', required=False, help='Cantidad de Tiempo, expresado en horas, de formación del Participante en el Saber referido por el Certificado, que son acreditadas a través del mismo'),
        'fecha_emision': fields.datetime('Fecha de Emisión', required=False, help='Fecha de Emisión (Impresión) del Cartón por parte del INCES (no la del Acto de Consignación al Participante).'),
        'fecha_consignacion': fields.datetime('Fecha de Consignación', required=False, help='Fecha de Entrega del Certificado al Participante. Momento en el cual, el Participante firma el Acta/Libro de Entrega, en confirmación de recepción física del cartón'),
        'estatus_certificado': fields.many2one('for.pis.acsea_certificados_estatus', 'Estatus', required=False, help='Estatus del Certificado'),
        'proyecto_id': fields.many2one('for.pis.registro_inicial', 'Formación', help='Formación de cara al cual se Acredita y Certifica al Participante Social en Aprendizaje'),
        'denominacion_pis': fields.related('proyecto_id', 'denominacion_pis_id', type='many2one', relation='for.pis.opciones_formativas', string='Formación', store=False, help='Nombre, Título o Denominación de la Formación'),
        #'estructura_curricular_ids': fields.one2many('for.estructura_curricular', 'proyecto_id', 'Estructura Curricular', help='Estructura Curricular de la Formación'),
        #'estructura_curricular_ids': fields.related('proyecto_id', 'estructura_curricular_ids', type='one2many', relation='for.pis.registro_inicial'),
        'reverso_tematica_ids': fields.one2many('for.acsea_certificados_reverso', 'certificado_id', 'Estructura Curricular', help='Estructura Curricular de la Formación'),
        'perfil_egreso': fields.text('Perfil de Egreso', required=False, help='Descripción Detallada del Perfil de Egreso del Participante Social en Aprendizaje'),
    }
for_acsea_certificados_sujetos()


class for_acsea_certificados_reverso(osv.osv):
    """Registro Maestro de los reversos de Certificados (Estructura Curricular de las Formaciones)"""
    _name = 'for.acsea_certificados_reverso'
    _rec_name = 'ec_tema'
    _columns = {
		'certificado_id': fields.many2one('for.acsea_certificados_sujetos','Certificado', help='Certificado al cual se asocia la Estructura Curricular'),
        'proyecto_id': fields.many2one('for.pis.registro_inicial','Formación', help='Formación al cual se asocia la Estructura Curricular'),
        'ec_tema': fields.char('Tema', size=250, required=False, help='Tema de la Matriz Curricular de la Formación'),
        'ec_horas': fields.integer('Horas', required=False, help='Horas asignadas al desarrollo del tema identificado en la Matriz Curricular de la Formación'),
        'ec_observaciones': fields.text('Observaciones', required=False, help='Observaciones del tema identificado en la Matriz Curricular de la Formación'),
        'ec_problema_resuelve': fields.text('Problema que resuelve', required=False, help='Problema que resuleve el tema identificado en la Matriz Curricular de la Formación'),
        'categoria_id': fields.many2one('for.categorias_contenidos','Categoría', help='Categoría de Contenido en cual se ubica el tema identificado en la Matriz Curricular de la Formación'),
    }
for_acsea_certificados_reverso()

