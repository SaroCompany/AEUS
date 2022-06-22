#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 11/06/2020
@author: Ing. John Arroyo
DiVi ver. 1.0
"""
from scripts.data import ConexionBaseDatos

class CalculosInternosVPrincipal():

    def __init__(self):
        self.manejo_datos = ConexionBaseDatos()

    def acero_requerido_viga(self):
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
        self.fluencia_acero = self.manejo_datos.consultar_dato(
            'fy', 'data/base', 'PROPMATS', 'VALOR')
        self.resistencia_concreto = self.manejo_datos.consultar_dato(
            'fc', 'data/base', 'PROPMATS', 'VALOR')
        self.parametro_phib = self.manejo_datos.consultar_dato(
            'phib', 'data/base', 'PROPMATS', 'VALOR')
        self.parametro_B1 = self.manejo_datos.consultar_dato(
            'B1', 'data/base', 'PROPMATS', 'VALOR')
        self.deformacion_ultima_concreto = self.manejo_datos.consultar_dato(
            'Ecu', 'data/base', 'PROPMATS', 'VALOR')
        self.deformacion_minima_acero = self.manejo_datos.consultar_dato(
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
        self.peso_propio_viga = self.base_viga_d*self.altura_viga_d*self.longitud_libre_viga
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
        self.label_acero_superior_izquierdo_ductil.setText(str(self.lista_aceros_requeridos_momentos[0]))
        self.label_acero_superior_derecho_ductil.setText(str(self.lista_aceros_requeridos_momentos[20]))
        self.acero_inferior_izquierdo_ductil = self.acero_inferior_ductilidad(
            self.lista_aceros_requeridos_momentos[0], self.lista_aceros_requeridos_momentos[5])
        self.label_acero_inferior_izquierdo_ductil.setText(str(self.acero_inferior_izquierdo_ductil))
        self.acero_inferior_derecho_ductil = self.acero_inferior_ductilidad(
            self.lista_aceros_requeridos_momentos[20], self.lista_aceros_requeridos_momentos[25])
        self.label_acero_inferior_derecho_ductil.setText(str(self.acero_inferior_derecho_ductil))
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
        self.guardar_cambio(
            'As1_sup_req', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[0])
        self.guardar_cambio(
            'As1_inf_req', 'CALCVIG', 'VALOR', self.acero_inferior_izquierdo_ductil)
        self.guardar_cambio(
            'As2_sup_req', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[20])
        self.guardar_cambio(
            'As2_inf_req', 'CALCVIG', 'VALOR', self.acero_inferior_derecho_ductil)
        self.guardar_cambio(
            'Wpp', 'CALCVIG', 'VALOR', self.peso_propio_viga)

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

    def acero_inferior_ductilidad(self, acero_superior, acero_inferior_requerido):
        self.acero_inferior = max(acero_superior/2, acero_inferior_requerido)
        return self.acero_inferior

    def area_acero(self, cod):
        if cod == '':
            area = 0
        elif cod == '#2':
            area = self.datos_memoria.area_N2
        elif cod == '#3':
            area = self.datos_memoria.area_N3
        elif cod == '#4':
            area = self.datos_memoria.area_N4
        elif cod == '#5':
            area = self.datos_memoria.area_N5
        elif cod == '#6':
            area = self.datos_memoria.area_N6
        elif cod == '#7':
            area = self.datos_memoria.area_N7
        elif cod == '#8':
            area = self.datos_memoria.area_N8
        elif cod == '#9':
            area = self.datos_memoria.area_N9
        elif cod == '#10':
            area = self.datos_memoria.area_N10
        elif cod == '#11':
            area = self.datos_memoria.area_N11
        elif cod == '#14':
            area = self.datos_memoria.area_N14
        elif cod == '#18':
            area = self.datos_memoria.area_N18
        return area

    def acero_impuesto(self, can1, cod1, can2, cod2):
        area1 = self.area_acero(cod1)
        area2 = self.area_acero(cod2)
        area_acero_impuesto = (can1*area1+can2*area2)/100
        return area_acero_impuesto

    def acero_impuesto_superior_izquierdo(self):
        try:
            self.cantidad1_acero_superior_izquierdo = int(self.combo_box_cantidad1_acero_superior_izquierdo.currentText())
        except ValueError:
            self.cantidad1_acero_superior_izquierdo = 0
        try:
            self.codigo1_acero_superior_izquierdo = self.combo_box_codigo1_acero_superior_izquierdo.currentText()
        except ValueError:
            self.codigo1_acero_superior_izquierdo = 0
        try:
            self.cantidad2_acero_superior_izquierdo = int(self.combo_box_cantidad2_acero_superior_izquierdo.currentText())
        except ValueError:
            self.cantidad2_acero_superior_izquierdo = 0
        try:
            self.codigo2_acero_superior_izquierdo = self.combo_box_codigo2_acero_superior_izquierdo.currentText()
        except ValueError:
            self.codigo2_acero_superior_izquierdo = 0
        self.acero_superior_izquierdo_impuesto = self.acero_impuesto(
            self.cantidad1_acero_superior_izquierdo, self.codigo1_acero_superior_izquierdo,
            self.cantidad2_acero_superior_izquierdo, self.codigo2_acero_superior_izquierdo)
        self.label_acero_superior_izquierdo_impuesto.setText(str(self.acero_superior_izquierdo_impuesto))
        self.acero_centro_ductilidad_superior()
        self.guardar_cambio(
            'As1_sup', 'CALCVIG', 'VALOR', self.acero_superior_izquierdo_impuesto)

    def acero_impuesto_superior_derecho(self):
        try:
            self.cantidad1_acero_superior_derecho = int(self.combo_box_cantidad1_acero_superior_derecho.currentText())
        except ValueError:
            self.cantidad1_acero_superior_derecho = 0
        try:
            self.codigo1_acero_superior_derecho = self.combo_box_codigo1_acero_superior_derecho.currentText()
        except ValueError:
            self.codigo1_acero_superior_derecho = 0
        try:
            self.cantidad2_acero_superior_derecho = int(self.combo_box_cantidad2_acero_superior_derecho.currentText())
        except ValueError:
            self.cantidad2_acero_superior_derecho = 0
        try:
            self.codigo2_acero_superior_derecho = self.combo_box_codigo2_acero_superior_derecho.currentText()
        except ValueError:
            self.codigo2_acero_superior_derecho = 0
        self.acero_superior_derecho_impuesto = self.acero_impuesto(
            self.cantidad1_acero_superior_derecho, self.codigo1_acero_superior_derecho,
            self.cantidad2_acero_superior_derecho, self.codigo2_acero_superior_derecho)
        self.label_acero_superior_derecho_impuesto.setText(str(self.acero_superior_derecho_impuesto))
        self.acero_centro_ductilidad_superior()
        self.guardar_cambio(
            'As2_sup', 'CALCVIG', 'VALOR', self.acero_superior_derecho_impuesto)

    def acero_impuesto_inferior_derecho(self):
        try:
            self.cantidad1_acero_inferior_derecho = int(self.combo_box_cantidad1_acero_inferior_derecho.currentText())
        except ValueError:
            self.cantidad1_acero_inferior_derecho = 0
        try:
            self.codigo1_acero_inferior_derecho = self.combo_box_codigo1_acero_inferior_derecho.currentText()
        except ValueError:
            self.codigo1_acero_inferior_derecho = 0
        try:
            self.cantidad2_acero_inferior_derecho = int(self.combo_box_cantidad2_acero_inferior_derecho.currentText())
        except ValueError:
            self.cantidad2_acero_inferior_derecho = 0
        try:
            self.codigo2_acero_inferior_derecho = self.combo_box_codigo2_acero_inferior_derecho.currentText()
        except ValueError:
            self.codigo2_acero_inferior_derecho = 0
        self.acero_inferior_derecho_impuesto = self.acero_impuesto(
            self.cantidad1_acero_inferior_derecho, self.codigo1_acero_inferior_derecho,
            self.cantidad2_acero_inferior_derecho, self.codigo2_acero_inferior_derecho)
        self.label_acero_inferior_derecho_impuesto.setText(str(self.acero_inferior_derecho_impuesto))
        self.acero_centro_ductilidad_inferior()
        self.guardar_cambio(
            'As2_inf', 'CALCVIG', 'VALOR', self.acero_inferior_derecho_impuesto)

    def acero_impuesto_inferior_izquierdo(self):
        try:
            self.cantidad1_acero_inferior_izquierdo = int(self.combo_box_cantidad1_acero_inferior_izquierdo.currentText())
        except ValueError:
            self.cantidad1_acero_inferior_izquierdo = 0
        try:
            self.codigo1_acero_inferior_izquierdo = self.combo_box_codigo1_acero_inferior_izquierdo.currentText()
        except ValueError:
            self.codigo1_acero_inferior_izquierdo = 0
        try:
            self.cantidad2_acero_inferior_izquierdo = int(self.combo_box_cantidad2_acero_inferior_izquierdo.currentText())
        except ValueError:
            self.cantidad2_acero_inferior_izquierdo = 0
        try:
            self.codigo2_acero_inferior_izquierdo = self.combo_box_codigo2_acero_inferior_izquierdo.currentText()
        except ValueError:
            self.codigo2_acero_inferior_izquierdo = 0
        self.acero_inferior_izquierdo_impuesto = self.acero_impuesto(
            self.cantidad1_acero_inferior_izquierdo, self.codigo1_acero_inferior_izquierdo,
            self.cantidad2_acero_inferior_izquierdo, self.codigo2_acero_inferior_izquierdo)
        self.label_acero_inferior_izquierdo_impuesto.setText(str(self.acero_inferior_izquierdo_impuesto))
        self.acero_centro_ductilidad_inferior()
        self.guardar_cambio(
            'As1_inf', 'CALCVIG', 'VALOR', self.acero_inferior_izquierdo_impuesto)

    def acero_impuesto_superior_centro(self):
        try:
            self.cantidad1_acero_superior_centro = int(self.combo_box_cantidad1_acero_superior_centro.currentText())
        except ValueError:
            self.cantidad1_acero_superior_centro = 0
        try:
            self.codigo1_acero_superior_centro = self.combo_box_codigo1_acero_superior_centro.currentText()
        except ValueError:
            self.codigo1_acero_superior_centro = 0
        try:
            self.cantidad2_acero_superior_centro = int(self.combo_box_cantidad2_acero_superior_centro.currentText())
        except ValueError:
            self.cantidad2_acero_superior_centro = 0
        try:
            self.codigo2_acero_superior_centro = self.combo_box_codigo2_acero_superior_centro.currentText()
        except ValueError:
            self.codigo2_acero_superior_centro = 0
        self.acero_superior_centro_impuesto = self.acero_impuesto(
            self.cantidad1_acero_superior_centro, self.codigo1_acero_superior_centro,
            self.cantidad2_acero_superior_centro, self.codigo2_acero_superior_centro)
        self.label_acero_superior_centro_impuesto.setText(str(self.acero_superior_centro_impuesto))
        self.guardar_cambio(
            'As_sup', 'CALCVIG', 'VALOR', self.acero_superior_centro_impuesto)

    def acero_impuesto_inferior_centro(self):
        try:
            self.cantidad1_acero_inferior_centro = int(self.combo_box_cantidad1_acero_inferior_centro.currentText())
        except ValueError:
            self.cantidad1_acero_inferior_centro = 0
        try:
            self.codigo1_acero_inferior_centro = self.combo_box_codigo1_acero_inferior_centro.currentText()
        except ValueError:
            self.codigo1_acero_inferior_centro = 0
        try:
            self.cantidad2_acero_inferior_centro = int(self.combo_box_cantidad2_acero_inferior_centro.currentText())
        except ValueError:
            self.cantidad2_acero_inferior_centro = 0
        try:
            self.codigo2_acero_inferior_centro = self.combo_box_codigo2_acero_inferior_centro.currentText()
        except ValueError:
            self.codigo2_acero_inferior_centro = 0
        self.acero_inferior_centro_impuesto = self.acero_impuesto(
            self.cantidad1_acero_inferior_centro, self.codigo1_acero_inferior_centro,
            self.cantidad2_acero_inferior_centro, self.codigo2_acero_inferior_centro)
        self.label_acero_inferior_centro_impuesto.setText(str(self.acero_inferior_centro_impuesto))
        self.guardar_cambio(
            'As_inf', 'CALCVIG', 'VALOR', self.acero_inferior_centro_impuesto)

    def acero_centro_ductilidad_inferior(self):
        self.acero_inferior_izquierdo_impuesto = float(self.label_acero_inferior_izquierdo_impuesto.text())
        self.acero_inferior_derecho_impuesto = float(self.label_acero_inferior_derecho_impuesto.text())
        self.acero_inferior_centro_requerido = float(self.label_acero_requerido_4.text())
        self.acero_inferior_centro_ductilidad = self.acero_centro_ductilidad(
            self.acero_inferior_centro_requerido, self.acero_inferior_derecho_impuesto, self.acero_inferior_izquierdo_impuesto)
        self.label_acero_inferior_centro_ductil.setText(str(self.acero_inferior_centro_ductilidad))
        self.guardar_cambio(
            'As_inf_req', 'CALCVIG', 'VALOR', self.acero_inferior_centro_ductilidad)

    def acero_centro_ductilidad_superior(self):
        self.acero_superior_izquierdo_impuesto = float(self.label_acero_superior_izquierdo_impuesto.text())
        self.acero_superior_derecho_impuesto = float(self.label_acero_superior_derecho_impuesto.text())
        self.acero_superior_centro_requerido = float(self.label_acero_requerido_3.text())
        self.acero_superior_centro_ductilidad = self.acero_centro_ductilidad(
            self.acero_superior_centro_requerido, self.acero_superior_derecho_impuesto, self.acero_superior_izquierdo_impuesto)
        self.label_acero_superior_centro_ductil.setText(str(self.acero_superior_centro_ductilidad))
        self.guardar_cambio(
            'As_sup_req', 'CALCVIG', 'VALOR', self.acero_superior_centro_ductilidad)

    def acero_centro_ductilidad(self, acero_centro_requerido, acero_derecho_impuesto, acero_izquierdo_impuesto):
        acero_centro_ductil = max(
            acero_centro_requerido, acero_derecho_impuesto/4, acero_izquierdo_impuesto/4)
        return acero_centro_ductil

    def corte_maximo_caso_A(self):
        self.acero_superior_izquierdo_impuesto = float(self.label_acero_superior_izquierdo_impuesto.text())
        self.acero_inferior_izquierdo_impuesto = float(self.label_acero_inferior_izquierdo_impuesto.text())
        self.caso_A = self.corte_maximo(self.acero_superior_izquierdo_impuesto, self.acero_inferior_izquierdo_impuesto)
        self.caso_A.append(self.caso_A[2]+self.caso_A[5]) # Ve1 = Vg + Vp
        self.caso_A.append(self.caso_A[2]-self.caso_A[5]) # Ve2 = Vg - Vp

    def corte_maximo_caso_B(self):
        self.acero_superior_derecho_impuesto = float(self.label_acero_superior_derecho_impuesto.text())
        self.acero_inferior_derecho_impuesto = float(self.label_acero_inferior_derecho_impuesto.text())
        self.caso_B = self.corte_maximo(self.acero_superior_derecho_impuesto, self.acero_inferior_derecho_impuesto)
        self.caso_B.append(self.caso_B[2]-self.caso_B[5]) # Ve1 = Vg - Vp
        self.caso_B.append(self.caso_B[2]+self.caso_B[5]) # Ve2 = Vg + Vp

    def cortes_maximos(self):
        self.corte_maximo_caso_A()
        self.corte_maximo_caso_B()
        self.corte_izquierdo = round(max(self.caso_A[6], self.caso_B[6]), 3)
        self.corte_derecho = round(max(self.caso_A[7], self.caso_B[7]), 3)
        self.corte_capacidad = round(max(self.caso_A[5], self.caso_B[5]), 3)
        self.label_corte_izquierdo.setText(str(self.corte_izquierdo))
        self.label_corte_derecho.setText(str(self.corte_derecho))
        self.label_corte_capacidad.setText(str(self.corte_capacidad))
        self.guardar_cambio(
            'acero1_1', 'CALCVIG', 'VALOR', self.caso_A[0][0]) # Superior
        self.guardar_cambio(
            'acero2_1', 'CALCVIG', 'VALOR', self.caso_A[0][1]) # Inferior
        self.guardar_cambio(
            'Wu_1', 'CALCVIG', 'VALOR', self.caso_A[1])
        self.guardar_cambio(
            'Vg_1', 'CALCVIG', 'VALOR', self.caso_A[2])
        self.guardar_cambio(
            'a1_1', 'CALCVIG', 'VALOR', self.caso_A[4][0])
        self.guardar_cambio(
            'Mmp1_1', 'CALCVIG', 'VALOR', self.caso_A[3][0])
        self.guardar_cambio(
            'a2_1', 'CALCVIG', 'VALOR', self.caso_A[4][1])
        self.guardar_cambio(
            'Mmp2_1', 'CALCVIG', 'VALOR', self.caso_A[3][1])
        self.guardar_cambio(
            'Vp_1', 'CALCVIG', 'VALOR', self.caso_A[5])
        self.guardar_cambio(
            'Ve_1_CasoA', 'CALCVIG', 'VALOR', self.caso_A[6])
        self.guardar_cambio(
            'Ve_2_CasoA', 'CALCVIG', 'VALOR', self.caso_A[7])
        self.guardar_cambio(
            'acero1_2', 'CALCVIG', 'VALOR', self.caso_B[0][0]) # Superior
        self.guardar_cambio(
            'acero2_2', 'CALCVIG', 'VALOR', self.caso_B[0][1]) # Inferior
        self.guardar_cambio(
            'Wu_2', 'CALCVIG', 'VALOR', self.caso_B[1])
        self.guardar_cambio(
            'Vg_2', 'CALCVIG', 'VALOR', self.caso_B[2])
        self.guardar_cambio(
            'a1_2', 'CALCVIG', 'VALOR', self.caso_B[4][0])
        self.guardar_cambio(
            'Mmp1_2', 'CALCVIG', 'VALOR', self.caso_B[3][0])
        self.guardar_cambio(
            'a2_2', 'CALCVIG', 'VALOR', self.caso_B[4][1])
        self.guardar_cambio(
            'Mmp2_2', 'CALCVIG', 'VALOR', self.caso_B[3][1])
        self.guardar_cambio(
            'Vp_2', 'CALCVIG', 'VALOR', self.caso_B[5])
        self.guardar_cambio(
            'Ve_1_CasoB', 'CALCVIG', 'VALOR', self.caso_B[6])
        self.guardar_cambio(
            'Ve_2_CasoB', 'CALCVIG', 'VALOR', self.caso_B[7])
        self.guardar_cambio(
            'Ve_1', 'CALCVIG', 'VALOR', self.corte_izquierdo)
        self.guardar_cambio(
            'Ve_2', 'CALCVIG', 'VALOR', self.corte_derecho)
        self.guardar_cambio(
            'Vp', 'CALCVIG', 'VALOR', self.corte_capacidad)
        

    def corte_maximo(self, acero_sup, acero_inf):
        self.profundidades_bloques_whitney = []
        self.momentos_maximos_probables = []
        self.sobrecarga_permanente_viga = float(self.line_edit_sobrecarga_permanente_viga.text())
        self.peso_propio_viga = float(self.label_peso_propio_viga.text())
        self.sobrecarga_variable_viga = float(self.line_edit_sobrecarga_variable_viga.text())
        self.longitud_libre_viga = float(self.line_edit_longitud_libre_viga.text())
        self.base_viga_d = float(self.line_edit_base_viga_d.text())
        self.sobrerresistencia_acero = self.manejo_datos.consultar_dato(
            'Fsr', 'data/base', 'PROPMATS', 'VALOR')
        self.fluencia_acero = self.manejo_datos.consultar_dato(
            'fy', 'data/base', 'PROPMATS', 'VALOR')
        self.resistencia_concreto = self.manejo_datos.consultar_dato(
            'fc', 'data/base', 'PROPMATS', 'VALOR')
        self.altura_util = self.manejo_datos.consultar_dato(
            'd', 'data/base', 'CALCVIG', 'VALOR')
        self.carga_muerta_viga = self.sobrecarga_permanente_viga + self.peso_propio_viga
        self.aceros_requeridos = [acero_sup, acero_inf]
        self.carga_ultima_viga = 1.2*self.carga_muerta_viga + 1.6*self.sobrecarga_variable_viga
        self.corte_gravitacional = self.carga_ultima_viga*self.longitud_libre_viga/2
        #Análisis de casos
        for acero in self.aceros_requeridos:
            self.profundidad_bloque_whitney = self.sobrerresistencia_acero*self.fluencia_acero*acero/(0.85*self.resistencia_concreto*self.base_viga_d)
            self.momento_maximo_probable = (self.sobrerresistencia_acero*self.fluencia_acero*acero*(self.altura_util - self.profundidad_bloque_whitney/2))/100000
            self.profundidades_bloques_whitney.append(self.profundidad_bloque_whitney)
            self.momentos_maximos_probables.append(self.momento_maximo_probable)
        self.corte_por_capacidad = (self.momentos_maximos_probables[0] + self.momentos_maximos_probables[1])/self.longitud_libre_viga
        data = [self.aceros_requeridos, self.carga_ultima_viga, self.corte_gravitacional, self.momentos_maximos_probables, self.profundidades_bloques_whitney, self.corte_por_capacidad]
        return data

    def ayuda_area_transversal_refuerzo(self, nRama, areaEstribo):
        return nRama*areaEstribo/100

    def diseno_estribos(self, Vp, Vd, Pu, bw, h, fc, d, Phiv, AV, fy, db):
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
