#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 11/06/2020
@author: Ing. John Arroyo
DiVi ver. 1.0
"""
class CalculosInternos():

    def revisionLimitesDimensionales(self, bw, h, r, Ln, dataBase, base):
        self.d = h - r #Altura útil de la sección
        self.chequeoLimite_1 = 4*self.d/100 #se lleva a metros
        self.chequeoLimite_2 = 0.3*h
        self.datos=[
            ('d', self.d), #cm
            ('chk1', self.chequeoLimite_1), #m
            ('chk2', self.chequeoLimite_2) #mm
        ]

        count = 0
        for self.dato in self.datos:
            base.guardarDato(self.dato[count], dataBase, 'VCALC', 'VALOR',str(self.dato[count+1]))
            count+1
        return self.d
    
    def aceroMinimo(self, bw, d, fy, fc, dataBase, base):
        self.Asmin_1 = 14/fy*bw*d
        self.Asmin_2 = 0.80*(fc)**(1/2)/fy*bw*d
        self.Asmin = max(self.Asmin_1, self.Asmin_2)
        self.datos = [('Asmin_1', self.Asmin_1), 
                    ('Asmin_2', self.Asmin_2), 
                    ('Asmin', self.Asmin)
                    ]
        count = 0
        for self.dato in self.datos:
            base.guardarDato(self.dato[count], dataBase, 'VCALC', 'VALOR',str(self.dato[count+1]))
            count+1
        return self.Asmin
    
    def aceroRequeridoMomento(self, Muresult, d, B1, fc, fy, phib, bw, Ecu, Esmin, Asmin):
        self.Mu = Muresult*1000*100 #Momento último, se convierte a kgf-cm
        self.a = d - (d**2 - 2*self.Mu/(0.85*fc*phib*bw))**(1/2) #Profundidad del bloque equivalente de whitney (cm)
        self.c = self.a/B1 #Profundidad del eje neutro (cm)
        self.cmax = (Ecu/(Ecu+Esmin))*d #Profundidad máxima del eje neutro para garantizar una falla controlada por tracción (cm)
        if self.c <= self.cmax:
            self.Ascalc = self.Mu/(phib*fy*(d-self.a/2))
            self.Asreq = max(self.Ascalc, Asmin)
        else:
            self.Ascalc = 0
            self.Asreq = 0
        return self.Asreq, self.a, self.c, self.cmax,self.Ascalc
    
    def ayudaBarrasRefuerzo(self, cantidad1, cantidad2, area1, area2):
        self.ayuda = (cantidad1*area1 + cantidad2*area2)/100
        return self.ayuda
    
    def ayudaAreaTransversalRefuerzo(self, nRama, areaEstribo):
        return nRama*areaEstribo/100

    
    def aceroDuctilidadInferior(self, aceroSuperior, aceroInferiorRequerido):
        self.aceroInferior = max(aceroSuperior/2, aceroInferiorRequerido)
        return self.aceroInferior
    
    def corteMaximo(self, Wcp, Wcv, Ln, Fsr, fy, Fc, bw, acero1, acero2, h, r, dp, Fcv):
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
    
    def disenoEstribos(self, Vp, Vd, Pu,bw,h,fc,d,Phiv,AV,fy,db):
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






