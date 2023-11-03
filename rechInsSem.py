# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rechInsSem.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import back



class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.columns=["Num d'inscription","Code Matiere","Note DS","Note EX"]
        

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.columns[section])

    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return 4

class Ui_Dialog(object):
    def __init__(self,Isimm):
        self.inst=Isimm
        
    def affInsSem(self):
        alternative=[]
        
        for note in self.inst.rechInsSem(self.lineEdit.text(),self.comboBox_2.currentText()):
            notes=[]
            notes.append(note.num)
            notes.append(note.code)
            notes.append(note.ds)
            notes.append(note.ex)
            alternative.append(notes)

        self.modal=TableModel(alternative)
        
        self.tableView.setModel(self.modal)
        self.horizontal_header = self.tableView.horizontalHeader()
        self.vertical_header = self.tableView.verticalHeader()
        self.horizontal_header.setSectionResizeMode(3)
        self.tableView.horizontalHeader().setStretchLastSection(True)
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1121, 600)
        icon = QtGui.QIcon.fromTheme("C:\\Users\\yessi\\Desktop\\python\\Project\\window_icon.png")
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(810, 100, 150, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background: rgb(255,255,255);\n"
"background: rgba(46,82,101,255);\n"
"  border: 0 solid #E2E8F0;\n"
"  color: rgb(255, 255, 255);\n"
"  font-size: 12px;\n"
"  font-weight: 700;\n"
"  height: 56px;\n"
"  border-radius: 8px;\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(270, 10, 581, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgba(46,82,101,255);\n"
"background-color:rgba(0,0,0,0);\n"
"")
        self.label_10.setObjectName("label_10")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(710, 100, 71, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgba(46,82,101,255);\n"
"padding-bottom:7px;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(20, 180, 1081, 391))
        self.tableView.setStyleSheet("background:rgba(0,0,0,0);\n"
"border:none;")
        self.tableView.setObjectName("tableView")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(590, 100, 121, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color:rgb(104, 121, 143);\n"
"padding-bottom:7px;")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(-10, -150, 1131, 761))
        self.label_4.setStyleSheet("border-image:url(:/img/1.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(300, 100, 250, 35))
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
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 100, 241, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color:rgb(104, 121, 143);\n"
"padding-bottom:7px;")
        self.label.setObjectName("label")
        self.label_4.raise_()
        self.pushButton.raise_()
        self.label_10.raise_()
        self.comboBox_2.raise_()
        self.tableView.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.pushButton.clicked.connect(self.affInsSem)
        
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Rechercher"))
        self.label_10.setText(_translate("Dialog", "Recherche par num Inscription et Semestre"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "S1"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "S2"))
        self.label_2.setText(_translate("Dialog", "Semestre :"))
        self.label.setText(_translate("Dialog", "Numéro d\'inscription :"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())