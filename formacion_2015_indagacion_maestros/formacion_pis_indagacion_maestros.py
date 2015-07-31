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
from datetime import date, datetime
from dateutil import parser

class for_pis_maestros(osv.osv):
    """Registro Maestro de Formadores"""
    _name = 'for.pis.maestros'
    _rec_name = 'apellidos'
    _columns = {
        'cedula': fields.char('Cédula de Identidad', size=12, required=True, help='Número de Cédula de Identidad'),
        'nombres': fields.char('1º y 2º Nombres', size=120, required=True, help='Nombres del Formador'),
        'apellidos': fields.char('1º y 2º Apellidos', size=120, required=True, help='Apellidos del Formador'),
        'nacionalidad': fields.many2one('for.pis.nacionalidades', 'Nacionalidad', help='Nacionalidad'),
        'fecha_nacimiento': fields.date('Fecha de Nacimiento', required=True, help='Fecha de Nacimiento del Formador'),
        'edad': fields.integer('Edad (años)', required=False, help='Edad del Formador'),
        'genero_id': fields.many2one('for.pis.generos', 'Género', required=True, help='Género (Masculino/Femenino)'),
        'pueblo_indigena_id': fields.many2one('for.pis.pueblos_indigenas', 'Pueblo Indígena', help='Si el Formador pertenece a algún Pueblo Indígena, indique a cuál'),
        'discapacidad_ids': fields.one2many('for.pis.mae_discapacidades', 'maestro_id', 'Diversidad Funcionales', help='Si el Formador posee alguna Diversidad Funcional, indique cuál(es)'),
        'estado_civil_id': fields.many2one('for.pis.estados_civiles', 'Estado Civil', required=True, help='Estado Civíl del Formador'),
        'hijos_ids': fields.one2many('for.pis.mae_familiares', 'maestro_id', 'Familiares', help='Familiares del Formador'),
        'estado_id': fields.many2one('for.pis.estados', 'Estado', required=True, help='Estado donde reside'),
        'municipio_id': fields.many2one('for.pis.municipios', 'Municipio', required=True, help='Municipio donde reside'),
        'parroquia_id': fields.many2one('for.pis.parroquias', 'Parroquia', required=True, help='Parroquia donde reside'),
        'comunidad_id': fields.many2one('for.pis.tipos_comunidades','Comunidad', required=True, help='Tipo de comunidad donde reside'),
        'direccion_habitacion': fields.char('Dirección Habitación', size=120, required=True, help='Dirección de habitación donde reside'),
        'telefono_fijo': fields.char('Teléfono Fijo', size=11, required=False, help='Número de teléfono fijo (sólo los números, sin puntos, parentesis, ni caracteres especiales)'),
        'telefono_celular': fields.char('Teléfono Celular', size=11, required=False, help='Número de teléfono celular (solo los números, sin puntos, parentesis, ni caracteres especiales)'),
        'correo_electronico': fields.char('Correo Electrónico', size=50, required=False, help='Dirección de correo electrónico'),
        'redes_sociales_ids': fields.one2many('for.pis.mae_redes_sociales', 'maestro_id', 'Redes Sociales', help='Nombre(s) de las red(es) social(es) y cuenta(s)'),
        'deportes_ids': fields.one2many('for.pis.mae_deportes_practicados', 'maestro_id', 'Deporte(s) que practica', help='Deporte(s) que practica'),
        'actividades_culturales_ids': fields.one2many('for.pis.mae_actividades_practicadas', 'maestro_id', 'Actividad(es) Cultural(es) que practica', help='Actividad(es) Cultural(es) que practica'),
        'organizaciones_ids': fields.one2many('for.pis.mae_organizaciones_milita', 'maestro_id', 'Organización Socio-Política', help='Organizacion(es) Socio y/o Política(s) en la(s) que milita'),
        'misiones_ids': fields.one2many('for.pis.mae_misiones_pertenece', 'maestro_id', 'Mision(es) a la(s) que pertenece', help='Misiones Sociales a las que pertenece'),
        'formacion_ids': fields.one2many('for.pis.mae_formacion_academica', 'maestro_id', 'Formación Académica', help='Formación Académica'),
        'ultimo_cursado': fields.char('Último año cursado', size=60, required=False, help='Último año cursado'),
        'especialidad_id': fields.many2one('for.pis.especialidades', 'Especialidad', help='Especialidad'),
        'otras_formaciones': fields.text('Otras formaciones', help='Cursos, Talleres y otras formaciones'),
        'experiencias_empiricas': fields.one2many('for.pis.mae_experiencias_empiricas', 'maestro_id', 'Experiencias Empíricas', help='Experiencias Empíricas'),
        'experiencias_docentes': fields.one2many('for.pis.mae_experiencias_docentes', 'maestro_id', 'Experiencias Docentes', help='Experiencias Docentes'),
        'experiencias_laborales': fields.one2many('for.pis.mae_experiencias_laborales', 'maestro_id', 'Experiencias Laborales', help='Experiencias Laborales'),
        'condicion_laboral': fields.many2one('for.pis.condiciones_laborales', 'Condición Laboral', help='Condición laboral en la que se encuentra (Fijo, Contratado, otro)'),
        'trabaja_actualmente': fields.boolean('¿Trabaja actualmente?', help='Indique si trabaja actualmente'),
        'fecha_ingreso': fields.datetime('Fecha Ingreso', help='Fecha de ingreso al último trabajo'),
        'tiempo_experiencia': fields.integer('Años experiencia', help='Años de Experiencia en el trabajo'),
        'casea_conocimientos_ids': fields.one2many('for.pis.mae_casea_conocimientos', 'maestro_id', 'Areas de Conocimiento para CASEA', help='Areas de Conocimiento para la Certificación y Acreditación de Saberes Empíricos y Académicos'),
        'pis_participado': fields.one2many('for.pis.mae_participacion_pis', 'maestro_id', 'En cuántas Formaciones ha participado', help='Relación de las Formaciones en los cuales ha participado'),
        'frecuencia_colectivos_aprendizaje_id': fields.many2one('for.pis.frecuencias_participacion', 'Participación Colectivo Formadores', help='Frecuencia de Participación en el Colectivo de Formadores'),
        'frecuencia_colectivo_cfs_id': fields.many2one('for.pis.frecuencias_participacion', 'Participación Colectivo del CFS', help='Frecuencia de Participación en el Colectivo del CFS'),
        'frecuencia_matriz_planificacion_id': fields.many2one('for.pis.frecuencias_participacion', 'Participación Matriz de Planificación', help='Frecuencia de Participación en la Matriz de Planificación del Proceso Formativo, Colectivo, Integral'),
        'frecuencia_cuaderno_sistematizacion_id': fields.many2one('for.pis.frecuencias_participacion', 'Registra en el cuaderno de Sistematización', help='Frecuencia con la cual registra en el Cuaderno de Sistematización de Experiencias'),
        'frecuencia_cuaderno_sistema_sujetos_id': fields.many2one('for.pis.frecuencias_participacion', 'Garantiza que las y los Participantes registren en su cuaderno de Sistematización', help='Frecuencia con la cual garantiza que los Participantes registren en el Cuaderno de Sistematización de Experiencias'),
        'frecuencia_intercambio_saberes_id': fields.many2one('for.pis.frecuencias_participacion', 'Realiza intercambio de saberes', help='Realiza intercambio de sabes con los Formadores para socializar los registros de los cuadernos'),
        'frecuencia_encuentros_socializacion_id': fields.many2one('for.pis.frecuencias_participacion', 'Participa en encuentros', help='¿Ha participado en encuentros o socialización de saberes con otras Formaciones?'),
        'intereses_formativos_ids': fields.one2many('for.pis.mae_intereses_formativos', 'maestro_id', 'Intereses Formativos', help='Intereses formativos del Formador'),
        'tecnologias_ids': fields.one2many('for.pis.mae_tecnologias_utilizadas', 'maestro_id', 'Tecnologías (TIC) que utiliza', help='Tecnologías de Información y Comunicación que utiliza'),
        'frecuencia_fase_I': fields.many2one('for.pis.frecuencias_participacion', 'Participación Fase I', help='Frecuencia con la que participa en la construcción del trabajo Formación. Fase I'),
        'frecuencia_fase_II': fields.many2one('for.pis.frecuencias_participacion', 'Participación Fase II', help='Frecuencia con la que participa en la construcción del trabajo Formación. Fase II'),
        'frecuencia_fase_III': fields.many2one('for.pis.frecuencias_participacion', 'Participación Fase III', help='Frecuencia con la que participa en la construcción del trabajo Formación. Fase III'),
        'observaciones': fields.text('Observaciones', help='Observaciones'),
		
        
        'horas_trabajadas': fields.integer('Horas Trabajadas', help='Total de horas trabajadas por el Formador'),
        'nivel_id': fields.many2one('for.pis.mae_valor_hora', 'Valor Hora', help='Valor de la hora (BsF) para pago al Formador'),
        'entidad_id': fields.many2one('for.pis.mae_cuentas_nomina', 'Entidad Bancaria', help='Nombre de la Entidad Bancaria Cuenta Bancaria a traves de la cual INCES paga nomina de Formadores'),
        'cuenta_id': fields.char('Cuenta Formador', size=20, required=True, help='Número de la Cuenta Bancaria donde el Formador desea que sea realiado su pago'),
        'tipo_cuenta_id': fields.many2one('for.pis.mae_tipos_cuenta', 'Tipo de Cuenta', help='Tipo de Cuenta Bancaria del Formador'),
        'asistencias_ids': fields.one2many('for.pis.mae_asistencias', 'maestro_id', 'Asistencias', help='Control de Asistencias a las Formaciones donde participa'),
		
    }
    

    def onchange_calcular_edad(self, cr, uid, ids, fecha, context=None):
        born = datetime.strptime(fecha, '%Y-%m-%d')
        today = date.today()
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        v = {'value':{}}
        v['value']['edad'] = age
        return v
            
