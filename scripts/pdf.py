import time
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm


class GenerarReportePDF():

    def __init__(self):
        self.logo = 'img/logoSARO.png'
        self.imgMomentos = 'img/DetalleMomentos.png'
        self.imgDefinicion = 'img/DefinicionResistenciaNominalFlexion.png'
        self.imgDuctilidad = 'img/RequisitosAceroLongitudinalDuctilidad.png'
        self.imgMmpCasoA = 'img/MomentoMaximoProbableCasoA.png'
        self.imgMmpCasoB = 'img/MomentoMaximoProbableCasoB.png'
        self.imgVgCasoA = 'img/CorteMaximoProbableCasoA.png'
        self.imgVgCasoB = 'img/CorteMaximoProbableCasoB.png'
        self.imgDisposicionAceroTransversal = 'img/DisposicionAceroTransversal.png'
        self.imgUbicacionSolapesAceroLongitudinal = 'img/UbicacionSolapesAceroLongitudinal.png'
    
    def insertarTexto(self, Story, styles, text):
        ptext = '<font size="12">%s</font>' %text
        Story.append(Paragraph(ptext, styles))

    def pdfViga(self, dataBase, base, memoria, pdfPath):
        self.doc = SimpleDocTemplate(pdfPath,pagesize=letter,
                                                rightMargin=2*cm,leftMargin=4*cm,
                                                topMargin=3*cm,bottomMargin=3*cm)
        Story=[]
        im = Image(self.logo, 2*cm, 2*cm)
        iMom = Image(self.imgMomentos, 15*cm, 6*cm)
        imDef = Image(self.imgDefinicion, 15*cm, 6*cm)
        imDuct = Image(self.imgDuctilidad, 15*cm, 6*cm)
        imMmpA = Image(self.imgMmpCasoA, 15*cm, 6*cm)
        imMmpB = Image(self.imgMmpCasoB, 15*cm, 6*cm)
        imVgA = Image(self.imgVgCasoA, 15*cm, 6*cm)
        imVgB = Image(self.imgVgCasoB, 15*cm, 6*cm)
        imDisposicionAceroTransversal = Image(self.imgDisposicionAceroTransversal, 15*cm, 8*cm)
        imUbicacionSolapesAceroLongitudinal = Image(self.imgUbicacionSolapesAceroLongitudinal, 15*cm, 6*cm)
        styles=getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
        styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
        Story.append(im)
        Story.append(Spacer(1, 12))
        self.insertarTexto(Story, styles['Center'], 'DISEÑO DE UNA VIGA DE PÓRTICO RESISTENTE A MOMENTO CON \
                                                    CAPACIDAD ESPECIAL DE DISIPACIÓN DE ENERGÍA (DES)')
        self.insertarTexto(Story, styles['Center'], '(Incluye el cálculo de ductilidad de sección y ductilidad estimada de entrepiso)')
        self.insertarTexto(Story, styles['Center'], 'Aplicación de la norma NSR-10')
        Story.append(Spacer(1, 12))
        self.insertarTexto(Story, styles['Justify'], '1 - Datos de la viga')
        Story.append(Spacer(1, 12))
        self.insertarTexto(Story, styles['Justify'], 'Ancho de la viga (bw) = '+str(memoria.bw)+' cm')
        self.insertarTexto(Story, styles['Justify'], 'Altura de la viga (h) = '+str(memoria.h)+' cm')
        self.insertarTexto(Story, styles['Justify'], 'Recubrimiento inferior (r) = '+str(memoria.r)+' cm')
        self.insertarTexto(Story, styles['Justify'], 'Recubrimiento superior (dp) = '+str(memoria.dp)+' cm')
        self.insertarTexto(Story, styles['Justify'], 'Longitud libre (Ln) = '+str(memoria.Ln)+' cm')
        Story.append(Spacer(1, 24))
        self.insertarTexto(Story, styles['Justify'], '1.2 - Materiales')
        Story.append(Spacer(1, 12))
        self.insertarTexto(Story, styles['Justify'], 'Resistencia del concreto (fc) = '+str(memoria.fc)+' Kgf/cm2')
        self.insertarTexto(Story, styles['Justify'], 'Módulo de elasticidad del concreto (Ec) = '+str(memoria.Ec)+' Kgf/cm2')
        self.insertarTexto(Story, styles['Justify'], 'Peso especifico del concreto armado (Yc) = '+str(memoria.Yc)+' Kgf/m3')
        self.insertarTexto(Story, styles['Justify'], 'Deformación última del concreto (Ecu) = '+str(memoria.Ecu))
        self.insertarTexto(Story, styles['Justify'], '(B1) = '+str(memoria.B1))
        self.insertarTexto(Story, styles['Justify'], 'Factor de minoración para resistencia al corte (Phiv) = '+str(memoria.phiv))
        self.insertarTexto(Story, styles['Justify'], 'Factor de minoración para resistencia a flexión (Phib) = '+str(memoria.phib))
        self.insertarTexto(Story, styles['Justify'], 'Esfuerzo cedente del acero de refuerzo (fy) = '+str(memoria.fy)+' Kgf/cm2')
        self.insertarTexto(Story, styles['Justify'], 'Módulo de elasticidad del acero (Es) = '+str(memoria.Es)+' Kgf/cm2')
        self.insertarTexto(Story, styles['Justify'], 'Deformación cedente del acero (Ey) = '+str(memoria.Ey))
        self.insertarTexto(Story, styles['Justify'], 'Deformación mínima del acero (Esmin) = '+str(memoria.Esmin))
        self.insertarTexto(Story, styles['Justify'], 'Factor de sobre-resistencia del acero (Fsr) = '+str(memoria.Fsr))
        Story.append(Spacer(1, 24))
        self.insertarTexto(Story, styles['Justify'], '1.3 - Revisión de límites dimensionales')
        Story.append(Spacer(1, 12))
        self.insertarTexto(Story, styles['Justify'], 'La luz libre de la viga no debe ser menor que cuatro veces la altura útil de la \
                                                    sección:')
        Story.append(Spacer(1, 12))
        self.insertarTexto(Story, styles['Justify'], 'd = h - r = '+str(memoria.d)+' cm')
        self.insertarTexto(Story, styles['Justify'], '4*d = '+str(memoria.chk1)+' m')
        if memoria.Ln >= memoria.chk1:
            self.insertarTexto(Story, styles['Justify'], str(memoria.Ln)+' >= '+str(memoria.chk1)+'  CUMPLE')
        else:
            self.insertarTexto(Story, styles['Justify'], str(memoria.Ln)+' < '+str(memoria.chk1)+'  NO CUMPLE')
        Story.append(Spacer(1, 12))
        self.insertarTexto(Story, styles['Justify'], 'El ancho de la sección debe ser al menos igual al menor valor entre 0.3 veces la \
                                                    altura de la misma y 25 cm:')
        Story.append(Spacer(1, 12))
        self.insertarTexto(Story, styles['Justify'], '0.3*h = '+str(memoria.chk2)+' cm')
        self.minChk = min(25, memoria.chk2)
        if memoria.bw >= self.minChk:
            self.insertarTexto(Story, styles['Justify'], '< bw  CUMPLE')
        else:
            self.insertarTexto(Story, styles['Justify'], '< bw  CUMPLE')
        Story.append(Spacer(1, 24))
        self.insertarTexto(Story, styles['Justify'], '2 - Diseño del refuerzo longitudinal')
        Story.append(Spacer(1, 12))
        self.insertarTexto(Story, styles['Justify'], '2.1 - Momentos últimos provenientes del análisis')
        Story.append(Spacer(1, 12))
        Story.append(iMom)
        Story.append(Spacer(1, 12))
        self.insertarTexto(Story, styles['Justify'], 'Mu_neg_izq = '+str(memoria.Mu_neg_izq)+' Tonf-m')
        self.insertarTexto(Story, styles['Justify'], 'Mu_pos_izq = '+str(memoria.Mu_pos_izq)+' Tonf-m')
        self.insertarTexto(Story, styles['Justify'], 'Mu_neg_cen = '+str(memoria.Mu_neg_cen)+' Tonf-m')
        self.insertarTexto(Story, styles['Justify'], 'Mu_pos_cen = '+str(memoria.Mu_pos_cen)+' Tonf-m')
        self.insertarTexto(Story, styles['Justify'], 'Mu_neg_der = '+str(memoria.Mu_neg_der)+' Tonf-m')
        self.insertarTexto(Story, styles['Justify'], 'Mu_pos_der = '+str(memoria.Mu_pos_der)+' Tonf-m')
        Story.append(Spacer(1, 12))
        self.insertarTexto(Story, styles['Justify'], '2.2 - Definición de la resistencia nominal a flexión')
        Story.append(Spacer(1, 12))
        Story.append(imDef)
        Story.append(Spacer(1, 12))
        self.insertarTexto(Story, styles['Justify'], '2.3 - Acero mínimo')
        Story.append(Spacer(1, 12))
        self.insertarTexto(Story, styles['Justify'], 'Asmin_1 = 14*bw*d/fy = '+str(round(memoria.Asmin_1,2))+' cm2')
        self.insertarTexto(Story, styles['Justify'], 'Asmin_2 = 0.8*(fc^(1/2))*bw*d/fy = '+str(round(memoria.Asmin_2,2))+' cm2')
        self.insertarTexto(Story, styles['Justify'], 'Asmin = max(Asmin_1, Asmin_2) = '+str(round(memoria.Asmin,2))+'cm2')
        Story.append(Spacer(1, 12))
        self.insertarTexto(Story, styles['Justify'], '2.4 - Acero longitudinal requerido conforme al análisis')
        Story.append(Spacer(1, 12))
        self.insertarTexto(Story, styles['Justify'], '2.4.1 - Acero requerido para el momento negativo en el extremo izquierdo')
        Story.append(Spacer(1, 12))
        self.insertarTexto(Story, styles['Justify'], 'Mu = '+str(round(memoria.Mu_neg_izq,2))+' Tonf-m')
        self.insertarTexto(Story, styles['Justify'], 'a = d-(d^2-2*Mu/(0.85*fc*Phib*bw))^(1/2) = '+str(round(memoria.a_1,2))+' cm')
        self.insertarTexto(Story, styles['Justify'], 'c = a/B1 = '+str(round(memoria.c_1,2))+' cm')
        self.insertarTexto(Story, styles['Justify'], 'cmax = Ecu*d/(Ecu+Esmin) = '+str(round(memoria.cmax_1,2))+' cm')
        if memoria.c_1 <= memoria.cmax_1:
            self.insertarTexto(Story, styles['Justify'], 'c < cmax = Falla controlada por tracción')
        else:
            self.insertarTexto(Story, styles['Justify'], 'c > cmax = Aumentar la sección')
        self.insertarTexto(Story, styles['Justify'], 'Asreq = max( Mu/(Phib*fy*(d-a/2)), Asmin) = '+str(round(memoria.Asreq_1,2))+' cm2')
        Story.append(Spacer(1, 12))





        ptext = '<font size="12">2.4.2 - Acero requerido para el momento positivo en el extremo izquierdo</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Mu = %s Tonf-m</font>' %round(memoria.Mu_pos_izq,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">a = d-(d^2-2*Mu/(0.85*fc*Phib*bw))^(1/2) = %s cm</font>' %round(memoria.a_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">c = a/B1 = %s cm</font>' %round(memoria.c_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">cmax = Ecu*d/(Ecu+Esmin) = %s cm</font>' %round(memoria.cmax_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        if memoria.c_2 <= memoria.cmax_2:
            ptext = '<font size="12"> c < cmax = Falla controlada por tracción</font>'
            Story.append(Paragraph(ptext, styles["Justify"]))
        else:
            ptext = '<font size="12"> c > cmax = Aumentar la sección</font>'
            Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12"> Asreq = max( Mu/(Phib*fy*(d-a/2)), Asmin) = %s cm2</font>' %round(memoria.Asreq_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">2.4.3 - Acero requerido para el momento negativo en el centro</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Mu = %s Tonf-m</font>' %round(memoria.Mu_neg_cen,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">a = d-(d^2-2*Mu/(0.85*fc*Phib*bw))^(1/2) = %s cm</font>' %round(memoria.a_3,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">c = a/B1 = %s cm</font>' %round(memoria.c_3,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">cmax = Ecu*d/(Ecu+Esmin) = %s cm</font>' %round(memoria.cmax_3,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        if memoria.c_3 <= memoria.cmax_3:
            ptext = '<font size="12"> c < cmax = Falla controlada por tracción</font>'
            Story.append(Paragraph(ptext, styles["Justify"]))
        else:
            ptext = '<font size="12"> c > cmax = Aumentar la sección</font>'
            Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12"> Asreq = max( Mu/(Phib*fy*(d-a/2)), Asmin) = %s cm2</font>' %round(memoria.Asreq_3,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">2.4.4 - Acero requerido para el momento positivo en el centro</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Mu = %s Tonf-m</font>' %round(memoria.Mu_pos_cen,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">a = d-(d^2-2*Mu/(0.85*fc*Phib*bw))^(1/2) = %s cm</font>' %round(memoria.a_4,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">c = a/B1 = %s cm</font>' %round(memoria.c_4,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">cmax = Ecu*d/(Ecu+Esmin) = %s cm</font>' %round(memoria.cmax_4,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        if memoria.c_4 <= memoria.cmax_4:
            ptext = '<font size="12"> c < cmax = Falla controlada por tracción</font>'
            Story.append(Paragraph(ptext, styles["Justify"]))
        else:
            ptext = '<font size="12"> c > cmax = Aumentar la sección</font>'
            Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12"> Asreq = max( Mu/(Phib*fy*(d-a/2)), Asmin) = %s cm2</font>' %round(memoria.Asreq_4,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">2.4.5 - Acero requerido para el momento negativo en el extremo derecho</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Mu = %s Tonf-m</font>' %round(memoria.Mu_neg_der,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">a = d-(d^2-2*Mu/(0.85*fc*Phib*bw))^(1/2) = %s cm</font>' %round(memoria.a_5,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">c = a/B1 = %s cm</font>' %round(memoria.c_5,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">cmax = Ecu*d/(Ecu+Esmin) = %s cm</font>' %round(memoria.cmax_5,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        if memoria.c_5 <= memoria.cmax_5:
            ptext = '<font size="12"> c < cmax = Falla controlada por tracción</font>'
            Story.append(Paragraph(ptext, styles["Justify"]))
        else:
            ptext = '<font size="12"> c > cmax = Aumentar la sección</font>'
            Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12"> Asreq = max( Mu/(Phib*fy*(d-a/2)), Asmin) = %s cm2</font>' %round(memoria.Asreq_5,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 36))
        ptext = '<font size="12">2.4.6 - Acero requerido para el momento positivo en el extremo derecho</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Mu = %s Tonf-m</font>' %round(memoria.Mu_pos_der,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">a = d-(d^2-2*Mu/(0.85*fc*Phib*bw))^(1/2) = %s cm</font>' %round(memoria.a_6,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">c = a/B1 = %s cm</font>' %round(memoria.c_6,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">cmax = Ecu*d/(Ecu+Esmin) = %s cm</font>' %round(memoria.cmax_6,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        if memoria.c_6 <= memoria.cmax_6:
            ptext = '<font size="12"> c < cmax = Falla controlada por tracción</font>'
            Story.append(Paragraph(ptext, styles["Justify"]))
        else:
            ptext = '<font size="12"> c > cmax = Aumentar la sección</font>'
            Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12"> Asreq = max( Mu/(Phib*fy*(d-a/2)), Asmin) = %s cm2</font>' %round(memoria.Asreq_6,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 24))
        ptext = '<font size="12">2.5 - Requisitos de acero por ductilidad</font>'
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
        ptext = '<font size="12">As1_sup_req = %s cm2</font>'%round(memoria.As1_sup_req,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">As1_sup = %s cm2 SUMINISTRADO</font>'%round(memoria.As1_sup,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">As1_inf_req = max (As1_inf_cal, As1_sup/2) = %s cm2</font>'%round(memoria.As1_inf_req,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">As1_inf = %s cm2 SUMINISTRADO</font>'%round(memoria.As1_inf,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">2.5.2 - Extremo derecho</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">As2_sup_req = %s cm2</font>'%round(memoria.As2_sup_req,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">As2_sup = %s cm2 SUMINISTRADO</font>'%round(memoria.As2_sup,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">As2_inf_req = max (As1_inf_cal, As1_sup/2) = %s cm2</font>'%round(memoria.As2_inf_req,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">As2_inf = %s cm2 SUMINISTRADO</font>'%round(memoria.As2_inf,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 36))
        ptext = '<font size="12">2.5.3 - Centro</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">As_sup_req = %s cm2</font>'%round(memoria.As_sup_req,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">As_sup = %s cm2 SUMINISTRADO</font>'%round(memoria.As_sup,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">As_inf_req = max (As_inf_cal, As_sup/2) = %s cm2</font>'%round(memoria.As_inf_req,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">As_inf = %s cm2 SUMINISTRADO</font>'%round(memoria.As_inf,2)
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
        ptext = '<font size="12">Wpp = Yc*bw*h = %s tonf/m</font>'%round(memoria.Wpp,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Wscp = %s tonf/m</font>'%round(memoria.Wscp,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Wcp = Wpp + Wscp = %s tonf/m</font>'%round(memoria.Wcp,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Wcv = %s tonf/m</font>'%round(memoria.Wcv,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">3.1.3 - Análisis del caso A</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Wu = 1.2*Wcp + Y*Wcv = %s tonf/m</font>'%round(memoria.Wu_1,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Vg = Wu*Ln/2 = %s tonf</font>'%round(memoria.Vg_1,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">a1 = Fsr*fy*As1_sup/(0.85*fc*bw) = %s cm</font>'%round(memoria.a1_1,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Mmp1 = Fsr*fy*As1_sup*(d-a/2) = %s tonf-m</font>'%round(memoria.Mmp1_1,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">a2 = Fsr*fy*As1_inf/(0.85*fc*bw) = %s cm</font>'%round(memoria.a2_1,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Mmp2 = Fsr*fy*As1_inf*(d-a/2) = %s tonf-m</font>'%round(memoria.Mmp2_1,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Vp = (Mmp1+Mmp2)/Ln = %s tonf</font>'%round(memoria.Vp_1,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Ve1 = Vg + Vp = %s tonf</font>'%round(memoria.Ve1_1,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Ve2 = Vg - Vp = %s tonf</font>'%round(memoria.Ve2_1,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        Story.append(imVgA)
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">3.1.4 - Análisis del caso B</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Wu = 1.2*Wcp + Fcv*Wcv = %s tonf/m</font>'%round(memoria.Wu_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Vg = Wu*Ln/2 = %s tonf</font>'%round(memoria.Vg_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">a1 = Fsr*fy*As1_sup/(0.85*fc*bw) = %s cm</font>'%round(memoria.a1_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Mmp1 = Fsr*fy*As1_sup*(d-a/2) = %s tonf-m</font>'%round(memoria.Mmp1_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">a2 = Fsr*fy*As1_inf/(0.85*fc*bw) = %s cm</font>'%round(memoria.a2_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Mmp2 = Fsr*fy*As1_inf*(d-a/2) = %s tonf-m</font>'%round(memoria.Mmp2_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Vp = (Mmp1+Mmp2)/Ln = %s tonf</font>'%round(memoria.Vp_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Ve1 = Vg - Vp = %s tonf</font>'%round(memoria.Ve1_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Ve2 = Vg + Vp = %s tonf</font>'%round(memoria.Ve2_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        Story.append(imVgB)
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Finalmente, se tiene:</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Ve_1 = max (Ve1_CasoA, Ve1_CasoB) = %s tonf</font>'%round(memoria.Ve_1,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Ve_2 = max (Ve2_CasoA, Ve2_CasoB) = %s tonf</font>'%round(memoria.Ve_2,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Vp = max (Vp_CasoA, Vp_CasoB) = %s tonf</font>'%round(memoria.Vp,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 24))
        ptext = '<font size="12">3.2 - Diseño del acero transversal</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">3.2.1 - Corte de diseño</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Corte último del análisis (Vu) = %s tonf</font>'%round(memoria.Vu,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        self.Ve = max(memoria.Ve_1,memoria.Ve_2)
        ptext = '<font size="12">Corte máximo probable (Ve) = max (Ve_1, Ve_2) = %s tonf</font>'%round(self.Ve,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Corte de diseño (Vd) = max (Vu, Ve) = %s tonf</font>'%round(memoria.Vd,2)
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
        ptext = '<font size="12">Corte por capacidad (Vp) =  %s tonf</font>'%round(memoria.Vp,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Relación de cortes (Vp/Vd) =  %s</font>'%round(memoria.RC,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Fuerza axial (Pu) =  %s tonf</font>'%round(memoria.Pu,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Área gruesa (Ag) = bw*h = %s cm2</font>'%round(memoria.Ag/1000,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Pc =  Ag*fc/20 = %s tonf</font>'%round(memoria.Pc,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Vc =  %s tonf</font>'%round(memoria.Vc,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">3.2.3 - Disposición del acero transversal en zona de confinamiento</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">a) Definición y separación máxima de estribos por demanda.</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Vs =  Vd/phiv-Vc = %s tonf</font>'%round(memoria.Vs,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">AV =  NRamas*Ab = %s cm2</font>'%round(memoria.AV,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Smcal = AV*fy*d/Vs = %s cm</font>'%round(memoria.Smcal,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">b) Separación máxima normativa de estribos y longitud de confinamiento.</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Smnorma = min(d/4, 6*db, 15) = %s cm</font>'%round(memoria.Smnorma,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size="12">Lc = 2*h = %s cm</font>'%round(memoria.Lc,2)
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
        ptext = '<font size="12">Sgm = d/2 = %s cm</font>'%round(memoria.Sgm,2)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">b) solapes.</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size="12">Sgsm = min (10, d/4) = %s cm</font>'%round(memoria.Sgsm,2)
        Story.append(Paragraph(ptext, styles["Justify"]))




        Story.append(Spacer(1, 24))
        self.insertarTexto(Story, styles['Justify'], '4 - Resultados finales')
        Story.append(Spacer(1, 12))
        self.insertarTexto(Story, styles['Justify'], 'bw = '+str(memoria.bw)+' cm')
        self.insertarTexto(Story, styles['Justify'], 'h = '+str(memoria.h)+' cm')
        self.insertarTexto(Story, styles['Justify'], 'r = '+str(memoria.r)+' cm')
        self.insertarTexto(Story, styles['Justify'], 'dp = '+str(memoria.dp)+' cm')
        self.insertarTexto(Story, styles['Justify'], 'As1_sup = ')
        self.insertarTexto(Story, styles['Justify'], 'As1_inf = ')
        self.insertarTexto(Story, styles['Justify'], 'As2_sup = ')
        self.insertarTexto(Story, styles['Justify'], 'As2_inf = ')
        self.insertarTexto(Story, styles['Justify'], 'As_sup = ')
        self.insertarTexto(Story, styles['Justify'], 'As_inf = ')
        self.insertarTexto(Story, styles['Justify'], 'AV = ')
        self.insertarTexto(Story, styles['Justify'], 'S =  cm')
        self.insertarTexto(Story, styles['Justify'], 'Sg =  cm')
        self.insertarTexto(Story, styles['Justify'], 'Sgs =  cm')
        Story.append(Spacer(1, 24))
        self.insertarTexto(Story, styles['Justify'], '5 - Detalles típicos')
        Story.append(Spacer(1, 12))
        self.insertarTexto(Story, styles['Justify'], '5.1 - Disposición del acero transversal')
        Story.append(Spacer(1, 12))
        Story.append(imDisposicionAceroTransversal)
        Story.append(Spacer(1, 12))
        self.insertarTexto(Story, styles['Justify'], '5.2 - Ubicación de solapes del acero longitudinal')
        Story.append(Spacer(1, 12))
        Story.append(imUbicacionSolapesAceroLongitudinal)
        Story.append(Spacer(1, 24))
        self.insertarTexto(Story, styles['Justify'], '6 - Revisión de la ductilidad para la sección crítica')
        Story.append(Spacer(1, 24))
        Story.append(Spacer(1, 24))
        self.insertarTexto(Story, styles['Justify'], '7 - Estimación de la ductilidad de entrepiso (mecanismo de columna fuerte-viga débil)')
        Story.append(Spacer(1, 12))
        


















    
        base.guardarDato('Ve',dataBase,'VCALC','VALOR',str(self.Ve))
        self.doc.build(Story)

