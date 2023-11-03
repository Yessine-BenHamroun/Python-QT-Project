# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'affNote.ui'
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
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1121, 600)
        icon = QtGui.QIcon.fromTheme("C:\\Users\\yessi\\Desktop\\python\\Project\\window_icon.png")
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(20, 100, 1081, 481))
        self.tableView.setStyleSheet("background:rgba(0,0,0,0);\n"
"border:none;")
        self.tableView.setObjectName("tableView")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, -140, 1131, 761))
        self.label_4.setStyleSheet("border-image:url(:/img/1.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(460, 20, 191, 51))
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
        self.label_4.raise_()
        self.tableView.raise_()
        self.label_10.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        alternative=[]
        
        for note in self.inst.listNote:
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

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_10.setText(_translate("Dialog", "List des Notes"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())