for_pis_maestros()


##############################herencia asistencia en formacion_pis_nomina_maestros####################################################
########################################################################################################################################
########################################################################################################################################
class for_pis_mae_asistencias_extended(osv.osv):
    """Registro de Asistencias de los Formadores a las Formaciones"""
    _name = 'for.pis.mae_asistencias'
    _inherit='for.pis.mae_asistencias'
    _rec_name = 'maestro_id'
    _columns = {
        'maestro_id': fields.many2one('for.pis.maestros','Formador', help='Formador con el que guarda parentesco el familiar'),
        'cedula': fields.related('maestro_id', 'cedula', type='char', relation='for.pis.maestros', string='Cédula', store=False),
        'nombres': fields.related('maestro_id', 'nombres', type='char', relation='for.pis.maestros', string='Nombres', store=False),
        'apellidos': fields.related('maestro_id', 'apellidos', type='char', relation='for.pis.maestros', string='Apellidos', store=False),
    }
for_pis_mae_asistencias_extended()
#########################################################################################################################################
##########################################################################################################################################
##############################fin herencia asistencia en formacion_pis_nomina_maestros####################################################


##########################################################################################################################################################################3
##########################################################################################################################################################################3
############################herencia de formacion_pis_base##################################################################################################################3
class for_pis_maestros_registro_inicial_extended(osv.osv):
    """Registro Inicial de las Formaciones"""
    _name = 'for.pis.registro_inicial'
    #_rec_name = 'denominacion_pis'
    _inherit= 'for.pis.registro_inicial'
    _columns = {
        'pis_maestro_formacion_ids': fields.one2many('for.pis.mae_participacion_pis', 'maestro_id', 'Formadores en esta Formación', help='Formadores que participan en la Formación'),
    }
