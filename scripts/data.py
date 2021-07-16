import sqlite3


class ConexionBaseDatos():

    def guardar_dato(self, busqueda, ubicacion_base, tabla, criterio, cambio):
        self.abre_conexion(ubicacion_base)
        self.mi_cursor.execute(
            f'UPDATE {tabla} SET {criterio}="{cambio}" WHERE \
                CODIGO="{busqueda}"')
        self.cierra_conexion()

    def consultar_dato(self, busqueda, ubicacion_base, tabla, criterio):
        self.abre_conexion(ubicacion_base)
        comando = f'SELECT {criterio} FROM {tabla} WHERE CODIGO="{busqueda}"'
        self.mi_cursor.execute(comando)
        self.consulta = self.mi_cursor.fetchone()
        self.dato = self.consulta[0]
        self.cierra_conexion()
        return self.dato

    def abre_conexion(self, ubicacion):
        self.mi_conexion = sqlite3.connect(ubicacion)
        self.mi_cursor = self.mi_conexion.cursor()

    def cierra_conexion(self):
        self.mi_conexion.commit()
        self.mi_conexion.close()
