# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flexureDiagram.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaGuiaDiagramaFlexion(object):
    def setupUi(self, VentanaGuiaDiagramaFlexion):
        VentanaGuiaDiagramaFlexion.setObjectName("VentanaGuiaDiagramaFlexion")
        VentanaGuiaDiagramaFlexion.resize(589, 278)
        self.centralwidget = QtWidgets.QWidget(VentanaGuiaDiagramaFlexion)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 591, 281))
        self.label.setStyleSheet("border-image: url(:/imagenes/DefinicionResistenciaNominalFlexion.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        VentanaGuiaDiagramaFlexion.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaGuiaDiagramaFlexion)
        QtCore.QMetaObject.connectSlotsByName(VentanaGuiaDiagramaFlexion)

    def retranslateUi(self, VentanaGuiaDiagramaFlexion):
        _translate = QtCore.QCoreApplication.translate
        VentanaGuiaDiagramaFlexion.setWindowTitle(_translate("VentanaGuiaDiagramaFlexion", "Resistencia nominal a la flexión"))
import imgs_rc
