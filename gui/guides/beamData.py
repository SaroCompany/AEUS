# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'beamData.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaGuiaDatosViga(object):
    def setupUi(self, VentanaGuiaDatosViga):
        VentanaGuiaDatosViga.setObjectName("VentanaGuiaDatosViga")
        VentanaGuiaDatosViga.resize(752, 180)
        self.centralwidget = QtWidgets.QWidget(VentanaGuiaDatosViga)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 201, 181))
        self.label.setStyleSheet("border-image: url(:/imagenes/DetalleCorte.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 0, 551, 181))
        self.label_2.setStyleSheet("border-image: url(:/imagenes/DetalleLongitudinal.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        VentanaGuiaDatosViga.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaGuiaDatosViga)
        QtCore.QMetaObject.connectSlotsByName(VentanaGuiaDatosViga)

    def retranslateUi(self, VentanaGuiaDatosViga):
        _translate = QtCore.QCoreApplication.translate
        VentanaGuiaDatosViga.setWindowTitle(_translate("VentanaGuiaDatosViga", "Guia datos viga"))
import imgs_rc
