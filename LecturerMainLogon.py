from sqlite3 import connect
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget
import sqlite3
import resource
import GUIresource
from lecturerPage import lecturerWindow
from Authentication import Authenticate

class lecturerloginpage(QWidget):
    def __init__(self):
        super(lecturerloginpage,self).__init__()
        loadUi("lecturerLogin.ui",self)
        self.LoginButton.clicked.connect(self.loginfunction)
        self.Passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self._new_window = None
        self.Videocapture_ = None
        
    def loginfunction(self):
        username=self.Usernamefield.text()
        password=self.Passwordfield.text()

        Auth=Authenticate(password)
        print(Auth.validate())
        if len(username)== 0 and len (password)==0:
            self.ErrorPop.setText("Please input all fields!")
            
        else:
            connection = sqlite3.connect("User.db")
            cursor = connection.cursor()
            query = 'SELECT password FROM Lecturer_info WHERE username =\''+username+"\'"
            cursor.execute(query)
            result_pass = cursor.fetchone()[0]
            if result_pass == password:
                self.LoginButton.clicked.connect(self.lecturerslot)
                self.ErrorPop.setText("")
            else:
                self.ErrorPop.setText("Invalid username or password")
    def refreshAll(self):
        self.Videocapture_ = "0"

    @pyqtSlot()
    def lecturerslot(self):
        self.refreshAll()
        self.lectureroutput()  # Create and open new output window

    def lectureroutput(self):
        self._new_window = lecturerWindow()
        self._new_window.show()

if  __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = lecturerloginpage()
    ui.show()
    sys.exit(app.exec_())   




