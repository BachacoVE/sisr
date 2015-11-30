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
import re
from osv import fields,osv
from datetime import date, datetime
from dateutil import parser

class for_pis_sujetos_aprendizaje(osv.osv):
    """Registro Maestro de Participantes """
    _name = 'for.pis.sujetos_aprendizaje'
    _rec_name = 'cedula'
    _columns = {
        'cedula': fields.char('Cédula de Identidad', size=12, required=True, help='Número de Cédula de Identidad'),
        'nombres': fields.char('1º y 2º Nombres', size=120, required=True, help='Nombres del Participante'),
        'apellidos': fields.char('1º y 2º Apellidos', size=120, required=True, help='Apellidos del Participante'),
        'nacionalidad': fields.many2one('for.pis.nacionalidades', 'Nacionalidad', help='Nacionalidad'),
        'fecha_nacimiento': fields.date('Fecha de Nacimiento', required=True, help='Fecha de Nacimiento del Participante'),
        'edad': fields.integer('Edad (años)', required=False, help='Edad del Participante'),
        'genero_id': fields.many2one('for.pis.generos', 'Género', required=True, help='Género (Masculino/Femenino)'),
        'pueblo_indigena_id': fields.many2one('for.pis.pueblos_indigenas', 'Pueblo Indígena', help='Si el Participante pertenece a algún Pueblo Indígena, indique a cuál'),
        'discapacidad_ids': fields.one2many('for.pis.discapacidades', 'sujeto_id', 'Discapacidades', help='Si el Participante posee alguna Discapacidad, indique cuál(es)'),
        'estado_civil_id': fields.many2one('for.pis.estados_civiles', 'Estado Civil', required=True, help='Estado Civíl del Participante'),
        'hijos_ids': fields.one2many('for.pis.familiares', 'sujeto_id', 'Familiares', help='Familiares del Participante'),
        'estado_id': fields.many2one('for.pis.estados', 'Estado', required=True, help='Estado donde reside'),
        'municipio_id': fields.many2one('for.pis.municipios', 'Municipio', required=True, help='Municipio donde reside'),
        'parroquia_id': fields.many2one('for.pis.parroquias', 'Parroquia', required=True, help='Parroquia donde reside'),
        'comunidad_id': fields.many2one('for.pis.tipos_comunidades','Comunidad', required=True, help='Tipo de comunidad donde reside'),
        'direccion_habitacion': fields.char('Dirección Habitación', size=120, required=True, help='Dirección de habitación donde reside'),
        'telefono_fijo': fields.char('Teléfono Fijo', size=11, required=False, help='Número de teléfono fijo (sólo los números, sin puntos, parentesis, ni caracteres especiales)'),
        'telefono_celular': fields.char('Teléfono Celular', size=11, required=False, help='Número de teléfono celular (solo los números, sin puntos, parentesis, ni caracteres especiales)'),
        'correo_electronico': fields.char('Correo Electrónico', size=50, required=False, help='Dirección de correo electrónico'),
        'redes_sociales_ids': fields.one2many('for.pis.redes_sociales', 'sujeto_id', 'Redes Sociales', help='Nombre(s) de las red(es) social(es) y cuenta(s)'),
        'deportes_ids': fields.one2many('for.pis.deportes_practicados', 'sujeto_id', 'Deporte(s) que practica', help='Deporte(s) que practica'),
        'actividades_culturales_ids': fields.one2many('for.pis.actividades_practicadas', 'sujeto_id', 'Actividad(es) Cultural(es) que practica', help='Actividad(es) Cultural(es) que practica'),
        'organizaciones_ids': fields.one2many('for.pis.organizaciones_milita', 'sujeto_id', 'Organización Socio-Política', help='Organizacion(es) Socio y/o Política(s) en la(s) que milita'),
        'misiones_ids': fields.one2many('for.pis.misiones_pertenece', 'sujeto_id', 'Mision(es) a la(s) que pertenece', help='Misiones Sociales a las que pertenece'),
        'formacion_ids': fields.one2many('for.pis.formacion_academica', 'sujeto_id', 'Formación Académica', help='Formación Académica'),
        'ultimo_cursado': fields.char('Último año cursado', size=60, required=False, help='Último año cursado'),
        'especialidad_id': fields.many2one('for.pis.especialidades', 'Especialidad', help='Especialidad'),
        'otras_formaciones': fields.text('Otras formaciones', help='Cursos, Talleres y otras formaciones'),
        'experiencias_empiricas': fields.one2many('for.pis.experiencias_empiricas', 'sujeto_id', 'Experiencias Empíricas', help='Experiencias Empíricas'),
        'experiencias_docentes': fields.one2many('for.pis.experiencias_docentes', 'sujeto_id', 'Experiencias Docentes', help='Experiencias Docentes'),
        'experiencias_laborales': fields.one2many('for.pis.experiencias_laborales', 'sujeto_id', 'Experiencias Laborales', help='Experiencias Laborales'),
        'condicion_laboral': fields.many2one('for.pis.condiciones_laborales', 'Condición Laboral', help='Condición laboral en la que se encuentra (Fijo, Contratado, otro)'),
        'trabaja_actualmente': fields.boolean('¿Trabaja actualmente?', help='Indique si trabaja actualmente'),
        'fecha_ingreso': fields.datetime('Fecha Ingreso', help='Fecha de ingreso al último trabajo'),
        'tiempo_experiencia': fields.integer('Años experiencia', help='Años de Experiencia en el trabajo'),
        'casea_conocimientos_ids': fields.one2many('for.pis.casea_conocimientos', 'sujeto_id', 'Areas de Conocimiento para CASEA', help='Areas de Conocimiento para la Certificación y Acreditación de Saberes Empíricos y Académicos'),
        'pis_participado': fields.one2many('for.pis.participacion_pis', 'sujeto_id', 'En cuántas Formaciones ha participado', help='Relación de las Formaciones en los cuales ha participado'),
        'frecuencia_colectivos_aprendizaje_id': fields.many2one('for.pis.frecuencias_participacion', 'Participación Colectivo Participantes', help='Frecuencia de Participación en el Colectivo de Participantes'),
        'frecuencia_matriz_planificacion_id': fields.many2one('for.pis.frecuencias_participacion', 'Participación Matriz de Planificación', help='Frecuencia de Participación en la Matriz de Planificación del Proceso Formativo, Colectivo, Integral'),
        'frecuencia_cuaderno_sistematizacion_id': fields.many2one('for.pis.frecuencias_participacion', 'Registra en el cuaderno de Sistematización', help='Frecuencia con la cual registra en el Cuaderno de Sistematización de Experiencias'),
        'frecuencia_intercambio_saberes_id': fields.many2one('for.pis.frecuencias_participacion', 'Realiza intercambio de saberes', help='Realiza intercambio de sabes con los Participantes para socializar los registros de los cuadernos'),
        'frecuencia_encuentros_socializacion_id': fields.many2one('for.pis.frecuencias_participacion', 'Participa en encuentros', help='¿Ha participado en encuentros o socialización de saberes con otras Formaciones?'),
        'intereses_formativos_ids': fields.one2many('for.pis.intereses_formativos', 'sujeto_id', 'Intereses Formativos', help='Intereses formativos del Participante'),
        'tecnologias_ids': fields.one2many('for.pis.tecnologias_utilizadas', 'sujeto_id', 'Tecnologías (TIC) que utiliza', help='Tecnologías de Información y Comunicación que utiliza'),
        'frecuencia_fase_I': fields.many2one('for.pis.frecuencias_participacion', 'Participación Fase I', help='Frecuencia con la que participa en la construcción del trabajo en la Formación. Fase I'),
        'frecuencia_fase_II': fields.many2one('for.pis.frecuencias_participacion', 'Participación Fase II', help='Frecuencia con la que participa en la construcción del trabajo PIS. Fase II'),
        'frecuencia_fase_III': fields.many2one('for.pis.frecuencias_participacion', 'Participación Fase III', help='Frecuencia con la que participa en la construcción del trabajo PIS. Fase III'),
        'observaciones': fields.text('Observaciones', help='Observaciones'),
    }
    def validar_numero(self, cr, uid, ids):
        for rec in self.browse(cr, uid, ids):
            digito = rec.cedula
            if re.match("^[0-9]*$", digito):
                return True
        return False

    _constraints = [(validar_numero, 'La cedula solo puede contener numeros', ['cedula'])]
    _sql_constraints = [('cedula_uniq', 'unique(cedula)', 'Este participante ya ha sido cargado (cedula repetida)')]

  
