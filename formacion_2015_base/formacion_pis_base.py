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

class for_pis_estados(osv.osv):
    """Tabla de Referencia de Estados (Geográfico)"""
    _name = 'for.pis.estados'
    _rec_name = 'estado'
    _columns = {
        'codigo': fields.char('Código',size=3,required=True, help='Código del Estado'),
        'estado': fields.char('Estado',size=30,required=True, help='Nombre del Estado'),
    }
for_pis_estados()

class for_pis_municipios(osv.osv):
    """Tabla de Referencia de Municipios (Geográfico)"""
    _name = 'for.pis.municipios'
    _rec_name = 'municipio'
    _columns = {
        'codigo': fields.char('Código',size=3,required=True, help='Código del Municipio'),
        'municipio': fields.char('Municipio',size=30,required=True, help='Nombre del Municipio'),
        'estado_id': fields.many2one('for.pis.estados','Estado'),
    }
for_pis_municipios()

class for_pis_parroquias(osv.osv):
    """Tabla de Referencia de Parroquias (Geográfico)"""
    _name = 'for.pis.parroquias'
    _rec_name = 'parroquia'
    _columns = {
        'codigo': fields.char('Código',size=3,required=True, help='Código de Identificación de la Parroquia'),
        'parroquia': fields.char('Parroquia',size=30,required=True, help='Nombre de la Parroquia'),
        'municipio_id': fields.many2one('for.pis.municipios','Municipio', help='Municipio al cual pertenece la Parroquia'),
    }
for_pis_parroquias()

class for_pis_sectores_economicos(osv.osv):
    """Tabla de referencia del Sector Económico de la Formación (Económico)"""
    _name = 'for.pis.sectores_economicos'
    _rec_name = 'sector_economico'
    _columns = {
        'codigo': fields.char('Código',size=3,required=True, help='Código de Identificación del Sector Económico'),
        'sector_economico': fields.char('Sector Económico',size=30,required=True, help='Nombre del Sector Económico'),
    }
for_pis_sectores_economicos()

class for_pis_areas_economicas(osv.osv):
    """Tabla de Referencia del Area Economica"""
    _name = 'for.pis.areas_economicas'
    _rec_name = 'area_economica'
    _columns = {
        'codigo': fields.char('Código',size=3,required=True, help='Código de Identificación del Area Económica'),
        'area_economica': fields.char('Area Económica',size=200,required=True, help='Nombre del Area Económica'),
        'sector_id': fields.many2one('for.pis.sectores_economicos','Sector Económico', help='Sector Económico al cual pertenece el Area Económica'),
    }
for_pis_areas_economicas()

class for_pis_subareas_economicas(osv.osv):
    """Tabla de Referencia de Subareas Economicas"""
    _name = 'for.pis.subareas_economicas'
    _rec_name = 'subarea_economica'
    _columns = {
        'codigo': fields.char('Codigo',size=3,required=True, help='Código de Identificación de la Sub Area Económica'),
        'subarea_economica': fields.char('Subarea Económica',size=200,required=True, help='Nombre de la Sub Area Económica'),
        'area_id': fields.many2one('for.pis.areas_economicas','Area', help='Area Económica a la cual corresponde la Sub Area'),
    }
for_pis_subareas_economicas()

class for_pis_tipos_procedencias(osv.osv):
    """Tabla de Referencia de Tipos de Procedencias"""
    _name = 'for.pis.tipos_procedencias'
    _rec_name = 'tipo_procedencia'
    _columns = {
        'codigo': fields.char('Código',size=3,required=True, help='Codigo de Identificación del Tipo de Procedencia'),
        'tipo_procedencia': fields.char('Tipo de Procedencia',size=30,required=True, help='Nombre del Tipo de Procedencia'),
        'descripcion': fields.char('Descripción',size=250,required=True, help='Descripción del Tipo de Procedencia'),
    }
for_pis_tipos_procedencias()