for_pis_maestros_registro_inicial_extended()
##########################################################################################################################################################################3
##########################################################################################################################################################################3


class for_pis_mae_familiares(osv.osv):
    """Registro Maestro de Familiares de los Formadores"""
    _name = 'for.pis.mae_familiares'
    _rec_name = 'apellidos'
    _columns = {
        'maestro_id': fields.many2one('for.pis.maestros', 'Formador', help='Formador que guarda parentesco con el familiar'),
        'cedula': fields.char('Nº Cédula de Identidad', size=12, required=False, help='Numero de la Cédula de Identidad'),
        'nombres': fields.char('1º y 2º Nombres', size=120, required=True, help='Nombres del Familiar'),
        'apellidos': fields.char('1º y 2º Apellidos', size=120, required=True, help='Apellidos del Familiar'),
        'fecha_nacimiento': fields.datetime('Fecha Nacimiento', help='Fecha de Nacimiento del Familiar'),
        'genero_id': fields.many2one('for.pis.generos', 'Genero', help='Género del Familiar'),
        'parentesco_id': fields.many2one('for.pis.parentescos', 'Parentesco', help='Parentesco con el Formador'),
        'discapacidad_id': fields.many2one('for.pis.categorias_discapacidades', 'Diversidad Funcional', help='Si el familiar tiene una Diversidad Funcional, indique cual'),
        'estado_civil_id': fields.many2one('for.pis.estados_civiles', 'Estado Civil', help='Estado Civíl del Familiar'),
    }