##################################################################################################################################################################            
###             Ejecución del conteo de participantes en una formacion, por medio de los metodos ORM, haciendo uso de campos function                          #####
###        En la Clase 'for.pis.registro_inicial' existe un campo function, que permite contar la cantidad de participantes relacionados a sí misma en la tabla #####
###        'for_pis_participacion_pis'. Un campo function se ejecuta cada vez que los Métodos ORM 'create' o 'write' es instanciado sobre el modelo donde se    #####
###        encuentra. Por lo cual a través de la función que sigue a continuación solo se ejecuta el método write en registro inicial cuando un participante      #####
###        es creado o editado.                                                                                                                                  #####
##################################################################################################################################################################
    def create(self, cr, uid, vals, context=None):
        new_id = super(for_pis_sujetos_aprendizaje, self).create(cr, uid, vals, context=None)
        res={}
        if 'pis_participado' in vals:
            for registro_formacion in vals['pis_participado']:
                if registro_formacion[0]==0:
                    id_formacion=registro_formacion[2]['numero_id']
                    self.pool.get('for.pis.registro_inicial').write(cr, 1, id_formacion, res)                    
        return new_id

    def write(self, cr, uid, ids, vals, context=None):
        res={}
        id_formacion=[]
        if 'pis_participado' in vals:
            for registro_formacion in vals['pis_participado']:
                if registro_formacion[0]==0:
                    id_formacion.append(registro_formacion[2]['numero_id'])
                elif registro_formacion[0]==2 or registro_formacion[0]==1:
                    id_formacion.append(self.pool.get('for.pis.participacion_pis').browse(cr, uid, registro_formacion[1], context).numero_id.id)
        new_id = super(for_pis_sujetos_aprendizaje, self).write(cr, uid, ids, vals, context=None)
        self.pool.get('for.pis.registro_inicial').write(cr, 1, id_formacion, res)
        return new_id



    def name_get(self, cr, uid, ids, context={}):
        if not len(ids):
            return []
        
        res=[]
        for participante in self.browse(cr, uid, ids,context=context):
            res.append((participante.id, participante.cedula +' - '+ participante.nombres + ' ' + participante.apellidos))    
        return res


    def onchange_calcular_edad(self, cr, uid, ids, fecha, context=None):
        born = datetime.strptime(fecha, '%Y-%m-%d')
        today = date.today()
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        v = {'value':{}}
        v['value']['edad'] = age
        return v

    def on_change_limpiar_campo(self, cr, uid, ids, *args):
        v = {'value':{}}
        for campo in args:
            v['value'][campo] = ''
        return v


