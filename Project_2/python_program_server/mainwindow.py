from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
from ui_mainwindow import Ui_MainWindow
import helper
import datetime
import time
#import Adafruit_DHT

global midnight
midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

# Variable used for Degree Celsius to Fahrenheit conversion
var1 = [1, 1.8]
var2 = [0, 32]
unit = ['°C', '°F']
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
    initialized_flag = False
    status = 'Failed'
    current_temp = 0.0
    current_hum = 0.0
    old_temp = 0.0
    old_hum = 0.0
    ave_temp = 0.0
    ave_hum = 0.0
    high_temp = 0.0
    high_hum = 0.0
    low_temp = 0.0
    low_hum = 0.0
    temp_unit = 0
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.button_unit.clicked.connect(self.onClicked)

    def onClicked(self):
        MainWindow.temp_unit ^= 1
        # Update displayed data on the QT interface
        temp_display = str("{:.2f}".format(MainWindow.current_temp*var1[MainWindow.temp_unit]+var2[MainWindow.temp_unit]))
        hum_display = str("{:.1f}".format(MainWindow.current_hum))
        ave_temp_display = str("{:.2f}".format(MainWindow.ave_temp*var1[MainWindow.temp_unit]+var2[MainWindow.temp_unit]))
        ave_hum_display = str("{:.1f}".format(MainWindow.ave_hum))
        high_temp_display = str("{:.2f}".format(MainWindow.high_temp*var1[MainWindow.temp_unit]+var2[MainWindow.temp_unit]))
        high_hum_display = str("{:.1f}".format(MainWindow.high_hum))
        low_temp_display = str("{:.2f}".format(MainWindow.low_temp*var1[MainWindow.temp_unit]+var2[MainWindow.temp_unit]))
        low_hum_display = str("{:.1f}".format(MainWindow.low_hum))
        self.current_temperature_text.setPlainText(temp_display)
        self.current_humidity_text.setPlainText(hum_display)
        self.ave_temp_text.setPlainText(ave_temp_display)
        self.ave_hum_text.setPlainText(ave_hum_display)
        self.high_temp_text.setPlainText(high_temp_display)
        self.high_hum_text.setPlainText(high_hum_display)
        self.low_temp_text.setPlainText(low_temp_display)
        self.low_hum_text.setPlainText(low_hum_display)
        self.current_temp_unit_text.setPlainText(unit[MainWindow.temp_unit])
        self.ave_temp_unit_text.setPlainText(unit[MainWindow.temp_unit])
        self.high_temp_unit_text.setPlainText(unit[MainWindow.temp_unit])
        self.low_temp_unit_text.setPlainText(unit[MainWindow.temp_unit])

    def Update(self):

        # Device Initialization
        if MainWindow.initialized_flag == False:
            for i in range(1,3):
                humidity = 15
                temperature = 22
                #humidity, temperature = Adafruit_DHT.read(22, 4)
                if humidity is not None and temperature is not None:
                    MainWindow.current_temp += temperature
                    MainWindow.current_hum += humidity
                time.sleep(2)
            MainWindow.current_temp = MainWindow.current_temp / 2
            MainWindow.current_hum = MainWindow.current_hum /2
            MainWindow.old_temp = temperature
            MainWindow.old_hum = humidity
            MainWindow.ave_temp = temperature
            MainWindow.ave_hum = humidity
            MainWindow.high_temp = temperature
            MainWindow.high_hum =humidity
            MainWindow.low_temp = temperature
            MainWindow.low_hum = humidity
            MainWindow.initialized_flag = True
            self.plainTextEdit_Database.setPlainText('CONNECTED')

        # Regular device data update
        else:
            MainWindow.status = 'Failed'
            humidity = 15
            temperature = 22
            #humidity, temperature = Adafruit_DHT.read(22, 4)

            # Record sample time
            now = datetime.datetime.now()
            seconds_since_midnight = (now - midnight).seconds

            # Check for data validity
            if humidity is not None and temperature is not None and \
            abs(temperature - MainWindow.old_temp) < 3.0 and \
            abs(humidity - MainWindow.old_hum) < 3.0:
                MainWindow.current_temp = temperature
                MainWindow.current_hum = humidity
                # Get average/highest/lowest value
                MainWindow.ave_temp  = (MainWindow.ave_temp + temperature)/2
                MainWindow.ave_hum = (MainWindow.ave_hum + humidity) /2
                if temperature > MainWindow.high_temp:
                    MainWindow.high_temp = temperature
                elif temperature < MainWindow.low_temp:
                    MainWindow.low_temp = temperature
                if humidity > MainWindow.high_hum:
                    MainWindow.high_hum = humidity
                elif humidity < MainWindow.low_hum:
                    MainWindow.low_hum = humidity
                MainWindow.old_temp = temperature
                MainWindow.old_hum = humidity
                MainWindow.status = 'Success'

                # Store data into the database
                helper.tinydb_write([seconds_since_midnight, temperature, humidity])

        # Display data on the QT interface
        temp_display = str("{:.2f}".format(MainWindow.current_temp*var1[MainWindow.temp_unit]+var2[MainWindow.temp_unit]))
        hum_display = str("{:.1f}".format(MainWindow.current_hum))
        ave_temp_display = str("{:.2f}".format(MainWindow.ave_temp*var1[MainWindow.temp_unit]+var2[MainWindow.temp_unit]))
        ave_hum_display = str("{:.1f}".format(MainWindow.ave_hum))
        high_temp_display = str("{:.2f}".format(MainWindow.high_temp*var1[MainWindow.temp_unit]+var2[MainWindow.temp_unit]))
        high_hum_display = str("{:.1f}".format(MainWindow.high_hum))
        low_temp_display = str("{:.2f}".format(MainWindow.low_temp*var1[MainWindow.temp_unit]+var2[MainWindow.temp_unit]))
        low_hum_display = str("{:.1f}".format(MainWindow.low_hum))
        self.current_temperature_text.setPlainText(temp_display)
        self.current_humidity_text.setPlainText(hum_display)
        self.ave_temp_text.setPlainText(ave_temp_display)
        self.ave_hum_text.setPlainText(ave_hum_display)
        self.high_temp_text.setPlainText(high_temp_display)
        self.high_hum_text.setPlainText(high_hum_display)
        self.low_temp_text.setPlainText(low_temp_display)
        self.low_hum_text.setPlainText(low_hum_display)

        # Update data timestamp
        now = datetime.datetime.today()
        self.request_stamp_text.setPlainText('Last Update at ' + str(now)+ ': ' + MainWindow.status)
        # Start the timer again
        QtCore.QTimer.singleShot(5000, self.Update)
