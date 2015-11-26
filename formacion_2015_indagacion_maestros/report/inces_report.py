import time
import datetime
from numero_a_texto import Numero_a_Texto
from convertir import convertir#agregar para RML
from report import report_sxw
from osv import fields,osv

class reporte_inces(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(reporte_inces, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'obt_texto':self.obt_texto,
            'lang':context['lang'],
            'vcedula':self.vcedula,
            'convertir':self.convertir,
            'formatear_fecha':self.formatear_fecha,
            'sumar_horas':self.sumar_horas,
            'min_fecha':self.min_fecha,
            'max_fecha':self.max_fecha,
            'determinar_valor_hora':self.determinar_valor_hora,
            'marcar_contrato_generado':self.marcar_contrato_generado,
            'agregar_a_clase_contratos':self.agregar_a_clase_contratos,
        })

    def obt_texto(self,cantidad):
        res=Numero_a_Texto(cantidad).escribir
        return res

    def vcedula(self,nacionalidad):
        if (nacionalidad == 'Venezolana') or (nacionalidad == 'Venezolano'):
            return 'V'
        else:
            return 'E'

    def convertir(self,cedula):
        return convertir(cedula)

    def formatear_fecha(self,fecha):
        return fecha[8:10]+"/"+fecha[5:7]+"/"+fecha[0:4]

    def sumar_horas(self,datos):
        total=0
        for k in datos:
            total=total+k
        return total

    def min_fecha(self,fecha):
        fec_min = min(fecha)
        return fec_min[8:10]+"/"+fec_min[5:7]+"/"+fec_min[0:4]

    def max_fecha(self,fecha):
        fec_max = max(fecha)
        return fec_max[8:10]+"/"+fec_max[5:7]+"/"+fec_max[0:4]

    def determinar_valor_hora(self, cedula):
        self.cr.execute("SELECT min(for_pis_registro_inicial.fecha_inicio) from for_pis_mae_participacion_pis  \
                        INNER JOIN for_pis_maestros  \
                        ON for_pis_maestros.id=for_pis_mae_participacion_pis.maestro_id  \
                        INNER JOIN for_pis_registro_inicial  \
                        ON for_pis_registro_inicial.id=for_pis_mae_participacion_pis.numero_id  \
                        WHERE for_pis_maestros.cedula='%s'" % cedula)
        fec_minima=self.cr.fetchone()
        if(fec_minima<0):
            #fec_minima='2015-05-01'
            return 0

        else:
            if(fec_minima > '2015-05-01'):
                self.cr.execute("SELECT valor_hora \
                            FROM for_pis_maestros \
                            INNER JOIN for_pis_mae_valor_hora \
                            ON for_pis_maestros.nivel_id=for_pis_mae_valor_hora.id \
                            WHERE for_pis_maestros.cedula='%s'" % (cedula))
                resultado1=self.cr.fetchone()
                if(resultado1<0):
                    return 0
                else:
                    return resultado1[0]
            else:
                self.cr.execute("SELECT valor_hora \
                            FROM for_pis_maestros \
                            INNER JOIN for_pis_mae_valor_hora \
                            ON for_pis_maestros.nivel_viejo_id=for_pis_mae_valor_hora.id \
                            WHERE for_pis_maestros.cedula='%s'" % (cedula))
                resultado2=self.cr.fetchone()
                if(resultado2<0):
                    #self.cr.execute("SELECT valor_hora \
                    #        FROM for_pis_maestros \
                    #        INNER JOIN for_pis_mae_valor_hora \
                    #        ON for_pis_maestros.nivel_id=for_pis_mae_valor_hora.id \
                    #        WHERE for_pis_maestros.cedula='%s'" % (cedula))
                    #resultado1=self.cr.fetchone()
                    #if(resultado1<0):
                    #    return 0
                    #else:
                    #    return resultado1[0]
                    return 0
                else:
                    return resultado2[0]

    def marcar_contrato_generado(self, cedula):
        self.cr.execute("SELECT apr_generar FROM for_pis_maestros WHERE cedula='%s'" % (cedula))
        booleano=self.cr.fetchone()
        if(booleano[0]==None or booleano[0]==False):
            self.cr.execute("UPDATE for_pis_maestros SET apr_generar='%s' WHERE cedula='%s'" % (True,cedula))

    def agregar_a_clase_contratos(self, cedula, nombres, apellidos, nacionalidad, estado_civil, domicilio, municipio, estado, fecha_inicio, fecha_cierre, cfs, total_horas, valor_hora, condicion_laboral):
        fecha_generado=time.strftime("%d-%m-%Y")
        create_uid=1
        create_date=datetime.datetime.now()
        write_date=0
        write_uid=0
        total_pagar=total_horas*valor_hora
        active=True
        
        self.cr.execute("SELECT count(*) from for_pis_mae_participacion_pis \
                        INNER JOIN for_pis_maestros \
                        ON for_pis_maestros.id=for_pis_mae_participacion_pis.maestro_id \
                        WHERE for_pis_maestros.cedula='%s'" % cedula)
        total_formaciones=self.cr.fetchone()
        if(total_formaciones<0):
            total_formaciones=0

        self.cr.execute("SELECT for_dependencias.dependencia \
                        FROM dependencia_formador_rel \
                        INNER JOIN for_pis_maestros  \
                        ON for_pis_maestros.id=dependencia_formador_rel.formador_id  \
                        INNER JOIN for_dependencias \
                        ON for_dependencias.id=dependencia_formador_rel.dependencia_id \
                        WHERE for_pis_maestros.cedula='%s'" % (cedula))
        dependencia=self.cr.fetchone()
        if(dependencia<0):
            dependencia = "CAMPO VACIO" 

        if(cedula<0):
            cedula=0

        if(nombres<0):
            nombres="SIN NOMBRES"

        if(apellidos<0):
            apellidos="SIN APELLIDOS"

        if(nacionalidad<0):
            nacionalidad="SIN NACIONALIDAD"

        if(estado_civil<0):
            estado_civil="SIN ESTADO CIVIL"

        if(domicilio<0):
            domicilio="SIN DOMICILIO"

        if(municipio<0):
            municipio="SIN MUNICIPIO"

        if(estado<0):
            estado="SIN ESTADO"

        if(fecha_inicio<'0000-00-00'):
            fecha_inicio='0000-00-00'

        if(fecha_cierre<'0000-00-00'):
            fecha_cierre='0000-00-00'

        if(cfs==''):
            cfs="SIN CFS"

        if(total_horas<0):
            total_horas=0

        if(valor_hora<0):
            valor_hora=0

        if(condicion_laboral<0):
            condicion_laboral="SIN CONDICION LABORAL"

        self.cr.execute("INSERT INTO for_pis_contratos (create_uid, create_date, cedula, nombres, apellidos, nacionalidad, estado_civil, domicilio, municipio, estado, fecha_inicio, fecha_cierre, cfs, total_horas, valor_hora, fecha_generado, total_pagar, condicion_laboral, active, total_formaciones, dependencia) \
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (create_uid,create_date,cedula, nombres, apellidos, nacionalidad, estado_civil, domicilio, municipio, estado, fecha_inicio, fecha_cierre, cfs, total_horas, valor_hora, fecha_generado, total_pagar, condicion_laboral, active, total_formaciones, dependencia))

report_sxw.report_sxw('report.contrato.por.hora', 'for.pis.maestros', 'addons/formacion_2015_indagacion_maestros/report/por_hora.rml', parser=reporte_inces, header="False")
report_sxw.report_sxw('report.participantes.formadores', 'for.pis.maestros', 'addons/formacion_2015_indagacion_maestros/report/participantes_formadores.rml', parser=reporte_inces, header="False")