#    def unlink(self, cr, uid, ids, context=None):
#        cr.execute()    
#        return super(for_pis_sujetos_aprendizaje, self).unlink(cr, uid, ids, context=None)

for_pis_sujetos_aprendizaje()

##########################################################################################################################################################################3
##########################################################################################################################################################################3
############################herencia de formacion_pis_base##################################################################################################################3
class for_pis_registro_inicial_extended(osv.osv):
    """Registro Inicial de Formaciones"""
    _name = 'for.pis.registro_inicial'
    #_rec_name = 'denominacion_pis'
    _inherit= 'for.pis.registro_inicial'
    _columns = {
        'participacion_pis_ids': fields.one2many('for.pis.participacion_pis', 'numero_id', 'Participantes', help='Participantes de la Formación'),
    }

for_pis_registro_inicial_extended()
##########################################################################################################################################################################3
##########################################################################################################################################################################3

class for_pis_estados_civiles(osv.osv):
    """Tabla de Referencia de Estados Civiles"""
    _name = 'for.pis.estados_civiles'
    _rec_name = 'estado_civil'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación del Estado Civíl'),
        'estado_civil': fields.char('Estado Civil', size=30, required=True, help='Nombre del Estado Civíl'),
    }
for_pis_estados_civiles()

class for_pis_tipos_comunidades(osv.osv):
    """Tabla Referencial de Tipos de Comunidades"""
    _name = 'for.pis.tipos_comunidades'
    _rec_name = 'tipos_comunidades'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación de Tipos de Comunicaciones'),
        'tipos_comunidades': fields.char('Tipos de Comunidades', size=30, required=True, help='Nombre del Tipo de Comunidad'),
    }
for_pis_tipos_comunidades()

class for_pis_parentescos(osv.osv):
    """Tabla Referencial de Parentescos"""
    _name = 'for.pis.parentescos'
    _rec_name = 'parentesco'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación de Parentescos'),
        'parentesco': fields.char('Parentesco', size=30, required=True, help='Nombre del Parentesco'),
    }
for_pis_parentescos()

class for_pis_generos(osv.osv):
    """Tabla de Referencia de Géneros"""
    _name = 'for.pis.generos'
    _rec_name = 'genero'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación de Géneros'),
        'genero': fields.char('Género', size=30, required=True, help='Nombre del Género'),
    }
