

class FuncionesAdicionalesVPrincipal():

    def guardar_cambio(self, busqueda, tabla, criterio,  dato_cambiado):
        self.manejo_datos.guardar_dato(
            busqueda, self.ubicacion_base, tabla, criterio, dato_cambiado)

    def cambiar_stacks(self, stack):
        self.stacked_principal.setCurrentIndex(stack)

    def cambiar_stacks_losa(self, stack):
        self.stacked_widget_losa.setCurrentIndex(stack)
