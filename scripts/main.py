from PyQt5 import QtWidgets, uic
import sys
from scripts.mem import DatosMemoria
from scripts.data import ConexionBaseDatos
from scripts.mainload import CargarDatosVPrincipal
from scripts.mainfun import FuncionesVPrincipal
from scripts.maincon import ConexionesVPrincipal
from scripts.mainextra import FuncionesAdicionalesVPrincipal


class VentanaPrincipalAEUS(
        QtWidgets.QMainWindow, ConexionesVPrincipal,
        FuncionesAdicionalesVPrincipal, FuncionesVPrincipal,
        CargarDatosVPrincipal):

    def __init__(self):
        super(VentanaPrincipalAEUS, self).__init__()
        uic.loadUi('gui/main.ui', self)
        self.manejo_datos = ConexionBaseDatos()
        self.ubicacion_base = 'data/base'
        self.datos_memoria = DatosMemoria(
            self.ubicacion_base, self.manejo_datos)
        self.lista_departamentos = (
            self.datos_memoria.diccionario_colombia.keys())
        self.cargar_datos_en_ventana_principal()
        self.conectar_funciones_ventana_principal()

    def conectar_funciones_ventana_principal(self):
        self.conectar_clicks_ventana_principal()
        self.conectar_cambios_texto_frame_inicio()
        self.conectar_cambios_texto_frame_general()
        self.conectar_clicks_frame_dimension()
        self.conectar_cambios_texto_frame_dimension()

    def cargar_datos_en_ventana_principal(self):
        self.cargar_datos_frame_inicio()
        self.cargar_datos_frame_general()
        self.cargar_datos_frame_predimension()

    def closeEvent(self, event):  # Evento de lanzamiento del sistema
        resultado = QtWidgets.QMessageBox.question(
            self, 'Salir AEUS', '¿ Seguro que quieres salir ?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if resultado == QtWidgets.QMessageBox.Yes:
            sys.exit()
            event.accept()
        else:
            event.ignore()
