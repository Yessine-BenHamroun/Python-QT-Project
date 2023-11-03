import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from mainWindows import Ui_MainWindow
from Isimm import Isimm
class fenetre:
    def __init__(self) -> None:
        self.institu=Isimm()
        self.fen=QMainWindow()
        self.ui=Ui_MainWindow(self.institu)
        self.ui.setupUi(self.fen)
        self.fen.show()
        
app=QtWidgets.QApplication(sys.argv)
window=fenetre()

app.exec_()