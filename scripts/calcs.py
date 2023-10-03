#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 02/02/2023
@author: Ing(c). John J. Arroyo O.
AEUS ver. 1.0
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
        try:
            self.recubrimiento_inferior_viga = float(self.line_edit_recubrimiento_inferior_viga.text())
        except ValueError:
            self.recubrimiento_inferior_viga = 0
        try:
            self.recubrimiento_superior_viga = float(self.line_edit_recubrimiento_superior_viga.text())
        except ValueError:
            self.recubrimiento_superior_viga = 0
        try:
            self.longitud_libre_viga = float(self.line_edit_longitud_libre_viga.text())
        except ValueError:
            self.longitud_libre_viga = 0
        try:
            self.momento_negativo_izquierdo_viga = float(self.line_edit_momento_negativo_izquierdo_viga.text())
        except ValueError:
            self.momento_negativo_izquierdo_viga = 0
        try:
            self.momento_positivo_izquierdo_viga = float(self.line_edit_momento_positivo_izquierdo_viga.text())
        except ValueError:
            self.momento_positivo_izquierdo_viga = 0
        try:
            self.momento_negativo_centro_viga = float(self.line_edit_momento_negativo_centro_viga.text())
        except ValueError:
            self.momento_negativo_centro_viga = 0
        try:
            self.momento_positivo_centro_viga = float(self.line_edit_momento_positivo_centro_viga.text())
        except ValueError:
            self.momento_positivo_centro_viga = 0
        try:
            self.momento_negativo_derecho_viga = float(self.line_edit_momento_negativo_derecho_viga.text())
        except ValueError:
            self.momento_negativo_derecho_viga = 0
        try:
            self.momento_positivo_derecho_viga = float(self.line_edit_momento_positivo_derecho_viga.text())
        except ValueError:
            self.momento_positivo_derecho_viga = 0
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
        self.peso_propio_viga = round((self.base_viga_d/100)*(self.altura_viga_d/100)*2.4, 4) # peso especifico concreto = 2.4Tonf/m3
        # (kgf/cm2)/10 => MPa
        self.cuantia_minima_1 = 0.25*(self.resistencia_concreto/10)**(1/2)/(self.fluencia_acero/10)
        self.cuantia_minima_2 = 1.4/(self.fluencia_acero/10)
        self.cuantia_minima = max(self.cuantia_minima_1, self.cuantia_minima_2)
        self.acero_minimo = self.cuantia_minima*(self.base_viga_d)*(self.altura_util) # cm2
        self.cuantia_balanceada = (0.85*self.parametro_B1*(self.resistencia_concreto/10)/(self.fluencia_acero/10))*(600/(600+(self.fluencia_acero/10)))
        self.cuantia_maxima = min(0.75*self.cuantia_balanceada, 0.025)
        for momento in self.lista_momentos:
            self.acero_momento = self.acero_requerido_momento(momento)
            self.lista_aceros_requeridos_momentos.append(round(self.acero_momento, 2))          # 0
            self.lista_aceros_requeridos_momentos.append(round(self.momento_ultimo, 2))         # 1
            self.lista_aceros_requeridos_momentos.append(round(self.parametro_m, 2))            # 2
            self.lista_aceros_requeridos_momentos.append(round(self.parametro_k, 2))            # 3
            self.lista_aceros_requeridos_momentos.append(round(self.cuantia_requerida, 5))      # 4
            self.lista_aceros_requeridos_momentos.append(self.chequeo_cuantia)                  # 5
            self.lista_aceros_requeridos_momentos.append(round(self.altura_bloque_whitney, 2))  # 6
            self.lista_aceros_requeridos_momentos.append(round(self.altura_eje_neutro, 2))      # 7
            self.lista_aceros_requeridos_momentos.append(round(self.deformacion_acero, 3))      # 8
            self.lista_aceros_requeridos_momentos.append(round(self.momento_resistente, 2))     # 9
        self.label_acero_minimo.setText(str(self.acero_minimo))
        self.label_acero_requerido_1.setText(str(self.lista_aceros_requeridos_momentos[0]))
        self.label_acero_requerido_2.setText(str(self.lista_aceros_requeridos_momentos[10]))
        self.label_acero_requerido_3.setText(str(self.lista_aceros_requeridos_momentos[20]))
        self.label_acero_requerido_4.setText(str(self.lista_aceros_requeridos_momentos[30]))
        self.label_acero_requerido_5.setText(str(self.lista_aceros_requeridos_momentos[40]))
        self.label_acero_requerido_6.setText(str(self.lista_aceros_requeridos_momentos[50]))
        self.label_acero_superior_izquierdo_ductil.setText(str(self.lista_aceros_requeridos_momentos[0]))
        self.label_acero_superior_derecho_ductil.setText(str(self.lista_aceros_requeridos_momentos[40]))
        self.acero_inferior_izquierdo_ductil = self.acero_inferior_ductilidad(
            self.lista_aceros_requeridos_momentos[0], self.lista_aceros_requeridos_momentos[10])
        self.label_acero_inferior_izquierdo_ductil.setText(str(self.acero_inferior_izquierdo_ductil))
        self.acero_inferior_derecho_ductil = self.acero_inferior_ductilidad(
            self.lista_aceros_requeridos_momentos[40], self.lista_aceros_requeridos_momentos[50])
        self.label_acero_inferior_derecho_ductil.setText(str(self.acero_inferior_derecho_ductil))
        self.label_peso_propio_viga.setText(str(self.peso_propio_viga))
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
            'Wpp', 'CALCVIG', 'VALOR', self.peso_propio_viga)
        self.guardar_cambio(
            'Pmin_1', 'CALCVIG', 'VALOR', self.cuantia_minima_1)
        self.guardar_cambio(
            'Pmin_2', 'CALCVIG', 'VALOR', self.cuantia_minima_2)
        self.guardar_cambio(
            'Pmin', 'CALCVIG', 'VALOR', self.cuantia_minima)
        self.guardar_cambio(
            'Asmin', 'CALCVIG', 'VALOR', self.acero_minimo)
        self.guardar_cambio(
            'Pb', 'CALCVIG', 'VALOR', self.cuantia_balanceada)
        self.guardar_cambio(
            'Pmax', 'CALCVIG', 'VALOR', self.cuantia_maxima)
        self.guardar_cambio(
            'As_1', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[0])
        self.guardar_cambio(
            'Mu_1', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[1])
        self.guardar_cambio(
            'm_1', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[2])
        self.guardar_cambio(
            'k_1', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[3])
        self.guardar_cambio(
            'P_1', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[4])
        self.guardar_cambio(
            'check_P_1', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[5])
        self.guardar_cambio(
            'a_1', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[6])
        self.guardar_cambio(
            'c_1', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[7])
        self.guardar_cambio(
            'Et_1', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[8])
        self.guardar_cambio(
            'Mr_1', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[9])
        self.guardar_cambio(
            'As_2', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[10])
        self.guardar_cambio(
            'Mu_2', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[11])
        self.guardar_cambio(
            'm_2', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[12])
        self.guardar_cambio(
            'k_2', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[13])
        self.guardar_cambio(
            'P_2', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[14])
        self.guardar_cambio(
            'check_P_2', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[15])
        self.guardar_cambio(
            'a_2', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[16])
        self.guardar_cambio(
            'c_2', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[17])
        self.guardar_cambio(
            'Et_2', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[18])
        self.guardar_cambio(
            'Mr_2', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[19])
        self.guardar_cambio(
            'As_3', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[20])
        self.guardar_cambio(
            'Mu_3', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[21])
        self.guardar_cambio(
            'm_3', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[22])
        self.guardar_cambio(
            'k_3', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[23])
        self.guardar_cambio(
            'P_3', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[24])
        self.guardar_cambio(
            'check_P_3', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[25])
        self.guardar_cambio(
            'a_3', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[26])
        self.guardar_cambio(
            'c_3', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[27])
        self.guardar_cambio(
            'Et_3', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[28])
        self.guardar_cambio(
            'Mr_3', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[29])
        self.guardar_cambio(
            'As_4', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[30])
        self.guardar_cambio(
            'Mu_4', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[31])
        self.guardar_cambio(
            'm_4', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[32])
        self.guardar_cambio(
            'k_4', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[33])
        self.guardar_cambio(
            'P_4', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[34])
        self.guardar_cambio(
            'check_P_4', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[35])
        self.guardar_cambio(
            'a_4', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[36])
        self.guardar_cambio(
            'c_4', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[37])
        self.guardar_cambio(
            'Et_4', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[38])
        self.guardar_cambio(
            'Mr_4', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[39])
        self.guardar_cambio(
            'As_5', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[40])
        self.guardar_cambio(
            'Mu_5', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[41])
        self.guardar_cambio(
            'm_5', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[42])
        self.guardar_cambio(
            'k_5', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[43])
        self.guardar_cambio(
            'P_5', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[44])
        self.guardar_cambio(
            'check_P_5', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[45])
        self.guardar_cambio(
            'a_5', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[46])
        self.guardar_cambio(
            'c_5', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[47])
        self.guardar_cambio(
            'Et_5', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[48])
        self.guardar_cambio(
            'Mr_5', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[49])
        self.guardar_cambio(
            'As_6', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[50])
        self.guardar_cambio(
            'Mu_6', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[51])
        self.guardar_cambio(
            'm_6', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[52])
        self.guardar_cambio(
            'k_6', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[53])
        self.guardar_cambio(
            'P_6', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[54])
        self.guardar_cambio(
            'check_P_6', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[55])
        self.guardar_cambio(
            'a_6', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[56])
        self.guardar_cambio(
            'c_6', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[57])
        self.guardar_cambio(
            'Et_6', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[58])
        self.guardar_cambio(
            'Mr_6', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[59])
        self.guardar_cambio(
            'As1_sup_req', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[0])
        self.guardar_cambio(
            'As1_inf_req', 'CALCVIG', 'VALOR', self.acero_inferior_izquierdo_ductil)
        self.guardar_cambio(
            'As2_sup_req', 'CALCVIG', 'VALOR', self.lista_aceros_requeridos_momentos[40])
        self.guardar_cambio(
            'As2_inf_req', 'CALCVIG', 'VALOR', self.acero_inferior_derecho_ductil)

    def acero_requerido_momento(self, momento_ultimo_resultado):
        # Tonf-m*10 => kN-m
        momento_ultimo_resultado = momento_ultimo_resultado*10
        # kN-m*(1000N/kN)*(1000mm/m) => N*mm
        self.momento_ultimo = momento_ultimo_resultado*1000*1000
        self.parametro_m = (self.fluencia_acero/10)/(0.85*(self.resistencia_concreto/10))
        # cm*10 => mm
        try:
            self.parametro_k = self.momento_ultimo/(self.base_viga_d*10*((self.altura_util*10)**2))
        except ZeroDivisionError:
            self.parametro_k = 0
        try:
            self.cuantia_requerida = float(1/self.parametro_m*(1-(1-2*self.parametro_m*self.parametro_k/(self.parametro_phib*(self.fluencia_acero/10)))**(1/2)))
        except TypeError:
            self.cuantia_requerida = 0
        if self.cuantia_requerida <= self.cuantia_minima:
            self.chequeo_cuantia = 'MINIMO'
            self.acero_calculado = self.acero_minimo
        elif self.cuantia_requerida >= self.cuantia_minima and self.cuantia_requerida <= self.cuantia_maxima:
            self.chequeo_cuantia = 'DISEÑO'
            self.acero_calculado = self.cuantia_requerida*(self.base_viga_d)*(self.altura_util) # cm2
        else:
            self.chequeo_cuantia = 'SUPERA LIMITES'
            self.acero_calculado = 0
        if self.acero_calculado != 0:
            self.acero_requerido = self.acero_calculado
            self.altura_bloque_whitney = (self.acero_calculado*100)*(self.fluencia_acero/10)/(0.85*(self.resistencia_concreto/10)*(self.base_viga_d*10))
            self.altura_eje_neutro = self.altura_bloque_whitney/self.parametro_B1
            self.deformacion_acero = ((self.altura_util*10)-self.altura_eje_neutro)/self.altura_eje_neutro*self.deformacion_ultima_concreto
            if self.deformacion_acero <= 0.005:
                self.acero_requerido = 0
            self.momento_resistente = self.parametro_phib*(self.acero_calculado*100)*(self.fluencia_acero/10)*(self.altura_util*10-self.altura_bloque_whitney/2)
            if self.momento_ultimo > round(self.momento_resistente, 0):
                self.acero_requerido = 0
        else:
            self.acero_requerido = 0
            self.altura_bloque_whitney = 0
            self.altura_eje_neutro = 0
            self.deformacion_acero = 0
            self.momento_resistente = 0
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
        self.label_acero_superior_izquierdo_impuesto_2.setText(str(self.acero_superior_izquierdo_impuesto))
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
        self.label_acero_superior_derecho_impuesto_2.setText(str(self.acero_superior_derecho_impuesto))
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
        self.label_acero_inferior_derecho_impuesto_2.setText(str(self.acero_inferior_derecho_impuesto))
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
        self.label_acero_inferior_izquierdo_impuesto_2.setText(str(self.acero_inferior_izquierdo_impuesto))
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
        self.label_acero_superior_centro_impuesto_2.setText(str(self.acero_superior_centro_impuesto))
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
        self.label_acero_inferior_centro_impuesto_2.setText(str(self.acero_inferior_centro_impuesto))
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
        try:
            self.corte_ultimo_viga = float(self.line_edit_corte_ultimo_viga.text())
        except ValueError:
            self.corte_ultimo_viga = 0
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
        self.guardar_cambio(
            'Vu', 'CALCVIG', 'VALOR', self.corte_ultimo_viga)

    def corte_maximo(self, acero_sup, acero_inf):
        self.profundidades_bloques_whitney = []
        self.momentos_maximos_probables = []
        try:
            self.sobrecarga_permanente_viga = float(self.line_edit_sobrecarga_permanente_viga.text())
        except ValueError:
            self.sobrecarga_permanente_viga = 0
        self.peso_propio_viga = float(self.label_peso_propio_viga.text())
        try:
            self.sobrecarga_variable_viga = float(self.line_edit_sobrecarga_variable_viga.text())
        except ValueError:
            self.sobrecarga_variable_viga = 0
        try:
            self.longitud_libre_viga = float(self.line_edit_longitud_libre_viga.text())
        except ValueError:
            self.longitud_libre_viga = 0
        try:
            self.base_viga_d = float(self.line_edit_base_viga_d.text())
        except ValueError:
            self.base_viga_d = 0
        self.sobrerresistencia_acero = self.manejo_datos.consultar_dato(
            'Fsr', 'data/base', 'PROPMATS', 'VALOR')
        self.minoracion_resistencia_corte = self.manejo_datos.consultar_dato(
            'phiv', 'data/base', 'PROPMATS', 'VALOR')
        self.fluencia_acero = self.manejo_datos.consultar_dato(
            'fy', 'data/base', 'PROPMATS', 'VALOR')
        self.resistencia_concreto = self.manejo_datos.consultar_dato(
            'fc', 'data/base', 'PROPMATS', 'VALOR')
        self.altura_util = self.manejo_datos.consultar_dato(
            'd', 'data/base', 'CALCVIG', 'VALOR')
        self.carga_muerta_viga = self.sobrecarga_permanente_viga + self.peso_propio_viga # tonf/m
        self.aceros_requeridos = [acero_sup, acero_inf]
        self.carga_ultima_viga = 1.2*self.carga_muerta_viga + 1.6*self.sobrecarga_variable_viga # tonf/m
        self.corte_gravitacional = self.carga_ultima_viga*self.longitud_libre_viga/2 # tonf
        # Análisis de casos
        for acero in self.aceros_requeridos:
            try:
                self.profundidad_bloque_whitney = self.sobrerresistencia_acero*self.fluencia_acero*acero/(0.85*self.resistencia_concreto*self.base_viga_d)
            except ZeroDivisionError:
                self.profundidad_bloque_whitney = 0.0
            self.momento_maximo_probable = (self.sobrerresistencia_acero*self.minoracion_resistencia_corte*self.fluencia_acero*acero*(self.altura_util - self.profundidad_bloque_whitney/2))/100000 # tonf-m
            self.profundidades_bloques_whitney.append(self.profundidad_bloque_whitney)
            self.momentos_maximos_probables.append(self.momento_maximo_probable)
        try:
            self.corte_por_capacidad = (self.momentos_maximos_probables[0] + self.momentos_maximos_probables[1])/self.longitud_libre_viga # tonf
        except ZeroDivisionError:
            self.corte_por_capacidad = 0.0
        data = [self.aceros_requeridos, self.carga_ultima_viga, self.corte_gravitacional, self.momentos_maximos_probables, self.profundidades_bloques_whitney, self.corte_por_capacidad]
        self.guardar_cambio(
            'Wscp', 'CALCVIG', 'VALOR', self.sobrecarga_permanente_viga)
        self.guardar_cambio(
            'Wcv', 'CALCVIG', 'VALOR', self.sobrecarga_variable_viga)
        self.guardar_cambio(
            'Wcp', 'CALCVIG', 'VALOR', self.carga_muerta_viga)
        self.guardar_cambio(
            'Wpp', 'CALCVIG', 'VALOR', self.peso_propio_viga)
        return data

    def ayuda_area_transversal_refuerzo(self):
        try:
            self.n_ramas = int(self.combo_box_n_ramas.currentText())
        except ValueError:
            self.n_ramas = 0
        self.diametro_estribo = self.combo_box_diametro_estribo.currentText()
        if self.diametro_estribo != '':
            self.area_estribo = self.manejo_datos.consultar_dato(
                self.diametro_estribo, 'data/base', 'BARS', 'AREA')
        else:
            self.area_estribo = 0
        self.area_transversal_refuerzo = self.n_ramas*self.area_estribo/100
        self.label_area_transversal_refuerzo.setText(str(self.area_transversal_refuerzo))
        self.label_area_transversal_refuerzo_2.setText(str(self.area_transversal_refuerzo))
        self.guardar_cambio(
            'AV', 'CALCVIG', 'VALOR', self.area_transversal_refuerzo)
        self.diseno_estribos()
    
    def guardar_fuerza_axial(self):
        try:
            self.fuerza_axial = float(self.line_edit_fuerza_axial.text())
        except ValueError:
            self.fuerza_axial = 0
        self.guardar_cambio(
            'Pu', 'CALCVIG', 'VALOR', self.fuerza_axial)
        self.diseno_estribos()

    def diseno_estribos(self):
        self.corte_capacidad = self.manejo_datos.consultar_dato(
            'Vp', 'data/base', 'CALCVIG', 'VALOR')
        self.corte_izquierdo = self.manejo_datos.consultar_dato(
            'Ve_1', 'data/base', 'CALCVIG', 'VALOR')
        self.corte_derecho = self.manejo_datos.consultar_dato(
            'Ve_2', 'data/base', 'CALCVIG', 'VALOR')
        self.corte_ultimo_viga = self.manejo_datos.consultar_dato(
            'Vu', 'data/base', 'CALCVIG', 'VALOR')
        self.base_viga_d = self.manejo_datos.consultar_dato(
            'bw', 'data/base', 'DATVIG', 'VALOR')
        self.altura_viga_d = self.manejo_datos.consultar_dato(
            'h', 'data/base', 'DATVIG', 'VALOR')
        self.resistencia_concreto = self.manejo_datos.consultar_dato(
            'fc', 'data/base', 'PROPMATS', 'VALOR')
        self.fluencia_acero = self.manejo_datos.consultar_dato(
            'fy', 'data/base', 'PROPMATS', 'VALOR')
        self.fuerza_axial = self.manejo_datos.consultar_dato(
            'Pu', 'data/base', 'CALCVIG', 'VALOR')
        self.altura_util = self.manejo_datos.consultar_dato(
            'd', 'data/base', 'CALCVIG', 'VALOR')
        self.minoracion_resistencia_corte = self.manejo_datos.consultar_dato(
            'phiv', 'data/base', 'PROPMATS', 'VALOR')
        self.area_transversal_refuerzo = self.manejo_datos.consultar_dato(
            'AV', 'data/base', 'CALCVIG', 'VALOR')
        self.acero_superior_izquierdo_impuesto = self.manejo_datos.consultar_dato(
            'As1_sup', 'data/base', 'CALCVIG', 'VALOR')
        self.acero_inferior_izquierdo_impuesto = self.manejo_datos.consultar_dato(
            'As1_inf', 'data/base', 'CALCVIG', 'VALOR')
        self.acero_superior_derecho_impuesto = self.manejo_datos.consultar_dato(
            'As2_sup', 'data/base', 'CALCVIG', 'VALOR')
        self.acero_inferior_derecho_impuesto = self.manejo_datos.consultar_dato(
            'As2_inf', 'data/base', 'CALCVIG', 'VALOR')
        self.diametro_mayor_barra_longitudinal = 19.1
        self.diametro_barra_estribo = 9.5
        self.separacion_estribo = 100
        self.separacion_minima_estribo = 50
        self.chequeo_estribo = 'cumple'
        self.corte_maximo_probable = max(self.corte_izquierdo, self.corte_derecho)
        self.corte_diseno = max(self.corte_ultimo_viga, self.corte_maximo_probable)
        try:
            self.relacion_cortes = round(self.corte_capacidad/self.corte_diseno, 2)
        except ZeroDivisionError:
            self.relacion_cortes = 0.0
        self.area_gruesa = self.base_viga_d*self.altura_viga_d #cm2
        self.producto = self.area_gruesa*self.resistencia_concreto/20000 # tonf
        if self.relacion_cortes>=0.5 and self.fuerza_axial<=self.producto:
            self.corte_resistente_concreto = 0
        else:
            try:
                self.corte_resistente_concreto = (0.17*((self.resistencia_concreto/10)**(1/2))*(self.base_viga_d*10)*(self.altura_viga_d*10))/10000 # tonf
            except ZeroDivisionError:
                self.corte_resistente_concreto = 0.0
        if self.corte_diseno >= (self.corte_resistente_concreto*self.minoracion_resistencia_corte)/2 and self.corte_diseno <= (self.corte_resistente_concreto*self.minoracion_resistencia_corte):
            self.separacion_minima_estribo = min(
                                        16*self.area_transversal_refuerzo*(self.fluencia_acero/10)/(self.base_viga_d*(self.resistencia_concreto/10)**(1/2)),
                                        2.86*self.area_transversal_refuerzo*(self.fluencia_acero/10)/self.base_viga_d,
                                        self.altura_util/2)
        elif self.corte_diseno >= (self.corte_resistente_concreto*self.minoracion_resistencia_corte):
            self.corte_resistente_acero_1 = self.corte_diseno - self.corte_resistente_concreto
            self.corte_resistente_acero_2 = ((self.area_transversal_refuerzo*100)*(self.fluencia_acero/10)*(self.altura_util*10)/self.separacion_estribo)/10000
            self.corte_resistente_acero = max(self.corte_resistente_acero_1, self.corte_resistente_acero_2)
            self.limite_superior_corte_resistente_acero = (0.66*((self.resistencia_concreto/10)**(1/2))*(self.base_viga_d*10)*(self.altura_viga_d*10))/10000
            if self.corte_resistente_acero <= self.limite_superior_corte_resistente_acero:
                self.separacion_estribo = round((self.minoracion_resistencia_corte*self.area_transversal_refuerzo*100*(self.fluencia_acero/10)*self.altura_util*10/(self.corte_resistente_acero*10000))/10, 2)
            else:
                self.chequeo_estribo = 'NO cumple'
        else:
            self.chequeo_estribo = 'NO cumple'
        self.separacion_maxima_norma = min(self.altura_util/4, 8*(self.diametro_mayor_barra_longitudinal/10), 24*self.diametro_barra_estribo, 30)
        self.separacion_maxima_requerida = min(self.separacion_estribo, self.separacion_maxima_norma)
        self.longitud_confinamiento = 2*self.altura_viga_d
        self.separacion_maxima_inconfinada = self.altura_util/2
        self.separacion_maxima_inconfinada_solapada = min(10, self.altura_util/4)
        self.label_corte_diseno.setText(str(self.corte_diseno))
        self.label_corte_concreto.setText(str(self.corte_resistente_concreto))
        self.label_corte_acero.setText(str(self.corte_resistente_acero))
        self.label_separacion_estribo.setText(str(self.separacion_estribo))
        self.label_separacion_maxima_norma.setText(str(self.separacion_maxima_norma))
        self.label_longitud_confinamiento.setText(str(self.longitud_confinamiento))
        self.label_separacion_maxima_inconfinada.setText(str(self.separacion_maxima_inconfinada))
        self.label_separacion_maxima_inconfinada_solapada.setText(str(self.separacion_maxima_inconfinada_solapada))
        self.guardar_cambio(
            'Ve', 'CALCVIG', 'VALOR', self.corte_maximo_probable)
        self.guardar_cambio(
            'Vd', 'CALCVIG', 'VALOR', self.corte_diseno)
        self.guardar_cambio(
            'Vc', 'CALCVIG', 'VALOR', self.corte_resistente_concreto)
        self.guardar_cambio(
            'Vs', 'CALCVIG', 'VALOR', self.corte_resistente_acero)
        self.guardar_cambio(
            'Vs1', 'CALCVIG', 'VALOR', self.corte_resistente_acero_1)
        self.guardar_cambio(
            'Vs2', 'CALCVIG', 'VALOR', self.corte_resistente_acero_2)
        self.guardar_cambio(
            'RC', 'CALCVIG', 'VALOR', self.relacion_cortes)
        self.guardar_cambio(
            'Pc', 'CALCVIG', 'VALOR', self.producto) 
        self.guardar_cambio(
            'Ag', 'CALCVIG', 'VALOR', self.area_gruesa)        
        self.guardar_cambio(
            'Smcal', 'CALCVIG', 'VALOR', self.separacion_estribo)
        self.guardar_cambio(
            'Smnorma', 'CALCVIG', 'VALOR', self.separacion_maxima_norma)
        self.guardar_cambio(
            'Smreq', 'CALCVIG', 'VALOR', self.separacion_maxima_requerida)
        self.guardar_cambio(
            'Lc', 'CALCVIG', 'VALOR', self.longitud_confinamiento)
        self.guardar_cambio(
            'Sgm', 'CALCVIG', 'VALOR', self.separacion_maxima_inconfinada)
        self.guardar_cambio(
            'Sgsm', 'CALCVIG', 'VALOR', self.separacion_maxima_inconfinada_solapada)
        self.guardar_cambio(
            'check_estribo', 'CALCVIG', 'VALOR', self.chequeo_estribo)

    def guardar_separaciones(self):
        try:
            self.separacion_definitiva = float(self.line_edit_separacion_definitiva.text())
        except ValueError:
            self.separacion_definitiva = 0
        try:
            self.separacion_inconfinada = float(self.line_edit_separacion_inconfinada.text())
        except ValueError:
            self.separacion_inconfinada = 0
        try:
            self.separacion_inconfinada_solapada = float(self.line_edit_separacion_inconfinada_solapada.text())
        except ValueError:
            self.separacion_inconfinada_solapada = 0
        self.label_separacion_definitiva.setText(str(self.separacion_definitiva))
        self.label_separacion_inconfinada.setText(str(self.separacion_inconfinada))
        self.label_separacion_inconfinada_solapada.setText(str(self.separacion_inconfinada_solapada))
        self.guardar_cambio(
            'S', 'CALCVIG', 'VALOR', self.separacion_definitiva)
        self.guardar_cambio(
            'Sg', 'CALCVIG', 'VALOR', self.separacion_inconfinada)
        self.guardar_cambio(
            'Sgs', 'CALCVIG', 'VALOR', self.separacion_inconfinada_solapada)