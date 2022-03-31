class CargarDatosVMateriales():

    def cargar_datos_ventana_materiales(self):
        self.line_edit_resistencia_concreto.setText(str(
            self.datos_memoria.resistencia_concreto))
        self.line_edit_elasticidad_concreto.setText(str(
            self.datos_memoria.elasticidad_concreto))
        self.line_edit_peso_propio_concreto.setText(str(
            self.datos_memoria.peso_propio_concreto))
        self.line_edit_deformacion_ultima_concreto.setText(str(
            self.datos_memoria.deformacion_ultima_concreto))
        self.line_edit_parametro_B1.setText(str(
            self.datos_memoria.parametro_B1))
        self.line_edit_minoracion_resistencia_corte.setText(str(
            self.datos_memoria.minoracion_resistencia_corte))
        self.line_edit_minoracion_resistencia_flexion.setText(str(
            self.datos_memoria.minoracion_resistencia_flexion))
        self.line_edit_fluencia_acero.setText(str(
            self.datos_memoria.fluencia_acero))
        self.line_edit_elasticidad_acero.setText(str(
            self.datos_memoria.elasticidad_acero))
        self.line_edit_deformacion_cedente_acero.setText(str(
            self.datos_memoria.deformacion_cedente_acero))
        self.line_edit_deformacion_minima_acero.setText(str(
            self.datos_memoria.deformacion_minima_acero))
        self.line_edit_sobrerresistencia_acero.setText(str(
            self.datos_memoria.sobrerresistencia_acero))