for_pis_generos()

class for_pis_rangos_edades(osv.osv):
    """Tabla Referencial de Rangos de Edades"""
    _name = 'for.pis.rangos_edades'
    _rec_name = 'grupo_rango'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación del Rango de Edades'),
        'grupo_rango': fields.char('Rango de Edades', size=3, required=True, help='Nombre del Grupo (Rango de Edades)'),
        'edad_desde': fields.integer('Edad desde', required=True, help='Valor límite mínimo del rango de edad'),
        'edad_hasta': fields.integer('Edad hasta', required=True, help='Valor límite máximo del rango de edad'),
    }
for_pis_rangos_edades()

class for_pis_categorias_discapacidades(osv.osv):
    """Tabla de Referencia de Categorías de Discapacidades"""
    _name = 'for.pis.categorias_discapacidades'
    _rec_name = 'categoria_discapacidad'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación de la Categoría de Discapacidad'),
        'categoria_discapacidad': fields.char('Discapacidad', size=30, required=True, help='Tabla de Referencia de Discapacidades'),
    }
for_pis_categorias_discapacidades()

class for_pis_tipos_redes_sociales(osv.osv):
    """Tabla de Referencia de los Tipos de Redes Sociales"""
    _name = 'for.pis.tipos_redes_sociales'
    _rec_name = 'red_social'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación de la Red Social'),
        'red_social': fields.char('Red Social', size=30,required=True, help='Nombre de la Red Social'),
        'tipo_red': fields.char('Tipo', size=30, required=True, help='Nombre del Tipo de Red Social (Blog, Microblog, Foro, Lista, otro)'),
    }
for_pis_tipos_redes_sociales()

class for_pis_nacionalidades(osv.osv):
    """Tabla Referencial de Nacionalidades"""
    _name = 'for.pis.nacionalidades'
    _rec_name = 'nacionalidad'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación de Nacionalidades'),
        'nacionalidad': fields.char('Nacionalidad', size=30, required=True, help='Nombre de la Nacionalidad'),
    }
for_pis_nacionalidades()

class for_pis_deportes(osv.osv):
    """Tabla Referencial de Deportes"""
    _name = 'for.pis.deportes'
    _rec_name = 'deporte'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación del Deporte'),
        'deporte': fields.char('Deporte', size=30, required=True, help='Nombre del Deporte'),
    }
for_pis_deportes()

class for_pis_organizaciones(osv.osv):
    """Tabla Referencial de Organizaciones Políticas y Sociales"""
    _name = 'for.pis.organizaciones'
    _rec_name = 'organizacion'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación de la Organización Social o Política'),
        'organizacion': fields.char('Organización', size=120, required=True, help='Nombre de la Organización Social o Política'),
    }
for_pis_organizaciones()

class for_pis_carreras_universitarias(osv.osv):
    """Tabla Referencial de Carreras Universitarias"""
    _name = 'for.pis.carreras_universitarias'
    _rec_name = 'carrera_universitaria'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación de la Carrera Universitaria'),
        'carrera_universitaria': fields.char('Carrera Universitaria', size=60, required=True, help='Nombre de la Carrera Universitaria'),
    }
for_pis_carreras_universitarias()

class for_pis_actividades_culturales(osv.osv):
    """Tabla Referencial de Actividades Culturales"""
    _name = 'for.pis.actividades_culturales'
    _rec_name = 'actividad_cultural'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación de la Actividad Cultural'),
        'actividad_cultural': fields.char('Actividad Cultural', size=60, required=True, help='Nombre de la Actividad Cultural'),
    }
for_pis_actividades_culturales()

class for_pis_niveles_academicos(osv.osv):
    """Tabla Referencial de Niveles de Educativos"""
    _name = 'for.pis.niveles_academicos'
    _rec_name = 'nivel_educativo'
    _columns = {
        'codigo': fields.char('Código', size=30, required=True, help='Código de Identificación del Nivel Educativo'),
        'nivel_educativo': fields.char('Nivel Educativo', size=30, required=True, help='Nombre del Nivel Educativo'),
    }
for_pis_niveles_academicos()

class for_pis_areas_conocimientos(osv.osv):
    """Tabla Referencial de Areas de Conocimiento"""
    _name = 'for.pis.areas_conocimientos'
    _rec_name = 'area_conocimiento'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación del Area de Conocimiento'),
        'area_conocimiento': fields.char('Area de Conocimiento', size=60, required=True, help='Nombre del Area de Conocimiento'),
    }
