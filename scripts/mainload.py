from PyQt5.QtGui import QPixmap

class CargarDatosVPrincipal():

    def cargar_datos_frame_inicio(self):
        self.text_edit_proyecto.setText(self.datos_memoria.proyecto)
        self.text_edit_descripcion.setText(
            self.datos_memoria.descripcion_proyecto)
        self.text_edit_herramientas.setText(
            self.datos_memoria.herramientas_proyecto)
        self.line_edit_responsable.setText(
            self.datos_memoria.responsable_proyecto)
        self.line_edit_equipo_trabajo.setText(
            self.datos_memoria.equipo_trabajo_proyecto)
        self.combo_box_norma.addItem(
            self.datos_memoria.norma_proyecto)
        qpixmap = QPixmap('img/logoSARO.png')
        self.label_logo_grande.setPixmap(qpixmap)
        self.label_logo_pequeno.setPixmap(qpixmap)

    def cargar_datos_frame_general(self):
        self.lista_municipios = self.datos_memoria.diccionario_colombia[
            self.datos_memoria.departamento_proyecto]
        self.lista_sistemas = (
            self.datos_memoria.diccionario_sistema_estructural.keys())
        self.lista_resistencia_horizontal = (
            self.datos_memoria.diccionario_sistema_estructural[
                self.datos_memoria.sistema_estructural].keys())
        self.lista_tipo_resistencia = (
            self.datos_memoria.diccionario_sistema_estructural[
                self.datos_memoria.sistema_estructural][
                    self.datos_memoria.resistencia_horizontal].keys())
        # SECCION IZQUIERDA - COMBO BOX
        self.combo_box_pais.addItem(
            self.datos_memoria.pais_proyecto)
        self.combo_box_departamento.addItems(self.lista_departamentos)
        self.combo_box_departamento.setCurrentText(
            self.datos_memoria.departamento_proyecto)
        self.combo_box_municipio.clear()
        self.combo_box_municipio.addItems(self.lista_municipios)
        self.combo_box_municipio.setCurrentText(
            self.datos_memoria.municipio_proyecto)
        self.combo_box_uso.clear()
        self.combo_box_uso.addItems(
            self.datos_memoria.lista_grupo_uso)
        self.combo_box_uso.setCurrentText(
            self.datos_memoria.grupo_uso)
        self.combo_box_sistema.clear()
        self.combo_box_sistema.addItems(self.lista_sistemas)
        self.combo_box_sistema.setCurrentText(
            self.datos_memoria.sistema_estructural)
        self.combo_box_resistencia_horizontal.clear()
        self.combo_box_resistencia_horizontal.addItems(
            self.lista_resistencia_horizontal)
        self.combo_box_resistencia_horizontal.setCurrentText(
            self.datos_memoria.resistencia_horizontal)
        self.combo_box_tipo_resistencia.clear()
        self.combo_box_tipo_resistencia.addItems(
            self.lista_tipo_resistencia)
        self.combo_box_tipo_resistencia.setCurrentText(
            self.datos_memoria.tipo_resistencia)
        # SECCION IZQUIERDA - LABEL
        self.label_codigo_municipio.setText(
            self.datos_memoria.codigo_municipio)
        self.label_aceleracion_pico_efectiva.setText(
            self.datos_memoria.aceleracion_pico_efectiva)
        self.label_velocidad_pico_efectiva.setText(
            self.datos_memoria.velocidad_pico_efectiva)
        self.label_aceleracion_pico_efectiva_reducida.setText(
            self.datos_memoria.aceleracion_pico_efectiva_reducida)
        self.label_aceleracion_sismo_diseno.setText(
            self.datos_memoria.aceleracion_sismo_diseno)
        self.label_amenaza_sismica.setText(
            self.datos_memoria.amenaza_sismica)
        self.label_disipacion_requerida.setText(
            self.datos_memoria.disipacion_requerida)
        self.label_coeficiente_importancia.setText(
            self.datos_memoria.coeficiente_importancia)
        # SECCION IZQUIERDA - LINE EDIT
        self.line_edit_numero_pisos.setText(
            self.datos_memoria.numero_pisos)
        self.line_edit_altura_maxima.setText(
            self.datos_memoria.altura_maxima)
        self.line_edit_altura_total.setText(
            self.datos_memoria.altura_total)
        # SECCION DERECHA - COMBO BOX
        self.combo_box_tipo_suelo.clear()
        self.combo_box_tipo_suelo.addItems(
            self.datos_memoria.lista_tipo_suelo)
        self.combo_box_tipo_suelo.setCurrentText(
            self.datos_memoria.tipo_suelo)
        self.combo_box_resistencia_concreto.clear()
        self.combo_box_resistencia_concreto.addItems(
            self.datos_memoria.lista_resistencia_concreto)
        try:
            self.combo_box_resistencia_concreto.setCurrentText(str(
                int(self.datos_memoria.resistencia_concreto_gen)))
        except ValueError:
            self.combo_box_resistencia_concreto.setCurrentText('')
        self.combo_box_masa_concreto.clear()
        self.combo_box_masa_concreto.addItems(
            self.datos_memoria.diccionario_modulo_elasticidad_concreto.keys())
        self.combo_box_masa_concreto.setCurrentText(self.datos_memoria.masa_concreto)
        if self.combo_box_masa_concreto.currentText() != 'Conoce masa del concreto':
            self.line_edit_peso_concreto.setEnabled(0)
        self.combo_box_origen_concreto.clear()
        self.combo_box_origen_concreto.addItems(
            self.datos_memoria.diccionario_modulo_elasticidad_concreto[
                self.datos_memoria.masa_concreto]['Origen'].keys())
        self.combo_box_origen_concreto.setCurrentText(self.datos_memoria.origen_concreto)
        # SECCION DERECHA - LABEL
        self.label_resistencia_vertical.setText(
            self.datos_memoria.resistencia_vertical)
        self.label_cumplimiento_sistema.setText(
            self.datos_memoria.cumplimiento_sistema)
        self.label_parametro_R.setText(
            self.datos_memoria.parametro_R)
        self.label_parametro_O.setText(
            self.datos_memoria.parametro_O)
        self.label_parametro_Fa.setText(
            self.datos_memoria.parametro_Fa)
        self.label_parametro_Fv.setText(
            self.datos_memoria.parametro_Fv)
        self.label_coeficiente_disipacion_energia.setText(
            self.datos_memoria.coeficiente_disipacion_energia)
        self.label_modulo_elasticidad_concreto.setText(
            self.datos_memoria.modulo_elasticidad_concreto)
        self.label_cumplimiento_fuerza_horizontal_equivalente.setText(
            self.datos_memoria.cumplimiento_fuerza_horizontal_equivalente)
        self.label_cumplimiento_dinamico_elastico.setText(
            self.datos_memoria.cumplimiento_dinamico_elastico)
        # SECCION DERECHA - LINE EDIT
        self.line_edit_irregularidad_planta.setText(
            self.datos_memoria.irregularidad_planta)
        self.line_edit_irregularidad_altura.setText(
            self.datos_memoria.irregularidad_altura)
        self.line_edit_ausencia_redundancia.setText(
            self.datos_memoria.ausencia_redundancia)
        self.line_edit_peso_concreto.setText(
            self.datos_memoria.peso_concreto)
        self.line_edit_modulo_poisson.setText(
            self.datos_memoria.modulo_poisson)
        self.line_edit_resistencia_acero.setText(
            self.datos_memoria.resistencia_acero)

    def cargar_datos_frame_predimension(self):
        # SECCION VIGA - LINE EDIT
        self.line_edit_longitud_simple_apoyo_viga.setText(
            self.datos_memoria.longitud_simple_apoyo_viga)
        self.line_edit_longitud_un_extremo_viga.setText(
            self.datos_memoria.longitud_un_extremo_viga)
        self.line_edit_longitud_ambos_extremos_viga.setText(
            self.datos_memoria.longitud_ambos_extremos_viga)
        self.line_edit_longitud_voladizo_viga.setText(
            self.datos_memoria.longitud_voladizo_viga)
        self.line_edit_recubrimiento_viga.setText(
            self.datos_memoria.recubrimiento_viga)
        self.line_edit_base_viga.setText(
            self.datos_memoria.base_viga)
        self.line_edit_altura_viga.setText(
            self.datos_memoria.altura_viga)
        # SECCION VIGA - LABEL
        self.label_segunda_nota.setText(
            self.datos_memoria.segunda_nota)
        self.label_tercera_nota.setText(
            self.datos_memoria.tercera_nota)
        self.label_viga_simple_apoyo_t1.setText(
            self.datos_memoria.altura_viga_simple_apoyo_t1)
        self.label_viga_simple_apoyo_t2.setText(
            self.datos_memoria.altura_viga_simple_apoyo_t2)
        self.label_viga_simple_apoyo_prom.setText(
            self.datos_memoria.altura_viga_simple_apoyo_prom)
        self.label_viga_un_extremo_t1.setText(
            self.datos_memoria.altura_viga_un_extremo_t1)
        self.label_viga_un_extremo_t2.setText(
            self.datos_memoria.altura_viga_un_extremo_t2)
        self.label_viga_un_extremo_prom.setText(
            self.datos_memoria.altura_viga_un_extremo_prom)
        self.label_viga_ambos_extremos_t1.setText(
            self.datos_memoria.altura_viga_ambos_extremos_t1)
        self.label_viga_ambos_extremos_t2.setText(
            self.datos_memoria.altura_viga_ambos_extremos_t2)
        self.label_viga_ambos_extremos_prom.setText(
            self.datos_memoria.altura_viga_ambos_extremos_prom)
        self.label_viga_voladizo_t1.setText(
            self.datos_memoria.altura_viga_voladizo_t1)
        self.label_viga_voladizo_t2.setText(
            self.datos_memoria.altura_viga_voladizo_t2)
        self.label_viga_voladizo_prom.setText(
            self.datos_memoria.altura_viga_voladizo_prom)
        # SECCION COLUMNA - LABEL
        self.label_norma_requisito_columna.setText(
            self.datos_memoria.norma_requisito_columna)
        self.label_dimension_min_columna.setText(
            self.datos_memoria.dimension_min_columna)
        self.label_area_min_columna.setText(
            self.datos_memoria.area_min_columna)
        self.label_dimensiones_cuadrado_columna.setText(
            self.datos_memoria.dimensiones_cuadrado_columna)
        self.label_refuerzo_longitudinal_requerido_columna.setText(
            self.datos_memoria.refuerzo_longitudinal_requerido_columna)
        # SECCION COLUMNA - LINE EDIT
        self.line_edit_recubrimiento_columna.setText(
            self.datos_memoria.recubrimiento_columna)
        self.line_edit_base_viga_sobre_columna.setText(
            self.datos_memoria.base_viga_sobre_columna)
        self.line_edit_altura_viga_sobre_columna.setText(
            self.datos_memoria.altura_viga_sobre_columna)
        self.line_edit_longitud_viga_sobre_columna.setText(
            self.datos_memoria.longitud_viga_sobre_columna)
        self.line_edit_area_aferente_columna.setText(
            self.datos_memoria.area_aferente_columna)
        self.line_edit_carga_muerta_columna.setText(
            self.datos_memoria.carga_muerta_columna)
        self.line_edit_carga_viva_columna.setText(
            self.datos_memoria.carga_viva_columna)
        self.line_edit_dimension_x_columna.setText(
            self.datos_memoria.dimension_x_columna)
        self.line_edit_dimension_y_columna.setText(
            self.datos_memoria.dimension_y_columna)
        # SECCION COLUMNA - COMBO BOX
        self.combo_box_ubicacion_columna.clear()
        self.combo_box_ubicacion_columna.addItems(
            self.datos_memoria.lista_ubicacion_columna)
        self.combo_box_ubicacion_columna.setCurrentText(
            self.datos_memoria.ubicacion_columna)
        # SECCION COLUMNA -  SPIN BOX
        self.spin_box_numero_pisos_columna.setValue(
            int(self.datos_memoria.numero_pisos_columna))
        # SECCION LOSA ALIGERADA EN UNA DIRECCION - COMBO BOX
        self.combo_box_uso_losa_aligerada_1d.clear()
        self.combo_box_uso_losa_aligerada_1d.addItems(
            self.datos_memoria.lista_uso_losa)
        self.combo_box_uso_losa_aligerada_1d.setCurrentText(
            self.datos_memoria.uso_losa_a1d)
        if self.combo_box_uso_losa_aligerada_1d.currentText() != 'Se usa':
            self.tab_widget_losa_A1D.setEnabled(0)
        self.combo_box_direccion_losa_a1d.clear()
        self.combo_box_direccion_losa_a1d.addItems(
            self.datos_memoria.lista_direcciones)
        self.combo_box_direccion_losa_a1d.setCurrentText(
            self.datos_memoria.direccion_losa_a1d)
        # SECCION LOSA ALIGERADA EN UNA DIRECCION - LINE EDIT
        self.line_edit_longitud_simple_apoyo_losa_a1d.setText(
            self.datos_memoria.longitud_simple_apoyo_losa_a1d)
        self.line_edit_longitud_un_extremo_losa_a1d.setText(
            self.datos_memoria.longitud_un_extremo_losa_a1d)
        self.line_edit_longitud_ambos_extremos_losa_a1d.setText(
            self.datos_memoria.longitud_ambos_extremos_losa_a1d)
        self.line_edit_altura_losa_a1d.setText(
            self.datos_memoria.altura_losa_a1d)
        self.line_edit_longitud_voladizo_losa_a1d.setText(
            self.datos_memoria.longitud_voladizo_losa_a1d)
        self.line_edit_base_nervio_losa_a1d.setText(
            self.datos_memoria.base_nervio_losa_a1d)
        self.line_edit_espesor_loseta_losa_a1d.setText(
            self.datos_memoria.espesor_loseta_losa_a1d)
        self.line_edit_separacion_nervadura_losa_a1d.setText(
            self.datos_memoria.separacion_nervadura_losa_a1d)
        # SECCION LOSA ALIGERADA EN UNA DIRECCION - LABEL
        self.label_losa_a1d_simple_apoyo_t1.setText(
            self.datos_memoria.losa_a1d_simple_apoyo_t1)
        self.label_losa_a1d_simple_apoyo_t2.setText(
            self.datos_memoria.losa_a1d_simple_apoyo_t2)
        self.label_losa_a1d_simple_apoyo_prom.setText(
            self.datos_memoria.losa_a1d_simple_apoyo_prom)
        self.label_losa_a1d_un_extremo_t1.setText(
            self.datos_memoria.losa_a1d_un_extremo_t1)
        self.label_losa_a1d_un_extremo_t2.setText(
            self.datos_memoria.losa_a1d_un_extremo_t2)
        self.label_losa_a1d_un_extremo_prom.setText(
            self.datos_memoria.losa_a1d_un_extremo_prom)
        self.label_losa_a1d_ambos_extremos_t1.setText(
            self.datos_memoria.losa_a1d_ambos_extremos_t1)
        self.label_losa_a1d_ambos_extremos_t2.setText(
            self.datos_memoria.losa_a1d_ambos_extremos_t2)
        self.label_losa_a1d_ambos_extremos_prom.setText(
            self.datos_memoria.losa_a1d_ambos_extremos_prom)
        self.label_losa_a1d_voladizo_t1.setText(
            self.datos_memoria.losa_a1d_voladizo_t1)
        self.label_losa_a1d_voladizo_t2.setText(
            self.datos_memoria.losa_a1d_voladizo_t2)
        self.label_losa_a1d_voladizo_prom.setText(
            self.datos_memoria.losa_a1d_voladizo_prom)
        self.label_espesor_minimo_loseta_losa_a1d.setText(
            self.datos_memoria.espesor_minimo_loseta_losa_a1d)
        self.label_base_minima_nervadura_losa_a1d.setText(
            self.datos_memoria.base_minima_nervadura_losa_a1d)
        self.label_altura_libre_maxima_nervio_losa_a1d.setText(
            self.datos_memoria.altura_libre_maxima_nervio_losa_a1d)
        self.label_separacion_maxima_nervadura_losa_a1d.setText(
            self.datos_memoria.separacion_maxima_nervadura_losa_a1d)
        self.label_espaseamiento_riostra_losa_a1d.setText(
            self.datos_memoria.espaseamiento_riostra_losa_a1d)
        # SECCION LOSA MACIZA EN UNA DIRECCION - COMBO BOX
        self.combo_box_uso_losa_maciza_1d.clear()
        self.combo_box_uso_losa_maciza_1d.addItems(
            self.datos_memoria.lista_uso_losa)
        self.combo_box_uso_losa_maciza_1d.setCurrentText(
            self.datos_memoria.uso_losa_m1d)
        if self.combo_box_uso_losa_maciza_1d.currentText() != 'Se usa':
            self.group_box_losa_M1D.setEnabled(0)
        # SECCION LOSA MACIZA EN UNA DIRECCION - LINE EDIT
        self.line_edit_longitud_simple_apoyo_losa_m1d.setText(
            self.datos_memoria.longitud_simple_apoyo_losa_m1d)
        self.line_edit_longitud_un_extremo_losa_m1d.setText(
            self.datos_memoria.longitud_un_extremo_losa_m1d)
        self.line_edit_longitud_ambos_extremos_losa_m1d.setText(
            self.datos_memoria.longitud_ambos_extremos_losa_m1d)
        self.line_edit_longitud_voladizo_losa_m1d.setText(
            self.datos_memoria.longitud_voladizo_losa_m1d)
        self.line_edit_altura_losa_m1d.setText(
            self.datos_memoria.altura_losa_m1d)
        # SECCION LOSA MACIZA EN UNA DIRECCION - LABEL
        self.label_losa_m1d_simple_apoyo_t1.setText(
            self.datos_memoria.losa_m1d_simple_apoyo_t1)
        self.label_losa_m1d_simple_apoyo_t2.setText(
            self.datos_memoria.losa_m1d_simple_apoyo_t2)
        self.label_losa_m1d_simple_apoyo_prom.setText(
            self.datos_memoria.losa_m1d_simple_apoyo_prom)
        self.label_losa_m1d_un_extremo_t1.setText(
            self.datos_memoria.losa_m1d_un_extremo_t1)
        self.label_losa_m1d_un_extremo_t2.setText(
            self.datos_memoria.losa_m1d_un_extremo_t2)
        self.label_losa_m1d_un_extremo_prom.setText(
            self.datos_memoria.losa_m1d_un_extremo_prom)
        self.label_losa_m1d_ambos_extremos_t1.setText(
            self.datos_memoria.losa_m1d_ambos_extremos_t1)
        self.label_losa_m1d_ambos_extremos_t2.setText(
            self.datos_memoria.losa_m1d_ambos_extremos_t2)
        self.label_losa_m1d_ambos_extremos_prom.setText(
            self.datos_memoria.losa_m1d_ambos_extremos_prom)
        self.label_losa_m1d_voladizo_t1.setText(
            self.datos_memoria.losa_m1d_voladizo_t1)
        self.label_losa_m1d_voladizo_t2.setText(
            self.datos_memoria.losa_m1d_voladizo_t2)
        self.label_losa_m1d_voladizo_prom.setText(
            self.datos_memoria.losa_m1d_voladizo_prom)
        # SECCION LOSA ALIGERADA EN DOS DIRECCIONES - COMBO BOX
        self.combo_box_uso_losa_aligerada_2d.clear()
        self.combo_box_uso_losa_aligerada_2d.addItems(
            self.datos_memoria.lista_uso_losa)
        if self.combo_box_uso_losa_aligerada_2d.currentText() != 'Se usa':
            self.tab_widget_losa_A2D.setEnabled(0)
        # SECCION LOSA MACIZA EN DOS DIRECCIONES - COMBO BOX
        self.combo_box_uso_losa_maciza_2d.clear()
        self.combo_box_uso_losa_maciza_2d.addItems(
            self.datos_memoria.lista_uso_losa)
        self.combo_box_uso_losa_maciza_2d.setCurrentText(
            self.datos_memoria.uso_losa_m2d)
        if self.combo_box_uso_losa_maciza_2d.currentText() != 'Se usa':
            self.group_box_losa_M2D.setEnabled(0)

    def cargar_datos_frame_sismo(self):
        # SECCION SOBRECARGA ENTREPISO - LINE EDIT
        self.line_edit_sobrecarga_particiones.setText(str(
            self.datos_memoria.sobrecarga_particiones))
        self.line_edit_sobrecarga_acabados.setText(str(
            self.datos_memoria.sobrecarga_acabados))
        self.line_edit_sobrecarga_cielo_raso.setText(str(
            self.datos_memoria.sobrecarga_cielo_raso))
        self.line_edit_sobrecarga_mortero_nivelacion.setText(str(
            self.datos_memoria.sobrecarga_mortero_nivelacion))
        self.line_edit_sobrecarga_instalaciones.setText(str(
            self.datos_memoria.sobrecarga_instalaciones))
        self.line_edit_sobrecarga_otros.setText(str(
            self.datos_memoria.sobrecarga_otros))
        self.label_sobrecarga_total_entrepiso.setText(str(
            self.datos_memoria.sobrecarga_total_entrepiso))
        # SECCION SOBRECARA ESCALERA - LINE EDIT
        self.line_edit_huella_escalera.setText(str(
            self.datos_memoria.huella_escalera))
        self.line_edit_contrahuella_escalera.setText(str(
            self.datos_memoria.contrahuella_escalera))
        # SECCION SOBRECARGA ESCALERA - LABEL
        self.label_sobrecarga_total_escalera.setText(str(
            self.datos_memoria.sobrecarga_total_escalera))
        # SECCION CARGAS VIVAS - LINE EDIT
        self.line_edit_carga_viva_uso.setText(str(
            self.datos_memoria.carga_viva_uso))
        self.line_edit_carga_viva_balcones.setText(str(
            self.datos_memoria.carga_viva_balcones))
        self.line_edit_carga_viva_escalera.setText(str(
            self.datos_memoria.carga_viva_escalera))
        # SECCION JUSTIFICACION MORTERO - LINE EDIT
        self.line_edit_espesor_mortero.setText(str(
            self.datos_memoria.espesor_mortero))
        # SECCION JUSTIFICAICON MORTERO - LABEL
        self.label_sobrecarga_mortero.setText(str(
            self.datos_memoria.sobrecarga_mortero))
        # SECCION JUSTIFICACION PARTICIONES - LINE EDIT
        self.line_edit_longitud_muro.setText(str(
            self.datos_memoria.longitud_muro))
        self.line_edit_altura_muro.setText(str(
            self.datos_memoria.altura_muro))
        self.line_edit_espesor_muro.setText(str(
            self.datos_memoria.espesor_muro))
        self.line_edit_area_total_losa.setText(str(
            self.datos_memoria.area_total_losa))
        # SECCION JUSTIFICACION PARTICIONES - LABEL
        self.label_volumen_muro.setText(str(
            self.datos_memoria.volumen_muro))
        self.label_peso_muro.setText(str(
            self.datos_memoria.peso_muro))
        self.label_sobrecarga_particiones_calculada.setText(str(
            self.datos_memoria.sobrecarga_particiones_calculada))
        # SECCION FUERZA HORIZONTAL EQUIVALENTE - COMBO BOX
        self.combo_box_direccion_sismo.clear()
        self.combo_box_direccion_sismo.addItems(
            self.datos_memoria.lista_direcciones)
        self.combo_box_direccion_sismo.setCurrentText(
            self.datos_memoria.direccion_sismo)
        # SECCION FUERZA HORIZONTAL EQUIVALENTE - LINE EDIT
        self.line_edit_parametro_Ct.setText(str(
            self.datos_memoria.parametro_Ct))
        self.line_edit_parametro_a.setText(str(
            self.datos_memoria.parametro_a))
        self.line_edit_periodo_elemento_finito.setText(str(
            self.datos_memoria.periodo_elemento_finito))
        self.line_edit_periodo_elegido.setText(str(
            self.datos_memoria.periodo_fundamental))
        # SECCION FUERZA HORIZONTAL EQUIVALENTE - LABEL
        self.label_parametro_Cu.setText(str(
            self.datos_memoria.coeficiente_calculo_periodo_maximo))
        self.label_periodo_aproximado.setText(str(
            self.datos_memoria.periodo_aproximado))
        self.label_periodo_maximo.setText(str(
            self.datos_memoria.periodo_maximo))
        self.label_periodo_inicial.setText(str(
            self.datos_memoria.periodo_inicial))
        self.label_periodo_corto.setText(str(
            self.datos_memoria.periodo_corto))
        self.label_periodo_largo.setText(str(
            self.datos_memoria.periodo_largo))
        self.label_periodo_fema.setText(str(
            self.datos_memoria.periodo_fema))
        self.label_condicion_espectro.setText(
            self.datos_memoria.condicion_espectro)
        self.label_espectro_aceleracion.setText(str(
            self.datos_memoria.espectro_aceleracion))

    def cargar_datos_frame_diseno_viga(self):
        # SECCION DATOS VIGA - LINE EDIT
        self.line_edit_base_viga_d.setText(str(
            self.datos_memoria.base_viga_d))
        self.line_edit_altura_viga_d.setText(str(
            self.datos_memoria.altura_viga_d))
        self.line_edit_recubrimiento_inferior_viga.setText(str(
            self.datos_memoria.recubrimiento_inferior_viga))
        self.line_edit_recubrimiento_superior_viga.setText(str(
            self.datos_memoria.recubrimiento_superior_viga))
        self.line_edit_longitud_libre_viga.setText(str(
            self.datos_memoria.longitud_libre_viga))
        # SECCION MOMENTOS VIGA - LINE EDIT
        self.line_edit_momento_negativo_izquierdo_viga.setText(str(
            self.datos_memoria.momento_negativo_izquierdo_viga))
        self.line_edit_momento_positivo_izquierdo_viga.setText(str(
            self.datos_memoria.momento_positivo_izquierdo_viga))
        self.line_edit_momento_negativo_centro_viga.setText(str(
            self.datos_memoria.momento_negativo_centro_viga))
        self.line_edit_momento_positivo_centro_viga.setText(str(
            self.datos_memoria.momento_positivo_centro_viga))
        self.line_edit_momento_negativo_derecho_viga.setText(str(
            self.datos_memoria.momento_negativo_derecho_viga))
        self.line_edit_momento_positivo_derecho_viga.setText(str(
            self.datos_memoria.momento_positivo_derecho_viga))
        # SECCION ACERO REQUERIDO - LABEL
        self.label_acero_minimo.setText(str(
            self.datos_memoria.acero_minimo))
        self.label_acero_requerido_1.setText(str(
            self.datos_memoria.acero_requerido_1))
        self.label_acero_requerido_2.setText(str(
            self.datos_memoria.acero_requerido_2))
        self.label_acero_requerido_3.setText(str(
            self.datos_memoria.acero_requerido_3))
        self.label_acero_requerido_4.setText(str(
            self.datos_memoria.acero_requerido_4))
        self.label_acero_requerido_5.setText(str(
            self.datos_memoria.acero_requerido_5))
        self.label_acero_requerido_6.setText(str(
            self.datos_memoria.acero_requerido_6))
        # SECCION ACERO DUCTIL - LABEL
        self.label_acero_superior_izquierdo_ductil.setText(str(
            self.datos_memoria.acero_superior_izquierdo_ductil))
        self.label_acero_superior_derecho_ductil.setText(str(
            self.datos_memoria.acero_superior_derecho_ductil))
        self.label_acero_inferior_izquierdo_ductil.setText(str(
            self.datos_memoria.acero_inferior_izquierdo_ductil))
        self.label_acero_inferior_derecho_ductil.setText(str(
            self.datos_memoria.acero_inferior_derecho_ductil))
        self.label_acero_inferior_centro_ductil.setText(str(
            self.datos_memoria.acero_inferior_centro_ductil))
        self.label_acero_superior_centro_ductil.setText(str(
            self.datos_memoria.acero_superior_centro_ductil))
        self.label_acero_superior_izquierdo_impuesto.setText(str(
            self.datos_memoria.acero_superior_izquierdo_impuesto))
        self.label_acero_inferior_izquierdo_impuesto.setText(str(
            self.datos_memoria.acero_inferior_izquierdo_impuesto))
        self.label_acero_superior_derecho_impuesto.setText(str(
            self.datos_memoria.acero_superior_derecho_impuesto))
        self.label_acero_inferior_derecho_impuesto.setText(str(
            self.datos_memoria.acero_inferior_derecho_impuesto))
        self.label_acero_superior_centro_impuesto.setText(str(
            self.datos_memoria.acero_superior_centro_impuesto))
        self.label_acero_inferior_centro_impuesto.setText(str(
            self.datos_memoria.acero_inferior_centro_impuesto))
        self.label_acero_superior_izquierdo_impuesto_2.setText(str(
            self.datos_memoria.acero_superior_izquierdo_impuesto))
        self.label_acero_inferior_izquierdo_impuesto_2.setText(str(
            self.datos_memoria.acero_inferior_izquierdo_impuesto))
        self.label_acero_superior_derecho_impuesto_2.setText(str(
            self.datos_memoria.acero_superior_derecho_impuesto))
        self.label_acero_inferior_derecho_impuesto_2.setText(str(
            self.datos_memoria.acero_inferior_derecho_impuesto))
        self.label_acero_superior_centro_impuesto_2.setText(str(
            self.datos_memoria.acero_superior_centro_impuesto))
        self.label_acero_inferior_centro_impuesto_2.setText(str(
            self.datos_memoria.acero_inferior_centro_impuesto))
        # SECCION ACERO DUCTIL - COMBO BOX
        self.combo_box_cantidad1_acero_superior_izquierdo.clear()
        self.combo_box_cantidad1_acero_superior_izquierdo.addItems(
            self.datos_memoria.lista_cantidad)
        self.combo_box_codigo1_acero_superior_izquierdo.clear()
        self.combo_box_codigo1_acero_superior_izquierdo.addItems(
            self.datos_memoria.lista_barras_longitudinales)
        self.combo_box_cantidad2_acero_superior_izquierdo.clear()
        self.combo_box_cantidad2_acero_superior_izquierdo.addItems(
            self.datos_memoria.lista_cantidad)
        self.combo_box_codigo2_acero_superior_izquierdo.clear()
        self.combo_box_codigo2_acero_superior_izquierdo.addItems(
            self.datos_memoria.lista_barras_longitudinales)
        self.combo_box_cantidad1_acero_superior_derecho.clear()
        self.combo_box_cantidad1_acero_superior_derecho.addItems(
            self.datos_memoria.lista_cantidad)
        self.combo_box_codigo1_acero_superior_derecho.clear()
        self.combo_box_codigo1_acero_superior_derecho.addItems(
            self.datos_memoria.lista_barras_longitudinales)
        self.combo_box_cantidad2_acero_superior_derecho.clear()
        self.combo_box_cantidad2_acero_superior_derecho.addItems(
            self.datos_memoria.lista_cantidad)
        self.combo_box_codigo2_acero_superior_derecho.clear()
        self.combo_box_codigo2_acero_superior_derecho.addItems(
            self.datos_memoria.lista_barras_longitudinales)
        self.combo_box_cantidad1_acero_inferior_derecho.clear()
        self.combo_box_cantidad1_acero_inferior_derecho.addItems(
            self.datos_memoria.lista_cantidad)
        self.combo_box_codigo1_acero_inferior_derecho.clear()
        self.combo_box_codigo1_acero_inferior_derecho.addItems(
            self.datos_memoria.lista_barras_longitudinales)
        self.combo_box_cantidad2_acero_inferior_derecho.clear()
        self.combo_box_cantidad2_acero_inferior_derecho.addItems(
            self.datos_memoria.lista_cantidad)
        self.combo_box_codigo2_acero_inferior_derecho.clear()
        self.combo_box_codigo2_acero_inferior_derecho.addItems(
            self.datos_memoria.lista_barras_longitudinales)
        self.combo_box_cantidad1_acero_inferior_izquierdo.clear()
        self.combo_box_cantidad1_acero_inferior_izquierdo.addItems(
            self.datos_memoria.lista_cantidad)
        self.combo_box_codigo1_acero_inferior_izquierdo.clear()
        self.combo_box_codigo1_acero_inferior_izquierdo.addItems(
            self.datos_memoria.lista_barras_longitudinales)
        self.combo_box_cantidad2_acero_inferior_izquierdo.clear()
        self.combo_box_cantidad2_acero_inferior_izquierdo.addItems(
            self.datos_memoria.lista_cantidad)
        self.combo_box_codigo2_acero_inferior_izquierdo.clear()
        self.combo_box_codigo2_acero_inferior_izquierdo.addItems(
            self.datos_memoria.lista_barras_longitudinales)
        self.combo_box_cantidad1_acero_inferior_centro.clear()
        self.combo_box_cantidad1_acero_inferior_centro.addItems(
            self.datos_memoria.lista_cantidad)
        self.combo_box_codigo1_acero_inferior_centro.clear()
        self.combo_box_codigo1_acero_inferior_centro.addItems(
            self.datos_memoria.lista_barras_longitudinales)
        self.combo_box_cantidad2_acero_inferior_centro.clear()
        self.combo_box_cantidad2_acero_inferior_centro.addItems(
            self.datos_memoria.lista_cantidad)
        self.combo_box_codigo2_acero_inferior_centro.clear()
        self.combo_box_codigo2_acero_inferior_centro.addItems(
            self.datos_memoria.lista_barras_longitudinales)
        self.combo_box_cantidad1_acero_superior_centro.clear()
        self.combo_box_cantidad1_acero_superior_centro.addItems(
            self.datos_memoria.lista_cantidad)
        self.combo_box_codigo1_acero_superior_centro.clear()
        self.combo_box_codigo1_acero_superior_centro.addItems(
            self.datos_memoria.lista_barras_longitudinales)
        self.combo_box_cantidad2_acero_superior_centro.clear()
        self.combo_box_cantidad2_acero_superior_centro.addItems(
            self.datos_memoria.lista_cantidad)
        self.combo_box_codigo2_acero_superior_centro.clear()
        self.combo_box_codigo2_acero_superior_centro.addItems(
            self.datos_memoria.lista_barras_longitudinales)
        # SECCION DEMANDA CORTE - LABEL
        self.label_peso_propio_viga.setText(str(
            self.datos_memoria.peso_propio_viga))
        self.label_corte_izquierdo.setText(str(
            self.datos_memoria.corte_izquierdo))
        self.label_corte_derecho.setText(str(
            self.datos_memoria.corte_derecho))
        self.label_corte_capacidad.setText(str(
            self.datos_memoria.corte_capacidad))
        # SECCION DEMANDA CORTE - LINE EDIT
        self.line_edit_sobrecarga_permanente_viga.setText(str(
            self.datos_memoria.sobrecarga_permanente_viga))
        self.line_edit_sobrecarga_variable_viga.setText(str(
            self.datos_memoria.sobrecarga_variable_viga))
        self.line_edit_corte_ultimo_viga.setText(str(
            self.datos_memoria.corte_ultimo_viga))
        # SECCION DISEÑO ESTRIBOS - COMBO BOX
        self.combo_box_n_ramas.clear()
        self.combo_box_n_ramas.addItems(
            self.datos_memoria.lista_cantidad_ramales)
        self.combo_box_diametro_estribo.clear()
        self.combo_box_diametro_estribo.addItems(
            self.datos_memoria.lista_barras_transversales)
        # SECCION DISEÑO ESTRIBOS - LABEL
        self.label_area_transversal_refuerzo.setText(str(
            self.datos_memoria.area_transversal_refuerzo))
        self.label_area_transversal_refuerzo_2.setText(str(
            self.datos_memoria.area_transversal_refuerzo))
        self.label_corte_diseno.setText(str(
            self.datos_memoria.corte_diseno))
        self.label_corte_concreto.setText(str(
            self.datos_memoria.cortante))
        self.label_corte_acero.setText(str(
            self.datos_memoria.demanda_corte))
        self.label_separacion_estribo.setText(str(
            self.datos_memoria.separacion_maxima_calculada_estribos))
        self.label_separacion_maxima_norma.setText(str(
            self.datos_memoria.separacion_maxima_norma))
        self.label_longitud_confinamiento.setText(str(
            self.datos_memoria.longitud_confinamiento))
        self.label_separacion_maxima_inconfinada.setText(str(
            self.datos_memoria.separacion_maxima_inconfinada))
        self.label_separacion_maxima_inconfinada_solapada.setText(str(
            self.datos_memoria.separacion_maxima_inconfinada_solapada))
        self.label_separacion_definitiva.setText(str(
            self.datos_memoria.separacion_definitiva))
        self.label_separacion_inconfinada.setText(str(
            self.datos_memoria.separacion_inconfinada))
        self.label_separacion_inconfinada_solapada.setText(str(
            self.datos_memoria.separacion_inconfinada_solapada))
        # SECCION DISEÑO ESTRIBOS - LINE EDIT
        self.line_edit_separacion_definitiva.setText(str(
            self.datos_memoria.separacion_definitiva))
        self.line_edit_separacion_inconfinada.setText(str(
            self.datos_memoria.separacion_inconfinada))
        self.line_edit_separacion_inconfinada_solapada.setText(str(
            self.datos_memoria.separacion_inconfinada_solapada))
        
