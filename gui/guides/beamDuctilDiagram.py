# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'beamDuctilDiagram.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaGuiaDuctilidad(object):
    def setupUi(self, VentanaGuiaDuctilidad):
        VentanaGuiaDuctilidad.setObjectName("VentanaGuiaDuctilidad")
        VentanaGuiaDuctilidad.resize(565, 241)
        self.centralwidget = QtWidgets.QWidget(VentanaGuiaDuctilidad)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 571, 241))
        self.label.setStyleSheet("border-image: url(:/imagenes/RequisitosAceroLongitudinalDuctilidad.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        VentanaGuiaDuctilidad.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaGuiaDuctilidad)
        QtCore.QMetaObject.connectSlotsByName(VentanaGuiaDuctilidad)

    def retranslateUi(self, VentanaGuiaDuctilidad):
        _translate = QtCore.QCoreApplication.translate
        VentanaGuiaDuctilidad.setWindowTitle(_translate("VentanaGuiaDuctilidad", "Guía barras elegidas para el refuerzo"))
import imgs_rc
