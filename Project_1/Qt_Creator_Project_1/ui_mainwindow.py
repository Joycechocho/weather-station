# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 350)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.graphicsView = PlotWidget(self.centralWidget)
        self.graphicsView.setGeometry(QtCore.QRect(250, 30, 361, 281))
        self.graphicsView.setObjectName("graphicsView")
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(190, 70, 20, 211))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_degree = QtWidgets.QLabel(self.centralWidget)
        self.label_degree.setGeometry(QtCore.QRect(120, 110, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_degree.setFont(font)
        self.label_degree.setObjectName("label_degree")
        self.textEdit_Humidity = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit_Humidity.setGeometry(QtCore.QRect(50, 170, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.textEdit_Humidity.setFont(font)
        self.textEdit_Humidity.setReadOnly(True)
        self.textEdit_Humidity.setObjectName("textEdit_Humidity")
        self.label_percent = QtWidgets.QLabel(self.centralWidget)
        self.label_percent.setGeometry(QtCore.QRect(120, 170, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_percent.setFont(font)
        self.label_percent.setObjectName("label_percent")
        self.button_refresh = QtWidgets.QPushButton(self.centralWidget)
        self.button_refresh.setGeometry(QtCore.QRect(50, 250, 71, 32))
        self.button_refresh.setObjectName("button_refresh")
        self.textEdit_Temp = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit_Temp.setGeometry(QtCore.QRect(50, 110, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.textEdit_Temp.setFont(font)
        self.textEdit_Temp.setReadOnly(True)
        self.textEdit_Temp.setObjectName("textEdit_Temp")
        self.textEdit_Location = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit_Location.setGeometry(QtCore.QRect(20, 50, 121, 31))
        self.textEdit_Location.setReadOnly(True)
        self.textEdit_Location.setObjectName("textEdit_Location")
        MainWindow.setCentralWidget(self.centralWidget)
        self.actionTemp = QtWidgets.QAction(MainWindow)
        self.actionTemp.setObjectName("actionTemp")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_degree.setText(_translate("MainWindow", "°C"))
        self.textEdit_Humidity.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15.3</p></body></html>"))
        self.label_percent.setText(_translate("MainWindow", "%"))
        self.button_refresh.setText(_translate("MainWindow", "Refresh"))
        self.textEdit_Temp.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15.23</p></body></html>"))
        self.textEdit_Location.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Boulder</span></p></body></html>"))
        self.actionTemp.setText(_translate("MainWindow", "Temp"))

from pyqtgraph import PlotWidget