for_pis_mae_familiares()

class for_pis_mae_redes_sociales(osv.osv):
    """Registro Maestro de Redes Sociales a las que estan suscritos los Formadores"""
    _name = 'for.pis.mae_redes_sociales'
    _rec_name = 'cuenta'
    _columns = {
        'maestro_id': fields.many2one('for.pis.maestros', 'Formador', help='Formador que usa la referida Red Social'),
        'tipo_red_social_id': fields.many2one('for.pis.tipos_redes_sociales', 'Tipo de Red Social', help='Nombre de la Red Social a la que esta suscrito el Formador'),
        'cuenta': fields.char('Cuenta', size=60, required=True, help='Nombre de usuario, dirección u otro dato de identificación de la cuenta'),
    }
for_pis_mae_redes_sociales()

class for_pis_mae_deportes_practicados(osv.osv):
    """Registro Maestro de Deportes Practicados por los Formadores"""
    _name = 'for.pis.mae_deportes_practicados'
    _rec_name = 'deporte_id'
    _columns = {
        'maestro_id': fields.many2one('for.pis.maestros', 'Formador', help='Formador que practica el referido deporte'),
        'deporte_id': fields.many2one('for.pis.deportes', 'Deporte', help='Deporte que practica'),
        'desde': fields.datetime('Desde', required=False, help='Fecha desde la cual practica el deporte referido'),
    }
for_pis_mae_deportes_practicados()

class for_pis_mae_actividades_practicadas(osv.osv):
    """Registro Maestro de Actividades Culturales Practicadas por los Formadores"""
    _name = 'for.pis.mae_actividades_practicadas'
    _rec_name = 'actividad_cultural_id'
    _columns = {
        'maestro_id': fields.many2one('for.pis.maestros', 'Formador', help='Formador que realiza la actividad cultural'),
        'actividad_cultural_id': fields.many2one('for.pis.actividades_culturales', 'Actividad Cultural', help='Actividad Cultural que practica'),
        'desde': fields.datetime('Desde', required=False, help='Fecha desde la cual practica la referida Actividad Cultural'),
    }
for_pis_mae_actividades_practicadas()

class for_pis_mae_organizaciones_milita(osv.osv):
    """Registro Maestro de Organizaciones Socio-Políticas donde militan los Formadores"""
    _name = 'for.pis.mae_organizaciones_milita'
    _rec_name = 'organizacion_id'
    _columns = {
        'maestro_id': fields.many2one('for.pis.maestros', 'Formador', help='Formador que milita en la referida Organización Social o Política'),
        'organizacion_id': fields.many2one('for.pis.organizaciones', 'Organización Social o Política', help='Organización Social o Política donde milita el Formador'),
        'desde': fields.datetime('Desde', required=False, help='Fecha desde la cual el Formador participa o milita en la referida Organización Social o Política'),
    }
for_pis_mae_organizaciones_milita()

class for_pis_mae_misiones_pertenece(osv.osv):
    """Registro Maestro de Misiones Sociales a las que pertenecen los Formadores"""
    _name = 'for.pis.mae_misiones_pertenece'
    _rec_name = 'mision_id'
    _columns = {
        'maestro_id': fields.many2one('for.pis.maestros', 'Formador', help='Formador que participa en la referida Misión Social'),
        'mision_id': fields.many2one('for.pis.misiones', 'Misión Social', help='Misión Social'),
        'desde': fields.datetime('Desde', required=False, help='Fecha desde la cual pertenece a la referida Misión Social'),
    }
