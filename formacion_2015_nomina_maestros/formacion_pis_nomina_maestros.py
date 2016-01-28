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


class for_pis_mae_asistencias(osv.osv):
    """Registro de Asistencias de los Facilitadores a las Formaciones"""
    _name = 'for.pis.mae_asistencias'
    #_rec_name = 'maestro_id'

    def _total_horas_asistencia(self, cr, uid, ids, nombre_campo, arg, context):
    	res = {}
    	for asistencia in self.browse(cr, uid, ids):
    		res[asistencia.id] = asistencia.horas_lunes + asistencia.horas_martes + asistencia.horas_miercoles + asistencia.horas_jueves + asistencia.horas_viernes + asistencia.horas_sabado + asistencia.horas_domingo
    	return res
    	
    _columns = {
    	'total_horas': fields.function(_total_horas_asistencia, method=True, type='integer', string='Total Horas', store=False),
        'anio_vigencia': fields.char('anio de vigencia', size=4),
################################################################################################################################################
####################estos campos son declarados en una extencion de herencia en formacion_pis_indagacion_maestros###############################
        #'maestro_id': fields.many2one('for.pis.maestros','Facilitador', help='Facilitador con el que guarda parentesco el familiar'),
        #'cedula': fields.related('maestro_id', 'cedula', type='char', relation='for.pis.maestros', string='Cédula', store=False),
        #'nombres': fields.related('maestro_id', 'nombres', type='char', relation='for.pis.maestros', string='Nombres', store=False),
        #'apellidos': fields.related('maestro_id', 'apellidos', type='char', relation='for.pis.maestros', string='Apellidos', store=False),
##################################################################################################################################################
##################################################################################################################################################
################################################################################################################################################
####################estos campos son declarados en una extencion de herencia en formacion_2015_nomina_consolidado###############################
#		'detalle_consolidado_id':fields.many2one('for.pis.mae_consolidado_detalle', 'Consolidado'),
##################################################################################################################################################
##################################################################################################################################################


        'dependencia_id': fields.many2one('for.dependencias', 'Dependencia'),
        'numero_id': fields.many2one('for.pis.registro_inicial','Formación donde participa', help='Formación donde participa o ha participado'),
        'calendario_id' : fields.many2one('for.pis.calendario', 'Semana Nro', help="Número de la Semana en la que trabajó el Facilitador"),
        'semana_desde': fields.related('calendario_id', 'inicio_semana', type='date', relation='for.pis.calendario', help='Fecha de inicio de la Semana', store=True, string="Desde"),
        'semana_hasta': fields.related('calendario_id', 'final_semana', type='date', relation='for.pis.calendario', help='Fecha de inicio de la Semana', store=True, string="Hasta"),
        
        'horas_lunes': fields.integer('Horas Lunes', size=2,  help='Total de horas trabajadas por el Facilitador el día lunes de la semana y Formaciones indicadas'),
        'motivo_falta_lunes_id': fields.many2one('for.pis.mae_motivos_falta', 'Motivo Falta Lunes', help='Motivo de Falta el día lunes'),
        'observaciones_lunes': fields.char('Observaciones', size=200,  help='Comentarios adicionales sobre novedades de asistencia el día lunes'),
        'lunes_laborable': fields.boolean('¿Lunes Laborable?'),
        
        'horas_martes': fields.integer('Horas Martes', size=2,  help='Total de horas trabajadas por el Facilitador el día martes de la semana y Formaciones indicadas'),
        'motivo_falta_martes_id': fields.many2one('for.pis.mae_motivos_falta', 'Motivo Falta Martes', help='Motivo de Falta el día martes'),
        'observaciones_martes': fields.char('Observaciones', size=200,  help='Comentarios adicionales sobre novedades de asistencia el día martes'),
        'martes_laborable': fields.boolean('¿Martes Laborable?'),        
                
        'horas_miercoles': fields.integer('Horas Miercoles', size=2,  help='Total de horas trabajadas por el Facilitador el día miercoles de la semana y Formaciones indicadas'),
        'motivo_falta_miercoles_id': fields.many2one('for.pis.mae_motivos_falta', 'Motivo Falta Miercoles', help='Motivo de Falta el día miercoles'),
        'observaciones_miercoles': fields.char('Observaciones', size=200,  help='Comentarios adicionales sobre novedades de asistencia el día miercoles'),
        'miercoles_laborable': fields.boolean('¿Miércoles Laborable?'),
        
        'horas_jueves': fields.integer('Horas Jueves', size=2,  help='Total de horas trabajadas por el Facilitador el día jueves de la semana y Formaciones indicadas'),
        'motivo_falta_jueves_id': fields.many2one('for.pis.mae_motivos_falta', 'Motivo Falta Jueves', help='Motivo de Falta el día jueves'),
        'observaciones_jueves': fields.char('Observaciones', size=200,  help='Comentarios adicionales sobre novedades de asistencia el día jueves'),
        'jueves_laborable': fields.boolean('¿Jueves Laborable?'),
        
        'horas_viernes': fields.integer('Horas Viernes', size=2,  help='Total de horas trabajadas por el Facilitador el día viernes de la semana y Formaciones indicadas'),
        'motivo_falta_viernes_id': fields.many2one('for.pis.mae_motivos_falta', 'Motivo Falta Viernes', help='Motivo de Falta el día viernes'),
        'observaciones_viernes': fields.char('Observaciones', size=200,  help='Comentarios adicionales sobre novedades de asistencia el día viernes'),
        'viernes_laborable': fields.boolean('¿Viernes Laborable?'),

        'horas_sabado': fields.integer('Horas Sabado', size=2,  help='Total de horas trabajadas por el Facilitador el día sabado de la semana y Formaciones indicadas'),
        'motivo_falta_sabado_id': fields.many2one('for.pis.mae_motivos_falta', 'Motivo Falta Sabado', help='Motivo de Falta el día sabado'),
        'observaciones_sabado': fields.char('Observaciones', size=200,  help='Comentarios adicionales sobre novedades de asistencia el día sabado'),
        'sabado_laborable': fields.boolean('¿Sábado Laborable?'),
        
        'horas_domingo': fields.integer('Horas Domingo', size=2,  help='Total de horas trabajadas por el Facilitador el día domingo de la semana y Formaciones indicadas'),
        'motivo_falta_domingo_id': fields.many2one('for.pis.mae_motivos_falta', 'Motivo Falta Domingo', help='Motivo de Falta el día domingo'),
        'observaciones_domingo': fields.char('Observaciones', size=200,  help='Comentarios adicionales sobre novedades de asistencia el día domingo'),
        'domingo_laborable': fields.boolean('¿Domingo Laborable?'),

        'state': fields.selection([('pagado','Pagado'),('no pagado','No Pagado')], 'Estatus', help='Estatus de Pagado o No Pagado en la asistencia'),

	}
    #_sql_constraints = [('asistencia_uniq', 'unique(numero_id,calendario_id,maestro_id)', 'Esta asistencia ya ha sido cargada. Formador, formacion y semana repetida')]
    _defaults = {'anio_vigencia': date.today().year, 'state': 'no pagado', 'horas_lunes':0, 'horas_martes':0, 'horas_miercoles':0, 'horas_jueves':0, 'horas_viernes':0, 'horas_sabado':0, 'horas_domingo':0}
    
    def on_change_limpiar_campo(self, cr, uid, ids, *args):
        v = {'value':{}}
        for campo in args:
            v['value'][campo] = ''
        return v

    def copy(self, cr, uid, id, default=None, context=None):
        raise osv.except_osv(('Prohibido duplicar'), ('No es posible duplicar el registro , por favor cree uno nuevo.'))

    def onchange_max_horas_lunes(self, cr, uid, ids, horas, context=None):
        if (horas > 5):
		    val = {'horas_lunes' : 5}
		    return {'value': val}
    
    def onchange_max_horas_martes(self, cr, uid, ids, horas, context=None):
        if (horas > 5):
		    val = {'horas_martes' : 5}
		    return {'value': val}

    def onchange_max_horas_miercoles(self, cr, uid, ids, horas, context=None):
        if (horas > 5):
		    val = {'horas_miercoles' : 5}
		    return {'value': val}

    def onchange_max_horas_jueves(self, cr, uid, ids, horas, context=None):
        if (horas > 5):
		    val = {'horas_jueves' : 5}
		    return {'value': val}

    def onchange_max_horas_viernes(self, cr, uid, ids, horas, context=None):
        if (horas > 5):
		    val = {'horas_viernes' : 5}
		    return {'value': val}

    def onchange_max_horas_sabado(self, cr, uid, ids, horas, context=None):
        if (horas > 5):
		    val = {'horas_sabado' : 5}
		    return {'value': val}

    def onchange_max_horas_domingo(self, cr, uid, ids, horas, context=None):
        if (horas > 5):
		    val = {'horas_domingo' : 5}
		    return {'value': val}
            
    def on_change_calendario_id(self, cr, uid, ids, calendario_id):
        
        v={}
        if calendario_id:


            calendario_obj=self.pool.get('for.pis.calendario').browse(cr, uid, calendario_id)
            

            v['horas_lunes']=0
            v['horas_martes']=0
            v['horas_miercoles']=0
            v['horas_jueves']=0
            v['horas_viernes']=0
            v['horas_sabado']=0
            v['horas_domingo']=0
            v['observaciones_lunes']=''
            v['observaciones_martes']=''
            v['observaciones_miercoles']=''
            v['observaciones_jueves']=''
            v['observaciones_viernes']=''
            v['observaciones_sabado']=''
            v['observaciones_domingo']=''
            v['motivo_falta_lunes_id']=None
            v['motivo_falta_martes_id']=None
            v['motivo_falta_miercoles_id']=None
            v['motivo_falta_jueves_id']=None
            v['motivo_falta_viernes_id']=None
            v['motivo_falta_sabado_id']=None
            v['motivo_falta_domingo_id']=None

            v['lunes_laborable']=calendario_obj.lunes
            v['martes_laborable']=calendario_obj.martes
            v['miercoles_laborable']=calendario_obj.miercoles
            v['jueves_laborable']=calendario_obj.jueves
            v['viernes_laborable']=calendario_obj.viernes
            v['sabado_laborable']=calendario_obj.sabado
            v['domingo_laborable']=calendario_obj.domingo
            v['semana_desde']=calendario_obj.inicio_semana
            v['semana_hasta']=calendario_obj.final_semana
        return {'value':v}



    def horas_limitadas(self, cr, uid, ids):
        dias=('horas_lunes', 'horas_martes', 'horas_miercoles', 'horas_jueves', 'horas_viernes', 'horas_sabado', 'horas_domingo')
        suma_horas=0
        for asistencia in self.browse(cr, uid, ids):
            for dia in dias:
                suma_horas += asistencia[dia]
        if suma_horas>25:
                return False
        return True
    _constraints = [(horas_limitadas, 'La asistencia excede del ĺimite de horas establecido, el limite de horas semanales es 25 ', ['de horas'])]

    def create(self, cr, uid, vals, context):
        repetido= self.pool.get('for.pis.mae_asistencias').search(cr,uid, [('maestro_id','=',vals['maestro_id']),('numero_id','=', vals['numero_id']),('calendario_id','=', vals['calendario_id'])])
        if repetido:
            raise osv.except_osv(('Asistencia repetida'),('Esta asistencia ya ha sido cargada'))
        return super(for_pis_mae_asistencias, self).create(cr, uid, vals, context)

    def write(self, cr, uid, ids, vals, context):
        campos=('maestro_id', 'numero_id', 'calendario_id')
        ls=[]
        cn=0
        for asistencia in self.browse(cr, uid, ids):
            for campo in campos:
                if campo in vals:
                    ls.append(vals[str(campo)])
                else:
                    ls.append(asistencia[campo].id)
                    cn+=1
        if cn<3:
            repetido= self.pool.get('for.pis.mae_asistencias').search(cr,uid, [('maestro_id','=',ls[0]),('numero_id','=', ls[1]),('calendario_id','=', ls[2])])
            if repetido:
                raise osv.except_osv(('Asistencia repetida'),('Esta asistencia ya ha sido cargada'))
        return super(for_pis_mae_asistencias, self).write(cr, uid, ids, vals, context)


            
    

