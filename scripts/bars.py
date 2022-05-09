from PyQt5 import QtWidgets, uic
import sys
from scripts.barsload import CargarDatosVBarras
from scripts.barscon import ConexionesVBarras
from scripts.barsfun import FuncionesVBarras
from scripts.mem import DatosMemoria
from scripts.data import ConexionBaseDatos
from scripts.mainextra import FuncionesAdicionalesVPrincipal

class VentanaBarras(
    QtWidgets.QDialog, CargarDatosVBarras,
    ConexionesVBarras, FuncionesVBarras, FuncionesAdicionalesVPrincipal):

    def __init__(self, parent=None):
        super(VentanaBarras, self).__init__()
        uic.loadUi('gui/bars.ui', self)
        self.manejo_datos = ConexionBaseDatos()
        self.ubicacion_base = 'data/base'
        self.datos_memoria = DatosMemoria(
            self.ubicacion_base, self.manejo_datos)
        self.cargar_datos_en_ventana_barras()
        self.conectar_funciones_ventana_barras()

    def cargar_datos_en_ventana_barras(self):
        self.cargar_datos_ventana_barras()

    def conectar_funciones_ventana_barras(self):
        self.conectar_cambios_texto_barras()