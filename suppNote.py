# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'suppNote.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Notes import Notes
import back
from tkinter import *
from tkinter import messagebox
class Ui_Dialog(object):
    def __init__(self,Isimm):
        self.inst=Isimm


    def suppNote(self):
        n=self.lineEdit.text()
        c=self.lineEdit_2.text()
        self.inst.suppNote(n,c)
        self.inst.afficherListeNote()
        messagebox.showinfo("Succes", "Note supprimée avec succès")


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1121, 600)
        icon = QtGui.QIcon.fromTheme("C:\\Users\\yessi\\Desktop\\python\\Project\\window_icon.png")
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(280, 220, 221, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color:rgb(104, 121, 143);\n"
"padding-bottom:7px;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(470, 520, 150, 45))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("  background: #FFFFFF;\n"
"  border: 0 solid #E2E8F0;\n"
"  color: #1A202C;\n"
"  font-size: 12px;\n"
"  font-weight: 700;\n"
"  height: 56px;\n"
"  border-radius: 8px;\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, -150, 1131, 761))
        self.label_4.setStyleSheet("border-image:url(:/img/1.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(500, 220, 250, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(410, 30, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgba(46,82,101,255);\n"
"background-color:rgba(0,0,0,0);\n"
"")
        self.label_10.setObjectName("label_10")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(500, 300, 250, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(310, 300, 191, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color:rgb(104, 121, 143);\n"
"padding-bottom:7px;")
        self.label_2.setObjectName("label_2")
        self.label_4.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.label_10.raise_()
        self.lineEdit_2.raise_()
        self.label_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.pushButton.clicked.connect(self.suppNote)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Numero inscription :"))
        self.pushButton.setText(_translate("Dialog", "Supprimer"))
        self.label_10.setText(_translate("Dialog", "Supprimer Note"))
        self.label_2.setText(_translate("Dialog", "Code de Matiere :"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