class for_pis_registro_inicial(osv.osv):
    """Registro Inicial de la Formación"""
    _name = 'for.pis.registro_inicial'
    _rec_name = 'denominacion_pis'
    _columns = {
        'nro_preimpreso': fields.integer('Nº Preimpreso',size=30,required=True, help='Número de Preimpreso de la Formación'),
        'denominacion_pis_id': fields.many2one('for.pis.opciones_formativas', 'Denominación',size=240,required=True, help='Denominación que el Colectivo adopto para su Formación'),
        'lapso_ejecucion': fields.related('denominacion_pis_id','horas',type='integer',relation='for.pis.opciones_formativas',string='Lapso de Ejecución',store=True, readonly=True),
        'fecha_inicio': fields.datetime('Fecha de Inicio',required=False, help='Fecha de Inicio de la formación'),
        'fecha_cierre': fields.datetime('Fecha de Cierre',required=False, help='Fecha de cierre de la formación'),
        'cantidad_sujetos': fields.integer('Cantidad de Participantes',required=False, help='Cantidad de Participantes que integran la Formación'),
        'cantidad_maestros': fields.integer('Cantidad de Facilitadores(as)',required=False, help='Cantidad de Facilitadoras y/o Facilitadores que atienden la Formación'),
        'accion_especifica': fields.selection([(1,'Acción Específica 1'),(3,'Acción Específica 3')],'Acción Específica',required=True, help='Acción Específica a la cual corresponde la Formación'),
        'estado_id': fields.many2one('for.pis.estados','Estado', required=True, help='Estado en el cual se desarrolla la Formación'),
        'municipio_id': fields.many2one('for.pis.municipios','Municipio', required=True, help='Municipio en el cual se desarrolla la Formación'),
        'parroquia_id': fields.many2one('for.pis.parroquias','Parroquia', required=True, help='Parroquia en la cual se desarrolla la Formación'),
        'cfs_id': fields.many2one('for.pis.cfs','CFS responsable', required=True, help='Centro de Formación Socialista en el cual se desarrolla el CFS'),
        'sector_id': fields.many2one('for.pis.sectores_economicos','Sector Económico', required=True, help='Sector Económico en el cual se enmarca la Formación'),
        'area_id': fields.many2one('for.pis.areas_economicas','Area Económica', required=True, help='Area Económica en la cual se enmarca la Formación'),
        'subarea_id': fields.many2one('for.pis.subareas_economicas','Subarea Económica', required=True, help='Sub Area Económica en la cual se enmarca la Formación'),
        'tipo_procedencia_id': fields.many2one('for.pis.tipos_procedencias','Procedencia de la Formación', required=True, help='Procedencia de la propuesta original de la Formación'),

##########################################################################################################################################################################################        
#####################################################################################################################################################################################
#####################el siguiente campo creado en formacion_pis_indagacion_matrices por herencia##################################################################################
        #'matriz_curricular_ids': fields.one2many('for.estructura_curricular', 'proyecto_id', 'Matriz Curricular', required=False,help='Temas que conforman la Matriz Curricular la Formación'),
########################################################################################################################################################################################



##########################################################################################################################################################################################        
#####################################################################################################################################################################################
#####################el siguiente campo creado en formacion_pis_indagacion por herencia##################################################################################
        #'participacion_pis_ids': fields.one2many('for.pis.participacion_pis', 'numero_id', 'Participantes', help='Participantes de la Formación'),
########################################################################################################################################################################################


##########################################################################################################################################################################################        
#####################################################################################################################################################################################
#####################el siguiente campo creado en formacion_pis_indagacion_espacios por herencia##################################################################################
#'turno_id': fields.many2one('for.pis.turnos', 'Turno', required=True, help='Turno en el cual opera el Espacio Socialista Integral'),
########################################################################################################################################################################################




        #Campos adicionales traidos de arranque 2015
        #CALENDARIO
        #FALTA APUNTARLO AL OTRO OBJETO TURNOS
        
        #Separador HORARIO#
        'fecha_inicio': fields.date('Fecha de Inicio',required=False, help='Indique la Fecha de Inicio de la Modalidad'),
        'fecha_cierre': fields.date('Fecha de Cierre',required=False, help='Indique la Fecha de Finalización de la Modalidad'),
        'hor_inicio': fields.char('Hora de Inicio', size=5, help='Colocar el Horario en que se dictara la Modalidad.(Ej. 7:00am a 11:00am)'),
        'hor_fin': fields.char('Hora de Fin', size=5, help='Colocar el Horario en que se dictara la Modalidad.(Ej. 7:00am a 11:00am)'),
        #Separador Dias#
        'for_dom': fields.boolean('Dom', help='Domingo'),
        'for_lun': fields.boolean('Lun', help='Lunes'),
        'for_mar': fields.boolean('Mar', help='Martes'),
        'for_mie': fields.boolean('Mie', help='Miércoles'),
        'for_jue': fields.boolean('Jue', help='Jueves'),
        'for_vie': fields.boolean('Vie', help='Viernes'),
        'for_sab': fields.boolean('Sab', help='Sábado'),
        #PROCEDENCIA
        #Separador PROCEDENCIA
        #'clasificacion': fields.many2one('for.pis.clasificacion_procedencia','Clasificación', help='Clasificación de la Procedencia de la Formación'),
        'dimension': fields.selection([('publico','Público'),('privado','Privado'),('comunal','Comunal')],'Dimensión', help='Dimensión'),
        'entidad': fields.char('Entidad', size=200, help='Nombre de la Entidad de procedencia de la Formación'), 
        
        #agregando las lineas de motores economicos del modulo arranque2015
        'motores_economicos_id': fields.related('denominacion_pis_id','motores_economicos_id', type='many2one',relation='for.pis.motores_economicos', string='Motores Económicos', readonly=True, store=True),
        'cadenas_formativas_id': fields.many2one('for.pis.cadenas_formativas', 'Áreas Priorizadas', required=True, help='Cadena Priorizada'),
        'modalidad_id': fields.related('denominacion_pis_id','modalidad_id',type='many2one',relation='for.pis.modalidad', string='Modalidad', store=True, readonly=True),
        #hasta aqui llegan las lineas agregadas

       }

    def on_change_modalidad_id(self, cr, uid, ids, denominacion_pis_id):
        v={}
        if denominacion_pis_id:
            opciones_formativas_obj=self.pool.get('for.pis.opciones_formativas').browse(cr, uid, denominacion_pis_id)
            #modalidad_obj=self.pool.get('for.pis.modalidad').browse(cr, uid, opciones_formativas_obj)
            v['modalidad_id']=opciones_formativas_obj.modalidad_id.id
            v['lapso_ejecucion']=opciones_formativas_obj.horas
            v['motores_economicos_id']=opciones_formativas_obj.motores_economicos_id.id
        return {'value':v}

        

