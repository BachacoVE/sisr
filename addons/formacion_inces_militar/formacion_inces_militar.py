
# -*- coding: utf-8 -*-
from osv import fields,osv
from openerp.tools.translate import _
from openerp.exceptions import Warning

class for_militar_componentes(osv.osv):
    _name = 'for.militar_componentes'
    _rec_name = 'componente'
    _columns = {
    'codigo': fields.char('Código', size=3, required=True, help='Código del Componente de las Fuerzas Armadas de la República Bolivariana de Venezuela'),
    'componente': fields.char('Componente', size=60, required=True, help='Nombre del Componente de las Fuerzas Armadas de la República Bolivariana de Venezuela'),
    }
for_militar_componentes()

class for_militar_unidades_dependecias(osv.osv):
    _name = 'for.militar_unidades_dependencias'
    _rec_name = 'unidad_dependencia'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de la Unidad o Dependencia de las Fuerzas Armadas de la República Bolivariana de Venezuela'),
        'unidad_dependencia': fields.char('Unidad o Dependencia', size=120, required=True, help='Nombre de la Unidad o Dependencia de las Fuerzas Armadas de la República Bolivariana de Venezuela'),
        'componente_id': fields.many2one('for.militar_componentes', 'Componente', required=True, help='Componente de las FARBV a la cual se asocia la Cateogoría'),
    }
for_militar_unidades_dependecias()

class for_militar_grados_jerarquias(osv.osv):
    _name = 'for.militar_grados_jerarquias'
    _rec_name = 'grado_jerarquia'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código del Grado o Jerarquía Militar de las FARBV'),
        'grado_jerarquia': fields.char('Grado o Jerarquía', size=120, required=True, help='Nombre del Grado o Jerarquía de las FARBV'),
        'categoria_id': fields.many2one('for.militar_categorias', 'Categoria', required=False, help='Categoria de Personal las FARBV a la cual pertenece'),
    }
for_militar_grados_jerarquias()

class for_militar_categorias(osv.osv):
    _name = 'for.militar_categorias'
    _rec_name = 'categoria'
    _columns = {
        'codigo': fields.char('Código', size=3, required=True, help='Código de la Categría de las Fuerzas Armadas de la República Bolivariana de Venezuela'),
        'categoria': fields.char('Categoría', size=120, required=True, help='Nombre de la Categría de las Fuerzas Armadas de la República Bolivariana de Venezuela'),
        'componente_id': fields.many2one('for.militar_componentes', 'Componente', required=True, help='Componente de las FARBV a la cual se asocia la Cateogoría'),
    }
for_militar_categorias()

class for_militar_registro_inicial(osv.osv):
    _name = 'for.pis.registro_inicial'
    _inherit = 'for.pis.registro_inicial'
    _columns = {
        'militar_proyecto': fields.boolean('Proyecto INCES Militar?', help='Marque si el Proyecto Integral Socialista es de INCES Militar'),
        'militar_componente_id': fields.many2one('for.militar_componentes', 'Componente', required=False, help='Componente de las FARBV a la cual pertenece'),
        'militar_unidad_id': fields.many2one('for.militar_unidades_dependencias', 'Unidad o Dependencia', required=False, help='Unidad o Dependencia de las FARBV a la cual pertenece'),
    }    
for_militar_registro_inicial()

class for_pis_maestros_extended(osv.osv):
    _name = 'for.pis.maestros'
    _inherit = 'for.pis.maestros'
    _columns = {
        'militar_maestro': fields.boolean('Maestro Militar?', help='Marque si el Maestro es Personal de las FARBV'),
        'militar_componente_id': fields.many2one('for.militar_componentes', 'Componente', required=False, help='Componente de las FARBV a la cual pertenece'),
        'militar_categoria_id': fields.many2one('for.militar_categorias', 'Categoria', required=False, help='Categoria de Personal las FARBV a la cual pertenece'),
        'militar_grado_id': fields.many2one('for.militar_grados_jerarquias', 'Grado Militar', required=False, help='Grado o Jerarquia de Personal las FARBV a la cual pertenece'),
        'militar_unidad_id': fields.many2one('for.militar_unidades_dependencias', 'Unidad o Dependencia', required=False, help='Unidad o Dependencia de las FARBV a la cual pertenece'),
    }
for_pis_maestros_extended()


class for_pis_sujetos_aprendizaje_extended(osv.osv):
     _name = 'for.pis.sujetos_aprendizaje'
     _inherit = 'for.pis.sujetos_aprendizaje'
     _columns = {
        'militar_sujeto': fields.boolean('Sujeto Militar?', help='Marque si el sujeto de aprendizaje es Personal de las FARBV'),
        'militar_componente_id': fields.many2one('for.militar_componentes','Componente', required=False, help='Nombre del Componente de las Fuerzas Armadas de la República Bolivariana de Venezuela'),
        'militar_categoria_id': fields.many2one('for.militar_categorias', 'Categoria', required=False, help='Categoria de Personal las FARBV a la cual pertenece'),
        'militar_grado_id': fields.many2one('for.militar_grados_jerarquias', 'Grado Militar', required=False, help='Grado o Jerarquia de Personal las FARBV a la cual pertenece'),
        'militar_unidad_id': fields.many2one('for.militar_unidades_dependencias','Unidad o Dependencia', required=False, help='Unidad o Dependencia de las FARBV a la cual pertenece' ),
     }
for_pis_sujetos_aprendizaje_extended()