for_pis_mae_asistencias()

class for_pis_mae_valor_hora(osv.osv):
    """Tabla Referencia del Valor de la Hora para el Pago de Facilitadores"""
    _name = 'for.pis.mae_valor_hora'
    _rec_name = 'valor_hora'
    _columns = {
        'cargo': fields.char('Cargo',size=120,required=True, help='Cargo del Facilitador'),
        'nivel': fields.integer('Nivel',size=2,required=True, help='Codigo de Identificacion del Valor de la Hora (Nivel del Facilitador)'),
        'grado_academico': fields.char('Grado Academico',size=120,required=True, help='Grado Academico del Facilitador'),
        'salidas_ocupa': fields.char('Salidas Ocupacionales',size=120,required=True, help='Salidas Ocupacionales'),
        'horas': fields.char('Horas',size=120,required=True, help='Horas'),
        'tiempo_servicio': fields.char('Tiempo de Servicio',size=120,required=True, help='Tiempo de Servicio del Facilitador'),
        'valor_hora': fields.float('Valor Hora',required=True, help='Valor de la Hora del Facilitador'),
        'fecha_resolucion': fields.date('Fecha Resolución', help="Fecha de la Resolución de aprobación del Tabulador"),
        'nro_resolucion': fields.char('Nro. Resolución', size=20, help="Número de la Resolución de aprobación del Tabulador"),
    }