for_pis_registro_inicial()

class for_pis_cfs(osv.osv):
    """Registro Facilitador de Centros Integrales (de Formación) Socialista"""
    _name = 'for.pis.cfs'
    _rec_name = 'nombre'
    _columns = {
        'codigo': fields.char('Código',size=3,required=True, help='Código de Identificación del Centro de Formación Socialista'),
        'nombre': fields.char('CFS',size=60,required=True, help='Nombre del Centro de Formación Socialista'),
        'ubicacion': fields.char('Ubicación',size=200,required=True, help='Direccion del Centro de Formación Socialista'),
        'telefono': fields.char('Teléfono',size=30,required=False, help='Número de Contacto Telefónico del Centro de Formación Socialista'),
        'observaciones': fields.char('Observaciones',size=300,required=False, help='Observaciones'),
        'estado_id': fields.many2one('for.pis.estados','Estado', required=True, help='Estado en el cual está ubicado el Centro de Formación'),
        'municipio_id': fields.many2one('for.pis.municipios','Municipio', required=True, help='Municipio en el cual está ubicado el Centro de Formación'),
        'parroquia_id': fields.many2one('for.pis.parroquias', 'Parroquia', required=True, help='Parroquia en la cual está ubicada el Centro de Formación'),
    }
for_pis_cfs()

#llamado de las tablas que utiliza, los motorores economicos, la modalidad, cadena formativa
class for_pis_motores_economicos(osv.osv):
    """Motores Económicos"""
    _name = 'for.pis.motores_economicos'
    _rec_name = 'descripcion'
    _columns = {
        'nombre': fields.char('Nombre', size=200, help='Nombre del Motor Económico'),
        'descripcion': fields.text('Descripción', help='Descripción del Motor Económico'),
    }
