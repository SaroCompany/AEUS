import time
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from scripts.mem import DatosMemoria
from scripts.data import ConexionBaseDatos
import easygui

class GenerarReportePDF():

    def __init__(self):
        self.logo = 'img/logoSARO.png'
        self.img_momentos = 'img/DetalleMomentos.png'
        self.img_definicion = 'img/DefinicionResistenciaNominalFlexion.png'
        self.img_ductilidad = 'img/RequisitosAceroLongitudinalDuctilidad.png'
        self.img_Mmp_CasoA = 'img/MomentoMaximoProbableCasoA.png'
        self.img_Mmp_CasoB = 'img/MomentoMaximoProbableCasoB.png'
        self.img_Vg_CasoA = 'img/CorteMaximoProbableCasoA.png'
        self.img_Vg_CasoB = 'img/CorteMaximoProbableCasoB.png'
        self.img_disposicion_acero_transversal = 'img/DisposicionAceroTransversal.png'
        self.img_ubicacion_solapes_acero_longitudinal = 'img/UbicacionSolapesAceroLongitudinal.png'
        self.manejo_datos = ConexionBaseDatos()
        self.ubicacion_base = 'data/base'
        self.datos_memoria = DatosMemoria(
            self.ubicacion_base, self.manejo_datos)
    
    def insertar_texto(self, Story, styles, text):
        ptext = '<font size="12">%s</font>' %text
        Story.append(Paragraph(ptext, styles))

    
    def insertar_texto_acero_requerido_momento(self, Story, styles, Mu, m, k, P, check_P, As, a, c, Et, Mr):
        self.insertar_texto(Story, styles['Justify'], f'Mu = {round(Mu, 2)} N-mm')
        self.insertar_texto(Story, styles['Justify'], f'm = fy/(0.85*fc) = {round(m, 5)}')
        self.insertar_texto(Story, styles['Justify'], f'k = Mu/(b*d^2) = {round(k, 2)} MPa')
        self.insertar_texto(Story, styles['Justify'], f'P = 1/m*(1-(1-2*m*k/(Phib*fy))^(1/2)) = {round(P, 5)}')
        self.insertar_texto(Story, styles['Justify'], f'Cuantia requerida = {check_P}')
        self.insertar_texto(Story, styles['Justify'], f'As = P*b*d = {round(As, 5)} cm2')
        self.insertar_texto(Story, styles['Justify'], f'a = As*fy/(0.85*fc*b) = {round(a, 5)} mm')
        self.insertar_texto(Story, styles['Justify'], f'c = a/B1 = {round(c, 5)} mm')
        self.insertar_texto(Story, styles['Justify'], f'Et = (d-c)/c*Ecu = {round(Et, 3)} >= 0.005')
        if Et >= 0.005:
            self.insertar_texto(Story, styles['Justify'], 'Falla dúctil')
        else:
            self.insertar_texto(Story, styles['Justify'], 'NO CUMPLE')
        self.insertar_texto(Story, styles['Justify'], f'Mr = Phib*As*fy*(d-a/2) = {round(Mr, 2)} N-mm >= Mu')
        if Mr >= Mu:
            self.insertar_texto(Story, styles['Justify'], 'CUMPLE')
        else:
            self.insertar_texto(Story, styles['Justify'], 'NO CUMPLE')
    '''
    # PARA UNIDADES TONF
    def insertar_texto_acero_requerido_momento(self, Story, styles, Mu, a, c, cmax, Asreq):
        self.insertar_texto(Story, styles['Justify'], f'Mu = {round(Mu, 2)} Tonf-m')
        self.insertar_texto(Story, styles['Justify'], f'a = d-(d^2-2*Mu/(0.85*fc*Phib*bw))^(1/2) = {round(a, 2)} cm')
        self.insertar_texto(Story, styles['Justify'], f'c = a/B1 = {round(c, 2)} cm')
        self.insertar_texto(Story, styles['Justify'], f'cmax = Ecu*d/(Ecu+Esmin) = {round(cmax, 2)} cm')
        if c <= cmax:
            self.insertar_texto(Story, styles['Justify'], 'c <= cmax : Falla controlada por tracción')
        else:
            self.insertar_texto(Story, styles['Justify'], 'c > cmax : Aumentar la sección')
        self.insertar_texto(Story, styles['Justify'], f'Asreq = max( Mu/(Phib*fy*(d-a/2)), Asmin) = {round(Asreq, 2)} cm2')
    '''
    def insertar_texto_acero_centro_ductilidad(self, Story, styles, ide, AsIzq, AsDer, AsCenReq, AsCenDuc, AsCen):
        self.insertar_texto(Story, styles['Justify'], f'As{ide}Izq impuesto = {AsIzq} ')
        self.insertar_texto(Story, styles['Justify'], f'As{ide}Der impuesto = {AsDer} ')
        self.insertar_texto(Story, styles['Justify'], f'As{ide}Cen requerido = {AsCenReq} ')
        self.insertar_texto(Story, styles['Justify'], f'As{ide}Cen ductil = max(AsCenReq, AsIzq/4, AsDer/4) = {AsCenDuc} ')
        self.insertar_texto(Story, styles['Justify'], f'As{ide}Cen impuesto = {AsCen} ')

    def insertar_texto_acero_extremo_ductilidad(self, Story, styles, iden, as_supreq, as_sup, as_induc, as_inf):
        self.insertar_texto(Story, styles['Justify'], f'As{iden}Sup requerido = {round(as_supreq, 2)} cm2')
        self.insertar_texto(Story, styles['Justify'], f'As{iden}Sup suministrado = {round(as_sup, 2)} cm2')
        self.insertar_texto(Story, styles['Justify'], f'As{iden}Inf requerido = max(AsInfReq, AsSup/2) = {round(as_induc, 2)} cm2')
        self.insertar_texto(Story, styles['Justify'], f'As{iden}Inf suministrado = {round(as_inf, 2)} cm2')
    
    def insertar_texto_casos_corte(self, Story, styles, Wu, Vg, a1, Mmp1, a2, Mmp2, Vp):
        self.insertar_texto(Story, styles['Justify'], f'Wu = 1.2*Wcp + 1.6*Wcv = {round(Wu, 2)} tonf/m')
        self.insertar_texto(Story, styles['Justify'], f'Vg = Wu*Ln/2 = {round(Vg, 2)} tonf')
        self.insertar_texto(Story, styles['Justify'], f'a1 = Fsr*fy*As1_sup/(0.85*fc*bw) = {round(a1, 2)} cm')
        self.insertar_texto(Story, styles['Justify'], f'Mmp1 = Fsr*fy*As1_sup*(d-a/2) = {round(Mmp1, 2)} tonf-m')
        self.insertar_texto(Story, styles['Justify'], f'a2 = Fsr*fy*As1_inf/(0.85*fc*bw) = {round(a2, 2)} cm')
        self.insertar_texto(Story, styles['Justify'], f'Mmp2 = Fsr*fy*As1_inf*(d-a/2) = {round(Mmp2, 2)} tonf-m')
        self.insertar_texto(Story, styles['Justify'], f'Vp = (Mmp1+Mmp2)/Ln = {round(Vp, 2)} tonf')

    def crear_pdf_viga(self):
        pdfPath = easygui.filesavebox(filetypes=["*.pdf"], default="*.pdf")
        self.doc = SimpleDocTemplate(pdfPath,pagesize=letter,
                                                rightMargin=2*cm,leftMargin=4*cm,
                                                topMargin=3*cm,bottomMargin=3*cm)
        Story=[]
        im = Image(self.logo, 2*cm, 2*cm)
        im_Mom = Image(self.img_momentos, 14*cm, 5*cm)
        im_Def = Image(self.img_definicion, 15*cm, 6*cm)
        im_Duct = Image(self.img_ductilidad, 15*cm, 6*cm)
        im_Mmp_A = Image(self.img_Mmp_CasoA, 15*cm, 6*cm)
        im_Mmp_B = Image(self.img_Mmp_CasoB, 15*cm, 6*cm)
        im_Vg_A = Image(self.img_Vg_CasoA, 15*cm, 6*cm)
        im_Vg_B = Image(self.img_Vg_CasoB, 15*cm, 6*cm)
        im_dis_acero_tran = Image(self.img_disposicion_acero_transversal, 15*cm, 8*cm)
        im_ubi_solapes_acero_long = Image(self.img_ubicacion_solapes_acero_longitudinal, 15*cm, 6*cm)
        styles=getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
        styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
        self.insertar_texto(Story, styles['Center'], 'AEUS - ASISTENTE ESTRUCTURAL')
        self.insertar_texto(Story, styles['Center'], 'UNIVERSIDAD DE SUCRE')
        Story.append(Spacer(1, 12))
        Story.append(im)
        Story.append(Spacer(1, 24))
        self.insertar_texto(Story, styles['Center'], 'DISEÑO DE UNA VIGA DE PÓRTICO RESISTENTE A MOMENTO')
        self.insertar_texto(Story, styles['Center'], 'CON DISIPACIÓN ESPECIAL DE ENERGÍA')
        self.insertar_texto(Story, styles['Center'], 'Aplicación de la norma NSR-10 - Colombia')
        Story.append(Spacer(1, 24))
        self.insertar_texto(Story, styles['Justify'], '1 - DATOS')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '1.1 - Datos de la viga')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], f'Ancho de la viga (bw) = {self.datos_memoria.base_viga_d} cm')
        self.insertar_texto(Story, styles['Justify'], f'Altura de la viga (h) = {self.datos_memoria.altura_viga_d} cm')
        self.insertar_texto(Story, styles['Justify'], f'Recubrimiento inferior (r) = {self.datos_memoria.recubrimiento_inferior_viga} cm')
        self.insertar_texto(Story, styles['Justify'], f'Recubrimiento superior (rp) = {self.datos_memoria.recubrimiento_superior_viga} cm')
        self.insertar_texto(Story, styles['Justify'], f'Longitud libre (Ln) = {self.datos_memoria.longitud_libre_viga} m')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '1.2 - Datos de los materiales')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], f'Resistencia del concreto (fc) = {self.datos_memoria.resistencia_concreto} Kgf/cm2')
        self.insertar_texto(Story, styles['Justify'], f'Módulo de elasticidad del concreto (Ec) = {self.datos_memoria.modulo_elasticidad_concreto} Kgf/cm2')
        self.insertar_texto(Story, styles['Justify'], f'Peso especifico del concreto armado (Yc) = {self.datos_memoria.peso_propio_concreto} Kgf/m3')
        self.insertar_texto(Story, styles['Justify'], f'Deformación última del concreto (Ecu) = {self.datos_memoria.deformacion_ultima_concreto}')
        self.insertar_texto(Story, styles['Justify'], f'Parámetro B1 (B1) = {self.datos_memoria.parametro_B1}')
        self.insertar_texto(Story, styles['Justify'], f'Factor de minoración para resistencia al corte (Phiv) = {self.datos_memoria.minoracion_resistencia_corte}')
        self.insertar_texto(Story, styles['Justify'], f'Factor de minoración para resistencia a flexión (Phib) = {self.datos_memoria.minoracion_resistencia_flexion}')
        self.insertar_texto(Story, styles['Justify'], f'Esfuerzo cedente del acero de refuerzo (fy) = {self.datos_memoria.fluencia_acero} Kgf/cm2')
        self.insertar_texto(Story, styles['Justify'], f'Módulo de elasticidad del acero (Es) = {self.datos_memoria.elasticidad_acero} Kgf/cm2')
        self.insertar_texto(Story, styles['Justify'], f'Deformación cedente del acero (Ey) = {self.datos_memoria.deformacion_cedente_acero}')
        self.insertar_texto(Story, styles['Justify'], f'Deformación mínima del acero (Esmin) = {self.datos_memoria.deformacion_minima_acero}')
        self.insertar_texto(Story, styles['Justify'], f'Factor de sobre-resistencia del acero (Fsr) = {self.datos_memoria.sobrerresistencia_acero}')
        Story.append(Spacer(1, 24))
        self.insertar_texto(Story, styles['Justify'], '2 - REVISIÓN')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '2.1 - Revisión de límites dimensionales')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], 'La luz libre de la viga no debe ser menor que cuatro veces la altura útil de la \
                                                    sección:')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], f'd = h - r = {self.datos_memoria.altura_util} cm')
        self.insertar_texto(Story, styles['Justify'], f'4*d = {self.datos_memoria.chequeo_limite_1} m')
        if self.datos_memoria.longitud_libre_viga >= self.datos_memoria.chequeo_limite_1:
            self.insertar_texto(Story, styles['Justify'], f'{self.datos_memoria.longitud_libre_viga} >= {self.datos_memoria.chequeo_limite_1}  CUMPLE')
        else:
            self.insertar_texto(Story, styles['Justify'], f'{self.datos_memoria.longitud_libre_viga} < {self.datos_memoria.chequeo_limite_1}  NO CUMPLE')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], 'El ancho de la sección debe ser al menos igual al menor valor entre 0.3 veces la \
                                                    altura de la misma y 25 cm:')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], f'0.3*h = {self.datos_memoria.chequeo_limite_2} cm')
        self.minChk = min(25, self.datos_memoria.chequeo_limite_2)
        if self.datos_memoria.base_viga_d >= self.minChk:
            self.insertar_texto(Story, styles['Justify'], f'bw >= {self.minChk} CUMPLE')
        else:
            self.insertar_texto(Story, styles['Justify'], f'bw < {self.minChk} NO CUMPLE')
        Story.append(Spacer(1, 24))
        self.insertar_texto(Story, styles['Justify'], '3 - DISEÑO')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1 - Diseño del refuerzo longitudinal')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1.1 - Momentos últimos provenientes del análisis')
        Story.append(Spacer(1, 12))
        Story.append(im_Mom)
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], f'Mu_neg_izq = {self.datos_memoria.momento_negativo_izquierdo_viga} Tonf-m')
        self.insertar_texto(Story, styles['Justify'], f'Mu_pos_izq = {self.datos_memoria.momento_positivo_izquierdo_viga} Tonf-m')
        self.insertar_texto(Story, styles['Justify'], f'Mu_neg_cen = {self.datos_memoria.momento_negativo_centro_viga} Tonf-m')
        self.insertar_texto(Story, styles['Justify'], f'Mu_pos_cen = {self.datos_memoria.momento_positivo_centro_viga} Tonf-m')
        self.insertar_texto(Story, styles['Justify'], f'Mu_neg_der = {self.datos_memoria.momento_negativo_derecho_viga} Tonf-m')
        self.insertar_texto(Story, styles['Justify'], f'Mu_pos_der = {self.datos_memoria.momento_positivo_derecho_viga} Tonf-m')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1.2 - Definición de la resistencia nominal a flexión')
        Story.append(Spacer(1, 12))
        Story.append(im_Def)
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1.3 - Cuantia mínima y máxima')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], f'Pmin_1 = 1.4/fy = {round(self.datos_memoria.cuantia_minima_1, 5)}')
        self.insertar_texto(Story, styles['Justify'], f'Pmin_2 = 0.25*(fc^(1/2))/fy = {round(self.datos_memoria.cuantia_minima_2, 5)}')
        self.insertar_texto(Story, styles['Justify'], f'Pmin = max(Pmin_1, Pmin_2) = {round(self.datos_memoria.cuantia_minima, 5)}')
        self.insertar_texto(Story, styles['Justify'], f'Pb = 0.85*B1*fc/fy*(600/(600+fy)) = {round(self.datos_memoria.cuantia_balanceada, 5)}')
        self.insertar_texto(Story, styles['Justify'], f'Pmax = 0.75*Pb = {round(self.datos_memoria.cuantia_maxima, 5)}')
        '''
        # PARA UNIDADES TONF
        self.insertar_texto(Story, styles['Justify'], f'Asmin_1 = 14*bw*d/fy = {round(self.datos_memoria.acero_minimo_1, 2)} cm2')
        self.insertar_texto(Story, styles['Justify'], f'Asmin_2 = 0.8*(fc^(1/2))*bw*d/fy = {round(self.datos_memoria.acero_minimo_2, 2)} cm2')
        self.insertar_texto(Story, styles['Justify'], f'Asmin = max(Asmin_1, Asmin_2) = {round(self.datos_memoria.acero_minimo, 2)} cm2')
        '''
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1.4 - Acero longitudinal requerido conforme al análisis')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1.4.1 - Acero requerido para el momento negativo izquierdo')
        Story.append(Spacer(1, 12))
        
        self.insertar_texto_acero_requerido_momento(Story, styles,
            self.datos_memoria.momento_ultimo_1,
            self.datos_memoria.parametro_m_1,
            self.datos_memoria.parametro_k_1,
            self.datos_memoria.cuantia_requerida_1,
            self.datos_memoria.chequeo_cuantia_1,
            self.datos_memoria.acero_requerido_1,
            self.datos_memoria.altura_bloque_whitney_1,
            self.datos_memoria.altura_eje_neutro_1,
            self.datos_memoria.deformacion_acero_1,
            self.datos_memoria.momento_resistente_1)
        '''
        # PARA UNIDADES TONF
        self.insertar_texto_acero_requerido_momento(Story, styles,
            self.datos_memoria.momento_negativo_izquierdo_viga,
            self.datos_memoria.profundidad_bloque_whitney_1,
            self.datos_memoria.profundidad_eje_neutro_1,
            self.datos_memoria.profundidad_eje_neutro_maximo_falla_traccion_1,
            self.datos_memoria.acero_requerido_1)
        '''
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1.4.2 - Acero requerido para el momento positivo izquierdo')
        Story.append(Spacer(1, 12))
        self.insertar_texto_acero_requerido_momento(Story, styles,
            self.datos_memoria.momento_ultimo_2,
            self.datos_memoria.parametro_m_2,
            self.datos_memoria.parametro_k_2,
            self.datos_memoria.cuantia_requerida_2,
            self.datos_memoria.chequeo_cuantia_2,
            self.datos_memoria.acero_requerido_2,
            self.datos_memoria.altura_bloque_whitney_2,
            self.datos_memoria.altura_eje_neutro_2,
            self.datos_memoria.deformacion_acero_2,
            self.datos_memoria.momento_resistente_2)
        '''
        self.insertar_texto_acero_requerido_momento(Story, styles,
            self.datos_memoria.momento_positivo_izquierdo_viga,
            self.datos_memoria.profundidad_bloque_whitney_2,
            self.datos_memoria.profundidad_eje_neutro_2,
            self.datos_memoria.profundidad_eje_neutro_maximo_falla_traccion_2,
            self.datos_memoria.acero_requerido_2)
        '''
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1.4.3 - Acero requerido para el momento negativo centro')
        Story.append(Spacer(1, 12))
        self.insertar_texto_acero_requerido_momento(Story, styles,
            self.datos_memoria.momento_ultimo_3,
            self.datos_memoria.parametro_m_3,
            self.datos_memoria.parametro_k_3,
            self.datos_memoria.cuantia_requerida_3,
            self.datos_memoria.chequeo_cuantia_3,
            self.datos_memoria.acero_requerido_3,
            self.datos_memoria.altura_bloque_whitney_3,
            self.datos_memoria.altura_eje_neutro_3,
            self.datos_memoria.deformacion_acero_3,
            self.datos_memoria.momento_resistente_3)
        '''
        self.insertar_texto_acero_requerido_momento(Story, styles,
            self.datos_memoria.momento_negativo_centro_viga,
            self.datos_memoria.profundidad_bloque_whitney_3,
            self.datos_memoria.profundidad_eje_neutro_3,
            self.datos_memoria.profundidad_eje_neutro_maximo_falla_traccion_3,
            self.datos_memoria.acero_requerido_3)
        '''
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1.4.4 - Acero requerido para el momento positivo centro')
        Story.append(Spacer(1, 12))
        self.insertar_texto_acero_requerido_momento(Story, styles,
            self.datos_memoria.momento_ultimo_4,
            self.datos_memoria.parametro_m_4,
            self.datos_memoria.parametro_k_4,
            self.datos_memoria.cuantia_requerida_4,
            self.datos_memoria.chequeo_cuantia_4,
            self.datos_memoria.acero_requerido_4,
            self.datos_memoria.altura_bloque_whitney_4,
            self.datos_memoria.altura_eje_neutro_4,
            self.datos_memoria.deformacion_acero_4,
            self.datos_memoria.momento_resistente_4)
        '''
        self.insertar_texto_acero_requerido_momento(Story, styles,
            self.datos_memoria.momento_positivo_centro_viga,
            self.datos_memoria.profundidad_bloque_whitney_4,
            self.datos_memoria.profundidad_eje_neutro_4,
            self.datos_memoria.profundidad_eje_neutro_maximo_falla_traccion_4,
            self.datos_memoria.acero_requerido_4)
        '''
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1.4.5 - Acero requerido para el momento negativo derecho')
        Story.append(Spacer(1, 12))
        self.insertar_texto_acero_requerido_momento(Story, styles,
            self.datos_memoria.momento_ultimo_5,
            self.datos_memoria.parametro_m_5,
            self.datos_memoria.parametro_k_5,
            self.datos_memoria.cuantia_requerida_5,
            self.datos_memoria.chequeo_cuantia_5,
            self.datos_memoria.acero_requerido_5,
            self.datos_memoria.altura_bloque_whitney_5,
            self.datos_memoria.altura_eje_neutro_5,
            self.datos_memoria.deformacion_acero_5,
            self.datos_memoria.momento_resistente_5)
        '''
        self.insertar_texto_acero_requerido_momento(Story, styles,
            self.datos_memoria.momento_negativo_derecho_viga,
            self.datos_memoria.profundidad_bloque_whitney_5,
            self.datos_memoria.profundidad_eje_neutro_5,
            self.datos_memoria.profundidad_eje_neutro_maximo_falla_traccion_5,
            self.datos_memoria.acero_requerido_5)
        '''
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1.4.6 - Acero requerido para el momento positivo derecho')
        Story.append(Spacer(1, 12))
        self.insertar_texto_acero_requerido_momento(Story, styles,
            self.datos_memoria.momento_ultimo_6,
            self.datos_memoria.parametro_m_6,
            self.datos_memoria.parametro_k_6,
            self.datos_memoria.cuantia_requerida_6,
            self.datos_memoria.chequeo_cuantia_6,
            self.datos_memoria.acero_requerido_6,
            self.datos_memoria.altura_bloque_whitney_6,
            self.datos_memoria.altura_eje_neutro_6,
            self.datos_memoria.deformacion_acero_6,
            self.datos_memoria.momento_resistente_6)
        '''
        self.insertar_texto_acero_requerido_momento(Story, styles,
            self.datos_memoria.momento_positivo_derecho_viga,
            self.datos_memoria.profundidad_bloque_whitney_6,
            self.datos_memoria.profundidad_eje_neutro_6,
            self.datos_memoria.profundidad_eje_neutro_maximo_falla_traccion_6,
            self.datos_memoria.acero_requerido_6)
        '''
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1.5 - Requisitos de acero por ductilidad')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], 'La resistencia a momento positivo en la cara del nodo, debe ser al menos igual que la mitad \
                de la resistencia a momento negativo proporcionada en esa misma cara. La resistencia a momento negativo o  \
                positivo, en cualquier sección a lo largo de la longitud del miembro, debe ser al menos igual a un cuarto de \
                la resistencia máxima a momento proporcionada en la cara de cualquiera de los nodos.')
        Story.append(Spacer(1, 12))
        Story.append(im_Duct)
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1.5.1 - Extremo izquierdo')
        Story.append(Spacer(1, 12))
        self.insertar_texto_acero_extremo_ductilidad(Story, styles, 'Izq',
            self.datos_memoria.acero_superior_izquierdo_ductil,
            self.datos_memoria.acero_superior_izquierdo_impuesto,
            self.datos_memoria.acero_inferior_izquierdo_ductil,
            self.datos_memoria.acero_inferior_izquierdo_impuesto)
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1.5.2 - Extremo derecho')
        Story.append(Spacer(1, 12))
        self.insertar_texto_acero_extremo_ductilidad(Story, styles, 'Der',
            self.datos_memoria.acero_superior_derecho_ductil,
            self.datos_memoria.acero_superior_derecho_impuesto,
            self.datos_memoria.acero_inferior_derecho_ductil,
            self.datos_memoria.acero_inferior_derecho_impuesto)
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1.5.3 - Centro superior')
        Story.append(Spacer(1, 12))
        self.insertar_texto_acero_centro_ductilidad(Story, styles, 'Sup',
            self.datos_memoria.acero_superior_izquierdo_impuesto,
            self.datos_memoria.acero_superior_derecho_impuesto,
            self.datos_memoria.acero_requerido_3,
            self.datos_memoria.acero_superior_centro_ductil,
            self.datos_memoria.acero_superior_centro_impuesto)
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1.5.4 - Centro inferior')
        Story.append(Spacer(1, 12))
        self.insertar_texto_acero_centro_ductilidad(Story, styles, 'Inf',
            self.datos_memoria.acero_inferior_izquierdo_impuesto,
            self.datos_memoria.acero_inferior_derecho_impuesto,
            self.datos_memoria.acero_requerido_4,
            self.datos_memoria.acero_inferior_centro_ductil,
            self.datos_memoria.acero_inferior_centro_impuesto)
        Story.append(Spacer(1, 24))
        self.insertar_texto(Story, styles['Justify'], '3.2 - Diseño del refuerzo transversal')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.2.1 - Demanda por corte')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.2.1.1 - Definición de casos de estudio:')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.2.1.1.1 - Caso A: Momentos probables de la viga en sentido antihorario')
        Story.append(Spacer(1, 12))
        Story.append(im_Mmp_A)
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.2.1.1.2 - Caso B: Momentos probables de la viga en sentido horario')
        Story.append(Spacer(1, 12))
        Story.append(im_Mmp_B)
        Story.append(Spacer(1, 36))
        self.insertar_texto(Story, styles['Justify'], '3.2.1.1.3 - Resistencia máxima a flexión')
        Story.append(Spacer(1, 12))
        Story.append(im_Def)
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.2.1.2 - Cargas distribuidas sobre la viga')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], f'Wpp = Yc*bw*h = {self.datos_memoria.peso_propio_viga} tonf/m')
        self.insertar_texto(Story, styles['Justify'], f'Wscp = {self.datos_memoria.sobrecarga_permanente_viga} tonf/m')
        self.insertar_texto(Story, styles['Justify'], f'Wcp = Wpp + Wscp = {self.datos_memoria.carga_muerta_viga} tonf/m')
        self.insertar_texto(Story, styles['Justify'], f'Wcv = {self.datos_memoria.sobrecarga_variable_viga} tonf/m')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.2.1.3 - Análisis del caso A')
        Story.append(Spacer(1, 12))
        self.insertar_texto_casos_corte(Story, styles,
            self.datos_memoria.carga_ultima_viga_1,
            self.datos_memoria.corte_gravitacional_1,
            self.datos_memoria.profundidad_bloque_whitney_1_1,
            self.datos_memoria.momento_maximo_probable_1_1,
            self.datos_memoria.profundidad_bloque_whitney_2_1,
            self.datos_memoria.momento_maximo_probable_2_1,
            self.datos_memoria.corte_por_capacidad_1)
        self.insertar_texto(Story, styles['Justify'], f'Ve1 = Vg + Vp = {round(self.datos_memoria.corte_probable_derecho_1, 3)} tonf')
        self.insertar_texto(Story, styles['Justify'], f'Ve2 = Vg - Vp = {round(self.datos_memoria.corte_probable_izquierdo_1, 3)} tonf')
        Story.append(Spacer(1, 12))
        Story.append(im_Vg_A)
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.2.1.4 - Análisis del caso B')
        Story.append(Spacer(1, 12))
        self.insertar_texto_casos_corte(Story, styles,
            self.datos_memoria.carga_ultima_viga_2,
            self.datos_memoria.corte_gravitacional_2,
            self.datos_memoria.profundidad_bloque_whitney_1_2,
            self.datos_memoria.momento_maximo_probable_1_2,
            self.datos_memoria.profundidad_bloque_whitney_2_2,
            self.datos_memoria.momento_maximo_probable_2_2,
            self.datos_memoria.corte_por_capacidad_2)
        self.insertar_texto(Story, styles['Justify'], f'Ve1 = Vg - Vp = {round(self.datos_memoria.corte_probable_derecho_2, 3)} tonf')
        self.insertar_texto(Story, styles['Justify'], f'Ve2 = Vg + Vp = {round(self.datos_memoria.corte_probable_izquierdo_2, 3)} tonf')
        Story.append(Spacer(1, 12))
        Story.append(im_Vg_B)
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], 'Finalmente, se tiene:')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], f'Ve_1 = max (Ve1_CasoA, Ve1_CasoB) = {self.datos_memoria.corte_izquierdo} tonf')
        self.insertar_texto(Story, styles['Justify'], f'Ve_2 = max (Ve2_CasoA, Ve2_CasoB) = {self.datos_memoria.corte_derecho} tonf')
        self.insertar_texto(Story, styles['Justify'], f'Vp = max (Vp_CasoA, Vp_CasoB) = {self.datos_memoria.corte_capacidad} tonf')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.2.2 - Diseño del acero transversal')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.2.2.1 - Corte de diseño')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], f'Corte último del análisis (Vu) = {self.datos_memoria.corte_ultimo_viga} tonf')
        self.insertar_texto(Story, styles['Justify'], f'Corte máximo probable (Ve) = max (Ve_1, Ve_2) = {self.datos_memoria.corte_maximo_probable} tonf')
        self.insertar_texto(Story, styles['Justify'], f'Corte de diseño (Vd) = max (Vu, Ve) = {self.datos_memoria.corte_diseno} tonf')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.2.2.2 - Resistencia del concreto a cortante')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], 'El refuerzo transversal debe diseñarse para resistir cortante suponiendo Vc = 0 cuando se produzcan simultaneamente: \
                a) La fuerza cortante inducida por el sismo calculada representa la mitad o mas de la resistencia maxima requerida. \
                            b) La fuerza axial de compresion mayorada es menor que Ag*fc/20.')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], f'Rv = Vp/Vd = {round(self.datos_memoria.relacion_cortes, 3)} > 0.5')
        self.insertar_texto(Story, styles['Justify'], f'Ag = b*h = {round(self.datos_memoria.area_gruesa, 3)} cm2')
        self.insertar_texto(Story, styles['Justify'], f'Pc = Ag*fc/20 = {round(self.datos_memoria.producto, 3)} tonf >= Pu')
        self.insertar_texto(Story, styles['Justify'], f'Vc =  0.17*(fc**(1/2))*b*d = {round(self.datos_memoria.cortante, 3)} tonf')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.2.2.3 - Resistencia del acero a cortante')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], 'a) Si el corte de diseño es menor que el corte resistente del concreto minorado pero mayor que la mitad \
                de la resistencia del concreto minorado, se requiere refuerzo mínimo.')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], 'b) Si el corte de diseño es superior a la resistencia del concreto a cortante minorado, \
                entonces se debe calcular la resistencia del acero a cortante.')
        Story.append(Spacer(1, 12))
        if self.datos_memoria.corte_diseno >= self.datos_memoria.cortante/2 and self.datos_memoria.corte_diseno <= self.datos_memoria.cortante:
            self.insertar_texto(Story, styles['Justify'], 'Se requiere refuerzo mínimo.')
        elif self.datos_memoria.corte_diseno > self.datos_memoria.cortante:
            self.insertar_texto(Story, styles['Justify'], 'Se debe calcular la resistencia del acero a cortante.')
            Story.append(Spacer(1, 12))
            self.insertar_texto(Story, styles['Justify'], f'Vs1 =  Vd-Vc = {round(self.datos_memoria.demanda_corte_1, 2)} tonf')
            self.insertar_texto(Story, styles['Justify'], f'Vs2 =  Av*fyt*d/s = {round(self.datos_memoria.demanda_corte_2, 2)} tonf')
            self.insertar_texto(Story, styles['Justify'], f'Vs =  max(Vs1 , Vs2) = {round(self.datos_memoria.demanda_corte, 2)} tonf')
            self.insertar_texto(Story, styles['Justify'], 'Vs <= 0.66*(fc**(1/2))*b*d')
            self.insertar_texto(Story, styles['Justify'], f'La sección {self.datos_memoria.chequeo_estribo} para realizar el diseño de estribos')
        else:
            Story.append(Spacer(1, 12))
            self.insertar_texto(Story, styles['Justify'], 'La sección NO CUMPLE')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.2.2.4 - Disposición del acero transversal en zona de confinamiento')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], f'AV =  NRamas*Ab = {self.datos_memoria.area_transversal_refuerzo} cm2')
        self.insertar_texto(Story, styles['Justify'], f'Smcal = Phiv*AV*fy*d/Vs = {round(self.datos_memoria.separacion_maxima_calculada_estribos, 2)} cm')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], 'Separación máxima normativa de estribos y longitud de confinamiento.')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], f'Smnorma = min(d/4, 8dbl, 24dbe, 30) = {self.datos_memoria.separacion_maxima_norma} cm')
        self.insertar_texto(Story, styles['Justify'], f'Lc = 2*h = {self.datos_memoria.longitud_confinamiento} cm')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.2.2.5 - Disposición del acero transversal fuera de la zona de confinamiento')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], 'Se mantiene el mismo diámetro y definición de estribos utilizados en la zona de \
                confinamiento, pero se hace un ajuste a la separación de los mismos.')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], 'a) sin solapes.')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], f'Sgm = d/2 = {self.datos_memoria.separacion_maxima_inconfinada} cm')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], 'b) con solape.')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], f'Sgsm = min (10, d/4) = {self.datos_memoria.separacion_maxima_inconfinada_solapada} cm')
        Story.append(Spacer(1, 24))
        self.insertar_texto(Story, styles['Justify'], '4 - RESULTADOS FINALES')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], f'bw = {self.datos_memoria.base_viga_d} cm')
        self.insertar_texto(Story, styles['Justify'], f'h = {self.datos_memoria.altura_viga_d} cm')
        self.insertar_texto(Story, styles['Justify'], f'r = {self.datos_memoria.recubrimiento_inferior_viga} cm')
        self.insertar_texto(Story, styles['Justify'], f'Ln = {self.datos_memoria.longitud_libre_viga} m')
        self.insertar_texto(Story, styles['Justify'], f'As1_sup = {self.datos_memoria.acero_superior_izquierdo_impuesto} cm2')
        self.insertar_texto(Story, styles['Justify'], f'As1_inf = {self.datos_memoria.acero_inferior_izquierdo_impuesto} cm2')
        self.insertar_texto(Story, styles['Justify'], f'As_sup = {self.datos_memoria.acero_superior_centro_impuesto} cm2')
        self.insertar_texto(Story, styles['Justify'], f'As_inf = {self.datos_memoria.acero_inferior_centro_impuesto} cm2')
        self.insertar_texto(Story, styles['Justify'], f'As2_sup = {self.datos_memoria.acero_superior_derecho_impuesto} cm2')
        self.insertar_texto(Story, styles['Justify'], f'As2_inf = {self.datos_memoria.acero_inferior_derecho_impuesto} cm2')
        self.insertar_texto(Story, styles['Justify'], f'AV = {self.datos_memoria.area_transversal_refuerzo} cm2')
        self.insertar_texto(Story, styles['Justify'], f'S = {self.datos_memoria.separacion_definitiva} cm')
        self.insertar_texto(Story, styles['Justify'], f'Sg = {self.datos_memoria.separacion_inconfinada} cm')
        self.insertar_texto(Story, styles['Justify'], f'Sgs = {self.datos_memoria.separacion_inconfinada_solapada} cm')
        Story.append(Spacer(1, 24))
        self.insertar_texto(Story, styles['Justify'], '5 - DETALLES TÍPICOS')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '5.1 - Disposición del acero transversal')
        Story.append(Spacer(1, 12))
        Story.append(im_dis_acero_tran)
        Story.append(Spacer(1, 36))
        self.insertar_texto(Story, styles['Justify'], '5.2 - Ubicación de solapes del acero longitudinal')
        Story.append(Spacer(1, 12))
        Story.append(im_ubi_solapes_acero_long)
        Story.append(Spacer(1, 12))
        self.doc.build(Story)
