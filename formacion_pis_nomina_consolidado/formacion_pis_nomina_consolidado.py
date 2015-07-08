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

class for_pis_mae_consolidado(osv.osv):
    """Registro Maestro de Reportes Consolidados de Asistencia y Pago de Facilitadores"""
    _name = 'for.pis.mae_consolidado'
    _rec_name = 'codigo'
    _columns = {
        'codigo': fields.char('Código', size=12, required=True, help='Código de Identificación del Reporte Consolidado, para los parámetros y período indicados'),
        'estado_id': fields.many2one('for.pis.estados','Estado', required=True, help='Estado del País al cual se aplica la consolidación'),
        'cfs_id': fields.many2one('for.pis.cfs','CFS', required=False, help='Centro de Formación Socialista al cual se aplica la consolidación'),
        'numero_id': fields.many2one('for.pis.registro_inicial','Formación', help='Proyecto Integral Socialista al cual se le Consolida la Asistencia y Pagos de los Facilitadores que participan en él'),
        'maestro_id': fields.many2one('for.pis.maestros','Facilitador', help='Facilitador al cual se le realiza el computo de total de horas trabajadas y monto del pago'),
        'consolidado_desde': fields.datetime('Desde', help='Fecha de inicio del período de consolidación de asistencias y pagos'),
        'consolidado_hasta': fields.datetime('Hasta', help='Fecha de culminación del período de consolidación de asistencias y pagos'),
        'observaciones': fields.text('Observaciones', help='Observaciones y comentarios importantes o adicionales acerca de la generación del Consolidado'),
        'responsable_1': fields.many2one('res.users','Responsable 1', help='Identificación (Nombre y Apellido) del Usuario Responsable (1) de avalar el Consolidado'),
        'responsable_1_aval': fields.boolean('Conforme 1', help='Indica si el responsable (1) avala o da conformidad a los datos presentes en el reporte consolidado (Operación post-generación y revisión del reporte).'),
        'responsable_1_fecha': fields.datetime('Fecha 1', help='Fecha en la cual el Responsable 1 realiza el aval o conformidad del contenido del reporte consolidado'),
        'responsable_2': fields.many2one('res.users', 'Responsable 2', help='Identificación (Nombre y Apellido) del Usuario Responsable (2) de avalar el Consolidado'),
        'responsable_2_aval': fields.boolean('Conforme 2', help='Indica si el responsable (2) avala o da conformidad a los datos presentes en el reporte consolidado (Operación post-generación y revisión del reporte).'),
        'responsable_2_fecha': fields.datetime('Fecha 2', help='Fecha en la cual el Responsable 2 realiza el aval o conformidad del contenido del reporte consolidado'),
        'responsable_3': fields.many2one('res.users', 'Responsable 3', help='Identificación (Nombre y Apellido) del Usuario Responsable (3) de avalar el Consolidado'),
        'responsable_3_aval': fields.boolean('Conforme 3', help='Indica si el responsable (3) avala o da conformidad a los datos presentes en el reporte consolidado (Operación post-generación y revisión del reporte).'),
        'responsable_3_fecha': fields.datetime('Fecha 3', help='Fecha en la cual el Responsable 3 realiza el aval o conformidad del contenido del reporte consolidado'),
        'estatus': fields.char('Estatus', size=3, required=False, help='Estado en el cual se encuentra el reporte Consolidado de Asistencias y Pagos a Facilitadores'),
        'detalle_ids': fields.one2many('for.pis.mae_consolidado_detalle','consolidado_id','Detalle', help='Detalle del Reporte Consolidado'),
    }
for_pis_mae_consolidado()

class for_pis_mae_consolidado_detalle(osv.osv):
    """Registro de Detalles de los Reportes Consolidados de Asistencia y Pago de Facilitadores"""
    _name = 'for.pis.mae_consolidado_detalle'
    _rec_name = 'maestro_id'
    _columns = {
        'consolidado_id': fields.many2one('for.pis.mae_consolidado','Reporte', help='Reporte Consolidado al cual pertenece el registro de detalle'),
        'estado_id': fields.many2one('for.pis.estados','Estado', help='Estado del País donde se realiza el Consolidado'),
        'cfs_id': fields.many2one('for.pis.cfs','CFS', help='Centro de Formación Socialista donde se realiza el Consolidado'),
        'desde': fields.datetime('Desde', help='Fecha de inicio del período de consolidación de asistencias'),
        'hasta': fields.datetime('Hasta', help='Fecha de culminación del período de consolidación de asistencias'),
        'maestro_id': fields.many2one('for.pis.maestros','Facilitador', help='Facilitador al cual se le realiza el computo de total de horas trabajadas y monto del pago'),
        'cedula': fields.char('Cédula', size=20, help='Cédula de Identidad del Facilitador'),
        'nombres': fields.char('Nombres', size=120, help='Primer y Segundo Nombres del Facilitador'),
        'apellidos': fields.char('Apellidos', size=120, help='Primer y Segundo Apellidos del Facilitador'),
        'cuenta_tipo': fields.char('Tipo de Cuenta', size=20, help='Tipo de Cuenta del Facilitador (Ahorro, Corriente, otros)'),
        'cuenta_numero': fields.char('Número de Cuenta', size=20, help='Numero de Cuenta Personal del Facilitador'),
        'entidad_bancaria': fields.char('Banco', size=120, help='Entidad Bancaria desde la cual el INCES paga a los Facilitadores (que el Facilitador selecciona)'),
        'valor_hora': fields.float('Valor Hora (Bsf)', help='Valor de pago de la hora de trabajo del Facilitador'),
        'pis_id': fields.many2one('for.pis.registro_inicial','Formación', help='Proyecto Integral Socialista donde participa o ha participado el Facilitador'),
        'pis_nombre': fields.char('Denominación', size=250, help='Título o Denominación del Proyecto Integral Socialista donde trabaja el Facilitador'),
        'total_horas': fields.integer('Total Horas', help='Total de horas trabajadas por el Facilitador, en el período y proyecto indicados'),
        'monto_pago': fields.float('Monto (BsF)', help='Monto del pago al Facilitador para el período de Consolidación'),
        'activo': fields.boolean('Activo', help='Indica si el registro está o no activo o habilitado, para su procesamiento'),
        'observaciones': fields.text('Observaciones', help='Observaciones o comentarios adicionales respecto al registro de detalle del reporte consolidado'),
    }
for_pis_mae_consolidado_detalle()