for_pis_motores_economicos()

class for_pis_modalidad(osv.osv):
    """Modalidad"""
    _name = 'for.pis.modalidad'
    _rec_name = 'nombre'
    _columns = {
        'nombre': fields.char('Nombre', size=60, help='Nombre de la modalidad Formativa'),
        'descripcion': fields.text('Descripción', help='Descripción de la modalidad'),
    }
for_pis_modalidad()

class for_pis_cadenas_formativas(osv.osv):
    """Modalidad"""
    _name = 'for.pis.cadenas_formativas'
    _rec_name = 'nombre'
    _columns = {
        'nombre': fields.char('Nombre', size=60, help='Nombre de la Cadena Formativa'),
        'descripcion': fields.text('Descripción', help='Descripción de la Cadena Formativa'),
    'motores_economicos_id':fields.many2one('for.pis.motores_economicos', 'Motor Economico', required=False, help='Motor Económico'),
    }
for_pis_cadenas_formativas()

class for_pis_calendario(osv.osv):
    """Calendario de días hábiles"""
    _name = 'for.pis.calendario'
    _rec_name = 'nro_semana'
    _columns = {
        'ano': fields.integer('Año del Calendario', help='Año del Calendario a Mostrar'),
        'nro_semana': fields.integer('Nro de la Semana', help='Número de la Semana'),
        'inicio_semana': fields.date('Inicio de Semana', help='Fecha de Inicio de la Semana'),
        'final_semana': fields.date('Final de Semana', help='Fecha de Finalización de la Semana'),
        'lunes': fields.boolean('Lunes', help='Campo de verificación para determinar si el Lunes es Laborable. (True = Sí)'),
        'martes': fields.boolean('Martes', help='Campo de verificación para determinar si el Martes es Laborable. (True = Sí)'),
        'miercoles': fields.boolean('Miércoles', help='Campo de verificación para determinar si el Miércoles es Laborable. (True = Sí)'),
        'jueves': fields.boolean('Jueves', help='Campo de verificación para determinar si el Jueves es Laborable. (True = Sí)'),
        'viernes': fields.boolean('Viernes', help='Campo de verificación para determinar si el Viernes es Laborable. (True = Sí)'),
        'sabado': fields.boolean('Sábado', help='Campo de verificación para determinar si el Sábado es Laborable. (True = Sí)'),
        'domingo': fields.boolean('Domingo', help='Campo de verificación para determinar si el Domingo es Laborable. (True = Sí)'),
        'active': fields.boolean('¿Semana Activa?', help="Campo de Activación o Desactivación de la Semana"),
    }
for_pis_calendario()

class for_pis_opciones_formativas(osv.osv):
    """Maestra de Cursos Disponibles por CFS"""
    _name = 'for.pis.opciones_formativas'
    _rec_name='denominacion'
    _columns = {
        'estado_id': fields.many2one('for.pis.estados','Estado', required=True, help='Estado en el cual se desarrolla la Formación'),
        'cfs_id': fields.many2one('for.pis.cfs','CFS responsable', required=True, help='Centro de Formación Socialista en el cual se desarrolla el CFS'),
        'motores_economicos_id': fields.many2one('for.pis.motores_economicos', 'Motores Económicos', required=True, help='Seleccione cual de los Motores Productivos corresponde la modalidad de Formación: Agroindustria, Hidrocarburo-Petroquímica, Hierro-Acero, Sector Eléctrico, Telecomunicaciones, Turismo, Construcción, Ciencia e Innovación y Diseño, Manufactura-Autopartes, Mineria, Textil-Calzado y Servicios'),
        'identificador': fields.integer('Identificador',size=30, help='Código Único Identificador de la Formación'),
        'denominacion': fields.char('Denominación',size=240,required=True, help='Denominación del Curso'),
        'horas': fields.integer('Horas',size=6,required=False, help='Horas de duración del Curso'),
        'modalidad_id': fields.many2one('for.pis.modalidad', 'Modalidad', required=False, help='Indique la Modalidad: Cursos, PIS, Taller, Diplomado, Seminario'),
    }
for_pis_opciones_formativas()
