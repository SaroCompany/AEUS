#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 11/06/2020
@author: Ing. John Arroyo
DiVi ver. 1.0
"""
from scripts.data import ConexionBaseDatos

class CalculosInternosVPrincipal():

    def acero_requerido_viga(self):
        self.manejo_base = ConexionBaseDatos()
        try:
            self.base_viga_d = float(self.line_edit_base_viga_d.text())
        except ValueError:
            self.base_viga_d = 0
        try:
            self.altura_viga_d = float(self.line_edit_altura_viga_d.text())
        except ValueError:
            self.altura_viga_d = 0
        self.recubrimiento_inferior_viga = float(self.line_edit_recubrimiento_inferior_viga.text())
        self.recubrimiento_superior_viga = float(self.line_edit_recubrimiento_superior_viga.text())
        self.longitud_libre_viga = float(self.line_edit_longitud_libre_viga.text())
        self.momento_negativo_izquierdo_viga = float(self.line_edit_momento_negativo_izquierdo_viga.text())
        self.momento_positivo_izquierdo_viga = float(self.line_edit_momento_positivo_izquierdo_viga.text())
        self.momento_negativo_centro_viga = float(self.line_edit_momento_negativo_centro_viga.text())
        self.momento_positivo_centro_viga = float(self.line_edit_momento_positivo_centro_viga.text())
        self.momento_negativo_derecho_viga = float(self.line_edit_momento_negativo_derecho_viga.text())
        self.momento_positivo_derecho_viga = float(self.line_edit_momento_positivo_derecho_viga.text())
        self.fluencia_acero = self.manejo_base.consultar_dato(
            'fy', 'data/base', 'PROPMATS', 'VALOR')
        self.resistencia_concreto = self.manejo_base.consultar_dato(
            'fc', 'data/base', 'PROPMATS', 'VALOR')
        self.parametro_phib = self.manejo_base.consultar_dato(
            'phib', 'data/base', 'PROPMATS', 'VALOR')
        self.parametro_B1 = self.manejo_base.consultar_dato(
            'B1', 'data/base', 'PROPMATS', 'VALOR')
        self.deformacion_ultima_concreto = self.manejo_base.consultar_dato(
            'Ecu', 'data/base', 'PROPMATS', 'VALOR')
        self.deformacion_minima_acero = self.manejo_base.consultar_dato(
            'Esmin', 'data/base', 'PROPMATS', 'VALOR')
        self.lista_aceros_requeridos_momentos = []
        self.lista_momentos = [self.momento_negativo_izquierdo_viga,
                            self.momento_positivo_izquierdo_viga,
                            self.momento_negativo_centro_viga,
                            self.momento_positivo_centro_viga,
                            self.momento_negativo_derecho_viga,
                            self.momento_positivo_derecho_viga]
        self.altura_util = self.altura_viga_d - self.recubrimiento_inferior_viga
        self.chequeo_limite_1 = 4*self.altura_util/100
        self.chequeo_limite_2 = 0.3*self.altura_viga_d
        self.acero_minimo_1 = 14/self.fluencia_acero*self.base_viga_d*self.altura_util
        self.acero_minimo_2 = 0.80*(self.resistencia_concreto)**(1/2)/self.fluencia_acero*self.base_viga_d*self.altura_util
        self.acero_minimo = round(max(self.acero_minimo_1, self.acero_minimo_2), 2)
        for momento in self.lista_momentos:
            self.acero_momento = self.acero_requerido_momento(momento)
            self.lista_aceros_requeridos_momentos.append(round(self.acero_momento, 2))
            try:
                self.lista_aceros_requeridos_momentos.append(round(self.profundidad_bloque_whitney, 2))
            except TypeError:
                self.lista_aceros_requeridos_momentos.append(0)
            try:
                self.lista_aceros_requeridos_momentos.append(round(self.profundidad_eje_neutro, 2))
            except TypeError:
                self.lista_aceros_requeridos_momentos.append(0)
            try:
                self.lista_aceros_requeridos_momentos.append(round(self.profundidad_eje_neutro_maximo_falla_traccion, 2))
            except TypeError:
                self.lista_aceros_requeridos_momentos.append(0)
            self.lista_aceros_requeridos_momentos.append(round(self.acero_calculado, 2))
        self.label_acero_minimo.setText(str(self.acero_minimo))
        self.label_acero_requerido_1.setText(str(self.lista_aceros_requeridos_momentos[0]))
        self.label_acero_requerido_2.setText(str(self.lista_aceros_requeridos_momentos[5]))
        self.label_acero_requerido_3.setText(str(self.lista_aceros_requeridos_momentos[10]))
        self.label_acero_requerido_4.setText(str(self.lista_aceros_requeridos_momentos[15]))
        self.label_acero_requerido_5.setText(str(self.lista_aceros_requeridos_momentos[20]))
        self.label_acero_requerido_6.setText(str(self.lista_aceros_requeridos_momentos[25]))
        self.guardar_cambio(
            'bw', 'DATVIG', 'VALOR', self.base_viga_d)
        self.guardar_cambio(
            'h', 'DATVIG', 'VALOR', self.altura_viga_d)
        self.guardar_cambio(
            'r', 'DATVIG', 'VALOR', self.recubrimiento_inferior_viga)
        self.guardar_cambio(
            'rp', 'DATVIG', 'VALOR', self.recubrimiento_superior_viga)
        self.guardar_cambio(
            'Ln', 'DATVIG', 'VALOR', self.longitud_libre_viga)
        self.guardar_cambio(
            'Mu_neg_izq', 'MOMVIG', 'VALOR', self.momento_negativo_izquierdo_viga)
        self.guardar_cambio(
            'Mu_pos_izq', 'MOMVIG', 'VALOR', self.momento_positivo_izquierdo_viga)
        self.guardar_cambio(
            'Mu_neg_cen', 'MOMVIG', 'VALOR', self.momento_negativo_centro_viga)
        self.guardar_cambio(
            'Mu_pos_cen', 'MOMVIG', 'VALOR', self.momento_positivo_centro_viga)
        self.guardar_cambio(
            'Mu_neg_der', 'MOMVIG', 'VALOR', self.momento_negativo_derecho_viga)
        self.guardar_cambio(
            'Mu_pos_der', 'MOMVIG', 'VALOR', self.momento_positivo_derecho_viga)
        self.guardar_cambio(
            'd', 'CALCVIG', 'VALOR', self.altura_util)
        self.guardar_cambio(
            'chk1', 'CALCVIG', 'VALOR', self.chequeo_limite_1)
        self.guardar_cambio(
            'chk2', 'CALCVIG', 'VALOR', self.chequeo_limite_2)
        self.guardar_cambio(
            'Asmin_1', 'CALCVIG', 'VALOR', self.acero_minimo_1)
        self.guardar_cambio(
            'Asmin_2', 'CALCVIG', 'VALOR', self.acero_minimo_2)
        self.guardar_cambio(
            'Asmin', 'CALCVIG', 'VALOR', self.acero_minimo)
        self.guardar_cambio(
            'Asreq_1', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[0])
        self.guardar_cambio(
            'a_1', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[1])
        self.guardar_cambio(
            'c_1', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[2])
        self.guardar_cambio(
            'cmax_1', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[3])
        self.guardar_cambio(
            'Ascalc_1', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[4])
        self.guardar_cambio(
            'Asreq_2', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[5])
        self.guardar_cambio(
            'a_2', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[6])
        self.guardar_cambio(
            'c_2', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[7])
        self.guardar_cambio(
            'cmax_2', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[8])
        self.guardar_cambio(
            'Ascalc_2', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[9])
        self.guardar_cambio(
            'Asreq_3', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[10])
        self.guardar_cambio(
            'a_3', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[11])
        self.guardar_cambio(
            'c_3', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[12])
        self.guardar_cambio(
            'cmax_3', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[13])
        self.guardar_cambio(
            'Ascalc_3', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[14])
        self.guardar_cambio(
            'Asreq_4', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[15])
        self.guardar_cambio(
            'a_4', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[16])
        self.guardar_cambio(
            'c_4', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[17])
        self.guardar_cambio(
            'cmax_4', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[18])
        self.guardar_cambio(
            'Ascalc_4', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[19])
        self.guardar_cambio(
            'Asreq_5', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[20])
        self.guardar_cambio(
            'a_5', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[21])
        self.guardar_cambio(
            'c_5', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[22])
        self.guardar_cambio(
            'cmax_5', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[23])
        self.guardar_cambio(
            'Ascalc_5', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[24])
        self.guardar_cambio(
            'Asreq_6', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[25])
        self.guardar_cambio(
            'a_6', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[26])
        self.guardar_cambio(
            'c_6', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[27])
        self.guardar_cambio(
            'cmax_6', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[28])
        self.guardar_cambio(
            'Ascalc_6', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[29])

    def acero_requerido_momento(self, momento_ultimo_resultado):
        self.momento_ultimo = momento_ultimo_resultado*1000*100
        self.profundidad_bloque_whitney = self.altura_util - (self.altura_util**2 - 2*self.momento_ultimo/(0.85*self.resistencia_concreto*self.parametro_phib*self.base_viga_d))**(1/2)
        self.profundidad_eje_neutro = self.profundidad_bloque_whitney/self.parametro_B1
        self.profundidad_eje_neutro_maximo_falla_traccion = (self.deformacion_ultima_concreto/(self.deformacion_ultima_concreto+self.deformacion_minima_acero))*self.altura_util
        try:
            if self.profundidad_eje_neutro <= self.profundidad_eje_neutro_maximo_falla_traccion:
                self.acero_calculado = self.momento_ultimo/(self.parametro_phib*self.fluencia_acero*(self.altura_util-self.profundidad_bloque_whitney/2))
                self.acero_requerido = max(self.acero_calculado, self.acero_minimo)
        except TypeError:
            self.acero_calculado = 0
            self.acero_requerido = 0
        return self.acero_requerido
    
    def ayuda_barras_refuerzo(self, cantidad1, cantidad2, area1, area2):
        self.ayuda = (cantidad1*area1 + cantidad2*area2)/100
        return self.ayuda
    
    def ayuda_area_transversal_refuerzo(self, nRama, areaEstribo):
        return nRama*areaEstribo/100

    def acero_ductilidad_inferior(self, aceroSuperior, aceroInferiorRequerido):
        self.aceroInferior = max(aceroSuperior/2, aceroInferiorRequerido)
        return self.aceroInferior
    
    def corte_maximo(self, Wcp, Wcv, Ln, Fsr, fy, Fc, bw, acero1, acero2, h, r, dp, Fcv):
        self.vas = []
        self.Mmps = []
        self.acerosRequeridos = [acero1, acero2]
        self.d = h - r #Altura útil de la sección
        self.Wu = 1.2*Wcp + Fcv*Wcv #Carga última
        self.Vg = self.Wu*Ln/2 #Corte gravitacional
        #Análisis de casos
        for self.aceros in self.acerosRequeridos:
            self.a = Fsr*fy*self.aceros/(0.85*Fc*bw) #Altura bloque equivalente de Whitney (cm)
            self.Mpr = (Fsr*fy*self.aceros*(self.d - self.a/2))/100000 #Momento máximo probable, pasado de Kgf*cm a Tonf*m
            self.vas.append(self.a)
            self.Mmps.append(self.Mpr)
        self.Vp = (self.Mmps[0] + self.Mmps[1])/Ln #Corte por capacidad
        return self.acerosRequeridos, self.d, self.Wu, self.Vg, self.Mmps, self.vas, self.Vp
    
    def diseno_estribos(self, Vp, Vd, Pu,bw,h,fc,d,Phiv,AV,fy,db):
        self.relacionCortes = Vp/Vd
        self.Ag = bw*h #Area gruesa de acero
        self.Pc = self.Ag*fc/20000 #Producto a tonf
        if self.relacionCortes>=0.5 and Pu<=self.Pc:
            self.Vc = 0
        else:
            self.Vc = 0.53*(1+Pu/(140*self.Ag))*(fc**0.5)*bw*d #Cortante
        self.Vs = Vd/Phiv-self.Vc #Demanda por corte
        self.Smcal = AV*fy*d/(self.Vs*1000) #Separacion maxima calculada
        self.Smnorma = min(d/4,6*(db/10),15) #Separacion maxima norma
        self.Smreq = max(self.Smcal,self.Smnorma) #Separacion maxima requerida
        self.Lc = 2*h #Longitud de confinamiento
        self.Sgm = d/2 #Separacion maxima inconfinada
        self.Sgsm = min(10,d/4) #Separacion maxima inconfinada solapada
        return self.relacionCortes, self.Ag, self.Pc,self.Vc,self.Vs,self.Smcal,self.Smnorma,self.Smreq,self.Lc,self.Sgm,self.Sgsm
