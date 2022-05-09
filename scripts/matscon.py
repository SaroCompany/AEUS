class ConexionesVMateriales():

    def conectar_cambios_texto_materiales(self):
        self.line_edit_resistencia_concreto.textChanged.connect(
            lambda: self.guardar_cambio_materiales())
        self.line_edit_elasticidad_concreto.textChanged.connect(
            lambda: self.guardar_cambio_materiales())
        self.line_edit_peso_propio_concreto.textChanged.connect(
            lambda: self.guardar_cambio_materiales())
        self.line_edit_deformacion_ultima_concreto.textChanged.connect(
            lambda: self.guardar_cambio_materiales())
        self.line_edit_parametro_B1.textChanged.connect(
            lambda: self.guardar_cambio_materiales())
        self.line_edit_minoracion_resistencia_corte.textChanged.connect(
            lambda: self.guardar_cambio_materiales())
        self.line_edit_minoracion_resistencia_flexion.textChanged.connect(
            lambda: self.guardar_cambio_materiales())
        self.line_edit_fluencia_acero.textChanged.connect(
            lambda: self.guardar_cambio_materiales())
        self.line_edit_elasticidad_acero.textChanged.connect(
            lambda: self.guardar_cambio_materiales())
        self.line_edit_deformacion_cedente_acero.textChanged.connect(
            lambda: self.guardar_cambio_materiales())
        self.line_edit_deformacion_minima_acero.textChanged.connect(
            lambda: self.guardar_cambio_materiales())
        self.line_edit_sobrerresistencia_acero.textChanged.connect(
            lambda: self.guardar_cambio_materiales())