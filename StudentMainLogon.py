from sqlite3 import connect
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget
import sqlite3
import resource
import GUIresource
from studentPage import studentwindow
from Authentication import Authenticate

class studentloginpage(QWidget):
    def __init__(self):
        super(studentloginpage,self).__init__()
        loadUi("studentLogin.ui",self)
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
            query = 'SELECT password FROM Student_info WHERE username =\''+username+"\'"
            cursor.execute(query)
            result_pass = cursor.fetchone()[0]
            if result_pass == password:
                self.LoginButton.clicked.connect(self.runSlot)
                self.ErrorPop.setText("")
            else:
                self.ErrorPop.setText("Invalid username or password")

    def refreshAll(self):
        #Set the text of lineEdit once it's valid
        self.Videocapture_ = "0"

    @pyqtSlot()
    def runSlot(self):
        self.refreshAll()
        print(self.Videocapture_)
        self.outputWindow_()  # Create and open new output window

    def outputWindow_(self):
        """
        Created new window for visual output of the video in GUI
        """
        self._new_window = studentwindow()
        self._new_window.show()
        self._new_window.startVideo(self.Videocapture_)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = studentloginpage()
    ui.show()
    sys.exit(app.exec_())