for_pis_mae_valor_hora()

class for_pis_mae_motivos_falta(osv.osv):
    """Tabla Referencia de Motivos de Faltas de Asistencias de Facilitadores"""
    _name = 'for.pis.mae_motivos_falta'
    _rec_name = 'motivo_falta'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de Identificación del Motivo de Falta'),
        'motivo_falta': fields.char('Motivo de Falta', size=120, required=True, help='Descripción del Motivo de la Falta'),
        'calificacion': fields.char('Calificacion', size=120, required=True, help='Calificación de Gravedad o Impacto de la Falta'),
    }
for_pis_mae_motivos_falta()

class for_pis_mae_cuentas_nomina(osv.osv):
    """Tabla Referencia de Cuentas Bancarias de INCES para el Pago de Nomina de Facilitadores"""
    _name = 'for.pis.mae_cuentas_nomina'
    _rec_name = 'entidad_bancaria'
    _columns = {
        'codigo': fields.char('Código',size=3,required=True, help='Codigo de Identificacion de la Cuenta Bancaria de INCES para el Pago de Facilitadores'),
        'entidad_bancaria': fields.char('Entidad Bancaria',size=120,required=True, help='Entidad Bancaria'),
        'numero_cuenta': fields.char('Numero Cuenta',size=120,required=True, help='Numero de la Cuenta Bancaria'),
    }
