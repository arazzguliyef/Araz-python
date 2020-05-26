#Doslar bu Sadəcə Görünümüdür(Yəni belə desək ekarndır)
from PyQt5 import QtCore, QtGui, QtWidgets
import pyautogui as gui
import time
from random import choice
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(444, 327)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 20, 221, 211))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("tas.png"))
        self.label.setObjectName("label")
        self.tas = QtWidgets.QPushButton(Dialog)
        self.tas.setGeometry(QtCore.QRect(60, 250, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.tas.setFont(font)
        self.tas.setObjectName("pushButton")
        self.kagit = QtWidgets.QPushButton(Dialog)
        self.kagit.setGeometry(QtCore.QRect(170, 250, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.kagit.setFont(font)
        self.kagit.setObjectName("pushButton_2")
        self.makas = QtWidgets.QPushButton(Dialog)
        self.makas.setGeometry(QtCore.QRect(280, 250, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.makas.setFont(font)
        self.makas.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.tas.clicked.connect(self.Tas)
        self.kagit.clicked.connect(self.Kagit)
        self.makas.clicked.connect(self.Makas)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tas.setText(_translate("Dialog", "Taş"))
        self.kagit.setText(_translate("Dialog", "Kağıt"))
        self.makas.setText(_translate("Dialog", "Makas"))
    def Tas(self):
    	self.label.setPixmap(QtGui.QPixmap("tas.png"))
    def Kagit(self):
    	self.label.setPixmap(QtGui.QPixmap("kagit.png"))
    def Makas(self):
    	self.label.setPixmap(QtGui.QPixmap("makas.png"))

import sys
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())










