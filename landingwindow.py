from sqlite3 import connect
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QLineEdit,QDialog
import resource
import GUIresource
# from the outputwindow.py; importing the ui_outputdialog class
from StudentMainLogon import studentloginpage
from LecturerMainLogon import lecturerloginpage

class Welcome(QDialog):
    def __init__(self):
        super(Welcome, self).__init__()
        loadUi("Welcome.ui",self)
        self.studentButton.clicked.connect(self.studentlogin)
        self.lecturerButton.clicked.connect(self.lecturerlogin)

    @pyqtSlot()
    def studentlogin(self):
        self.studentloginfunction()
        
    def studentloginfunction(self):
        self._new_window = studentloginpage()
        self._new_window.show()
        ui.hide()

    @pyqtSlot()
    def lecturerlogin(self):
        self.lecturerloginfunction()
        
    def lecturerloginfunction(self):
        self._new_window = lecturerloginpage()
        self._new_window.show()
        ui.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Welcome()
    ui.show()
    sys.exit(app.exec_())

app=QApplication(sys.argv)
mainwindow=Welcome()
widget=QtWidgets.QStackedWidget()
widget.addWidget(Welcome)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()




