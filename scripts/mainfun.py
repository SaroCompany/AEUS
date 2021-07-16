import math


class FuncionesVPrincipal():

    # FRAME GENERAL - SECCION IZQUIERDA
    def funcion_combo_box_municipio(self):
        self.departamento_proyecto = self.combo_box_departamento.currentText()
        self.municipio_proyecto = str(self.combo_box_municipio.currentText())
        self.codigo_municipio = str(self.datos_memoria.diccionario_colombia[
            self.departamento_proyecto][self.municipio_proyecto][0])
        self.aceleracion_pico_efectiva = (
            self.datos_memoria.diccionario_colombia[self.departamento_proyecto]
            [self.municipio_proyecto][1])
        self.velocidad_pico_efectiva = (
            self.datos_memoria.diccionario_colombia[self.departamento_proyecto]
            [self.municipio_proyecto][2])
        self.aceleracion_pico_efectiva_reducida = (
            self.datos_memoria.diccionario_colombia[self.departamento_proyecto]
            [self.municipio_proyecto][3])
        self.aceleracion_sismo_diseno = (
            self.datos_memoria.diccionario_colombia[self.departamento_proyecto]
            [self.municipio_proyecto][4])
        self.label_codigo_municipio.setText(str(self.codigo_municipio))
        self.label_aceleracion_pico_efectiva.setText(
            str(self.aceleracion_pico_efectiva))
        self.label_velocidad_pico_efectiva.setText(
            str(self.velocidad_pico_efectiva))
        self.label_aceleracion_pico_efectiva_reducida.setText(
            str(self.aceleracion_pico_efectiva_reducida))
        self.label_aceleracion_sismo_diseno.setText(
            str(self.aceleracion_sismo_diseno))
        if self.aceleracion_pico_efectiva == 0 and {
                self.velocidad_pico_efectiva == 0}:
            self.label_amenaza_sismica.setText('Ninguna')
            self.label_disipacion_requerida.setText('Ninguna')
        elif self.aceleracion_pico_efectiva <= 0.1 and self.velocidad_pico_efectiva <= 0.1:
            self.label_amenaza_sismica.setText('Baja')
            self.label_disipacion_requerida.setText(
                'Disipación mínima - DMI')
        elif (self.aceleracion_pico_efectiva >= 0.1 or self.velocidad_pico_efectiva >= 0.1) and (self.aceleracion_pico_efectiva <= 0.2 and self.velocidad_pico_efectiva <= 0.2):
            self.label_amenaza_sismica.setText('Intermedia')
            self.label_disipacion_requerida.setText(
                'Disipación moderada - DMO')
        elif self.aceleracion_pico_efectiva > 0.2 or self.velocidad_pico_efectiva > 0.2:
            self.label_amenaza_sismica.setText('Alta')
            self.label_disipacion_requerida.setText(
                'Disipación especial - DES')
        self.amenaza_sismica = self.label_amenaza_sismica.text()
        self.disipacion_requerida = self.label_disipacion_requerida.text()
        self.guardar_cambio(
            'Municipio', 'GENERAL', 'DESCRIPCION',
            self.municipio_proyecto)
        self.guardar_cambio(
            'CodigoMunicipio', 'GENERAL', 'DESCRIPCION',
            self.codigo_municipio)
        self.guardar_cambio(
            'Aa', 'GENERAL', 'DESCRIPCION',
            self.aceleracion_pico_efectiva)
        self.guardar_cambio(
            'Av', 'GENERAL', 'DESCRIPCION',
            self.velocidad_pico_efectiva)
        self.guardar_cambio(
            'Ae', 'GENERAL', 'DESCRIPCION',
            self.aceleracion_pico_efectiva_reducida)
        self.guardar_cambio(
            'Ad', 'GENERAL', 'DESCRIPCION',
            self.aceleracion_sismo_diseno)
        self.guardar_cambio(
            'AmenazaSismica', 'GENERAL', 'DESCRIPCION',
            self.amenaza_sismica)
        self.guardar_cambio(
            'DisipacionRequerida', 'GENERAL', 'DESCRIPCION',
            self.disipacion_requerida)
        self.combo_box_tipo_suelo.clear()
        self.combo_box_tipo_suelo.addItems(
            self.datos_memoria.lista_tipo_suelo)
        self.combo_box_sistema.clear()
        self.combo_box_sistema.addItems(
            self.datos_memoria.diccionario_sistema_estructural.keys())

    def funcion_combo_box_departamento(self):
        self.departamento_proyecto = self.combo_box_departamento.currentText()
        self.combo_box_municipio.clear()
        self.lista_municipios = self.datos_memoria.diccionario_colombia[
            self.departamento_proyecto]
        self.combo_box_municipio.addItems(self.lista_municipios)
        self.guardar_cambio(
            'Departamento', 'GENERAL', 'DESCRIPCION',
            self.departamento_proyecto)

    def funcion_combo_box_uso(self):
        self.grupo_uso = self.combo_box_uso.currentText()
        if self.grupo_uso == 'IV - Edificaciones indispensables':
            self.label_coeficiente_importancia.setText('1.50')
        elif self.grupo_uso == 'III - Edificaciones de atención a la comunidad':
            self.label_coeficiente_importancia.setText('1.25')
        elif self.grupo_uso == 'II - Estructuras de ocupación especial':
            self.label_coeficiente_importancia.setText('1.10')
        elif self.grupo_uso == 'I - Estructuras de ocupación normal':
            self.label_coeficiente_importancia.setText('1.00')
        else:
            self.label_coeficiente_importancia.setText('0')
        self.coeficiente_importancia = self.label_coeficiente_importancia.text()
        self.guardar_cambio(
            'Uso', 'GENERAL', 'DESCRIPCION',
            self.grupo_uso)
        self.guardar_cambio(
            'CoeficienteImportancia', 'GENERAL', 'DESCRIPCION',
            self.coeficiente_importancia)

    def funcion_combo_box_resistencia_horizontal(self):
        self.resistencia_horizontal = (
            self.combo_box_resistencia_horizontal.currentText())
        self.guardar_cambio(
            'ResistenciaHorizontal', 'GENERAL', 'DESCRIPCION',
            self.resistencia_horizontal)
        self.lista_tipo_resistencia = (
            self.datos_memoria.diccionario_sistema_estructural[
                self.combo_box_sistema.currentText()][
                    self.resistencia_horizontal].keys())
        self.combo_box_tipo_resistencia.clear()
        self.combo_box_tipo_resistencia.addItems(
            self.lista_tipo_resistencia)
        self.disipacion_minima = 'Pórticos resistentes a momentos con capacidad mínima de disipación de energía (DMI)'
        self.disipacion_moderada = 'Pórticos resistentes a momentos con capacidad moderada de disipación de energía (DMO)'
        self.disipacion_especial = 'Pórticos resistentes a momentos con capacidad especial de disipación de energía (DES)'
        if self.resistencia_horizontal == self.disipacion_minima:
            self.segunda_nota = 'El ancho mínimo (bw) no tiene restricción'
            self.tercera_nota = ''
            self.norma_requisito_columna = 'Sin restricción'
            self.dimension_min_columna = ''
            self.area_min_columna = ''
        elif self.resistencia_horizontal == self.disipacion_moderada:
            self.segunda_nota = 'El ancho mínimo (bw) es 20 cm (C.21.3.4.1)'
            self.tercera_nota = ''
            self.norma_requisito_columna = 'C.21.3.5.1'
            self.dimension_min_columna = '25'
            self.area_min_columna = '625'
        elif self.resistencia_horizontal == self.disipacion_especial:
            self.segunda_nota = 'El ancho mínimo (bw) es 25cm o 0.3*h (C.21.5.1.3)'
            self.tercera_nota = 'El ancho bw no debe exceder el ancho del elemento de apoyo (C.21.5.1.4)'
            self.norma_requisito_columna = 'C.21.6.1.1'
            self.dimension_min_columna = '30'
            self.area_min_columna = '900'
        else:
            self.segunda_nota = ''
            self.tercera_nota = ''
            self.norma_requisito_columna = ''
            self.dimension_min_columna = ''
            self.area_min_columna = ''
        self.label_segunda_nota.setText(self.segunda_nota)
        self.label_tercera_nota.setText(self.tercera_nota)
        self.label_norma_requisito_columna.setText(self.norma_requisito_columna)
        self.label_dimension_min_columna.setText(self.dimension_min_columna)
        self.label_area_min_columna.setText(self.area_min_columna)
        self.guardar_cambio(
            'segunda_nota', 'PREDIMENSION', 'DESCRIPCION',
            self.segunda_nota)
        self.guardar_cambio(
            'tercera_nota', 'PREDIMENSION', 'DESCRIPCION',
            self.tercera_nota)
        self.guardar_cambio(
            'NormaReqColumna', 'PREDIMENSION', 'DESCRIPCION',
            self.norma_requisito_columna)
        self.guardar_cambio(
            'DimMinColumna', 'PREDIMENSION', 'DESCRIPCION',
            self.dimension_min_columna)
        self.guardar_cambio(
            'AreaMinColumna', 'PREDIMENSION', 'DESCRIPCION',
            self.area_min_columna)

    def funcion_combo_box_tipo_resistencia(self):
        self.resistencia_horizontal = (
            self.combo_box_resistencia_horizontal.currentText())
        self.tipo_resistencia = (
            self.combo_box_tipo_resistencia.currentText())
        self.guardar_cambio(
            'TipoResistencia', 'GENERAL', 'DESCRIPCION',
            self.tipo_resistencia)
        self.resistencia_vertical = (
            self.datos_memoria.diccionario_sistema_estructural[
                self.combo_box_sistema.currentText()][
                    self.resistencia_horizontal][
                        self.tipo_resistencia]['vertical'])
        self.parametro_R = (
            self.datos_memoria.diccionario_sistema_estructural[
                self.combo_box_sistema.currentText()][
                    self.resistencia_horizontal][
                        self.tipo_resistencia]['R'])
        self.parametro_O = (
            self.datos_memoria.diccionario_sistema_estructural[
                self.combo_box_sistema.currentText()][
                    self.resistencia_horizontal][
                        self.tipo_resistencia]['O'])
        self.restriccion_sistema = (
            self.datos_memoria.diccionario_sistema_estructural[
                self.combo_box_sistema.currentText()][
                    self.resistencia_horizontal][
                        self.tipo_resistencia]['amenaza'])
        self.guardar_cambio(
            'ResistenciaVertical', 'GENERAL', 'DESCRIPCION',
            self.resistencia_vertical)
        self.guardar_cambio(
            'R0', 'GENERAL', 'DESCRIPCION',
            self.parametro_R)
        self.guardar_cambio(
            'O0', 'GENERAL', 'DESCRIPCION',
            self.parametro_O)
        if self.parametro_R != 0 and self.label_amenaza_sismica.text() != 'Ninguna':
            self.chequeo = self.restriccion_sistema[
                self.label_amenaza_sismica.text()][1]
            if self.chequeo == 'no':
                self.cumplimiento_sistema = 'NO CUMPLE'
            elif self.chequeo == 'ilimitada':
                self.cumplimiento_sistema = 'CUMPLE'
            else:
                if float(self.chequeo) <= float(self.line_edit_altura_maxima.text()):
                    self.cumplimiento_sistema = 'NO CUMPLE'
                else:
                    self.cumplimiento_sistema = 'CUMPLE'
        else:
            self.cumplimiento_sistema = 'NO CUMPLE'
        self.guardar_cambio(
            'CumplimientoSistema', 'GENERAL', 'DESCRIPCION',
            self.cumplimiento_sistema)
        self.label_resistencia_vertical.setText(self.resistencia_vertical)
        self.label_cumplimiento_sistema.setText(self.cumplimiento_sistema)
        self.label_parametro_R.setText(str(self.parametro_R))
        self.label_parametro_O.setText(str(self.parametro_O))
        self.line_edit_irregularidad_planta.setText('0')
        self.line_edit_irregularidad_altura.setText('0')
        self.line_edit_ausencia_redundancia.setText('0')

    def funcion_combo_box_sistema(self):
        self.sistema_estructural = self.combo_box_sistema.currentText()
        self.guardar_cambio(
            'SistemaEstructural', 'GENERAL', 'DESCRIPCION',
            self.sistema_estructural)
        self.lista_resistencia_horizontal = (
            self.datos_memoria.diccionario_sistema_estructural[
                self.sistema_estructural].keys())
        self.combo_box_resistencia_horizontal.clear()
        self.combo_box_resistencia_horizontal.addItems(
            self.lista_resistencia_horizontal)

    def funcion_combo_box_tipo_suelo(self):
        self.tipo_suelo = self.combo_box_tipo_suelo.currentText()
        self.aceleracion_pico_efectiva = float(
            self.label_aceleracion_pico_efectiva.text())
        self.velocidad_pico_efectiva = float(
            self.label_velocidad_pico_efectiva.text())
        if self.aceleracion_pico_efectiva == 0:
            self.parametro_Fa = 0
        elif self.aceleracion_pico_efectiva <= 0.1:
            self.parametro_Fa = self.datos_memoria.diccionario_Fat[
                self.tipo_suelo][0.1]
        elif self.aceleracion_pico_efectiva > 0.1 and self.aceleracion_pico_efectiva < 0.2:
            self.parametro_Fa = (self.datos_memoria.diccionario_Fat[self.tipo_suelo][0.1]+self.datos_memoria.diccionario_Fat[self.tipo_suelo][0.2])/2
        elif self.aceleracion_pico_efectiva == 0.2:
            self.parametro_Fa = self.datos_memoria.diccionario_Fat[self.tipo_suelo][0.2]
        elif self.aceleracion_pico_efectiva > 0.2 and self.aceleracion_pico_efectiva < 0.3:
            self.parametro_Fa = (self.datos_memoria.diccionario_Fat[self.tipo_suelo][0.2]+self.datos_memoria.diccionario_Fat[self.tipo_suelo][0.3])/2
        elif self.aceleracion_pico_efectiva == 0.3:
            self.parametro_Fa = self.datos_memoria.diccionario_Fat[self.tipo_suelo][0.3]
        elif self.aceleracion_pico_efectiva > 0.3 and self.aceleracion_pico_efectiva < 0.4:
            self.parametro_Fa = (self.datos_memoria.diccionario_Fat[self.tipo_suelo][0.3]+self.datos_memoria.diccionario_Fat[self.tipo_suelo][0.4])/2
        elif self.aceleracion_pico_efectiva == 0.4:
            self.parametro_Fa = self.datos_memoria.diccionario_Fat[self.tipo_suelo][0.2]
        elif self.aceleracion_pico_efectiva > 0.4 and self.aceleracion_pico_efectiva < 0.5:
            self.parametro_Fa = (self.datos_memoria.diccionario_Fat[self.tipo_suelo][0.4]+self.datos_memoria.diccionario_Fat[self.tipo_suelo][0.5])/2
        else:
            self.parametro_Fa = self.datos_memoria.diccionario_Fat[self.tipo_suelo][0.5]
        if self.velocidad_pico_efectiva == 0:
            self.parametro_Fv = 0
        elif self.velocidad_pico_efectiva <= 0.1:
            self.parametro_Fv = self.datos_memoria.diccionario_Fvt[self.tipo_suelo][0.1]
        elif self.velocidad_pico_efectiva > 0.1 and self.velocidad_pico_efectiva < 0.2:
            self.parametro_Fv = (self.datos_memoria.diccionario_Fvt[self.tipo_suelo][0.1]+self.datos_memoria.diccionario_Fvt[self.tipo_suelo][0.2])/2
        elif self.velocidad_pico_efectiva == 0.2:
            self.parametro_Fv = self.datos_memoria.diccionario_Fvt[self.tipo_suelo][0.2]
        elif self.velocidad_pico_efectiva > 0.2 and self.velocidad_pico_efectiva < 0.3:
            self.parametro_Fv = (self.datos_memoria.diccionario_Fvt[self.tipo_suelo][0.2]+self.datos_memoria.diccionario_Fvt[self.tipo_suelo][0.3])/2
        elif self.velocidad_pico_efectiva == 0.3:
            self.parametro_Fv = self.datos_memoria.diccionario_Fvt[self.tipo_suelo][0.3]
        elif self.velocidad_pico_efectiva > 0.3 and self.velocidad_pico_efectiva < 0.4:
            self.parametro_Fv = (self.datos_memoria.diccionario_Fvt[self.tipo_suelo][0.3]+self.datos_memoria.diccionario_Fvt[self.tipo_suelo][0.4])/2
        elif self.velocidad_pico_efectiva == 0.4:
            self.parametro_Fv = self.datos_memoria.diccionario_Fvt[self.tipo_suelo][0.2]
        elif self.velocidad_pico_efectiva > 0.4 and self.velocidad_pico_efectiva < 0.5:
            self.parametro_Fv = (self.datos_memoria.diccionario_Fvt[self.tipo_suelo][0.4]+self.datos_memoria.diccionario_Fvt[self.tipo_suelo][0.5])/2
        else:
            self.parametro_Fv = self.datos_memoria.diccionario_Fvt[self.tipo_suelo][0.5]
        self.guardar_cambio(
            'Fa', 'GENERAL', 'DESCRIPCION',
            round(self.parametro_Fa, 2))
        self.guardar_cambio(
            'Fv', 'GENERAL', 'DESCRIPCION',
            round(self.parametro_Fv, 2))
        self.guardar_cambio(
            'TipoSuelo', 'GENERAL', 'DESCRIPCION',
            self.tipo_suelo)
        self.label_parametro_Fa.setText(str(round(self.parametro_Fa, 2)))
        self.label_parametro_Fv.setText(str(round(self.parametro_Fv, 2)))

    # FRAME GENERAL - SECCION DERECHA
    def calcular_disipacion_energia(self):
        self.irregularidad_planta = self.line_edit_irregularidad_planta.text()
        self.irregularidad_altura = self.line_edit_irregularidad_altura.text()
        self.ausencia_redundancia = self.line_edit_ausencia_redundancia.text()
        self.parametro_R = self.label_parametro_R.text()
        if self.irregularidad_planta == '':
            self.irregularidad_planta = 0
        if self.irregularidad_altura == '':
            self.irregularidad_altura = 0
        if self.ausencia_redundancia == '':
            self.ausencia_redundancia = 0
        self.coeficiente_disipacion_energia = float(self.parametro_R)*float(
            self.irregularidad_altura)*float(self.irregularidad_planta)*float(
                self.ausencia_redundancia)
        self.label_coeficiente_disipacion_energia.setText(str(
            self.coeficiente_disipacion_energia))
        self.guardar_cambio(
            'Op', 'GENERAL', 'DESCRIPCION',
            self.irregularidad_planta)
        self.guardar_cambio(
            'Oa', 'GENERAL', 'DESCRIPCION',
            self.irregularidad_altura)
        self.guardar_cambio(
            'Or', 'GENERAL', 'DESCRIPCION',
            self.ausencia_redundancia)
        self.guardar_cambio(
            'R', 'GENERAL', 'DESCRIPCION',
            self.coeficiente_disipacion_energia)

    def funcion_combo_box_resistencia_concreto(self):
        self.combo_box_masa_concreto.clear()
        self.combo_box_masa_concreto.addItems(
            self.datos_memoria.diccionario_modulo_elasticidad_concreto.keys())
        self.resistencia_concreto = (
            self.combo_box_resistencia_concreto.currentText())
        self.guardar_cambio(
            'fc', 'GENERAL', 'DESCRIPCION',
            self.resistencia_concreto)

    def funcion_combo_box_masa_concreto(self):
        self.masa_concreto = self.combo_box_masa_concreto.currentText()
        if self.masa_concreto != 'Conoce masa del concreto':
            self.line_edit_peso_concreto.setEnabled(0)
            self.line_edit_peso_concreto.setText('0')
        else:
            self.line_edit_peso_concreto.setEnabled(1)
            self.line_edit_peso_concreto.setText('2400')
        self.combo_box_origen_concreto.clear()
        self.combo_box_origen_concreto.addItems(
            self.datos_memoria.diccionario_modulo_elasticidad_concreto[
                self.masa_concreto]['Origen'].keys())
        self.guardar_cambio(
            'MasaConcreto', 'GENERAL', 'DESCRIPCION',
            self.masa_concreto)

    def funcion_combo_box_origen_concreto(self):
        self.origen_concreto = self.combo_box_origen_concreto.currentText()
        self.guardar_cambio(
            'OrigenConcreto', 'GENERAL', 'DESCRIPCION',
            self.origen_concreto)
        self.resistencia_concreto = (
            self.combo_box_resistencia_concreto.currentText())
        if self.resistencia_concreto == '':
            self.resistencia_concreto = 0
        else:
            self.resistencia_concreto = float(
                self.resistencia_concreto)*0.0980665
        self.peso_concreto = float(
            self.line_edit_peso_concreto.text())
        self.masa_concreto = self.combo_box_masa_concreto.currentText()
        self.ecuacion_modulo_elasticidad_concreto = (
            self.datos_memoria.diccionario_modulo_elasticidad_concreto[
                self.masa_concreto]['Origen'][self.origen_concreto])
        if self.ecuacion_modulo_elasticidad_concreto == '':
            self.modulo_elasticidad_concreto = 0
        elif self.ecuacion_modulo_elasticidad_concreto == '4700*fc**(1/2)':
            self.modulo_elasticidad_concreto = (
                4700*self.resistencia_concreto**(1/2))
        elif self.ecuacion_modulo_elasticidad_concreto == '5500*fc**(1/2)':
            self.modulo_elasticidad_concreto = (
                5500*self.resistencia_concreto**(1/2))
        elif self.ecuacion_modulo_elasticidad_concreto == '3600*fc**(1/2)':
            self.modulo_elasticidad_concreto = (
                3600*self.resistencia_concreto**(1/2))
        elif self.ecuacion_modulo_elasticidad_concreto == '3900*fc**(1/2)':
            self.modulo_elasticidad_concreto = (
                3900*self.resistencia_concreto**(1/2))
        elif self.ecuacion_modulo_elasticidad_concreto == (
                'wc**(1.5)*0.047*fc**(1/2)'):
            self.modulo_elasticidad_concreto = (
                self.peso_concreto**(1.5)*0.047*self.resistencia_concreto**(
                    1/2))
        elif self.ecuacion_modulo_elasticidad_concreto == (
                'wc**(1.5)*0.041*fc**(1/2)'):
            self.modulo_elasticidad_concreto = (
                self.peso_concreto**(1.5)*0.041*self.resistencia_concreto**(
                    1/2))
        elif self.ecuacion_modulo_elasticidad_concreto == (
                'wc**(1.5)*0.031*fc**(1/2)'):
            self.modulo_elasticidad_concreto = (
                self.peso_concreto**(1.5)*0.031*self.resistencia_concreto**(
                    1/2))
        elif self.ecuacion_modulo_elasticidad_concreto == (
                'wc**(1.5)*0.034*fc**(1/2)'):
            self.modulo_elasticidad_concreto = (
                self.peso_concreto**(1.5)*0.034*self.resistencia_concreto**(
                    1/2))
        self.modulo_elasticidad_concreto = round(
            self.modulo_elasticidad_concreto*10.1972, 0)
        self.label_modulo_elasticidad_concreto.setText(
            str(self.modulo_elasticidad_concreto))
        self.guardar_cambio(
            'Ec', 'GENERAL', 'DESCRIPCION',
            self.modulo_elasticidad_concreto)
        self.line_edit_modulo_poisson.setText('0.2')
        self.line_edit_resistencia_acero.setText('4200')

    # FRAME PREDIMENSION - SECCION VIGA
    def funcion_line_edit_longitud_simple_apoyo_viga(self):
        try:
            self.longitud_simple_apoyo_viga = float(
                self.line_edit_longitud_simple_apoyo_viga.text())*100
        except ValueError:
            self.longitud_simple_apoyo_viga = 0
        self.altura_viga_simple_apoyo_t1 = math.ceil(
            self.longitud_simple_apoyo_viga/16)
        self.altura_viga_simple_apoyo_t2 = math.ceil(
            self.longitud_simple_apoyo_viga/11)
        self.label_viga_simple_apoyo_t1.setText(
            str(self.altura_viga_simple_apoyo_t1))
        self.label_viga_simple_apoyo_t2.setText(
            str(self.altura_viga_simple_apoyo_t2))
        self.altura_viga_simple_apoyo_prom = math.ceil(
            (self.altura_viga_simple_apoyo_t1+self.altura_viga_simple_apoyo_t2)/2)
        self.label_viga_simple_apoyo_prom.setText(
            str(self.altura_viga_simple_apoyo_prom))
        self.guardar_cambio(
            'LongitudSAViga', 'PREDIMENSION', 'DESCRIPCION',
            self.longitud_simple_apoyo_viga/100)
        self.guardar_cambio(
            'h_SA_viga_t1', 'PREDIMENSION', 'DESCRIPCION',
            self.altura_viga_simple_apoyo_t1)
        self.guardar_cambio(
            'h_SA_viga_t2', 'PREDIMENSION', 'DESCRIPCION',
            self.altura_viga_simple_apoyo_t2)
        self.guardar_cambio(
            'h_SA_viga_prom', 'PREDIMENSION', 'DESCRIPCION',
            self.altura_viga_simple_apoyo_prom)

    def funcion_line_edit_longitud_un_extremo_viga(self):
        try:
            self.longitud_un_extremo_viga = float(
                self.line_edit_longitud_un_extremo_viga.text())*100
        except ValueError:
            self.longitud_un_extremo_viga = 0
        self.altura_viga_un_extremo_t1 = math.ceil(
            self.longitud_un_extremo_viga/18.5)
        self.altura_viga_un_extremo_t2 = math.ceil(
            self.longitud_un_extremo_viga/12)
        self.label_viga_un_extremo_t1.setText(
            str(self.altura_viga_un_extremo_t1))
        self.label_viga_un_extremo_t2.setText(
            str(self.altura_viga_un_extremo_t2))
        self.altura_viga_un_extremo_prom = math.ceil(
            (self.altura_viga_un_extremo_t1+self.altura_viga_un_extremo_t2)/2)
        self.label_viga_un_extremo_prom.setText(
            str(self.altura_viga_un_extremo_prom))
        self.guardar_cambio(
            'LongitudUECViga', 'PREDIMENSION', 'DESCRIPCION',
            self.longitud_un_extremo_viga/100)
        self.guardar_cambio(
            'h_UEC_viga_t1', 'PREDIMENSION', 'DESCRIPCION',
            self.altura_viga_un_extremo_t1)
        self.guardar_cambio(
            'h_UEC_viga_t2', 'PREDIMENSION', 'DESCRIPCION',
            self.altura_viga_un_extremo_t2)
        self.guardar_cambio(
            'h_UEC_viga_prom', 'PREDIMENSION', 'DESCRIPCION',
            self.altura_viga_un_extremo_prom)

    def funcion_line_edit_longitud_ambos_extremos_viga(self):
        try:
            self.longitud_ambos_extremos_viga = float(
                self.line_edit_longitud_ambos_extremos_viga.text())*100
        except ValueError:
            self.longitud_ambos_extremos_viga = 0
        self.altura_viga_ambos_extremos_t1 = math.ceil(
            self.longitud_ambos_extremos_viga/21)
        self.altura_viga_ambos_extremos_t2 = math.ceil(
            self.longitud_ambos_extremos_viga/14)
        self.label_viga_ambos_extremos_t1.setText(str(
            self.altura_viga_ambos_extremos_t1))
        self.label_viga_ambos_extremos_t2.setText(str(
            self.altura_viga_ambos_extremos_t2))
        self.altura_viga_ambos_extremos_prom = math.ceil(
            (self.altura_viga_ambos_extremos_t1+self.altura_viga_ambos_extremos_t2)/2)
        self.label_viga_ambos_extremos_prom.setText(
            str(self.altura_viga_ambos_extremos_prom))
        self.guardar_cambio(
            'LongitudAECViga', 'PREDIMENSION', 'DESCRIPCION',
            self.longitud_ambos_extremos_viga/100)
        self.guardar_cambio(
            'h_AEC_viga_t1', 'PREDIMENSION', 'DESCRIPCION',
            self.altura_viga_ambos_extremos_t1)
        self.guardar_cambio(
            'h_AEC_viga_t2', 'PREDIMENSION', 'DESCRIPCION',
            self.altura_viga_ambos_extremos_t2)
        self.guardar_cambio(
            'h_AEC_viga_prom', 'PREDIMENSION', 'DESCRIPCION',
            self.altura_viga_ambos_extremos_prom)

    def funcion_line_edit_longitud_voladizo_viga(self):
        try:
            self.longitud_voladizo_viga = float(
                self.line_edit_longitud_voladizo_viga.text())*100
        except ValueError:
            self.longitud_voladizo_viga = 0
        self.altura_viga_voladizo_t1 = math.ceil(self.longitud_voladizo_viga/8)
        self.altura_viga_voladizo_t2 = math.ceil(self.longitud_voladizo_viga/5)
        self.label_viga_voladizo_t1.setText(str(self.altura_viga_voladizo_t1))
        self.label_viga_voladizo_t2.setText(str(self.altura_viga_voladizo_t2))
        self.altura_viga_voladizo_prom = math.ceil(
            (self.altura_viga_voladizo_t1+self.altura_viga_voladizo_t2)/2)
        self.label_viga_voladizo_prom.setText(
            str(self.altura_viga_voladizo_prom))
        self.guardar_cambio(
            'LongitudVViga', 'PREDIMENSION', 'DESCRIPCION',
            self.longitud_voladizo_viga/100)
        self.guardar_cambio(
            'h_V_viga_t1', 'PREDIMENSION', 'DESCRIPCION',
            self.altura_viga_voladizo_t1)
        self.guardar_cambio(
            'h_V_viga_t2', 'PREDIMENSION', 'DESCRIPCION',
            self.altura_viga_voladizo_t2)
        self.guardar_cambio(
            'h_V_viga_prom', 'PREDIMENSION', 'DESCRIPCION',
            self.altura_viga_voladizo_prom)

    def funcion_dimensiones_viga(self):
        self.altura_viga = (
            self.line_edit_altura_viga.text())
        self.base_viga = (
            self.line_edit_base_viga.text())
        self.guardar_cambio(
            'h_viga', 'PREDIMENSION', 'DESCRIPCION',
            self.altura_viga)
        self.guardar_cambio(
            'bw_viga', 'PREDIMENSION', 'DESCRIPCION',
            self.base_viga)

    # FRAME PREDIMENSION - SECCION COLUMNA
    def calcular_predimensiones_columna(self):
        self.numero_pisos_columna = self.spin_box_numero_pisos_columna.value()
        self.ubicacion_columna = self.combo_box_ubicacion_columna.currentText()
        try:
            self.base_viga_sobre_columna = float(
                self.line_edit_base_viga_sobre_columna.text())
        except ValueError:
            self.base_viga_sobre_columna = 0
        try:
            self.altura_viga_sobre_columna = float(
                self.line_edit_altura_viga_sobre_columna.text())
        except ValueError:
            self.altura_viga_sobre_columna = 0
        try:
            self.longitud_viga_sobre_columna = float(
                self.line_edit_longitud_viga_sobre_columna.text())
        except ValueError:
            self.longitud_viga_sobre_columna = 0
        try:
            self.area_aferente_columna = float(
                self.line_edit_area_aferente_columna.text())
        except ValueError:
            self.area_aferente_columna = 0
        try:
            self.carga_muerta_columna = float(
                self.line_edit_carga_muerta_columna.text())
        except ValueError:
            self.carga_muerta_columna = 0
        try:
            self.carga_viva_columna = float(
                self.line_edit_carga_viva_columna.text())
        except ValueError:
            self.carga_viva_columna = 0
        self.peso_propio_viga_sobre_columna = self.longitud_viga_sobre_columna*(self.altura_viga_sobre_columna/100)*(self.base_viga_sobre_columna/100)*2.4/self.area_aferente_columna
        self.carga_muerta_total_columna = self.carga_muerta_columna+self.peso_propio_viga_sobre_columna
        self.carga_ultima_columna = 1.2*self.area_aferente_columna*self.numero_pisos_columna*self.carga_muerta_total_columna+1.6*self.area_aferente_columna*self.numero_pisos_columna*self.carga_viva_columna
        if self.ubicacion_columna == '':
            self.area_gruesa_columna = 0
        elif self.ubicacion_columna == 'INTERIOR':
            self.area_gruesa_columna = 18*self.carga_ultima_columna
        elif self.ubicacion_columna == 'LATERAL':
            self.area_gruesa_columna = 43*self.carga_ultima_columna
        if self.area_gruesa_columna != 0:
            self.raiz2_ag_columna = self.area_gruesa_columna**(1/2)
        else:
            self.raiz2_ag_columna = 0
        self.dimensiones_columna = f'{math.ceil(self.raiz2_ag_columna)}x{math.ceil(self.raiz2_ag_columna)}'
        self.label_dimensiones_cuadrado_columna.setText(self.dimensiones_columna)
        self.guardar_cambio(
            'NPisosColumna', 'PREDIMENSION', 'DESCRIPCION',
            self.numero_pisos_columna)
        self.guardar_cambio(
            'UbicacionColumna', 'PREDIMENSION', 'DESCRIPCION',
            self.ubicacion_columna)
        self.guardar_cambio(
            'bw_vigaColumna', 'PREDIMENSION', 'DESCRIPCION',
            self.base_viga_sobre_columna)
        self.guardar_cambio(
            'h_vigaColumna', 'PREDIMENSION', 'DESCRIPCION',
            self.altura_viga_sobre_columna)
        self.guardar_cambio(
            'Lv_vigaColumna', 'PREDIMENSION', 'DESCRIPCION',
            self.longitud_viga_sobre_columna)
        self.guardar_cambio(
            'AA_columna', 'PREDIMENSION', 'DESCRIPCION',
            self.area_aferente_columna)
        self.guardar_cambio(
            'CM_columna', 'PREDIMENSION', 'DESCRIPCION',
            self.carga_muerta_columna)
        self.guardar_cambio(
            'CV_columna', 'PREDIMENSION', 'DESCRIPCION',
            self.carga_viva_columna)
        self.guardar_cambio(
            'DimenCuadradoCol', 'PREDIMENSION', 'DESCRIPCION',
            self.dimensiones_columna)
        self.guardar_cambio(
            'PPv_col', 'PREDIMENSION', 'DESCRIPCION',
            self.peso_propio_viga_sobre_columna)
        self.guardar_cambio(
            'CMT_col', 'PREDIMENSION', 'DESCRIPCION',
            self.carga_muerta_total_columna)
        self.guardar_cambio(
            'Wu_col', 'PREDIMENSION', 'DESCRIPCION',
            self.carga_ultima_columna)
        self.guardar_cambio(
            'Ag_col', 'PREDIMENSION', 'DESCRIPCION',
            self.area_gruesa_columna)
        self.guardar_cambio(
            'Raiz2_Ag_col', 'PREDIMENSION', 'DESCRIPCION',
            self.raiz2_ag_columna)

    def calcular_refuerzo_longitudinal_requerido_columna(self):
        try:
            self.dimension_x_columna = float(
                self.line_edit_dimension_x_columna.text())
        except ValueError:
            self.dimension_x_columna = 0
        try:
            self.dimension_y_columna = float(
                self.line_edit_dimension_y_columna.text())
        except ValueError:
            self.dimension_y_columna = 0
        self.guardar_cambio(
            'x_columna', 'PREDIMENSION', 'DESCRIPCION',
            self.dimension_x_columna)
        self.guardar_cambio(
            'y_columna', 'PREDIMENSION', 'DESCRIPCION',
            self.dimension_y_columna)
        self.acero_min_columna = self.dimension_y_columna*self.dimension_x_columna*0.01
        self.guardar_cambio(
            'As_min_col', 'PREDIMENSION', 'DESCRIPCION',
            self.acero_min_columna)
        self.refuerzo_longitudinal_requerido_columna = f'MÍN {self.acero_min_columna} cm2'
        self.label_refuerzo_longitudinal_requerido_columna.setText(
            self.refuerzo_longitudinal_requerido_columna)
        self.guardar_cambio(
            'RefLongReqCol', 'PREDIMENSION', 'DESCRIPCION',
            self.refuerzo_longitudinal_requerido_columna)

    # FRAME PREDIMENSION - SECCION LOSA ALIGERADA EN UNA DIRECCION
    def determinar_uso_losa_a1d(self):
        self.uso_losa_a1d = self.combo_box_uso_losa_aligerada_1d.currentText()
        if self.uso_losa_a1d == 'NO se usa':
            self.tab_widget_losa_A1D.setEnabled(0)
        else:
            self.tab_widget_losa_A1D.setEnabled(1)
        self.guardar_cambio(
            'UsoLA1D', 'LOSAS', 'DESCRIPCION',
            self.uso_losa_a1d)

    def funcion_line_edit_longitud_simple_apoyo_losa_a1d(self):
        try:
            self.longitud_simple_apoyo_losa_a1d = float(
                self.line_edit_longitud_simple_apoyo_losa_a1d.text())*100
        except ValueError:
            self.longitud_simple_apoyo_losa_a1d = 0
        self.altura_losa_a1d_simple_apoyo_t1 = math.ceil(
            self.longitud_simple_apoyo_losa_a1d/16)
        self.altura_losa_a1d_simple_apoyo_t2 = math.ceil(
            self.longitud_simple_apoyo_losa_a1d/11)
        self.label_losa_a1d_simple_apoyo_t1.setText(
            str(self.altura_losa_a1d_simple_apoyo_t1))
        self.label_losa_a1d_simple_apoyo_t2.setText(
            str(self.altura_losa_a1d_simple_apoyo_t2))
        self.altura_losa_a1d_simple_apoyo_prom = math.ceil(
            (self.altura_losa_a1d_simple_apoyo_t1+self.altura_losa_a1d_simple_apoyo_t2)/2)
        self.label_losa_a1d_simple_apoyo_prom.setText(
            str(self.altura_losa_a1d_simple_apoyo_prom))
        self.guardar_cambio(
            'LongitudSALA1D', 'LOSAS', 'DESCRIPCION',
            self.longitud_simple_apoyo_losa_a1d/100)
        self.guardar_cambio(
            'h_SA_LA1D_t1', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_a1d_simple_apoyo_t1)
        self.guardar_cambio(
            'h_SA_LA1D_t2', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_a1d_simple_apoyo_t2)
        self.guardar_cambio(
            'h_SA_LA1D_prom', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_a1d_simple_apoyo_prom)

    def funcion_line_edit_longitud_un_extremo_losa_a1d(self):
        try:
            self.longitud_un_extremo_losa_a1d = float(
                self.line_edit_longitud_un_extremo_losa_a1d.text())*100
        except ValueError:
            self.longitud_un_extremo_losa_a1d = 0
        self.altura_losa_a1d_un_extremo_t1 = math.ceil(
            self.longitud_un_extremo_losa_a1d/18.5)
        self.altura_losa_a1d_un_extremo_t2 = math.ceil(
            self.longitud_un_extremo_losa_a1d/12)
        self.label_losa_a1d_un_extremo_t1.setText(
            str(self.altura_losa_a1d_un_extremo_t1))
        self.label_losa_a1d_un_extremo_t2.setText(
            str(self.altura_losa_a1d_un_extremo_t2))
        self.altura_losa_a1d_un_extremo_prom = math.ceil(
            (self.altura_losa_a1d_un_extremo_t1+self.altura_losa_a1d_un_extremo_t2)/2)
        self.label_losa_a1d_un_extremo_prom.setText(
            str(self.altura_losa_a1d_un_extremo_prom))
        self.guardar_cambio(
            'LongitudUECLA1D', 'LOSAS', 'DESCRIPCION',
            self.longitud_un_extremo_losa_a1d/100)
        self.guardar_cambio(
            'h_UEC_LA1D_t1', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_a1d_un_extremo_t1)
        self.guardar_cambio(
            'h_UEC_LA1D_t2', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_a1d_un_extremo_t2)
        self.guardar_cambio(
            'h_UEC_LA1D_prom', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_a1d_un_extremo_prom)

    def funcion_line_edit_longitud_ambos_extremos_losa_a1d(self):
        try:
            self.longitud_ambos_extremos_losa_a1d = float(
                self.line_edit_longitud_ambos_extremos_losa_a1d.text())*100
        except ValueError:
            self.longitud_ambos_extremos_losa_a1d = 0
        self.altura_losa_a1d_ambos_extremos_t1 = math.ceil(
            self.longitud_ambos_extremos_losa_a1d/21)
        self.altura_losa_a1d_ambos_extremos_t2 = math.ceil(
            self.longitud_ambos_extremos_losa_a1d/14)
        self.label_losa_a1d_ambos_extremos_t1.setText(str(
            self.altura_losa_a1d_ambos_extremos_t1))
        self.label_losa_a1d_ambos_extremos_t2.setText(str(
            self.altura_losa_a1d_ambos_extremos_t2))
        self.altura_losa_a1d_ambos_extremos_prom = math.ceil(
            (self.altura_losa_a1d_ambos_extremos_t1+self.altura_losa_a1d_ambos_extremos_t2)/2)
        self.label_losa_a1d_ambos_extremos_prom.setText(
            str(self.altura_losa_a1d_ambos_extremos_prom))
        self.guardar_cambio(
            'LongitudAECLA1D', 'LOSAS', 'DESCRIPCION',
            self.longitud_ambos_extremos_losa_a1d/100)
        self.guardar_cambio(
            'h_AEC_LA1D_t1', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_a1d_ambos_extremos_t1)
        self.guardar_cambio(
            'h_AEC_LA1D_t2', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_a1d_ambos_extremos_t2)
        self.guardar_cambio(
            'h_AEC_LA1D_prom', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_a1d_ambos_extremos_prom)

    def funcion_line_edit_longitud_voladizo_losa_a1d(self):
        try:
            self.longitud_voladizo_losa_a1d = float(
                self.line_edit_longitud_voladizo_losa_a1d.text())*100
        except ValueError:
            self.longitud_voladizo_losa_a1d = 0
        self.altura_losa_a1d_voladizo_t1 = math.ceil(self.longitud_voladizo_losa_a1d/8)
        self.altura_losa_a1d_voladizo_t2 = math.ceil(self.longitud_voladizo_losa_a1d/5)
        self.label_losa_a1d_voladizo_t1.setText(str(self.altura_losa_a1d_voladizo_t1))
        self.label_losa_a1d_voladizo_t2.setText(str(self.altura_losa_a1d_voladizo_t2))
        self.altura_losa_a1d_voladizo_prom = math.ceil(
            (self.altura_losa_a1d_voladizo_t1+self.altura_losa_a1d_voladizo_t2)/2)
        self.label_losa_a1d_voladizo_prom.setText(
            str(self.altura_losa_a1d_voladizo_prom))
        self.guardar_cambio(
            'LongitudVLA1D', 'LOSAS', 'DESCRIPCION',
            self.longitud_voladizo_losa_a1d/100)
        self.guardar_cambio(
            'h_V_LA1D_t1', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_a1d_voladizo_t1)
        self.guardar_cambio(
            'h_V_LA1D_t2', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_a1d_voladizo_t2)
        self.guardar_cambio(
            'h_V_LA1D_prom', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_a1d_voladizo_prom)

    def funcion_line_edit_altura_losa_a1d(self):
        self.guardar_cambio(
                'h_losa_a1d', 'LOSAS', 'DESCRIPCION',
                self.line_edit_altura_losa_a1d.text())
        self.combo_box_direccion_losa_a1d.clear()
        self.combo_box_direccion_losa_a1d.addItems(
            self.datos_memoria.lista_direcciones)

    def funcion_combo_box_direccion_losa_a1d(self):
        self.direccion_losa_a1d = (
            self.combo_box_direccion_losa_a1d.currentText())
        if self.direccion_losa_a1d == 'X' or self.direccion_losa_a1d == 'Y':
            self.espesor_minimo_loseta_losa_a1d = 4.5
            self.base_minima_nervadura_losa_a1d = 10
            try:
                self.altura_losa_a1d = float(
                    self.line_edit_altura_losa_a1d.text())
            except ValueError:
                self.altura_losa_a1d = 0
            self.separacion_maxima_nervadura_losa_a1d = (
                self.altura_losa_a1d*2.5)
            self.espaseamiento_riostra_losa_a1d = self.altura_losa_a1d/10  # h*10 => h*10/100
        else:
            self.espesor_minimo_loseta_losa_a1d = 0
            self.base_minima_nervadura_losa_a1d = 0
            self.altura_losa_a1d = 0
            self.separacion_maxima_nervadura_losa_a1d = 0
            self.espaseamiento_riostra_losa_a1d = 0
            self.line_edit_base_nervio_losa_a1d.clear()
            self.line_edit_espesor_loseta_losa_a1d.clear()
            self.line_edit_separacion_nervadura_losa_a1d.clear()
        self.label_espesor_minimo_loseta_losa_a1d.setText(str(
            self.espesor_minimo_loseta_losa_a1d))
        self.label_base_minima_nervadura_losa_a1d.setText(str(
            self.base_minima_nervadura_losa_a1d))
        self.label_separacion_maxima_nervadura_losa_a1d.setText(str(
            self.separacion_maxima_nervadura_losa_a1d))
        self.label_espaseamiento_riostra_losa_a1d.setText(str(
            self.espaseamiento_riostra_losa_a1d))
        self.guardar_cambio(
                'direccion_losa_a1d', 'LOSAS', 'DESCRIPCION',
                self.direccion_losa_a1d)
        self.guardar_cambio(
                'loseta_e_min_losa_a1d', 'LOSAS', 'DESCRIPCION',
                self.espesor_minimo_loseta_losa_a1d)
        self.guardar_cambio(
                'nervadura_bw_min_losa_a1d', 'LOSAS', 'DESCRIPCION',
                self.base_minima_nervadura_losa_a1d)
        self.guardar_cambio(
                'Sn_max_nervadura_losa_a1d', 'LOSAS', 'DESCRIPCION',
                self.separacion_maxima_nervadura_losa_a1d)
        self.guardar_cambio(
                'riostra_losa_a1d', 'LOSAS', 'DESCRIPCION',
                self.espaseamiento_riostra_losa_a1d)

    def funcion_line_edit_base_nervio_losa_a1d(self):
        try:
            self.base_nervio_losa_a1d = float(
                self.line_edit_base_nervio_losa_a1d.text())
        except ValueError:
            self.base_nervio_losa_a1d = 0
        self.altura_libre_maxima_nervio_losa_a1d = (
            self.base_nervio_losa_a1d*5)
        self.label_altura_libre_maxima_nervio_losa_a1d.setText(str(
            self.altura_libre_maxima_nervio_losa_a1d))
        self.guardar_cambio(
                'bw_nervio_losa_a1d', 'LOSAS', 'DESCRIPCION',
                self.base_nervio_losa_a1d)
        self.guardar_cambio(
                'h_libre_max_nervio_losa_a1d', 'LOSAS', 'DESCRIPCION',
                self.altura_libre_maxima_nervio_losa_a1d)

    # FRAME PREDIMENSION - SECCION LOSA MACIZA EN UNA DIRECCION
    def determinar_uso_losa_m1d(self):
        self.uso_losa_m1d = self.combo_box_uso_losa_maciza_1d.currentText()
        if self.uso_losa_m1d == 'NO se usa':
            self.group_box_losa_M1D.setEnabled(0)
        else:
            self.group_box_losa_M1D.setEnabled(1)
        self.guardar_cambio(
            'UsoLM1D', 'LOSAS', 'DESCRIPCION',
            self.uso_losa_m1d)

    def funcion_line_edit_longitud_simple_apoyo_losa_m1d(self):
        try:
            self.longitud_simple_apoyo_losa_m1d = float(
                self.line_edit_longitud_simple_apoyo_losa_m1d.text())*100
        except ValueError:
            self.longitud_simple_apoyo_losa_m1d = 0
        self.altura_losa_m1d_simple_apoyo_t1 = math.ceil(
            self.longitud_simple_apoyo_losa_m1d/20)
        self.altura_losa_m1d_simple_apoyo_t2 = math.ceil(
            self.longitud_simple_apoyo_losa_m1d/14)
        self.label_losa_m1d_simple_apoyo_t1.setText(
            str(self.altura_losa_m1d_simple_apoyo_t1))
        self.label_losa_m1d_simple_apoyo_t2.setText(
            str(self.altura_losa_m1d_simple_apoyo_t2))
        self.altura_losa_m1d_simple_apoyo_prom = math.ceil(
            (self.altura_losa_m1d_simple_apoyo_t1+self.altura_losa_m1d_simple_apoyo_t2)/2)
        self.label_losa_m1d_simple_apoyo_prom.setText(
            str(self.altura_losa_m1d_simple_apoyo_prom))
        self.guardar_cambio(
            'LongitudSALM1D', 'LOSAS', 'DESCRIPCION',
            self.longitud_simple_apoyo_losa_m1d/100)
        self.guardar_cambio(
            'h_SA_LM1D_t1', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_m1d_simple_apoyo_t1)
        self.guardar_cambio(
            'h_SA_LM1D_t2', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_m1d_simple_apoyo_t2)
        self.guardar_cambio(
            'h_SA_LM1D_prom', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_m1d_simple_apoyo_prom)

    def funcion_line_edit_longitud_un_extremo_losa_m1d(self):
        try:
            self.longitud_un_extremo_losa_m1d = float(
                self.line_edit_longitud_un_extremo_losa_m1d.text())*100
        except ValueError:
            self.longitud_un_extremo_losa_m1d = 0
        self.altura_losa_m1d_un_extremo_t1 = math.ceil(
            self.longitud_un_extremo_losa_m1d/24)
        self.altura_losa_m1d_un_extremo_t2 = math.ceil(
            self.longitud_un_extremo_losa_m1d/16)
        self.label_losa_m1d_un_extremo_t1.setText(
            str(self.altura_losa_m1d_un_extremo_t1))
        self.label_losa_m1d_un_extremo_t2.setText(
            str(self.altura_losa_m1d_un_extremo_t2))
        self.altura_losa_m1d_un_extremo_prom = math.ceil(
            (self.altura_losa_m1d_un_extremo_t1+self.altura_losa_m1d_un_extremo_t2)/2)
        self.label_losa_m1d_un_extremo_prom.setText(
            str(self.altura_losa_m1d_un_extremo_prom))
        self.guardar_cambio(
            'LongitudUECLM1D', 'LOSAS', 'DESCRIPCION',
            self.longitud_un_extremo_losa_m1d/100)
        self.guardar_cambio(
            'h_UEC_LM1D_t1', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_m1d_un_extremo_t1)
        self.guardar_cambio(
            'h_UEC_LM1D_t2', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_m1d_un_extremo_t2)
        self.guardar_cambio(
            'h_UEC_LM1D_prom', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_m1d_un_extremo_prom)

    def funcion_line_edit_longitud_ambos_extremos_losa_m1d(self):
        try:
            self.longitud_ambos_extremos_losa_m1d = float(
                self.line_edit_longitud_ambos_extremos_losa_m1d.text())*100
        except ValueError:
            self.longitud_ambos_extremos_losa_m1d = 0
        self.altura_losa_m1d_ambos_extremos_t1 = math.ceil(
            self.longitud_ambos_extremos_losa_m1d/28)
        self.altura_losa_m1d_ambos_extremos_t2 = math.ceil(
            self.longitud_ambos_extremos_losa_m1d/19)
        self.label_losa_m1d_ambos_extremos_t1.setText(str(
            self.altura_losa_m1d_ambos_extremos_t1))
        self.label_losa_m1d_ambos_extremos_t2.setText(str(
            self.altura_losa_m1d_ambos_extremos_t2))
        self.altura_losa_m1d_ambos_extremos_prom = math.ceil(
            (self.altura_losa_m1d_ambos_extremos_t1+self.altura_losa_m1d_ambos_extremos_t2)/2)
        self.label_losa_m1d_ambos_extremos_prom.setText(
            str(self.altura_losa_m1d_ambos_extremos_prom))
        self.guardar_cambio(
            'LongitudAECLM1D', 'LOSAS', 'DESCRIPCION',
            self.longitud_ambos_extremos_losa_m1d/100)
        self.guardar_cambio(
            'h_AEC_LM1D_t1', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_m1d_ambos_extremos_t1)
        self.guardar_cambio(
            'h_AEC_LM1D_t2', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_m1d_ambos_extremos_t2)
        self.guardar_cambio(
            'h_AEC_LM1D_prom', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_m1d_ambos_extremos_prom)

    def funcion_line_edit_longitud_voladizo_losa_m1d(self):
        try:
            self.longitud_voladizo_losa_m1d = float(
                self.line_edit_longitud_voladizo_losa_m1d.text())*100
        except ValueError:
            self.longitud_voladizo_losa_m1d = 0
        self.altura_losa_m1d_voladizo_t1 = math.ceil(
            self.longitud_voladizo_losa_m1d/10)
        self.altura_losa_m1d_voladizo_t2 = math.ceil(
            self.longitud_voladizo_losa_m1d/7)
        self.label_losa_m1d_voladizo_t1.setText(str(
            self.altura_losa_m1d_voladizo_t1))
        self.label_losa_m1d_voladizo_t2.setText(str(
            self.altura_losa_m1d_voladizo_t2))
        self.altura_losa_m1d_voladizo_prom = math.ceil(
            (self.altura_losa_m1d_voladizo_t1+self.altura_losa_m1d_voladizo_t2)/2)
        self.label_losa_m1d_voladizo_prom.setText(
            str(self.altura_losa_m1d_voladizo_prom))
        self.guardar_cambio(
            'LongitudVLM1D', 'LOSAS', 'DESCRIPCION',
            self.longitud_voladizo_losa_m1d/100)
        self.guardar_cambio(
            'h_V_LM1D_t1', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_m1d_voladizo_t1)
        self.guardar_cambio(
            'h_V_LM1D_t2', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_m1d_voladizo_t2)
        self.guardar_cambio(
            'h_V_LM1D_prom', 'LOSAS', 'DESCRIPCION',
            self.altura_losa_m1d_voladizo_prom)

    # FRAME PREDIMENSION - SECCION LOSA ALIGERADA EN DOS DIRECCIONES
    def determinar_uso_losa_a2d(self):
        self.uso_losa_a2d = self.combo_box_uso_losa_aligerada_2d.currentText()
        if self.uso_losa_a2d == 'NO se usa':
            self.tab_widget_losa_A2D.setEnabled(0)
        else:
            self.tab_widget_losa_A2D.setEnabled(1)

    # FRAME PREDIMENSION - SECCION LOSA MACIZA EN DOS DIRECCIONES
    def determinar_uso_losa_m2d(self):
        self.uso_losa_m2d = self.combo_box_uso_losa_maciza_2d.currentText()
        if self.uso_losa_m2d == 'NO se usa':
            self.group_box_losa_M2D.setEnabled(0)
        else:
            self.group_box_losa_M2D.setEnabled(1)
        self.guardar_cambio(
            'UsoLM2D', 'LOSAS', 'DESCRIPCION',
            self.uso_losa_m2d)

    def funcion_line_edit_longitud_libre_maxima_losa_m2d(self):
        self.longitud_libre_maxima_losa_m2d = float(
            self.line_edit_longitud_libre_maxima_losa_m2d.text())*100
        self.peralte_inicial_losa_m2d = self.longitud_libre_maxima_losa_m2d/40
        self.label_peralte_inicial_losa_m2d.setText(str(
            self.peralte_inicial_losa_m2d))
        self.guardar_cambio(
            'LongitudLibreMaximaLM2D', 'LOSAS', 'DESCRIPCION',
            self.longitud_libre_maxima_losa_m2d/100)
        self.guardar_cambio(
            'PeralteInicialLM2D', 'LOSAS', 'DESCRIPCION',
            self.peralte_inicial_losa_m2d)
        self.line_edit_altura_inicial_losa_m2d.setText(str(math.ceil(
            self.peralte_inicial_losa_m2d)))

    def calcular_factores_viga_interior_losa_m2d(self):
        try:
            self.altura_inicial_losa_m2d = float(
                self.line_edit_altura_inicial_losa_m2d.text())
        except ValueError:
            self.altura_inicial_losa_m2d = 0
        try:
            self.base_viga_interior_losa_m2d = float(
                self.line_edit_base_viga_interior_losa_m2d.text())
        except ValueError:
            self.base_viga_interior_losa_m2d = 0
        try:
            self.altura_viga_interior_losa_m2d = float(
                self.line_edit_altura_viga_interior_losa_m2d.text())
        except ValueError:
            self.altura_viga_interior_losa_m2d = 0
        self.parametro_a_vi_losa_m2d = (
            self.altura_viga_interior_losa_m2d - self.altura_inicial_losa_m2d)
        self.parametro_bf_vi_losa_m2d = (
            self.base_viga_interior_losa_m2d + 2*self.parametro_a_vi_losa_m2d)
        self.restriccion_bf_vi_losa_m2d = (
            self.base_viga_interior_losa_m2d + 8*self.altura_inicial_losa_m2d)
        if self.parametro_bf_vi_losa_m2d <= self.restriccion_bf_vi_losa_m2d:
            self.factor_b_h_vi_losa_m2d = (
                self.base_viga_interior_losa_m2d/self.altura_inicial_losa_m2d)
            self.factor_hv_h_vi_losa_m2d = (
                self.altura_viga_interior_losa_m2d / self.altura_inicial_losa_m2d)
        else:
            self.factor_b_h_vi_losa_m2d = 0
            self.factor_hv_h_vi_losa_m2d = 0
        self.label_factor_b_h_vi_losa_m2d.setText(str(
            self.factor_b_h_vi_losa_m2d))
        self.label_factor_hv_h_vi_losa_m2d.setText(str(
            self.factor_hv_h_vi_losa_m2d))

    def calcular_factores_viga_exterior_losa_m2d(self):
        try:
            self.altura_inicial_losa_m2d = float(
                self.line_edit_altura_inicial_losa_m2d.text())
        except ValueError:
            self.altura_inicial_losa_m2d = 0
        try:
            self.base_viga_exterior_losa_m2d = float(
                self.line_edit_base_viga_exterior_losa_m2d.text())
        except ValueError:
            self.base_viga_exterior_losa_m2d = 0
        try:
            self.altura_viga_exterior_losa_m2d = float(
                self.line_edit_altura_viga_exterior_losa_m2d.text())
        except ValueError:
            self.altura_viga_exterior_losa_m2d = 0
        self.parametro_a_ve_losa_m2d = (
            self.altura_viga_exterior_losa_m2d - self.altura_inicial_losa_m2d)
        self.parametro_bf_ve_losa_m2d = (
            4*self.altura_inicial_losa_m2d)
        if self.parametro_bf_ve_losa_m2d >= self.parametro_a_ve_losa_m2d:
            self.factor_b_h_ve_losa_m2d = (
                self.base_viga_exterior_losa_m2d/self.altura_inicial_losa_m2d)
            self.factor_hv_h_ve_losa_m2d = (
                self.altura_viga_exterior_losa_m2d / self.altura_inicial_losa_m2d)
        else:
            self.factor_b_h_ve_losa_m2d = 0
            self.factor_hv_h_ve_losa_m2d = 0
        self.label_factor_b_h_ve_losa_m2d.setText(str(
            self.factor_b_h_ve_losa_m2d))
        self.label_factor_hv_h_ve_losa_m2d.setText(str(
            self.factor_hv_h_ve_losa_m2d))

    def calcular_altura_final_losa_maciza_2d(self):
        try:
            self.base_viga_exterior_losa_m2d = float(
                self.line_edit_base_viga_exterior_losa_m2d.text())
        except ValueError:
            self.base_viga_exterior_losa_m2d = 0
        try:
            self.altura_viga_exterior_losa_m2d = float(
                self.line_edit_altura_viga_exterior_losa_m2d.text())
        except ValueError:
            self.altura_viga_exterior_losa_m2d = 0
        try:
            self.base_viga_interior_losa_m2d = float(
                self.line_edit_base_viga_interior_losa_m2d.text())
        except ValueError:
            self.base_viga_interior_losa_m2d = 0
        try:
            self.altura_viga_interior_losa_m2d = float(
                self.line_edit_altura_viga_interior_losa_m2d.text())
        except ValueError:
            self.altura_viga_interior_losa_m2d = 0
        try:
            self.base_viga_borde_losa_m2d = float(
                self.line_edit_base_viga_borde_losa_m2d.text())
        except ValueError:
            self.base_viga_borde_losa_m2d = 0
        try:
            self.altura_viga_borde_losa_m2d = float(
                self.line_edit_altura_viga_borde_losa_m2d.text())
        except ValueError:
            self.altura_viga_borde_losa_m2d = 0
        try:
            self.parametro_ka_losa_m2d = float(
                self.line_edit_parametro_ka_losa_m2d.text())
        except ValueError:
            self.parametro_ka_losa_m2d = 0
        try:
            self.parametro_kb_losa_m2d = float(
                self.line_edit_parametro_kb_losa_m2d.text())
        except ValueError:
            self.parametro_kb_losa_m2d = 0
        self.factor_b_h_vi_losa_m2d = self.label_factor_b_h_vi_losa_m2d.text()
        self.factor_hv_h_vi_losa_m2d = self.label_factor_hv_h_vi_losa_m2d.text()
        self.factor_b_h_ve_losa_m2d = self.label_factor_b_h_ve_losa_m2d.text()
        self.factor_hv_h_ve_losa_m2d = self.label_factor_hv_h_ve_losa_m2d.text()
        self.inercia_viga_interior = (self.base_viga_interior_losa_m2d+self.altura_viga_interior_losa_m2d**3)/12*self.parametro_ka_losa_m2d
        self.inercia_viga_exterior = (self.base_viga_exterior_losa_m2d+self.altura_viga_exterior_losa_m2d**3)/12*self.parametro_kb_losa_m2d
