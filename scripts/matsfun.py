
class FuncionesVMateriales():

    def guardar_cambio_materiales(self):
        try:
            self.resistencia_concreto = float(self.line_edit_resistencia_concreto.text())
        except ValueError:
            self.resistencia_concreto = 0
        try:
            self.elasticidad_concreto = float(self.line_edit_elasticidad_concreto.text())
        except ValueError:
            self.elasticidad_concreto = 0
        try:
            self.peso_propio_concreto = float(self.line_edit_peso_propio_concreto.text())
        except ValueError:
            self.peso_propio_concreto = 0
        try:
            self.deformacion_ultima_concreto = float(self.line_edit_deformacion_ultima_concreto.text())
        except ValueError:
            self.deformacion_ultima_concreto = 0
        try:
            self.parametro_B1 = float(self.line_edit_parametro_B1.text())
        except ValueError:
            self.parametro_B1 = 0
        try:
            self.minoracion_resistencia_corte = float(self.line_edit_minoracion_resistencia_corte.text())
        except ValueError:
            self.minoracion_resistencia_corte = 0
        try:
            self.minoracion_resistencia_flexion = float(self.line_edit_minoracion_resistencia_flexion.text())
        except ValueError:
            self.minoracion_resistencia_flexion = 0
        try:
            self.fluencia_acero = float(self.line_edit_fluencia_acero.text())
        except ValueError:
            self.fluencia_acero = 0
        try:
            self.elasticidad_acero = float(self.line_edit_elasticidad_acero.text())
        except ValueError:
            self.elasticidad_acero = 0
        try:
            self.deformacion_cedente_acero = float(self.line_edit_deformacion_cedente_acero.text())
        except ValueError:
            self.deformacion_cedente_acero = 0
        try:
            self.deformacion_minima_acero = float(self.line_edit_deformacion_minima_acero.text())
        except ValueError:
            self.deformacion_minima_acero = 0
        try:
            self.sobrerresistencia_acero = float(self.line_edit_sobrerresistencia_acero.text())
        except ValueError:
            self.sobrerresistencia_acero = 0
        self.guardar_cambio(
            'fc', 'PROPMATS', 'VALOR',
            self.resistencia_concreto)
        self.guardar_cambio(
            'Ec', 'PROPMATS', 'VALOR',
            self.elasticidad_concreto)
        self.guardar_cambio(
            'Yc', 'PROPMATS', 'VALOR',
            self.peso_propio_concreto)
        self.guardar_cambio(
            'Ecu', 'PROPMATS', 'VALOR',
            self.deformacion_ultima_concreto)
        self.guardar_cambio(
            'B1', 'PROPMATS', 'VALOR',
            self.parametro_B1)
        self.guardar_cambio(
            'phiv', 'PROPMATS', 'VALOR',
            self.minoracion_resistencia_corte)
        self.guardar_cambio(
            'phib', 'PROPMATS', 'VALOR',
            self.minoracion_resistencia_flexion)
        self.guardar_cambio(
            'fy', 'PROPMATS', 'VALOR',
            self.fluencia_acero)
        self.guardar_cambio(
            'Es', 'PROPMATS', 'VALOR',
            self.elasticidad_acero)
        self.guardar_cambio(
            'Ey', 'PROPMATS', 'VALOR',
            self.deformacion_cedente_acero)
        self.guardar_cambio(
            'Esmin', 'PROPMATS', 'VALOR',
            self.deformacion_minima_acero)
        self.guardar_cambio(
            'Fsr', 'PROPMATS', 'VALOR',
            self.sobrerresistencia_acero)
