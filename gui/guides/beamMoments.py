# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'beamMoments.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaGuiaMomentos(object):
    def setupUi(self, VentanaGuiaMomentos):
        VentanaGuiaMomentos.setObjectName("VentanaGuiaMomentos")
        VentanaGuiaMomentos.resize(686, 286)
        self.centralwidget = QtWidgets.QWidget(VentanaGuiaMomentos)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 691, 291))
        self.label.setStyleSheet("border-image: url(:/imagenes/DetalleMomentos.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        VentanaGuiaMomentos.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaGuiaMomentos)
        QtCore.QMetaObject.connectSlotsByName(VentanaGuiaMomentos)

    def retranslateUi(self, VentanaGuiaMomentos):
        _translate = QtCore.QCoreApplication.translate
        VentanaGuiaMomentos.setWindowTitle(_translate("VentanaGuiaMomentos", "Guía momentos en viga"))
import imgs_rc