for_pis_areas_conocimientos()

class for_pis_oficios(osv.osv):
    """Tabla de Referencia de Oficios"""
    _name = 'for.pis.oficios'
    _rec_name = 'oficio'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación del Oficio'),
        'oficio': fields.char('Oficio', size=60, required=True, help='Nombre del Oficio'),
    }
for_pis_oficios()

class for_pis_especialidades(osv.osv):
    """Tabla de Referencia de Especialidades"""
    _name = 'for.pis.especialidades'
    _rec_name = 'especialidad'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación de la Especialidad'),
        'especialidad': fields.char('Especialidad', size=60, required=True, help='Nombre de la Especialidad'),
    }
for_pis_especialidades()

class for_pis_misiones(osv.osv):
    """Tabla Referencial de Misiones"""
    _name = 'for.pis.misiones'
    _rec_name = 'mision'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación de la Misión'),
        'mision': fields.char('Mision', size=120, required=True, help='Nombre de la Mision Social'),
    }
for_pis_misiones()

class for_pis_frecuencias_participacion(osv.osv):
    """Tabla Referencial de Frecuencias de Participación"""
    _name = 'for.pis.frecuencias_participacion'
    _rec_name = 'frecuencia_participacion'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación de la Frecuencia de Participación'),
        'frecuencia_participacion': fields.char('Frecuencia de Participación', size=30, required=True, help='Nombre de la Frecuencia de Participación'),
    }
for_pis_frecuencias_participacion()

class for_pis_pueblos_indigenas(osv.osv):
    """Tabla de Referencia de Pueblos Indígenas"""
    _name = 'for.pis.pueblos_indigenas'
    _rec_name = 'pueblo_indigena'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación del Pueblo Indígena'),
        'pueblo_indigena': fields.char('Pueblo Indígena', size=30, required=True, help='Nombre del Pueblo Indígena'),
    }
for_pis_pueblos_indigenas()

class for_pis_familiares(osv.osv):
    """Registro Maestro de Familiares de los Participantes y/o Formadores"""
    _name = 'for.pis.familiares'
    _rec_name = 'apellidos'
    _columns = {
        'sujeto_id': fields.many2one('for.pis.sujetos_aprendizaje', 'Participante', help='Participante que guarda parentesco con el familiar'),
        'cedula': fields.char('Nº Cédula de Identidad', size=12, required=False, help='Numero de la Cédula de Identidad'),
        'nombres': fields.char('1º y 2º Nombres', size=120, required=True, help='Nombres del Familiar'),
        'apellidos': fields.char('1º y 2º Apellidos', size=120, required=True, help='Apellidos del Familiar'),
        'fecha_nacimiento': fields.date('Fecha Nacimiento', help='Fecha de Nacimiento del Familiar'),
        'genero_id': fields.many2one('for.pis.generos', 'Genero', help='Género del Familiar'),
        'parentesco_id': fields.many2one('for.pis.parentescos', 'Parentesco', help='Parentesco con el Participante o Formador'),
        'discapacidad_id': fields.many2one('for.pis.categorias_discapacidades', 'Discapacidad', help='Si el familiar tiene una discapacidad, indique cual'),
        'estado_civil_id': fields.many2one('for.pis.estados_civiles', 'Estado Civil', help='Estado Civíl del Familiar'),
    }
for_pis_familiares()

class for_pis_redes_sociales(osv.osv):
    """Registro Maestro de Redes Sociales a las que estan suscritos los Participantes y los Formadores"""
    _name = 'for.pis.redes_sociales'
    _rec_name = 'cuenta'
    _columns = {
        'sujeto_id': fields.many2one('for.pis.sujetos_aprendizaje', 'Participante', help='Participante que usa la referida Red Social'),
        'tipo_red_social_id': fields.many2one('for.pis.tipos_redes_sociales', 'Tipo de Red Social', help='Nombre de la Red Social a la que esta suscrito el Sujeto de Aprendizaje o el Formador'),
        'cuenta': fields.char('Cuenta', size=60, required=True, help='Nombre de usuario, dirección u otro dato de identificación de la cuenta'),
    }
for_pis_redes_sociales()

