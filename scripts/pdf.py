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
        self.insertar_texto(Story, styles['Justify'], f'Longitud libre (Ln) = {self.datos_memoria.longitud_libre_viga} cm')
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
        self.insertar_texto(Story, styles['Justify'], '3.1.3 - Acero mínimo')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], f'Asmin_1 = 14*bw*d/fy = {round(self.datos_memoria.acero_minimo_1, 2)} cm2')
        self.insertar_texto(Story, styles['Justify'], f'Asmin_2 = 0.8*(fc^(1/2))*bw*d/fy = {round(self.datos_memoria.acero_minimo_2, 2)} cm2')
        self.insertar_texto(Story, styles['Justify'], f'Asmin = max(Asmin_1, Asmin_2) = {round(self.datos_memoria.acero_minimo, 2)} cm2')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1.4 - Acero longitudinal requerido conforme al análisis')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1.4.1 - Acero requerido para el momento negativo izquierdo')
        Story.append(Spacer(1, 12))
        self.insertar_texto_acero_requerido_momento(Story, styles,
            self.datos_memoria.momento_negativo_izquierdo_viga,
            self.datos_memoria.profundidad_bloque_whitney_1,
            self.datos_memoria.profundidad_eje_neutro_1,
            self.datos_memoria.profundidad_eje_neutro_maximo_falla_traccion_1,
            self.datos_memoria.acero_requerido_1)
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1.4.2 - Acero requerido para el momento positivo izquierdo')
        Story.append(Spacer(1, 12))
        self.insertar_texto_acero_requerido_momento(Story, styles,
            self.datos_memoria.momento_positivo_izquierdo_viga,
            self.datos_memoria.profundidad_bloque_whitney_2,
            self.datos_memoria.profundidad_eje_neutro_2,
            self.datos_memoria.profundidad_eje_neutro_maximo_falla_traccion_2,
            self.datos_memoria.acero_requerido_2)
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1.4.3 - Acero requerido para el momento negativo centro')
        Story.append(Spacer(1, 12))
        self.insertar_texto_acero_requerido_momento(Story, styles,
            self.datos_memoria.momento_negativo_centro_viga,
            self.datos_memoria.profundidad_bloque_whitney_3,
            self.datos_memoria.profundidad_eje_neutro_3,
            self.datos_memoria.profundidad_eje_neutro_maximo_falla_traccion_3,
            self.datos_memoria.acero_requerido_3)
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1.4.4 - Acero requerido para el momento positivo centro')
        Story.append(Spacer(1, 12))
        self.insertar_texto_acero_requerido_momento(Story, styles,
            self.datos_memoria.momento_positivo_centro_viga,
            self.datos_memoria.profundidad_bloque_whitney_4,
            self.datos_memoria.profundidad_eje_neutro_4,
            self.datos_memoria.profundidad_eje_neutro_maximo_falla_traccion_4,
            self.datos_memoria.acero_requerido_4)
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1.4.5 - Acero requerido para el momento negativo derecho')
        Story.append(Spacer(1, 12))
        self.insertar_texto_acero_requerido_momento(Story, styles,
            self.datos_memoria.momento_negativo_derecho_viga,
            self.datos_memoria.profundidad_bloque_whitney_5,
            self.datos_memoria.profundidad_eje_neutro_5,
            self.datos_memoria.profundidad_eje_neutro_maximo_falla_traccion_5,
            self.datos_memoria.acero_requerido_5)
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '3.1.4.6 - Acero requerido para el momento positivo derecho')
        Story.append(Spacer(1, 12))
        self.insertar_texto_acero_requerido_momento(Story, styles,
            self.datos_memoria.momento_positivo_derecho_viga,
            self.datos_memoria.profundidad_bloque_whitney_6,
            self.datos_memoria.profundidad_eje_neutro_6,
            self.datos_memoria.profundidad_eje_neutro_maximo_falla_traccion_6,
            self.datos_memoria.acero_requerido_6)
        
        
        
        
        
        '''
        
        Story.append(Spacer(1, 24))
        ptext = '<font size="12">3.1.5 - Requisitos de acero por ductilidad</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">La resistencia a momento positivo en la cara del nodo, debe ser al menos igual que la mitad \
                de la resistencia a momento negativo proporcionada en esa misma cara. La resistencia a momento negativo o  \
                positivo, en cualquier sección a lo largo de la longitud del miembro, debe ser al menos igual a un cuarto de \
                la resistencia máxima a momento proporcionada en la cara de cualquiera de los nodos. </font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        Story.append(imDuct)
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">2.5.1 - Extremo izquierdo</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">As1_sup_req = %s cm2</font>'%round(self.datos_memoria.As1_sup_req,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">As1_sup = %s cm2 SUMINISTRADO</font>'%round(self.datos_memoria.As1_sup,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">As1_inf_req = max (As1_inf_cal, As1_sup/2) = %s cm2</font>'%round(self.datos_memoria.As1_inf_req,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">As1_inf = %s cm2 SUMINISTRADO</font>'%round(self.datos_memoria.As1_inf,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">2.5.2 - Extremo derecho</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">As2_sup_req = %s cm2</font>'%round(self.datos_memoria.As2_sup_req,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">As2_sup = %s cm2 SUMINISTRADO</font>'%round(self.datos_memoria.As2_sup,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">As2_inf_req = max (As1_inf_cal, As1_sup/2) = %s cm2</font>'%round(self.datos_memoria.As2_inf_req,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">As2_inf = %s cm2 SUMINISTRADO</font>'%round(self.datos_memoria.As2_inf,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 36))
        ptext = '<font size="12">2.5.3 - Centro</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">As_sup_req = %s cm2</font>'%round(self.datos_memoria.As_sup_req,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">As_sup = %s cm2 SUMINISTRADO</font>'%round(self.datos_memoria.As_sup,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">As_inf_req = max (As_inf_cal, As_sup/2) = %s cm2</font>'%round(self.datos_memoria.As_inf_req,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">As_inf = %s cm2 SUMINISTRADO</font>'%round(self.datos_memoria.As_inf,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 24))
        ptext = '<font size="12">3 - Diseño del refuerzo transversal</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">3.1 - Demanda por corte</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">3.1.1 - Definición de casos de estudio:</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">3.1.1.1 - Caso A: Momentos probables de la viga en sentido antihorario</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        Story.append(imMmpA)
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">3.1.1.2 - Caso B: Momentos probables de la viga en sentido horario</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        Story.append(imMmpB)
        Story.append(Spacer(1, 36))
        ptext = '<font size="12">3.1.1.3 - Resistencia máxima a flexión</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        Story.append(imDef)
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">3.1.2 - Cargas distribuidas sobre la viga</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Wpp = Yc*bw*h = %s tonf/m</font>'%round(self.datos_memoria.Wpp,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Wscp = %s tonf/m</font>'%round(self.datos_memoria.Wscp,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Wcp = Wpp + Wscp = %s tonf/m</font>'%round(self.datos_memoria.Wcp,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Wcv = %s tonf/m</font>'%round(self.datos_memoria.Wcv,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">3.1.3 - Análisis del caso A</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Wu = 1.2*Wcp + Y*Wcv = %s tonf/m</font>'%round(self.datos_memoria.Wu_1,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Vg = Wu*Ln/2 = %s tonf</font>'%round(self.datos_memoria.Vg_1,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">a1 = Fsr*fy*As1_sup/(0.85*fc*bw) = %s cm</font>'%round(self.datos_memoria.a1_1,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Mmp1 = Fsr*fy*As1_sup*(d-a/2) = %s tonf-m</font>'%round(self.datos_memoria.Mmp1_1,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">a2 = Fsr*fy*As1_inf/(0.85*fc*bw) = %s cm</font>'%round(self.datos_memoria.a2_1,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Mmp2 = Fsr*fy*As1_inf*(d-a/2) = %s tonf-m</font>'%round(self.datos_memoria.Mmp2_1,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Vp = (Mmp1+Mmp2)/Ln = %s tonf</font>'%round(self.datos_memoria.Vp_1,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Ve1 = Vg + Vp = %s tonf</font>'%round(self.datos_memoria.Ve1_1,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Ve2 = Vg - Vp = %s tonf</font>'%round(self.datos_memoria.Ve2_1,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        Story.append(imVgA)
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">3.1.4 - Análisis del caso B</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Wu = 1.2*Wcp + Fcv*Wcv = %s tonf/m</font>'%round(self.datos_memoria.Wu_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Vg = Wu*Ln/2 = %s tonf</font>'%round(self.datos_memoria.Vg_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">a1 = Fsr*fy*As1_sup/(0.85*fc*bw) = %s cm</font>'%round(self.datos_memoria.a1_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Mmp1 = Fsr*fy*As1_sup*(d-a/2) = %s tonf-m</font>'%round(self.datos_memoria.Mmp1_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">a2 = Fsr*fy*As1_inf/(0.85*fc*bw) = %s cm</font>'%round(self.datos_memoria.a2_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Mmp2 = Fsr*fy*As1_inf*(d-a/2) = %s tonf-m</font>'%round(self.datos_memoria.Mmp2_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Vp = (Mmp1+Mmp2)/Ln = %s tonf</font>'%round(self.datos_memoria.Vp_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Ve1 = Vg - Vp = %s tonf</font>'%round(self.datos_memoria.Ve1_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Ve2 = Vg + Vp = %s tonf</font>'%round(self.datos_memoria.Ve2_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        Story.append(imVgB)
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Finalmente, se tiene:</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Ve_1 = max (Ve1_CasoA, Ve1_CasoB) = %s tonf</font>'%round(self.datos_memoria.Ve_1,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Ve_2 = max (Ve2_CasoA, Ve2_CasoB) = %s tonf</font>'%round(self.datos_memoria.Ve_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Vp = max (Vp_CasoA, Vp_CasoB) = %s tonf</font>'%round(self.datos_memoria.Vp,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 24))
        ptext = '<font size="12">3.2 - Diseño del acero transversal</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">3.2.1 - Corte de diseño</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Corte último del análisis (Vu) = %s tonf</font>'%round(self.datos_memoria.Vu,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        self.Ve = max(self.datos_memoria.Ve_1,self.datos_memoria.Ve_2)
        ptext = '<font size="12">Corte máximo probable (Ve) = max (Ve_1, Ve_2) = %s tonf</font>'%round(self.Ve,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Corte de diseño (Vd) = max (Vu, Ve) = %s tonf</font>'%round(self.datos_memoria.Vd,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">3.2.2 - Definición de la resistencia por corte del concreto</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">El refuerzo transversal debe diseñarse para resistir cortante suponiendo Vc = 0, \
                donde ocurran simultáneamente las siguientes condiciones:</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 36))
        ptext = '<font size="12">a) La fuerza cortante inducida por el sísmo Vp, que se determina a tráves de los \
                momentos máximos probables de la viga, representa la mitad o más del corte de diseño.</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">b) La fuerza axial mayorada en la viga Pu, incluyendo la acción sísmica, es menor \
                que el producto del área gruesa por la resistencia del concreto entre veinte.</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Corte por capacidad (Vp) =  %s tonf</font>'%round(self.datos_memoria.Vp,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Relación de cortes (Vp/Vd) =  %s</font>'%round(self.datos_memoria.RC,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Fuerza axial (Pu) =  %s tonf</font>'%round(self.datos_memoria.Pu,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Área gruesa (Ag) = bw*h = %s cm2</font>'%round(self.datos_memoria.Ag/1000,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Pc =  Ag*fc/20 = %s tonf</font>'%round(self.datos_memoria.Pc,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Vc =  %s tonf</font>'%round(self.datos_memoria.Vc,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">3.2.3 - Disposición del acero transversal en zona de confinamiento</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">a) Definición y separación máxima de estribos por demanda.</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Vs =  Vd/phiv-Vc = %s tonf</font>'%round(self.datos_memoria.Vs,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">AV =  NRamas*Ab = %s cm2</font>'%round(self.datos_memoria.AV,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Smcal = AV*fy*d/Vs = %s cm</font>'%round(self.datos_memoria.Smcal,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">b) Separación máxima normativa de estribos y longitud de confinamiento.</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Smnorma = min(d/4, 6*db, 15) = %s cm</font>'%round(self.datos_memoria.Smnorma,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Lc = 2*h = %s cm</font>'%round(self.datos_memoria.Lc,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">3.2.4 - Disposición del acero transversal fuera de la zona de confinamiento</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Se mantiene el mismo diámetro y definición de estribos utilizados en la zona de \
                confinamiento, pero se hace un ajuste a la separación de los mismos.</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">a) sin solapes.</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Sgm = d/2 = %s cm</font>'%round(self.datos_memoria.Sgm,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">b) solapes.</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Sgsm = min (10, d/4) = %s cm</font>'%round(self.datos_memoria.Sgsm,2)
        Story.append(Paragraph(ptext, styles["Justify"]))




        Story.append(Spacer(1, 24))
        self.insertar_texto(Story, styles['Justify'], '4 - Resultados finales')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], 'bw = '+str(self.datos_memoria.bw)+' cm')
        self.insertar_texto(Story, styles['Justify'], 'h = '+str(self.datos_memoria.h)+' cm')
        self.insertar_texto(Story, styles['Justify'], 'r = '+str(self.datos_memoria.r)+' cm')
        self.insertar_texto(Story, styles['Justify'], 'dp = '+str(self.datos_memoria.dp)+' cm')
        self.insertar_texto(Story, styles['Justify'], 'As1_sup = ')
        self.insertar_texto(Story, styles['Justify'], 'As1_inf = ')
        self.insertar_texto(Story, styles['Justify'], 'As2_sup = ')
        self.insertar_texto(Story, styles['Justify'], 'As2_inf = ')
        self.insertar_texto(Story, styles['Justify'], 'As_sup = ')
        self.insertar_texto(Story, styles['Justify'], 'As_inf = ')
        self.insertar_texto(Story, styles['Justify'], 'AV = ')
        self.insertar_texto(Story, styles['Justify'], 'S =  cm')
        self.insertar_texto(Story, styles['Justify'], 'Sg =  cm')
        self.insertar_texto(Story, styles['Justify'], 'Sgs =  cm')
        Story.append(Spacer(1, 24))
        self.insertar_texto(Story, styles['Justify'], '5 - Detalles típicos')
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '5.1 - Disposición del acero transversal')
        Story.append(Spacer(1, 12))
        Story.append(imDisposicionAceroTransversal)
        Story.append(Spacer(1, 12))
        self.insertar_texto(Story, styles['Justify'], '5.2 - Ubicación de solapes del acero longitudinal')
        Story.append(Spacer(1, 12))
        Story.append(imUbicacionSolapesAceroLongitudinal)
        Story.append(Spacer(1, 24))
        self.insertar_texto(Story, styles['Justify'], '6 - Revisión de la ductilidad para la sección crítica')
        Story.append(Spacer(1, 24))
        Story.append(Spacer(1, 24))
        self.insertar_texto(Story, styles['Justify'], '7 - Estimación de la ductilidad de entrepiso (mecanismo de columna fuerte-viga débil)')
        Story.append(Spacer(1, 12))
        
        
        

        '''
       
        self.doc.build(Story)