for_pis_mae_cuentas_nomina()

class for_pis_mae_misiona01(osv.osv):
    """Tabla de interoperabilidad con Sistema Externo de Recursos Humanos"""
    _name = 'for.pis.mae_misiona01'
    _rec_name = 'cedula'
    _columns = {
        'tip_nom': fields.integer('tip_nom',required=False, help='tip_nom : smallint'),
        'nac': fields.char('nac',size=1,required=False, help='nac : char(1)'),
        'cedula': fields.integer('cedula',required=False, help='cedula : integer'),
        'nombre': fields.char('nombre',size=40,required=False, help='nombre : char(40)'),
        'ciu_nac': fields.char('ciu_nac',size=20,required=False, help='ciu_nac : char(20)'),
        'fec_nac': fields.date('fec_nac',required=False, help='fec_nac : date'),
        'sexo': fields.char('sexo',size=1,required=False, help='sexo : char(1)'),
        'fec_ing': fields.date('fec_ing',required=False, help='fec_ing : date'),
        'fec_egr': fields.date('fec_egr',required=False, help='fec_egr : date'),
        'cod_car': fields.integer('cod_car',required=False, help='cod_car : integer'),
        'cod_dep': fields.integer('cod_dep',required=False, help='cod_dep : integer'),
        'cod_edo': fields.integer('cod_edo',required=False, help='cod_edo : smallint'),
        'cod_mun': fields.integer('cod_mun',required=False, help='cod_mun : smallint'),
        'cod_par': fields.integer('cod_par',required=False, help='cod_par : smallint'),
        'situacion': fields.char('situacion', size=1, required=False, help='situacion : char(1)'),
        'fec_sta': fields.date('fec_sta',required=False, help='fec_sta : date'),
        'for_pag': fields.char('for_pag',size=1, required=False, help='for_pag : char(1)'),
        'tip_cta': fields.char('tip_cta',size=1, required=False, help='tip_cta : cahr(1)'),
        'num_cta': fields.char('num_cta',size=20, required=False, help='num_cta : char(20)'),
        'cod_bco': fields.integer('cod_bco', required=False, help='cod_bco : smallint'),
        'cod_age': fields.integer('cod_age', required=False, help='cod_age : smallint'),
        'usuario': fields.char('ususario', size=10, required=False, help='usuario : char(10)'),
        'fec_usu': fields.date('fec_usu', required=False),
        'hor_usu': fields.char('hor_usu', size=10, required=False, help='hor_usu : char(10)'),
        'cor_amo': fields.integer('cor_amo', required=False, help='cor_amo : integer'),
        'anio_vigencia': fields.char('anio de vigencia', size=4),
    }
