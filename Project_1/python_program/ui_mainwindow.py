# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPalette, QBrush
import pyqtgraph as pg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 350)
        oImage = QImage("cloud.jpg")
        palette = QPalette()
        palette.setBrush(10, QBrush(oImage)) 
        self.setPalette(palette)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        
        self.graphicsView = PlotWidget(self.centralWidget)
        self.graphicsView.setGeometry(QtCore.QRect(250, 30, 361, 281))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setBackground('default')
        self.graphicsView.plotItem.setTitle(title='Temperature Today')
        self.graphicsView.plotItem.getAxis('bottom').setLabel('Time', units='Hour')
        self.graphicsView.plotItem.getAxis('bottom').setPen(pen=pg.mkPen('b', width=3))
        self.graphicsView.plotItem.getAxis('left').setLabel('Temp', units='°C')
        self.graphicsView.plotItem.getAxis('bottom').setWidth(260)
        self.graphicsView.plotItem.enableAutoScale()
        self.graphicsView.plotItem.setMouseEnabled(True, True)
        self.graphicsView.plotItem.getAxis('bottom').setScale(0.000277778)
        self.graphicsView.plotItem.showGrid(False, False, 0.7)
        
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(190, 70, 20, 211))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.label_degree = QtWidgets.QLabel(self.centralWidget)
        self.label_degree.setGeometry(QtCore.QRect(120, 110, 21, 31))
        self.label_degree.setStyleSheet("QLabel {color:white}")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_degree.setFont(font)
        self.label_degree.setObjectName("label_degree")
        
        self.textEdit_Humidity = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit_Humidity.setGeometry(QtCore.QRect(50, 170, 61, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(50)
        font.setKerning(False)
        self.textEdit_Humidity.setFont(font)
        self.textEdit_Humidity.setReadOnly(True)
        self.textEdit_Humidity.setObjectName("textEdit_Humidity")
        self.textEdit_Humidity.viewport().setAutoFillBackground(False)
        self.textEdit_Humidity.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.textEdit_Humidity.setStyleSheet("QTextEdit {color:white}")
        self.textEdit_Humidity.setEnabled(False)
        
        self.textEdit_Request = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit_Request.setGeometry(QtCore.QRect(5, 330, 280, 60))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(50)
        font.setKerning(False)
        self.textEdit_Request.setFont(font)
        self.textEdit_Request.setReadOnly(True)
        self.textEdit_Request.setObjectName("textEdit_Request")
        self.textEdit_Request.viewport().setAutoFillBackground(False)
        self.textEdit_Request.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.textEdit_Request.setStyleSheet("QTextEdit {color:black}")
        self.textEdit_Request.setEnabled(False)
        
        self.label_percent = QtWidgets.QLabel(self.centralWidget)
        self.label_percent.setGeometry(QtCore.QRect(120, 170, 21, 31))
        self.label_percent.setStyleSheet("QLabel {color:white}")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_percent.setFont(font)
        self.label_percent.setObjectName("label_percent")
        
        self.button_refresh = QtWidgets.QPushButton(self.centralWidget)
        self.button_refresh.setGeometry(QtCore.QRect(50, 250, 71, 32))
        self.button_refresh.setObjectName("button_refresh")
        
        self.textEdit_Temp = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit_Temp.setGeometry(QtCore.QRect(53, 110, 65, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(50)
        font.setKerning(False)
        self.textEdit_Temp.setFont(font)
        self.textEdit_Temp.setReadOnly(True)
        self.textEdit_Temp.setObjectName("textEdit_Temp")
        self.textEdit_Temp.setObjectName("textEdit_Humidity")
        self.textEdit_Temp.viewport().setAutoFillBackground(False)
        self.textEdit_Temp.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.textEdit_Temp.setStyleSheet("QTextEdit {color:white}")
        self.textEdit_Temp.setEnabled(False)
        
        self.textEdit_Location = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit_Location.setGeometry(QtCore.QRect(20, 50, 125, 40))
        self.textEdit_Location.setReadOnly(True)
        self.textEdit_Location.setObjectName("textEdit_Location")
        self.textEdit_Location.viewport().setAutoFillBackground(False)
        self.textEdit_Location.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.textEdit_Location.setStyleSheet("QTextEdit {color:white}")
        self.textEdit_Location.setEnabled(False)
        
        
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
        
        self.textEdit_Request.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Last Request：10／02／2017 01：11：03</p></body></html>"))
        
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