class for_pis_deportes_practicados(osv.osv):
    """Registro Maestro de Deportes Practicados"""
    _name = 'for.pis.deportes_practicados'
    _rec_name = 'deporte_id'
    _columns = {
        'sujeto_id': fields.many2one('for.pis.sujetos_aprendizaje', 'Participante', help='Participante que practica el referido deporte'),
        'deporte_id': fields.many2one('for.pis.deportes', 'Deporte', help='Deporte que practica'),
        'desde': fields.datetime('Desde', required=False, help='Fecha desde la cual practica el deporte referido'),
    }
for_pis_deportes_practicados()

class for_pis_actividades_practicadas(osv.osv):
    """Registro Maestro de Actividades Culturales Practicadas"""
    _name = 'for.pis.actividades_practicadas'
    _rec_name = 'actividad_cultural_id'
    _columns = {
        'sujeto_id': fields.many2one('for.pis.sujetos_aprendizaje', 'Participante', help='Participante que realiza la actividad cultural'),
        'actividad_cultural_id': fields.many2one('for.pis.actividades_culturales', 'Actividad Cultural', help='Actividad Cultural que practica'),
        'desde': fields.datetime('Desde', required=False, help='Fecha desde la cual practica la referida Actividad Cultural'),
    }
for_pis_actividades_practicadas()

class for_pis_organizaciones_milita(osv.osv):
    """Registro Maestro de Organizaciones Socio-Políticas donde militan los Participantes y Formadores"""
    _name = 'for.pis.organizaciones_milita'
    _rec_name = 'organizacion_id'
    _columns = {
        'sujeto_id': fields.many2one('for.pis.sujetos_aprendizaje', 'Participante', help='Participante que milita en la referida Organización Social o Política'),
        'organizacion_id': fields.many2one('for.pis.organizaciones', 'Organización Social o Política', help='Organización Social o Política donde milita el Participante o Formador'),
        'desde': fields.datetime('Desde', required=False, help='Fecha desde la cual el Participante o Formador participa o milita en la referida Organización Social o Política'),
    }
for_pis_organizaciones_milita()

class for_pis_misiones_pertenece(osv.osv):
    """Registro Maestro de Misiones Sociales a las que pertenecen los Participantes y Formador"""
    _name = 'for.pis.misiones_pertenece'
    _rec_name = 'mision_id'
    _columns = {
        'sujeto_id': fields.many2one('for.pis.sujetos_aprendizaje', 'Participante', help='Participante que participa en la referida Misión Social'),
        'mision_id': fields.many2one('for.pis.misiones', 'Misión Social', help='Misión Social'),
        'desde': fields.datetime('Desde', required=False, help='Fecha desde la cual pertenece a la referida Misión Social'),
    }
for_pis_misiones_pertenece()

class for_pis_formacion_academica(osv.osv):
    """Registro Maestro de Formación Académica"""
    _name = 'for.pis.formacion_academica'
    _rec_name = 'nivel_educativo_id'
    _columns = {
        'sujeto_id': fields.many2one('for.pis.sujetos_aprendizaje', 'Participante', help='Participante que registra el grado o nivel de formación académica referida'),
        'nivel_educativo_id': fields.many2one('for.pis.niveles_academicos', 'Nivel Educativo', help='Nivel Educativo'),
        'estatus_educativo_id': fields.many2one('for.pis.estatus_niveles_educativos', 'Estado', help='Estado de Avance del Nivel Educativo (C=Culmino, I=No completo, P=En Progreso)'),
    }
for_pis_formacion_academica()

class for_pis_tecnologias_tic(osv.osv):
    """Tabla Referencial de Tecnologías de Información y Comunicación"""
    _name = 'for.pis.tecnologias_tic'
    _rec_name = 'tecnologia'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación de la Tecnología de Información y Comunicación'),
        'tecnologia': fields.char('Tecnología (TIC)', size=60, required=True, help='Nombre de la Tecnología de Información y Comunicación'),
    }
for_pis_tecnologias_tic()

class for_pis_intereses_formativos(osv.osv):
    """Registro Maestro de Intereses y Necesidades Formativas"""
    _name = 'for.pis.intereses_formativos'
    _rec_name = 'requirimiento'
    _columns = {
        'sujeto_id': fields.many2one('for.pis.sujetos_aprendizaje', 'Participante', help='Participante que muestra los intereses formativos indicados'),
        'sector_economico_id': fields.many2one('for.pis.sectores_economicos', 'Sector Económico', help='Sector Económico'),
        'area_economica_id': fields.many2one('for.pis.areas_economicas', 'Area Económica', help='Area Económica'),
        'requerimiento': fields.char('Requerimiento', size=300, required=False, help='Requerimiento o Necesidad de Formación'),
    }
