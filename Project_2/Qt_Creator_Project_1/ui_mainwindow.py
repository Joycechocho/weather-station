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
        MainWindow.resize(649, 468)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(69, 45, 91, 255), stop:0.719212 rgba(35, 40, 84, 255));\n"
"")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.frame_ave_temp = QtWidgets.QFrame(self.centralWidget)
        self.frame_ave_temp.setGeometry(QtCore.QRect(400, 50, 110, 110))
        self.frame_ave_temp.setStyleSheet("background-color: rgba(255,255,255,30%);\n"
"")
        self.frame_ave_temp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ave_temp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ave_temp.setObjectName("frame_ave_temp")
        self.ave_temp_label = QtWidgets.QLabel(self.frame_ave_temp)
        self.ave_temp_label.setGeometry(QtCore.QRect(10, 20, 111, 41))
        self.ave_temp_label.setStyleSheet("background: transparent;\n"
"font: \"Helvetica\";\n"
"color: white;")
        self.ave_temp_label.setObjectName("ave_temp_label")
        self.ave_temp_text = QtWidgets.QPlainTextEdit(self.frame_ave_temp)
        self.ave_temp_text.setGeometry(QtCore.QRect(6, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("12")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ave_temp_text.setFont(font)
        self.ave_temp_text.setStyleSheet("background: transparent;\n"
"color: white;\n"
"font: 24pt bold;\n"
"")
        self.ave_temp_text.setObjectName("ave_temp_text")
        self.label = QtWidgets.QLabel(self.frame_ave_temp)
        self.label.setGeometry(QtCore.QRect(10, 10, 50, 4))
        self.label.setStyleSheet("background: orange;\n"
"height: 8pt")
        self.label.setText("")
        self.label.setObjectName("label")
        self.ave_temp_unit_text = QtWidgets.QPlainTextEdit(self.frame_ave_temp)
        self.ave_temp_unit_text.setGeometry(QtCore.QRect(80, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("12")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ave_temp_unit_text.setFont(font)
        self.ave_temp_unit_text.setStyleSheet("background: transparent;\n"
"color: white;\n"
"font: 12pt bold;\n"
"")
        self.ave_temp_unit_text.setObjectName("ave_temp_unit_text")
        self.frame_ave_temp_2 = QtWidgets.QFrame(self.centralWidget)
        self.frame_ave_temp_2.setGeometry(QtCore.QRect(400, 170, 110, 110))
        self.frame_ave_temp_2.setStyleSheet("background-color: rgba(255,255,255,30%);\n"
"")
        self.frame_ave_temp_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ave_temp_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ave_temp_2.setObjectName("frame_ave_temp_2")
        self.high_temp_label = QtWidgets.QLabel(self.frame_ave_temp_2)
        self.high_temp_label.setGeometry(QtCore.QRect(10, 20, 111, 41))
        self.high_temp_label.setStyleSheet("background: transparent;\n"
"font: \"Helvetica\";\n"
"color: white;")
        self.high_temp_label.setObjectName("high_temp_label")
        self.high_temp_text = QtWidgets.QPlainTextEdit(self.frame_ave_temp_2)
        self.high_temp_text.setGeometry(QtCore.QRect(6, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("12")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.high_temp_text.setFont(font)
        self.high_temp_text.setStyleSheet("background: transparent;\n"
"color: white;\n"
"font: 24pt bold;\n"
"")
        self.high_temp_text.setObjectName("high_temp_text")
        self.label_2 = QtWidgets.QLabel(self.frame_ave_temp_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 72, 4))
        self.label_2.setStyleSheet("background: lightblue;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.high_temp_unit_text = QtWidgets.QPlainTextEdit(self.frame_ave_temp_2)
        self.high_temp_unit_text.setGeometry(QtCore.QRect(80, 70, 31, 31))
        font = QtGui.QFont()
        font.setFamily("12")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.high_temp_unit_text.setFont(font)
        self.high_temp_unit_text.setStyleSheet("background: transparent;\n"
"color: white;\n"
"font: 12pt bold;\n"
"")
        self.high_temp_unit_text.setObjectName("high_temp_unit_text")
        self.frame_ave_temp_3 = QtWidgets.QFrame(self.centralWidget)
        self.frame_ave_temp_3.setGeometry(QtCore.QRect(400, 290, 110, 110))
        self.frame_ave_temp_3.setStyleSheet("background-color: rgba(255,255,255,30%);\n"
"")
        self.frame_ave_temp_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ave_temp_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ave_temp_3.setObjectName("frame_ave_temp_3")
        self.low_temp_label = QtWidgets.QLabel(self.frame_ave_temp_3)
        self.low_temp_label.setGeometry(QtCore.QRect(10, 20, 111, 41))
        self.low_temp_label.setStyleSheet("background: transparent;\n"
"font: \"Helvetica\";\n"
"color: white;")
        self.low_temp_label.setObjectName("low_temp_label")
        self.low_temp_text = QtWidgets.QPlainTextEdit(self.frame_ave_temp_3)
        self.low_temp_text.setGeometry(QtCore.QRect(6, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("12")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.low_temp_text.setFont(font)
        self.low_temp_text.setStyleSheet("background: transparent;\n"
"color: white;\n"
"font: 24pt bold;\n"
"")
        self.low_temp_text.setObjectName("low_temp_text")
        self.label_3 = QtWidgets.QLabel(self.frame_ave_temp_3)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 20, 4))
        self.label_3.setStyleSheet("background: lightgrey;\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.low_temp_unit_text = QtWidgets.QPlainTextEdit(self.frame_ave_temp_3)
        self.low_temp_unit_text.setGeometry(QtCore.QRect(80, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("12")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.low_temp_unit_text.setFont(font)
        self.low_temp_unit_text.setStyleSheet("background: transparent;\n"
"color: white;\n"
"font: 12pt bold;\n"
"")
        self.low_temp_unit_text.setObjectName("low_temp_unit_text")
        self.frame_ave_temp_6 = QtWidgets.QFrame(self.centralWidget)
        self.frame_ave_temp_6.setGeometry(QtCore.QRect(520, 290, 110, 110))
        self.frame_ave_temp_6.setStyleSheet("background-color: rgba(255,255,255,30%);\n"
"")
        self.frame_ave_temp_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ave_temp_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ave_temp_6.setObjectName("frame_ave_temp_6")
        self.low_hum_label = QtWidgets.QLabel(self.frame_ave_temp_6)
        self.low_hum_label.setGeometry(QtCore.QRect(10, 20, 111, 41))
        self.low_hum_label.setStyleSheet("background: transparent;\n"
"font: \"Helvetica\";\n"
"color: white;")
        self.low_hum_label.setObjectName("low_hum_label")
        self.low_hum_text = QtWidgets.QPlainTextEdit(self.frame_ave_temp_6)
        self.low_hum_text.setGeometry(QtCore.QRect(6, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("12")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.low_hum_text.setFont(font)
        self.low_hum_text.setStyleSheet("background: transparent;\n"
"color: white;\n"
"font: 24pt bold;\n"
"")
        self.low_hum_text.setObjectName("low_hum_text")
        self.label_6 = QtWidgets.QLabel(self.frame_ave_temp_6)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 20, 4))
        self.label_6.setStyleSheet("background: pink;\n"
"")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.low_hum_unit_text = QtWidgets.QPlainTextEdit(self.frame_ave_temp_6)
        self.low_hum_unit_text.setGeometry(QtCore.QRect(65, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("12")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.low_hum_unit_text.setFont(font)
        self.low_hum_unit_text.setStyleSheet("background: transparent;\n"
"color: white;\n"
"font: 12pt bold;\n"
"")
        self.low_hum_unit_text.setObjectName("low_hum_unit_text")
        self.frame_ave_temp_5 = QtWidgets.QFrame(self.centralWidget)
        self.frame_ave_temp_5.setGeometry(QtCore.QRect(520, 170, 110, 110))
        self.frame_ave_temp_5.setStyleSheet("background-color: rgba(255,255,255,30%);\n"
"")
        self.frame_ave_temp_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ave_temp_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ave_temp_5.setObjectName("frame_ave_temp_5")
        self.high_hum_label = QtWidgets.QLabel(self.frame_ave_temp_5)
        self.high_hum_label.setGeometry(QtCore.QRect(10, 20, 111, 41))
        self.high_hum_label.setStyleSheet("background: transparent;\n"
"font: \"Helvetica\";\n"
"color: white;")
        self.high_hum_label.setObjectName("high_hum_label")
        self.high_hum_text = QtWidgets.QPlainTextEdit(self.frame_ave_temp_5)
        self.high_hum_text.setGeometry(QtCore.QRect(6, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("12")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.high_hum_text.setFont(font)
        self.high_hum_text.setStyleSheet("background: transparent;\n"
"color: white;\n"
"font: 24pt bold;\n"
"")
        self.high_hum_text.setObjectName("high_hum_text")
        self.label_5 = QtWidgets.QLabel(self.frame_ave_temp_5)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 72, 4))
        self.label_5.setStyleSheet("background: green;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.high_hum_uni_text = QtWidgets.QPlainTextEdit(self.frame_ave_temp_5)
        self.high_hum_uni_text.setGeometry(QtCore.QRect(65, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("12")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.high_hum_uni_text.setFont(font)
        self.high_hum_uni_text.setStyleSheet("background: transparent;\n"
"color: white;\n"
"font: 12pt bold;\n"
"")
        self.high_hum_uni_text.setObjectName("high_hum_uni_text")
        self.frame_ave_temp_4 = QtWidgets.QFrame(self.centralWidget)
        self.frame_ave_temp_4.setGeometry(QtCore.QRect(520, 50, 110, 110))
        self.frame_ave_temp_4.setStyleSheet("background-color: rgba(255,255,255,30%);\n"
"")
        self.frame_ave_temp_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ave_temp_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ave_temp_4.setObjectName("frame_ave_temp_4")
        self.ave_hum_label = QtWidgets.QLabel(self.frame_ave_temp_4)
        self.ave_hum_label.setGeometry(QtCore.QRect(10, 20, 111, 41))
        self.ave_hum_label.setStyleSheet("background: transparent;\n"
"font: \"Helvetica\";\n"
"color: white;")
        self.ave_hum_label.setObjectName("ave_hum_label")
        self.ave_hum_text = QtWidgets.QPlainTextEdit(self.frame_ave_temp_4)
        self.ave_hum_text.setGeometry(QtCore.QRect(6, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("12")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ave_hum_text.setFont(font)
        self.ave_hum_text.setStyleSheet("background: transparent;\n"
"color: white;\n"
"font: 24pt bold;\n"
"")
        self.ave_hum_text.setObjectName("ave_hum_text")
        self.label_4 = QtWidgets.QLabel(self.frame_ave_temp_4)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 50, 4))
        self.label_4.setStyleSheet("background: darkblue;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.ave_hum_unit_text = QtWidgets.QPlainTextEdit(self.frame_ave_temp_4)
        self.ave_hum_unit_text.setGeometry(QtCore.QRect(65, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("12")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ave_hum_unit_text.setFont(font)
        self.ave_hum_unit_text.setStyleSheet("background: transparent;\n"
"color: white;\n"
"font: 12pt bold;\n"
"")
        self.ave_hum_unit_text.setObjectName("ave_hum_unit_text")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(30, 170, 351, 231))
        self.frame.setStyleSheet("background-color: rgba(255,255,255,30%);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.current_temperature_text = QtWidgets.QPlainTextEdit(self.frame)
        self.current_temperature_text.setGeometry(QtCore.QRect(90, 50, 171, 101))
        self.current_temperature_text.setStyleSheet("font: 60pt;\n"
"color: white;\n"
"background: transparent")
        self.current_temperature_text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.current_temperature_text.setObjectName("current_temperature_text")
        self.current_humidity_text = QtWidgets.QPlainTextEdit(self.frame)
        self.current_humidity_text.setGeometry(QtCore.QRect(90, 140, 141, 101))
        self.current_humidity_text.setStyleSheet("font: 60pt;\n"
"color: white;\n"
"background: transparent")
        self.current_humidity_text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.current_humidity_text.setObjectName("current_humidity_text")
        self.button_unit = QtWidgets.QPushButton(self.frame)
        self.button_unit.setGeometry(QtCore.QRect(250, 10, 91, 31))
        self.button_unit.setStyleSheet("background: rgba(70,25,255);\n"
"")
        self.button_unit.setCheckable(False)
        self.button_unit.setAutoDefault(True)
        self.button_unit.setDefault(False)
        self.button_unit.setFlat(False)
        self.button_unit.setObjectName("button_unit")
        self.current_temp_unit_text = QtWidgets.QPlainTextEdit(self.frame)
        self.current_temp_unit_text.setGeometry(QtCore.QRect(260, 80, 51, 41))
        font = QtGui.QFont()
        font.setFamily("12")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.current_temp_unit_text.setFont(font)
        self.current_temp_unit_text.setStyleSheet("background: transparent;\n"
"color: white;\n"
"font: 24pt bold;\n"
"")
        self.current_temp_unit_text.setObjectName("current_temp_unit_text")
        self.current_hum_unit_text = QtWidgets.QPlainTextEdit(self.frame)
        self.current_hum_unit_text.setGeometry(QtCore.QRect(260, 170, 51, 41))
        font = QtGui.QFont()
        font.setFamily("12")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.current_hum_unit_text.setFont(font)
        self.current_hum_unit_text.setStyleSheet("background: transparent;\n"
"color: white;\n"
"font: 24pt bold;\n"
"")
        self.current_hum_unit_text.setObjectName("current_hum_unit_text")
        self.temperature_icon = QtWidgets.QLabel(self.frame)
        self.temperature_icon.setGeometry(QtCore.QRect(15, 60, 60, 60))
        self.temperature_icon.setStyleSheet("background: transparent;")
        self.temperature_icon.setText("")
        self.temperature_icon.setPixmap(QtGui.QPixmap("../python_program_server/ui_img/thermometer.png"))
        self.temperature_icon.setObjectName("temperature_icon")
        self.humidity_icon = QtWidgets.QLabel(self.frame)
        self.humidity_icon.setGeometry(QtCore.QRect(15, 150, 60, 60))
        self.humidity_icon.setStyleSheet("background: transparent;")
        self.humidity_icon.setText("")
        self.humidity_icon.setPixmap(QtGui.QPixmap("../python_program_server/ui_img/drop.png"))
        self.humidity_icon.setObjectName("humidity_icon")
        self.plainTextEdit_location = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit_location.setGeometry(QtCore.QRect(20, 30, 291, 79))
        self.plainTextEdit_location.setStyleSheet("font: 50pt;\n"
"color: white;\n"
"background: transparent")
        self.plainTextEdit_location.setObjectName("plainTextEdit_location")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(20, 100, 201, 31))
        self.plainTextEdit_2.setStyleSheet("font: 14pt;\n"
"color: white;\n"
"background: transparent")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_Database = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit_Database.setGeometry(QtCore.QRect(170, 100, 111, 31))
        self.plainTextEdit_Database.setStyleSheet("font: 14pt;\n"
"color: green;\n"
"background: transparent")
        self.plainTextEdit_Database.setObjectName("plainTextEdit_Database")
        self.request_stamp_text = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.request_stamp_text.setGeometry(QtCore.QRect(30, 420, 431, 31))
        self.request_stamp_text.setStyleSheet("background: transparent;\n"
"font: 12pt;\n"
"color: lightgrey;")
        self.request_stamp_text.setObjectName("request_stamp_text")
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(20, 120, 201, 31))
        self.plainTextEdit_5.setStyleSheet("font: 14pt;\n"
"color: white;\n"
"background: transparent")
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.plainTextEdit_Server = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit_Server.setGeometry(QtCore.QRect(70, 120, 111, 31))
        self.plainTextEdit_Server.setStyleSheet("font: 14pt;\n"
"color: green;\n"
"background: transparent")
        self.plainTextEdit_Server.setObjectName("plainTextEdit_Server")
        self.frame_ave_temp.raise_()
        self.frame_ave_temp_2.raise_()
        self.frame_ave_temp_3.raise_()
        self.frame_ave_temp_6.raise_()
        self.frame_ave_temp_5.raise_()
        self.frame_ave_temp_4.raise_()
        self.frame.raise_()
        self.plainTextEdit_location.raise_()
        self.plainTextEdit_2.raise_()
        self.plainTextEdit_Database.raise_()
        self.request_stamp_text.raise_()
        self.plainTextEdit_5.raise_()
        self.plainTextEdit_Server.raise_()
        self.current_temperature_text.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        self.actionTemp = QtWidgets.QAction(MainWindow)
        self.actionTemp.setObjectName("actionTemp")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ave_temp_label.setText(_translate("MainWindow", "\n"
"<html><head/><body><p/><p>Average <br/>Temperature</p></body></html>"))
        self.ave_temp_text.setPlainText(_translate("MainWindow", "22.33\n"
""))
        self.ave_temp_unit_text.setPlainText(_translate("MainWindow", "°C"))
        self.high_temp_label.setText(_translate("MainWindow", "<html><head/><body><p>Highest <br/>Temperature</p></body></html>"))
        self.high_temp_text.setPlainText(_translate("MainWindow", "22.33\n"
""))
        self.high_temp_unit_text.setPlainText(_translate("MainWindow", "°C"))
        self.low_temp_label.setText(_translate("MainWindow", "<html><head/><body><p>Lowest <br/>Temperature</p></body></html>"))
        self.low_temp_text.setPlainText(_translate("MainWindow", "22.33\n"
""))
        self.low_temp_unit_text.setPlainText(_translate("MainWindow", "°C"))
        self.low_hum_label.setText(_translate("MainWindow", "<html><head/><body><p>Lowest <br/>Humidity</p></body></html>"))
        self.low_hum_text.setPlainText(_translate("MainWindow", "10.1\n"
""))
        self.low_hum_unit_text.setPlainText(_translate("MainWindow", "%"))
        self.high_hum_label.setText(_translate("MainWindow", "<html><head/><body><p>Highest <br/>Humidity</p></body></html>"))
        self.high_hum_text.setPlainText(_translate("MainWindow", "70.4\n"
""))
        self.high_hum_uni_text.setPlainText(_translate("MainWindow", "%"))
        self.ave_hum_label.setText(_translate("MainWindow", "<html><head/><body><p>Average <br/>Humidity</p></body></html>"))
        self.ave_hum_text.setPlainText(_translate("MainWindow", "35.3\n"
""))
        self.ave_hum_unit_text.setPlainText(_translate("MainWindow", "%"))
        self.current_temperature_text.setPlainText(_translate("MainWindow", "22.44"))
        self.current_humidity_text.setPlainText(_translate("MainWindow", "34.5"))
        self.button_unit.setText(_translate("MainWindow", "°C <-> °F"))
        self.current_temp_unit_text.setPlainText(_translate("MainWindow", "°C"))
        self.current_hum_unit_text.setPlainText(_translate("MainWindow", "%"))
        self.plainTextEdit_location.setPlainText(_translate("MainWindow", "Boulder, CO"))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", "Database Connection:"))
        self.plainTextEdit_Database.setPlainText(_translate("MainWindow", "CONNECTED"))
        self.request_stamp_text.setPlainText(_translate("MainWindow", "last request:"))
        self.plainTextEdit_5.setPlainText(_translate("MainWindow", "Server:"))
        self.plainTextEdit_Server.setPlainText(_translate("MainWindow", "RUNNING"))
        self.actionTemp.setText(_translate("MainWindow", "Temp"))