for_pis_mae_misiones_pertenece()

class for_pis_mae_formacion_academica(osv.osv):
    """Registro Maestro de Formación Académica por los Formadores"""
    _name = 'for.pis.mae_formacion_academica'
    _rec_name = 'nivel_educativo_id'
    _columns = {
        'maestro_id': fields.many2one('for.pis.maestros', 'Formador', help='Formador que registra el grado o nivel de formación académica referida'),
        'nivel_educativo_id': fields.many2one('for.pis.niveles_academicos', 'Nivel Educativo', help='Nivel Educativo'),
        'estatus_educativo_id': fields.many2one('for.pis.estatus_niveles_educativos', 'Estado', help='Estado de Avance del Nivel Educativo (C=Culmino, I=No completo, P=En Progreso)'),
    }
for_pis_mae_formacion_academica()

class for_pis_mae_intereses_formativos(osv.osv):
    """Registro Maestro de Intereses y Necesidades Formativas por los Formadores"""
    _name = 'for.pis.mae_intereses_formativos'
    _rec_name = 'requirimiento'
    _columns = {
        'maestro_id': fields.many2one('for.pis.maestros', 'Formador', help='Formador que muestra los intereses formativos indicados'),
        'sector_economico_id': fields.many2one('for.pis.sectores_economicos', 'Sector Económico', help='Sector Económico'),
        'area_economica_id': fields.many2one('for.pis.areas_economicas', 'Area Económica', help='Area Económica'),
        'requerimiento': fields.char('Requerimiento', size=300, required=False, help='Requerimiento o Necesidad de Formación'),
    }
for_pis_mae_intereses_formativos()

class for_pis_mae_tecnologias_utilizadas(osv.osv):
    """Registro Maestro de Tecnologías de Información y Comunicación utilizadas por Formadores"""
    _name = 'for.pis.mae_tecnologias_utilizadas'
    _rec_name = 'tecnologia'
    _columns = {
        'maestro_id': fields.many2one('for.pis.maestros', 'Formador', help='Formador que usa la tencología TIC referida'),
        'tecnologia': fields.many2one('for.pis.tecnologias_tic', 'Tecnología', help='Tecnología de Información y Comunicación que utiliza'),
    }
for_pis_mae_tecnologias_utilizadas()

class for_pis_mae_participacion_pis(osv.osv):
    """Registro Maestro de Participación de los Formadores en Formaciones"""
    _name = 'for.pis.mae_participacion_pis'
    _rec_name = 'numero_id'
    _columns = {
        'maestro_id': fields.many2one('for.pis.maestros', 'Formador', help='Formador que participa en la Formación referida'),
        'numero_id': fields.many2one('for.pis.registro_inicial', 'Formación donde participa', help='Formación donde participa o ha participado'),
    }
for_pis_mae_participacion_pis()

class for_pis_mae_experiencias_empiricas(osv.osv):
    """Registro Maestro de Experiencias Empíricas de los Formadores"""
    _name = 'for.pis.mae_experiencias_empiricas'
    _rec_name = 'area_conocimiento_id'
    _columns = {
        'maestro_id': fields.many2one('for.pis.maestros', 'Formador', help='Formador que registra la Experiencia Empírica referida'),
        'area_conocimiento_id': fields.many2one('for.pis.areas_conocimientos', 'Area de Conocimiento', help='Area(s) de Conocimiento(s)'),
        'tiempo_experiencias': fields.integer('Tiempo (meses)', required=True, help='Tiempo de Experiencia (expresado en Meses)'),
        'portafolio_evidencias': fields.boolean('¿Portafolio de Evidencias?', help='Portafolio de Evidencias'),
        'protafolio_enlace': fields.char('Enlace', size=120, required=False, help='Enlace (Ruta/URL) al portafolio de evidencias'),
    }
for_pis_mae_experiencias_empiricas()

