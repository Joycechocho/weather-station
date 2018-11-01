from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
from ui_mainwindow import Ui_MainWindow
import pyqtgraph
import helper
import datetime
import numpy as np
#import Adafruit_DHT

global midnight
global temp_history
global time_history

today = datetime.date.today()
year = str(today.timetuple().tm_year)
month = str(today.timetuple().tm_mon)
day = str(today.timetuple().tm_mday)

data = np.genfromtxt('temperature_history_log/'+month+day+year+'.csv',delimiter=",")
time_history = list(data[:,0])
temp_history = list(data[:,1])
midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)



class MainWindow(QMainWindow, Ui_MainWindow):
    first_graph = True
    def __init__(self):
        pyqtgraph.setConfigOption('background', 'w')

        QMainWindow.__init__(self)
        self.setupUi(self)

        self.button_refresh.clicked.connect(self.onClicked)

    def onClicked(self):
        print('clicked')
        now = datetime.datetime.today()
        self.textEdit_Temp.setText('...')
        self.textEdit_Humidity.setText('...')
        humidity = 10
        temperature = 10
        #humidity, temperature = Adafruit_DHT.read(22,4)
        if humidity is not None and temperature is not None:
            if temperature>25.0:
                oImage = QImage("hot_day.jpg")
                palette = QPalette()
                palette.setBrush(10, QBrush(oImage))
                self.setPalette(palette)
            else:
                oImage = QImage("cloud.jpg")
                palette = QPalette()
                palette.setBrush(10, QBrush(oImage))
                self.setPalette(palette)
            
            temp = str("{:.2f}".format(temperature))
            hum = str("{:.1f}".format(humidity))
            self.textEdit_Temp.setText(temp)
            self.textEdit_Humidity.setText(hum)
            status = 'success'
        else:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle(_translate("LoginDialog", "refresh", None))
            msgBox.setText(_translate("LoginDialog", "Refresh too frequently, sensor is not ready!", None))
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            status = 'failed'
        self.textEdit_Request.setText('Last Request: '+str(now)+' '+status)

    def tempUpdate(self):
        temp = helper.getTemp()
        now = datetime.datetime.now()
        seconds_since_midnight = (now - midnight).seconds
        temp_history.append(int(temp[0]))
        time_history.append(int(seconds_since_midnight))
        if temp[0]>25.0:
            oImage = QImage("hot_day.jpg")
            palette = QPalette()
            palette.setBrush(10, QBrush(oImage))
            self.setPalette(palette)
        else:
            oImage = QImage("cloud.jpg")
            palette = QPalette()
            palette.setBrush(10, QBrush(oImage))
            self.setPalette(palette)
        self.textEdit_Temp.setText(str(temp[0]))
        self.textEdit_Humidity.setText(str(temp[1]))
        self.tempGraphUpdate(seconds_since_midnight, time_history, temp_history)
        QtCore.QTimer.singleShot(5000, self.tempUpdate)

    def tempGraphUpdate(self, x, time, temp):
        if MainWindow.first_graph:
            if x - 7200 < 0:
                self.graphicsView.plotItem.setRange(xRange=[0, x + 7200])
            elif x + 7200 > 86400:
                self.graphicsView.plotItem.setRange(xRange=[x-7200, 86400])
            else:
                self.graphicsView.plotItem.setRange(xRange=[x-7200, x+7200])
            self.graphicsView.plotItem.setRange(yRange=[temp[-1] - 15, temp[-1] + 15])
            MainWindow.first_graph = False

        self.graphicsView.plot(time, temp, pen=pyqtgraph.mkPen('b', width=3), clear=True)