for_pis_intereses_formativos()

class for_pis_tecnologias_utilizadas(osv.osv):
    """Registro Maestro de Tecnologías de Información y Comunicación utilizadas por Formadores y Participantes"""
    _name = 'for.pis.tecnologias_utilizadas'
    _rec_name = 'tecnologia'
    _columns = {
        'sujeto_id': fields.many2one('for.pis.sujetos_aprendizaje', 'Participante', help='Participante que usa la tencología TIC referida'),
        'tecnologia': fields.many2one('for.pis.tecnologias_tic', 'Tecnología', help='Tecnología de Información y Comunicación que utiliza'),
    }
for_pis_tecnologias_utilizadas()

class for_pis_participacion_pis(osv.osv):
    """Registro Maestro de Participación en Formaciones"""
    _name = 'for.pis.participacion_pis'
    _rec_name = 'numero_id'
    _columns = {
        'sujeto_id': fields.many2one('for.pis.sujetos_aprendizaje', 'Participante', onupdate='cascade', ondelete='cascade', help='Participante que participa la formación referida'),
        'numero_id': fields.many2one('for.pis.registro_inicial', 'Formación donde participa', onupdate='cascade', ondelete='cascade', help='Formación donde participa o ha participado'),
        'estatus': fields.selection([('proceso', 'En proceso'),('retirado', 'Retirado'),('egresado', 'Egresado')], 'Estatus', help='Estatus del participante en la formación'),
        'dependencia_formacion': fields.related('numero_id', 'dependencia_id', type='many2one', relation='for.dependencias', string='Dependencia', store=True, help='Dependencia de donde se registra la formacion'),
        'motores_economicos_id': fields.related('numero_id', 'motores_economicos_id', type='many2one', relation='for.pis.motores_economicos', string='Motor', store=True, help='Motor economico de donde se registra la formacion'),
        'cfs_id': fields.related('numero_id', 'cfs_id', type='many2one', relation='for.pis.cfs', string='C.F.S.', store=True, help='C.F.S. donde se da la formacion'),
    }

    _sql_constraints = [('participante_en_formacion_uniq', 'unique(sujeto_id,numero_id)', 'Este participante ya pertenece a esta formacion')]


    def unlink(self, cr, uid, ids, context=None):
        id_formacion=[]
        res={}
        for participacion in ids:
            obj_participacion=self.browse(cr, uid, ids, context)
            id_formacion.append(obj_participacion[0].numero_id.id)
        validate=super(for_pis_participacion_pis, self).unlink(cr, uid, ids, context=None)
        for formaciones in id_formacion:
            id_reg=self.pool.get('for.pis.registro_inicial').write(cr, 1, formaciones, res, context=None)
        return validate
for_pis_participacion_pis()

class for_pis_experiencias_empiricas(osv.osv):
    """Registro Maestro de Experiencias Empíricas"""
    _name = 'for.pis.experiencias_empiricas'
    _rec_name = 'area_conocimiento_id'
    _columns = {
        'sujeto_id': fields.many2one('for.pis.sujetos_aprendizaje', 'Participante', help='Participante que registra la Experiencia Empírica referida'),
        'area_conocimiento_id': fields.many2one('for.pis.areas_conocimientos', 'Area de Conocimiento', help='Area(s) de Conocimiento(s)'),
        'tiempo_experiencias': fields.integer('Tiempo (meses)', required=True, help='Tiempo de Experiencia (expresado en Meses)'),
        'portafolio_evidencias': fields.boolean('¿Portafolio de Evidencias?', help='Portafolio de Evidencias'),
        'protafolio_enlace': fields.char('Enlace', size=120, required=False, help='Enlace (Ruta/URL) al portafolio de evidencias'),
    }
for_pis_experiencias_empiricas()

class for_pis_experiencias_docentes(osv.osv):
    """Registro Maestro de Experiencias Docentes"""
    _name = 'for.pis.experiencias_docentes'
    _rec_name = 'area_conocimiento_id'
    _columns = {
        'sujeto_id': fields.many2one('for.pis.sujetos_aprendizaje', 'Participante', help='Participante que registra la Experiencia Docente referida'),
        'entidad_educativa': fields.char('Institución Educativa', size=120, required=True, help='Institución Educativa donde laboró'),
        'tiempo_experiencia': fields.integer('Tiempo (meses)', required=True, help='Tiempo de Experiencia Docente en la referida institución educativa (en Meses)'),
        'area_conocimiento_id': fields.many2one('for.pis.areas_conocimientos', 'Area de Conocimiento', help='Area(s) de Conocimiento'),
    }
