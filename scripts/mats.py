from PyQt5 import QtWidgets, uic
import sys
from scripts.matsload import CargarDatosVMateriales
from scripts.matscon import ConexionesVMateriales
from scripts.matsfun import FuncionesVMateriales
from scripts.mem import DatosMemoria
from scripts.data import ConexionBaseDatos
from scripts.mainextra import FuncionesAdicionalesVPrincipal

class VentanaMateriales(
    QtWidgets.QDialog, CargarDatosVMateriales,
    ConexionesVMateriales, FuncionesVMateriales, FuncionesAdicionalesVPrincipal):

    def __init__(self, parent=None):
        super(VentanaMateriales, self).__init__()
        uic.loadUi('gui/mats.ui', self)
        self.manejo_datos = ConexionBaseDatos()
        self.ubicacion_base = 'data/base'
        self.datos_memoria = DatosMemoria(
            self.ubicacion_base, self.manejo_datos)
        self.cargar_datos_en_ventana_materiales()
        self.conectar_funciones_ventana_materiales()

    def cargar_datos_en_ventana_materiales(self):
        self.cargar_datos_ventana_materiales()

    def conectar_funciones_ventana_materiales(self):
        self.conectar_cambios_texto_materiales()