for_pis_mae_misiona01()

class for_pis_mae_misiona05(osv.osv):
    """Tabla de interoperabilidad con Sistema Externo de Recursos Humanos"""
    _name = 'for.pis.mae_misiona05'
    _rec_name = 'cedula'
    _columns = {
        'tip_nom': fields.integer('tip_nom',required=False, help='tip_nom : smallint'),
        'cedula': fields.integer('cedula',required=False, help='cedula : integer'),
        'tip_mov': fields.char('tip_mov',size=1,required=False, help='tip_mov : char(1)'),
        'cod_mov': fields.integer('cod_mov', required=False, help='cod_mov : smallint'),
        'cri_mov': fields.integer('cri_mov', required=False, help='cri_mov : smallint'),
        'fec_ini': fields.date('fec_ini',required=False, help='fec_ini'),
        'fec_fin': fields.date('fec_fin',required=False, help='fec_fin'),
        'fec_retro': fields.date('fec_retro',required=False, help='fec_retro : decimal(14,2)'),
        'sal_ini': fields.float('sal_ini',required=False, help='sal_ini : decimal(14,2)'),
        'mon_mov': fields.float('mon_mov',required=False, help='mon_mov : decimal(14,2)'),
        'apo_pat': fields.float('apo_pat',required=False, help='apo_pat : decimal(14,2)'),
        'sal_mov': fields.float('sal_mov',required=False, help='sal_mov : decimal(14,2)'),
        'sal_ant': fields.float('sal_ant',required=False, help='sal_ant : decimal(14,2)'),
        'stat_05': fields.char('stat_05', size=1, required=False, help='stat_05 : char(1)'),
        'usuario': fields.char('usuario', size=10, required=False, help='usuario : char(10)'),
        'fec_usu': fields.date('fec_usu', required=False, help='fec_usu : date'),
        'hor_usu': fields.char('hor_usu', size=10, required=False, help='hor_usu : char(10)'),
        'anio_vigencia': fields.char('anio de vigencia', size=4),
    }
for_pis_mae_misiona05()

#Contratos Abril

class for_pis_contratos(osv.osv):
    """Objeto definido para importar el query de generación con los contratos abril 2015"""
    _name = 'for.pis.contratos'
    _rec_name = ''
    _columns = {
        'nombres': fields.char('Nombres', size=120, help='Nombres del Facilitador'),
        'apellidos': fields.char('Apellidos', size=120, help='Apellidos del Facilitador'),
        'cedula': fields.char('Cédula', size=120, help='Cédula del Facilitador'),
        'nacionalidad': fields.char('Nacionalidad', size=120, help='Nacionalidad  del Facilitador'),
        'estado_civil': fields.char('Estado Civil', size=60, help='Estado Civil del Facilitador'),
        'dependencia': fields.char('Dependencia', size=120, help='Depenciancia donde trabaja el Facilitador'),
        'domicilio': fields.char('Domicilio', size=120, help='Domicilio  del Facilitador'),
        'municipio': fields.char('Municipio', size=120, help='Municipio del Facilitador'),
        'estado': fields.char('Estado', size=120, help='Estado del Facilitador'),
        'total_horas': fields.integer('Total Horas', help='Total Horas de Formación del Facilitador'),
        'fecha_inicio': fields.date('Fecha Inicio', help='Fecha de Inicio de la primera Formación  del Facilitador'),
        'fecha_cierre': fields.date('Fecha de Cierre', help='Fecha de Cierra de la última Formación  del Facilitador'),
        'cfs': fields.char('C.F.S.', size=120, help='Centro de Formación Socialista del Facilitador'),
        'total_pagar': fields.float('Total a Pagar', help='Total a Pagar al Facilitador (total_horas*valor_hora)'),
        #Campos adicionales para referencias
        'total_formaciones': fields.integer('Total Formaciones', help='Total de Formaciones del Facilitador'),
        'valor_hora': fields.float('Valor Hora', help='Valor Hora del Facilitador'),
        'condicion_laboral': fields.char('Condición Laboral', size=120, help='Condición Laboral del Facilitador'),
        'active': fields.boolean('Aprobado para generar', help="¿Aprobado para generarse el contrato?"), 
        'fecha_generado': fields.date('Fecha Generado', help='Fecha en la que se generó el contrato'),
    }
    
    _defaults = {
        'active' : True,
    }
    
for_pis_contratos()

