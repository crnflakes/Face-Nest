from email import header
import sys
import os
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog,QApplication, QTableWidgetItem
import pandas as pd
import numpy as np
import csv
import resource
import GUIresource
import xlwings as xw
from openpyxl import workbook, load_workbook
import io
import datetime
import time
from PyQt5.QtCore import pyqtSlot, QDate, QDateTime


class lecturerWindow(QDialog):
    def __init__(self):
        super(lecturerWindow, self).__init__()
        loadUi("lectuerPageUI.ui", self)
        self.StudentTable.setColumnWidth(0,150)
        self.StudentTable.setColumnWidth(1,150)
        self.StudentTable.setColumnWidth(2,150)
        self.StudentTable.setColumnWidth(3,150)

        self.loadrecords.clicked.connect(self.loadexcel)
        self.loadstatus.clicked.connect(self.loadpivot)
        self.Homebutton.clicked.connect(self.home)
        self.sorttoday.clicked.connect(self.rectoday)

    def rectoday(self):
        dataset = 'Attendance.csv'
        fields= ['Name', 'Time Elapsed','Class']
        df=pd.read_csv(dataset, header=0, skipinitialspace=True, usecols=fields)
        df['Time Elapsed'] = pd.to_timedelta(df['Time Elapsed'])
        df['Time Elapsed'] = df.groupby(['Name','Class'])['Time Elapsed'].transform('sum')
        timethreshold = datetime.timedelta(minutes=30)
        df['Attendance status'] = df['Time Elapsed'].apply(lambda x: 'Absent' if x<=timethreshold  else 'Present')
        selectclass = str(self.comboBox.currentText())
        is_class = df['Class']==selectclass 
        df_class = df[is_class]

        new_df = df_class.drop_duplicates(subset=['Name','Class'])

        Rows = len(new_df.index)
        self.statustable.setColumnCount(len(new_df.columns))
        self.statustable.setRowCount(Rows)
        

        for i in range(Rows):
            for j in range(len(new_df.columns)):
                self.statustable.setItem(i, j, QTableWidgetItem(str(new_df.iat[i, j])))
        
        self.statustable.resizeColumnsToContents()
        self.statustable.resizeRowsToContents()

    
    def loadexcel(self):
        self.all_data = pd.read_csv('Attendance.csv')
        NumRows = len(self.all_data.index)
        self.StudentTable.setColumnCount(len(self.all_data.columns))
        self.StudentTable.setRowCount(NumRows)

        for i in range(NumRows):
            for j in range(len(self.all_data.columns)):
                self.StudentTable.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.StudentTable.resizeColumnsToContents()
        self.StudentTable.resizeRowsToContents()

    def loadpivot(self):
        dataset = 'Attendance.csv'
        fields= ['Name', 'Time Elapsed','Class']
        df=pd.read_csv(dataset, header=0, skipinitialspace=True, usecols=fields)
        df['Time Elapsed'] = pd.to_timedelta(df['Time Elapsed'])
        df['Time Elapsed'] = df.groupby(['Name','Class'])['Time Elapsed'].transform('sum')
        timethreshold = datetime.timedelta(minutes=30)
        df['Attendance status'] = df['Time Elapsed'].apply(lambda x: 'Absent' if x<=timethreshold  else 'Present')
        new_df = df.drop_duplicates(subset=['Name','Class'])
        
        Rows = len(new_df.index)
        self.statustable.setColumnCount(len(new_df.columns))
        self.statustable.setRowCount(Rows)

        for i in range(Rows):
            for j in range(len(new_df.columns)):
                self.statustable.setItem(i, j, QTableWidgetItem(str(new_df.iat[i, j])))

        self.statustable.resizeColumnsToContents()
        self.statustable.resizeRowsToContents()


    @pyqtSlot()
    def home(self):
        sys.exit()
                
if  __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = lecturerWindow()
    ui.show()
    sys.exit(app.exec_())





