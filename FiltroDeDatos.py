# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataframe.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from pandas import *
import pandas as pd
import time
listaCont = ["America", "Africa", "Asia", "Europe", "Oceania", "Other"]
data = read_csv("Proyecto-Final-Seminario-de-Traductores-de-Lenguajes-II/Paises3.csv")
listaPaises = data['countriesAndTerritories'].tolist()
#print("Month: ", listaPaises)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
"background: #0077b6;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("QWidget {\n"
"background-color: #00b4d8;\n"
"color: #caf0f8;\n"
"}")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 150, 121, 22))
        self.comboBox.setStyleSheet("QWidget {\n"
"color: #caf0f8;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 201, 16))
        self.label_2.setStyleSheet("QWidget {\n"
"color: #caf0f8;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 120, 201, 16))
        self.label_3.setStyleSheet("QWidget {\n"
"color: #caf0f8;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(420, 150, 121, 22))
        self.comboBox_2.setStyleSheet("QWidget {\n"
"color: #caf0f8;\n"
"}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(250, 170, 91, 22))
        self.comboBox_3.setStyleSheet("QWidget {\n"
"color: #caf0f8;\n"
"}")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(200, 250, 181, 31))
        self.plainTextEdit.setStyleSheet("QWidget {\n"
"background-color: #FFFFFF;\n"
"color: #000000;\n"
"}\n"
"")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 230, 201, 16))
        self.label_4.setStyleSheet("QWidget {\n"
"color: #caf0f8;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 330, 91, 23))
        self.pushButton.setStyleSheet("QWidget {\n"
"background-color: #caf0f8;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 390, 561, 23))
        self.progressBar.setStyleSheet("QWidget {\n"
"background-color: #FFFFFF;\n"
"}")
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setMinimum(0)
        n = 200
        self.progressBar.setMaximum(n)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 370, 101, 16))
        self.label_5.setStyleSheet("QWidget {\n"
"color: #caf0f8;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.spinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinbox.setGeometry(QtCore.QRect(420, 150, 100, 20))
        self.spinbox.setObjectName("spinbox")
        self.spinbox.setMaximum(250000)
        self.spinbox.setMinimum(0)
        self.pushButton.clicked.connect(self.generarArchivo)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Filtrado de datos con Pandas Dataframe"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Número de muertes"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Número de casos"))
        self.comboBox.setItemText(2, _translate("MainWindow", "País"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Continente"))
        self.label_2.setText(_translate("MainWindow", "Selecciona el modo de filtrado de datos"))
        self.label_3.setText(_translate("MainWindow", "Ingresa el valor de tu filtro de búsqueda"))
        #self.comboBox_2.setItemText(0, _translate("MainWindow", "0-500"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Mayor a"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Menor a"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Igual a"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Mayor o igual a"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Menor o igual a"))
        self.label_4.setText(_translate("MainWindow", "Escribe el nombre del archivo a generar"))
        self.pushButton.setText(_translate("MainWindow", "Generar archivo"))
        self.label_5.setText(_translate("MainWindow", "Archivo generado"))
        self.preconf()
    
    def run(self, n): 
        for i in range(n):
            time.sleep(0.01)
            self.progressBar.setValue(i+1)


    def preconf(self):
        self.comboBox_2.hide()
        self.progressBar.hide()
        self.label_5.hide()
        self.proceso()

    def valorcombo(self, value):
        #print("combobox changed", value)
        self.proceso2(value)
    
    def proceso(self):
        self.comboBox.currentTextChanged.connect(self.valorcombo)
        combo = self.comboBox.currentText()
        #print("Combo", combo)

    def generarArchivo(self):
        tipo = self.comboBox.currentText()
        relacional = self.comboBox_3.currentText()
        dato = self.comboBox_2.currentText()
        numero = self.spinbox.value()
        fileName = self.plainTextEdit.toPlainText()
        self.plainTextEdit.clear()
        self.progressBar.show()
        self.run(200)
        df = pd.read_csv("Proyecto-Final-Seminario-de-Traductores-de-Lenguajes-II/COVID19.csv")
        self.label_5.show()
        
        if fileName == "":
            fileName = "Archivo"
        
        if (tipo == "Número de casos"):
            if relacional == "Mayor a":
                df = df[['countriesAndTerritories', 'cases', 'deaths', 'dateRep', 'popData2019']][df["cases"] > numero]
            elif relacional == "Menor a":
                df = df[['countriesAndTerritories', 'cases', 'deaths', 'dateRep', 'popData2019']][df["cases"] < numero]
            elif relacional == "Igual a":
                df = df[['countriesAndTerritories', 'cases', 'deaths', 'dateRep', 'popData2019']][df["cases"] == numero]
            elif relacional == "Mayor o igual a":
                df = df[['countriesAndTerritories', 'cases', 'deaths', 'dateRep', 'popData2019']][df["cases"] >= numero]
            elif relacional == "Menor o igual a":
                df = df[['countriesAndTerritories', 'cases', 'deaths', 'dateRep', 'popData2019']][df["cases"] <= numero]
            df = pd.DataFrame(df)
            df.to_csv("Proyecto-Final-Seminario-de-Traductores-de-Lenguajes-II/Archivos/" + fileName + ".csv")
        elif (tipo == "Número de muertes"):
            if relacional == "Mayor a":
                df = df[['countriesAndTerritories', 'cases', 'deaths', 'dateRep', 'popData2019']][df["deaths"] > numero]
            elif relacional == "Menor a":
                df = df[['countriesAndTerritories', 'cases', 'deaths', 'dateRep', 'popData2019']][df["deaths"] < numero]
            elif relacional == "Igual a":
                df = df[['countriesAndTerritories', 'cases', 'deaths', 'dateRep', 'popData2019']][df["deaths"] == numero]
            elif relacional == "Mayor o igual a":
                df = df[['countriesAndTerritories', 'cases', 'deaths', 'dateRep', 'popData2019']][df["deaths"] >= numero]
            elif relacional == "Menor o igual a":
                df = df[['countriesAndTerritories', 'cases', 'deaths', 'dateRep', 'popData2019']][df["deaths"] <= numero]
            df = pd.DataFrame(df)
            df.to_csv("Proyecto-Final-Seminario-de-Traductores-de-Lenguajes-II/Archivos/" + fileName + ".csv")
        elif (tipo == "País"):
            df = df[['countriesAndTerritories', 'cases', 'deaths', 'dateRep', 'popData2019']][df["countriesAndTerritories"] == dato]
            df = pd.DataFrame(df)
            df.to_csv("Proyecto-Final-Seminario-de-Traductores-de-Lenguajes-II/Archivos/" + fileName + ".csv")
        elif (tipo == "Continente"):
            df = df[['countriesAndTerritories', 'cases', 'deaths', 'dateRep', 'popData2019']][df["continentExp"] == dato]
            df = pd.DataFrame(df)
            df.to_csv("Proyecto-Final-Seminario-de-Traductores-de-Lenguajes-II/Archivos/" + fileName + ".csv")

    def proceso2(self, value):
        print("Valiuuuuuuuu", value)
        valor = self.comboBox.currentText()
        if (valor == "Número de casos"):
            self.comboBox_2.clear()
            self.comboBox_2.hide()
            self.comboBox_3.show()
            self.spinbox.show()
        elif (valor == "Número de muertes"):
            self.comboBox_3.show()
            self.comboBox_2.clear()
            self.comboBox_2.hide()
            self.spinbox.show()
        elif (valor == "País"):
            self.spinbox.hide()
            self.comboBox_2.clear()
            self.comboBox_2.show()
            self.comboBox_3.hide()
            self.comboBox_2.setDisabled(False)
            i=0
            while i < 214:
                self.comboBox_2.addItem(listaPaises[i], listaPaises[i])
                i+=1
        elif (valor == "Continente"):
            self.spinbox.hide()
            self.comboBox_2.clear()
            self.comboBox_2.show()
            self.comboBox_3.hide()
            self.comboBox_2.setDisabled(False)
            i=0
            while i < 6:
                self.comboBox_2.addItem(listaCont[i], listaCont[i])
                i+=1




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