class for_pis_mae_experiencias_docentes(osv.osv):
    """Registro Maestro de Experiencias Docentes de los Formadores"""
    _name = 'for.pis.mae_experiencias_docentes'
    _rec_name = 'area_conocimiento_id'
    _columns = {
        'maestro_id': fields.many2one('for.pis.maestros', 'Formador', help='Formador que registra la Experiencia Docente referida'),
        'entidad_educativa': fields.char('Institución Educativa', size=120, required=True, help='Institución Educativa donde laboró'),
        'tiempo_experiencia': fields.integer('Tiempo (meses)', required=True, help='Tiempo de Experiencia Docente en la referida institución educativa (en Meses)'),
        'area_conocimiento_id': fields.many2one('for.pis.areas_conocimientos', 'Area de Conocimiento', help='Area(s) de Conocimiento'),
    }
for_pis_mae_experiencias_docentes()

class for_pis_mae_experiencias_laborales(osv.osv):
    """Registro Maestro de Experiencias Laborales de los Formadores"""
    _name = 'for.pis.mae_experiencias_laborales'
    _rec_name = 'profesion_ocupacion_id'
    _columns = {
        'maestro_id': fields.many2one('for.pis.maestros', 'Formador', help='Formador que registra las Experiencas Laborales referidas'),
        'profesion_ocupacion_id': fields.many2one('for.pis.profesiones_ocupaciones', 'Profesión u Ocupación', help='Profesión u Ocupación'),
        'tiempo_experiencia': fields.integer('Tiempo (Meses)', required=True, help='Tiempo total de experiencia (expresada en Meses)'),
        'lugar': fields.char('Lugar', size=120, required=True, help='Lugar (Empresa, Unidad Productiva, Organización o Institución) donde trabajó'),
    }
for_pis_mae_experiencias_laborales()

class for_pis_mae_casea_conocimientos(osv.osv):
    """Registro Maestro de Conocimientos para Certificación y Acreditación de Saberes Empíricos y Académicos de los Formadores"""
    _name = 'for.pis.mae_casea_conocimientos'
    _rec_name = 'area_conocimiento_id'
    _columns = {
        'maestro_id': fields.many2one('for.pis.maestros', 'Formador', help='Formador que desea certificar o acreditar el conocimiento'),
        'area_conocimiento_id': fields.many2one('for.pis.areas_conocimientos', 'Area de Conocimiento', help='Area de Conocimiento en la que desea obtener Certificación o Acreditación'),
        'tiempo_experiencia': fields.integer('Tiempo Experiencia', required=True, help='Tiempo de Experiencia en el conocimiento que desea acreditar o certificar'),
        'donde': fields.char('Indique dónde', size=120, required=True, help='Dónde desarrolló el conocimiento o experiencia que desea certificar o acreditar'),
        'portafolio_evidencias': fields.boolean('Portafolio de Evidencias', help=' Portafolio de Evidencias '),
        'portafolio_enlace': fields.char('Enlace', size=120, required=False, help='Enlace al Portafolio de Evidencias'),
    }
for_pis_mae_casea_conocimientos()

class for_pis_mae_discapacidades(osv.osv):
    """Registro Maestro de Diversidad Funcionales de los Formadores"""
    _name = 'for.pis.mae_discapacidades'
    _rec_name = 'categoria_discapacidad_id'
    _columns = {
        'maestro_id': fields.many2one('for.pis.maestros', 'Formador', help='Formador que presenta la Diversidad Funcional'),
        'categoria_discapacidad_id': fields.many2one('for.pis.categorias_discapacidades', 'Diversidad Funcional', help='Diversidad Funcional que presenta el Formador'),
        'observaciones': fields.text('Observaciones', size=300, required=False, help='Comentarios adicionales respecto a la Diversidad Funcional presentada por el Formador'),
    }
for_pis_mae_discapacidades()

class for_pis_mae_tipos_cuenta(osv.osv):
    """Tabla Referencial de Tipos de Cuentas Bancarias"""
    _name = 'for.pis.mae_tipos_cuenta'
    _rec_name = 'tipo_cuenta'
    _columns = {
        'codigo': fields.char('Código', size=3, required=False, help='Código del Tipo de Cuenta Bancaria'),
        'tipo_cuenta': fields.char('Tipo de Cuenta', size=60, required=False, help='Nombre del Tipo de Cuenta Bancaria'),
        'codigo_ext': fields.char('Código Externo', size=3, required=False, help='Código del Tipo de Cuenta, usado para integración con otros sistemas'),
    }
for_pis_mae_tipos_cuenta()
