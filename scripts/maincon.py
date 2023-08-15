
class ConexionesVPrincipal():

    def conectar_clicks_ventana_principal(self):
        self.boton_frame_principal.clicked.connect(
            lambda: self.cambiar_stacks(1))
        self.boton_frame_general.clicked.connect(
            lambda: self.cambiar_stacks(2))
        self.boton_frame_dimension.clicked.connect(
            lambda: self.cambiar_stacks(3))
        self.boton_frame_sismo.clicked.connect(
            lambda: self.cambiar_stacks(4))
        self.boton_frame_diseno_viga.clicked.connect(
            lambda: self.cambiar_stacks(0))
        self.boton_pdf_viga.clicked.connect(
            lambda: self.generar_pdf_viga())

    def conectar_acciones_ventana_principal(self):
        self.action_materiales.triggered.connect(
            lambda: self.abrir_ventana_materiales())
        self.action_barras_acero.triggered.connect(
            lambda: self.abrir_ventana_barras())

    def conectar_cambios_texto_frame_inicio(self):
        self.text_edit_proyecto.textChanged.connect(
            lambda: self.guardar_cambio(
                'Proyecto', 'GENERAL', 'DESCRIPCION',
                self.text_edit_proyecto.toPlainText()))
        self.text_edit_descripcion.textChanged.connect(
            lambda: self.guardar_cambio(
                'DescripcionProyecto', 'GENERAL', 'DESCRIPCION',
                self.text_edit_descripcion.toPlainText()))
        self.text_edit_herramientas.textChanged.connect(
            lambda: self.guardar_cambio(
                'Herramienta', 'GENERAL', 'DESCRIPCION',
                self.text_edit_herramientas.toPlainText()))
        self.line_edit_responsable.textChanged.connect(
            lambda: self.guardar_cambio(
                'Responsable', 'GENERAL', 'DESCRIPCION',
                self.line_edit_responsable.text()))
        self.line_edit_equipo_trabajo.textChanged.connect(
            lambda: self.guardar_cambio(
                'Equipo', 'GENERAL', 'DESCRIPCION',
                self.line_edit_equipo_trabajo.text()))

    def conectar_cambios_texto_frame_general(self):
        # SECCION IZQUIERDA - COMBO BOX
        self.combo_box_departamento.currentIndexChanged.connect(
            lambda: self.funcion_combo_box_departamento())
        self.combo_box_municipio.currentIndexChanged.connect(
            lambda: self.funcion_combo_box_municipio())
        self.combo_box_uso.currentIndexChanged.connect(
            lambda: self.funcion_combo_box_uso())
        self.combo_box_sistema.currentIndexChanged.connect(
            lambda: self.funcion_combo_box_sistema())
        self.combo_box_resistencia_horizontal.currentIndexChanged.connect(
            lambda: self.funcion_combo_box_resistencia_horizontal())
        self.combo_box_tipo_resistencia.currentIndexChanged.connect(
            lambda: self.funcion_combo_box_tipo_resistencia())
        self.combo_box_tipo_suelo.currentIndexChanged.connect(
            lambda: self.funcion_combo_box_tipo_suelo())
        # SECCION IZQUIERDA - LINE EDIT
        self.line_edit_numero_pisos.textChanged.connect(
            lambda: self.guardar_cambio(
                'NumeroPisos', 'GENERAL', 'DESCRIPCION',
                self.line_edit_numero_pisos.text()))
        self.line_edit_altura_maxima.textChanged.connect(
            lambda: self.guardar_cambio(
                'AlturaMaxima', 'GENERAL', 'DESCRIPCION',
                self.line_edit_altura_maxima.text()))
        self.line_edit_altura_total.textChanged.connect(
            lambda: self.guardar_cambio(
                'AlturaTotal', 'GENERAL', 'DESCRIPCION',
                self.line_edit_altura_total.text()))
        # SECCION DERECHA - COMBO BOX
        self.combo_box_resistencia_concreto.currentIndexChanged.connect(
            lambda: self.funcion_combo_box_resistencia_concreto())
        self.combo_box_masa_concreto.currentIndexChanged.connect(
            lambda: self.funcion_combo_box_masa_concreto())
        self.combo_box_origen_concreto.currentIndexChanged.connect(
            lambda: self.funcion_combo_box_origen_concreto())
        # SECCION DERECHA - LINE EDIT
        self.line_edit_irregularidad_planta.textChanged.connect(
            lambda: self.calcular_disipacion_energia())
        self.line_edit_irregularidad_altura.textChanged.connect(
            lambda: self.calcular_disipacion_energia())
        self.line_edit_ausencia_redundancia.textChanged.connect(
            lambda: self.calcular_disipacion_energia())
        self.line_edit_peso_concreto.textChanged.connect(
            lambda: self.guardar_cambio(
                'Wc', 'GENERAL', 'DESCRIPCION',
                self.line_edit_peso_concreto.text()))
        self.line_edit_modulo_poisson.textChanged.connect(
            lambda: self.guardar_cambio(
                'u', 'GENERAL', 'DESCRIPCION',
                self.line_edit_modulo_poisson.text()))
        self.line_edit_resistencia_acero.textChanged.connect(
            lambda: self.guardar_cambio(
                'fy', 'GENERAL', 'DESCRIPCION',
                self.line_edit_resistencia_acero.text()))

    def conectar_clicks_frame_dimension(self):
        self.push_button_losa_1d.clicked.connect(
            lambda: self.cambiar_stacks_losa(0))
        '''self.push_button_losa_2d.clicked.connect(
            lambda: self.cambiar_stacks_losa(1))'''

    def conectar_cambios_texto_frame_dimension(self):
        # SECCION VIGA - LINE EDIT
        self.line_edit_longitud_simple_apoyo_viga.textChanged.connect(
            lambda: self.funcion_line_edit_longitud_simple_apoyo_viga())
        self.line_edit_longitud_un_extremo_viga.textChanged.connect(
            lambda: self.funcion_line_edit_longitud_un_extremo_viga())
        self.line_edit_longitud_ambos_extremos_viga.textChanged.connect(
            lambda: self.funcion_line_edit_longitud_ambos_extremos_viga())
        self.line_edit_longitud_voladizo_viga.textChanged.connect(
            lambda: self.funcion_line_edit_longitud_voladizo_viga())
        self.line_edit_recubrimiento_viga.textChanged.connect(
            lambda: self.guardar_cambio(
                'r_viga', 'PREDIMENSION', 'DESCRIPCION',
                self.line_edit_recubrimiento_viga.text()))
        self.line_edit_base_viga.textChanged.connect(
            lambda: self.funcion_dimensiones_viga())
        self.line_edit_altura_viga.textChanged.connect(
            lambda: self.funcion_dimensiones_viga())
        # SECCION COLUMNA - SPIN BOX
        self.spin_box_numero_pisos_columna.valueChanged.connect(
            lambda: self.calcular_predimensiones_columna())
        # SECCION COLUMNA - COMBO BOX
        self.combo_box_ubicacion_columna.currentIndexChanged.connect(
            lambda: self.calcular_predimensiones_columna())
        # SECCION COLUMNA - LINE EDIT
        self.line_edit_recubrimiento_columna.textChanged.connect(
            lambda: self.guardar_cambio(
                'r_columna', 'PREDIMENSION', 'DESCRIPCION',
                self.line_edit_recubrimiento_columna.text()))
        self.line_edit_base_viga_sobre_columna.textChanged.connect(
            lambda: self.calcular_predimensiones_columna())
        self.line_edit_altura_viga_sobre_columna.textChanged.connect(
            lambda: self.calcular_predimensiones_columna())
        self.line_edit_longitud_viga_sobre_columna.textChanged.connect(
            lambda: self.calcular_predimensiones_columna())
        self.line_edit_area_aferente_columna.textChanged.connect(
            lambda: self.calcular_predimensiones_columna())
        self.line_edit_carga_muerta_columna.textChanged.connect(
            lambda: self.calcular_predimensiones_columna())
        self.line_edit_carga_viva_columna.textChanged.connect(
            lambda: self.calcular_predimensiones_columna())
        self.line_edit_dimension_x_columna.textChanged.connect(
            lambda: self.calcular_refuerzo_longitudinal_requerido_columna())
        self.line_edit_dimension_y_columna.textChanged.connect(
            lambda: self.calcular_refuerzo_longitudinal_requerido_columna())
        # SECCION LOSA ALIGERADA EN UNA DIRECCION - COMBO BOX
        self.combo_box_uso_losa_aligerada_1d.currentIndexChanged.connect(
            lambda: self.determinar_uso_losa_a1d())
        self.combo_box_direccion_losa_a1d.currentIndexChanged.connect(
            lambda: self.funcion_combo_box_direccion_losa_a1d())
        # SECCION LOSA ALIGERADA EN UNA DIRECCION - LINE EDIT
        self.line_edit_longitud_simple_apoyo_losa_a1d.textChanged.connect(
            lambda: self.funcion_line_edit_longitud_simple_apoyo_losa_a1d())
        self.line_edit_longitud_un_extremo_losa_a1d.textChanged.connect(
            lambda: self.funcion_line_edit_longitud_un_extremo_losa_a1d())
        self.line_edit_longitud_ambos_extremos_losa_a1d.textChanged.connect(
            lambda: self.funcion_line_edit_longitud_ambos_extremos_losa_a1d())
        self.line_edit_longitud_voladizo_losa_a1d.textChanged.connect(
            lambda: self.funcion_line_edit_longitud_voladizo_losa_a1d())
        self.line_edit_altura_losa_a1d.textChanged.connect(
            lambda: self.funcion_line_edit_altura_losa_a1d())
        self.line_edit_base_nervio_losa_a1d.textChanged.connect(
            lambda: self.funcion_line_edit_base_nervio_losa_a1d())
        self.line_edit_espesor_loseta_losa_a1d.textChanged.connect(
            lambda: self.guardar_cambio(
                'e_loseta_losa_a1d', 'LOSAS', 'DESCRIPCION',
                self.line_edit_espesor_loseta_losa_a1d.text()))
        self.line_edit_separacion_nervadura_losa_a1d.textChanged.connect(
            lambda: self.guardar_cambio(
                'Sn_nervadura_losa_a1d', 'LOSAS', 'DESCRIPCION',
                self.line_edit_separacion_nervadura_losa_a1d.text()))
        # SECCION LOSA MACIZA EN UNA DIRECCION - COMBO BOX
        self.combo_box_uso_losa_maciza_1d.currentIndexChanged.connect(
            lambda: self.determinar_uso_losa_m1d())
        # SECCION LOSA MACIZA EN UNA DIRECCION - LINE EDIT
        self.line_edit_longitud_simple_apoyo_losa_m1d.textChanged.connect(
            lambda: self.funcion_line_edit_longitud_simple_apoyo_losa_m1d())
        self.line_edit_longitud_un_extremo_losa_m1d.textChanged.connect(
            lambda: self.funcion_line_edit_longitud_un_extremo_losa_m1d())
        self.line_edit_longitud_ambos_extremos_losa_m1d.textChanged.connect(
            lambda: self.funcion_line_edit_longitud_ambos_extremos_losa_m1d())
        self.line_edit_longitud_voladizo_losa_m1d.textChanged.connect(
            lambda: self.funcion_line_edit_longitud_voladizo_losa_m1d())
        self.line_edit_altura_losa_m1d.textChanged.connect(
            lambda: self.guardar_cambio(
                'h_losa_m1d', 'LOSAS', 'DESCRIPCION',
                self.line_edit_altura_losa_m1d.text()))
        # SECCION LOSA ALIGERADA EN DOS DIRECCIONES - COMBO BOX
        self.combo_box_uso_losa_aligerada_2d.currentIndexChanged.connect(
            lambda: self.determinar_uso_losa_a2d())
        # SECCION LOSA MACIZA EN DOS DIRECCIONES - COMBO BOX
        self.combo_box_uso_losa_maciza_2d.currentIndexChanged.connect(
            lambda: self.determinar_uso_losa_m2d())
        # SECCION LOSA MACIZA EN DOS DIRECCIONES - LINE EDIT
        self.line_edit_longitud_libre_maxima_losa_m2d.textChanged.connect(
            lambda: self.funcion_line_edit_longitud_libre_maxima_losa_m2d())
        self.line_edit_altura_inicial_losa_m2d.textChanged.connect(
            lambda: self.guardar_cambio(
                'h_inicial_LM2D', 'LOSAS', 'DESCRIPCION',
                self.line_edit_altura_inicial_losa_m2d.text()))
        self.line_edit_base_viga_interior_losa_m2d.textChanged.connect(
            lambda: self.calcular_factores_viga_interior_losa_m2d())
        self.line_edit_altura_viga_interior_losa_m2d.textChanged.connect(
            lambda: self.calcular_factores_viga_interior_losa_m2d())
        self.line_edit_base_viga_exterior_losa_m2d.textChanged.connect(
            lambda: self.calcular_factores_viga_exterior_losa_m2d())
        self.line_edit_altura_viga_exterior_losa_m2d.textChanged.connect(
            lambda: self.calcular_factores_viga_exterior_losa_m2d())

    def conectar_cambios_texto_frame_sismo(self):
        # SECCION SOBRECARGAS - LINE EDIT
        self.line_edit_sobrecarga_particiones.textChanged.connect(
            lambda: self.totalizar_sobrecargas())
        self.line_edit_sobrecarga_acabados.textChanged.connect(
            lambda: self.totalizar_sobrecargas())
        self.line_edit_sobrecarga_cielo_raso.textChanged.connect(
            lambda: self.totalizar_sobrecargas())
        self.line_edit_sobrecarga_mortero_nivelacion.textChanged.connect(
            lambda: self.totalizar_sobrecargas())
        self.line_edit_sobrecarga_instalaciones.textChanged.connect(
            lambda: self.totalizar_sobrecargas())
        self.line_edit_sobrecarga_otros.textChanged.connect(
            lambda: self.totalizar_sobrecargas())
        self.line_edit_huella_escalera.textChanged.connect(
            lambda: self.calcular_sobrecarga_escalera())
        self.line_edit_contrahuella_escalera.textChanged.connect(
            lambda: self.calcular_sobrecarga_escalera())
        # SECCION JUSTIFICACIONES - LINE EDIT
        self.line_edit_espesor_mortero.textChanged.connect(
            lambda: self.justificacion_sobrecarga_mortero_nivelacion())
        self.line_edit_longitud_muro.textChanged.connect(
            lambda: self.justificacion_sobrecarga_particiones())
        self.line_edit_altura_muro.textChanged.connect(
            lambda: self.justificacion_sobrecarga_particiones())
        self.line_edit_espesor_muro.textChanged.connect(
            lambda: self.justificacion_sobrecarga_particiones())
        self.line_edit_area_total_losa.textChanged.connect(
            lambda: self.justificacion_sobrecarga_particiones())
        # SECCION FUERZA HORIZONTAL EQUIVALENTE - COMBOBOX
        self.combo_box_direccion_sismo.currentIndexChanged.connect(
            lambda: self.funcion_combo_box_direccion_sismo())
        # SECCION FUERZA HORIZONTAL EQUIVALENTE - LINE EDIT
        self.line_edit_parametro_Ct.textChanged.connect(
            lambda: self.calcular_periodos())
        self.line_edit_parametro_a.textChanged.connect(
            lambda: self.calcular_periodos())
        self.line_edit_periodo_elemento_finito.textChanged.connect(
            lambda: self.funcion_line_edit_periodo_elemento_finito())
        self.line_edit_periodo_elegido.textChanged.connect(
            lambda: self.funcion_line_edit_periodo_elegido())
        # SECCION FUERZA HORIZONTAL EQUIVALENTE - PUSH BUTTON
        self.push_button_grafico_espectro.clicked.connect(
            lambda: self.funcion_push_button_grafico_espectro())

    def conectar_cambios_texto_frame_diseno_viga(self):
        # DATOS VIGA - LINE EDIT
        self.line_edit_base_viga_d.textChanged.connect(
            lambda: self.acero_requerido_viga())
        self.line_edit_altura_viga_d.textChanged.connect(
            lambda: self.acero_requerido_viga())
        self.line_edit_recubrimiento_inferior_viga.textChanged.connect(
            lambda: self.acero_requerido_viga())
        self.line_edit_recubrimiento_superior_viga.textChanged.connect(
            lambda: self.acero_requerido_viga())
        self.line_edit_longitud_libre_viga.textChanged.connect(
            lambda: self.acero_requerido_viga())
        # MOMENTOS ANALISIS - LINE EDIT
        self.line_edit_momento_negativo_izquierdo_viga.textChanged.connect(
            lambda: self.acero_requerido_viga())
        self.line_edit_momento_positivo_izquierdo_viga.textChanged.connect(
            lambda: self.acero_requerido_viga())
        self.line_edit_momento_negativo_centro_viga.textChanged.connect(
            lambda: self.acero_requerido_viga())
        self.line_edit_momento_positivo_centro_viga.textChanged.connect(
            lambda: self.acero_requerido_viga())
        self.line_edit_momento_negativo_derecho_viga.textChanged.connect(
            lambda: self.acero_requerido_viga())
        self.line_edit_momento_positivo_derecho_viga.textChanged.connect(
            lambda: self.acero_requerido_viga())
        # ACERO DUCTIL - COMBO BOX
        self.combo_box_cantidad1_acero_superior_izquierdo.currentIndexChanged.connect(
            lambda: self.acero_impuesto_superior_izquierdo())
        self.combo_box_cantidad2_acero_superior_izquierdo.currentIndexChanged.connect(
            lambda: self.acero_impuesto_superior_izquierdo())
        self.combo_box_codigo1_acero_superior_izquierdo.currentIndexChanged.connect(
            lambda: self.acero_impuesto_superior_izquierdo())
        self.combo_box_codigo2_acero_superior_izquierdo.currentIndexChanged.connect(
            lambda: self.acero_impuesto_superior_izquierdo())
        self.combo_box_cantidad1_acero_superior_derecho.currentIndexChanged.connect(
            lambda: self.acero_impuesto_superior_derecho())
        self.combo_box_cantidad2_acero_superior_derecho.currentIndexChanged.connect(
            lambda: self.acero_impuesto_superior_derecho())
        self.combo_box_codigo1_acero_superior_derecho.currentIndexChanged.connect(
            lambda: self.acero_impuesto_superior_derecho())
        self.combo_box_codigo2_acero_superior_derecho.currentIndexChanged.connect(
            lambda: self.acero_impuesto_superior_derecho())
        self.combo_box_cantidad1_acero_inferior_derecho.currentIndexChanged.connect(
            lambda: self.acero_impuesto_inferior_derecho())
        self.combo_box_cantidad2_acero_inferior_derecho.currentIndexChanged.connect(
            lambda: self.acero_impuesto_inferior_derecho())
        self.combo_box_codigo1_acero_inferior_derecho.currentIndexChanged.connect(
            lambda: self.acero_impuesto_inferior_derecho())
        self.combo_box_codigo2_acero_inferior_derecho.currentIndexChanged.connect(
            lambda: self.acero_impuesto_inferior_derecho())
        self.combo_box_cantidad1_acero_inferior_izquierdo.currentIndexChanged.connect(
            lambda: self.acero_impuesto_inferior_izquierdo())
        self.combo_box_cantidad2_acero_inferior_izquierdo.currentIndexChanged.connect(
            lambda: self.acero_impuesto_inferior_izquierdo())
        self.combo_box_codigo1_acero_inferior_izquierdo.currentIndexChanged.connect(
            lambda: self.acero_impuesto_inferior_izquierdo())
        self.combo_box_codigo2_acero_inferior_izquierdo.currentIndexChanged.connect(
            lambda: self.acero_impuesto_inferior_izquierdo())
        self.combo_box_cantidad1_acero_inferior_centro.currentIndexChanged.connect(
            lambda: self.acero_impuesto_inferior_centro())
        self.combo_box_cantidad2_acero_inferior_centro.currentIndexChanged.connect(
            lambda: self.acero_impuesto_inferior_centro())
        self.combo_box_codigo1_acero_inferior_centro.currentIndexChanged.connect(
            lambda: self.acero_impuesto_inferior_centro())
        self.combo_box_codigo2_acero_inferior_centro.currentIndexChanged.connect(
            lambda: self.acero_impuesto_inferior_centro())
        self.combo_box_cantidad1_acero_superior_centro.currentIndexChanged.connect(
            lambda: self.acero_impuesto_superior_centro())
        self.combo_box_cantidad2_acero_superior_centro.currentIndexChanged.connect(
            lambda: self.acero_impuesto_superior_centro())
        self.combo_box_codigo1_acero_superior_centro.currentIndexChanged.connect(
            lambda: self.acero_impuesto_superior_centro())
        self.combo_box_codigo2_acero_superior_centro.currentIndexChanged.connect(
            lambda: self.acero_impuesto_superior_centro())
        # DEMANDA CORTE - LINE EDIT
        self.line_edit_sobrecarga_permanente_viga.textChanged.connect(
            lambda: self.cortes_maximos())
        self.line_edit_sobrecarga_variable_viga.textChanged.connect(
            lambda: self.cortes_maximos())
        self.line_edit_corte_ultimo_viga.textChanged.connect(
            lambda: self.cortes_maximos())
        # ACERO ESTRIBO - COMBO BOX
        self.combo_box_n_ramas.currentIndexChanged.connect(
            lambda: self.ayuda_area_transversal_refuerzo())
        self.combo_box_diametro_estribo.currentIndexChanged.connect(
            lambda: self.ayuda_area_transversal_refuerzo())
        # ACERO ESTRIBO - LINE EDIT
        self.line_edit_separacion_definitiva.textChanged.connect(
            lambda: self.guardar_separaciones())
        self.line_edit_separacion_inconfinada.textChanged.connect(
            lambda: self.guardar_separaciones())
        self.line_edit_separacion_inconfinada_solapada.textChanged.connect(
            lambda: self.guardar_separaciones())

    def conectar_clicks_frame_diseno_viga(self):
        pass