for_pis_experiencias_docentes()

class for_pis_experiencias_laborales(osv.osv):
    """Registro Maestro de Experiencias Laborales"""
    _name = 'for.pis.experiencias_laborales'
    _rec_name = 'profesion_ocupacion_id'
    _columns = {
        'sujeto_id': fields.many2one('for.pis.sujetos_aprendizaje', 'Participante', help='Participante que registra las Experiencas Laborales referidas'),
        'profesion_ocupacion_id': fields.many2one('for.pis.profesiones_ocupaciones', 'Profesión u Ocupación', help='Profesión u Ocupación'),
        'tiempo_experiencia': fields.integer('Tiempo (Meses)', required=True, help='Tiempo total de experiencia (expresada en Meses)'),
        'lugar': fields.char('Lugar', size=120, required=True, help='Lugar (Empresa, Unidad Productiva, Organización o Institución) donde trabajó'),
    }
for_pis_experiencias_laborales()

class for_pis_casea_conocimientos(osv.osv):
    """Registro Maestro de Conocimientos para Certificación y Acreditación de Saberes Empíricos y Académicos"""
    _name = 'for.pis.casea_conocimientos'
    _rec_name = 'area_conocimiento_id'
    _columns = {
        'sujeto_id': fields.many2one('for.pis.sujetos_aprendizaje', 'Participante', help='Participante que desea cetrificar o acreditar el conocimiento'),
        'area_conocimiento_id': fields.many2one('for.pis.areas_conocimientos', 'Area de Conocimiento', help='Area de Conocimiento en la que desea obtener Certificación o Acreditación'),
        'tiempo_experiencia': fields.integer('Tiempo Experiencia', required=True, help='Tiempo de Experiencia en el conocimiento que desea acreditar o certificar'),
        'donde': fields.char('Indique dónde', size=120, required=True, help='Dónde desarrolló el conocimiento o experiencia que desea certificar o acreditar'),
        'portafolio_evidencias': fields.boolean('Portafolio de Evidencias', help=' Portafolio de Evidencias '),
        'portafolio_enlace': fields.char('Enlace', size=120, required=False, help='Enlace al Portafolio de Evidencias'),
    }
for_pis_casea_conocimientos()

class for_pis_profesiones_ocupaciones(osv.osv):
    """Tabla Referencial de Profesiones u Ocupaciones"""
    _name = 'for.pis.profesiones_ocupaciones'
    _rec_name = 'nombre'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación de la Profesión'),
        'nombre': fields.char('Profesión u Ocupación', size=120, required=True, help='Profesión u Ocupación'),
    }
for_pis_profesiones_ocupaciones()

class for_pis_estatus_niveles_educativos(osv.osv):
    """Tabla Referencial de Estados de Avance de los Niveles Educativos"""
    _name = 'for.pis.estatus_niveles_educativos'
    _rec_name = 'estatus'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación del Estatus de Avance del Nivel Educativo'),
        'estatus': fields.char('Descripción', size=120, required=True, help='Descripcion del Estatus de Avance del Nivel Educativo'),
    }
for_pis_estatus_niveles_educativos()

class for_pis_discapacidades(osv.osv):
    """Registro Maestro de Discapacidades de los Participantes y Formadores"""
    _name = 'for.pis.discapacidades'
    _rec_name = 'categoria_discapacidad_id'
    _columns = {
        'sujeto_id': fields.many2one('for.pis.sujetos_aprendizaje', 'Participante', help='Participante que presenta la discapacidad'),
        'categoria_discapacidad_id': fields.many2one('for.pis.categorias_discapacidades', 'Discapacidad', help='Discapacidad que presenta el Participante'),
        'observaciones': fields.text('Observaciones', size=300, required=False, help='Comentarios adicionales respecto a la discapacidad presentada por el Participante'),
    }
for_pis_discapacidades()

class for_pis_condiciones_laborales(osv.osv):
    """Tabla Referencial de Condiciones Laborales"""
    _name = 'for.pis.condiciones_laborales'
    _rec_name = 'condicion_laboral'
    _columns = {
        'codigo': fields.char('Código', size=3, required=False, help='Código de Identificación de la Condición Laboral'),
        'condicion_laboral': fields.char('Condición Laboral', size=120, required=True, help='Nombre o Descripción de la Condición Laboral'),
    }
for_pis_condiciones_laborales()
