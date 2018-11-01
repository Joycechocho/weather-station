from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
from ui_mainwindow import Ui_MainWindow
import helper
import datetime
import time
import json
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

    def __init__(self, client=None):
        self.aws_client = client
        self.status = 'Failed'
        self.current_temp = 0.0
        self.current_hum = 0.0
        self.old_temp = 0.0
        self.old_hum = 0.0
        self.ave_temp = 0.0
        self.ave_hum = 0.0
        self.high_temp = 0.0
        self.high_hum = 0.0
        self.low_temp = 0.0
        self.low_hum = 0.0
        self.temp_unit = 0
        self.average_temp_filter = []
        self.average_hum_filter = []
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.button_unit.clicked.connect(self.onClicked)

        while len(self.average_temp_filter) < 4:
            humidity = 15
            temperature = 22
            # humidity, temperature = Adafruit_DHT.read(22, 4)
            if humidity is not None and temperature is not None:
                self.current_temp += temperature
                self.current_hum += humidity
                self.average_temp_filter.append(temperature)
                self.average_hum_filter.append(humidity)
            time.sleep(2)
        self.current_temp = self.current_temp / 4
        self.current_hum = self.current_hum / 4
        self.old_temp = self.current_temp
        self.old_hum = self.current_hum
        self.ave_temp = self.current_temp
        self.ave_hum = self.current_hum
        self.high_temp = self.current_temp
        self.high_hum = self.current_hum
        self.low_temp = self.current_temp
        self.low_hum = self.current_hum
        self.plainTextEdit_Database.setPlainText('CONNECTED')

    def onClicked(self):
        self.temp_unit ^= 1
        # Update displayed data on the QT interface
        self.current_temperature_text.setPlainText(str("{:.2f}".format(self.current_temp * var1[self.temp_unit] + var2[self.temp_unit])))
        self.ave_temp_text.setPlainText(str("{:.2f}".format(self.ave_temp * var1[self.temp_unit] + var2[self.temp_unit])))
        self.high_temp_text.setPlainText(str("{:.2f}".format(self.high_temp * var1[self.temp_unit] + var2[self.temp_unit])))
        self.low_temp_text.setPlainText(str("{:.2f}".format(self.low_temp * var1[self.temp_unit] + var2[self.temp_unit])))

        self.current_temp_unit_text.setPlainText(unit[self.temp_unit])
        self.ave_temp_unit_text.setPlainText(unit[self.temp_unit])
        self.high_temp_unit_text.setPlainText(unit[self.temp_unit])
        self.low_temp_unit_text.setPlainText(unit[self.temp_unit])

    def Update(self):

        self.status = 'Failed'
        humidity = 15
        temperature = 22
        #humidity, temperature = Adafruit_DHT.read(22, 4)

        # Record sample time
        now = datetime.datetime.now()
        seconds_since_midnight = (now - midnight).seconds

        # Check for data validity
        if humidity is not None and temperature is not None and \
           abs(temperature - self.old_temp) < 3.0 and \
           abs(humidity - self.old_hum) < 3.0:
            self.current_temp = temperature
            self.current_hum = humidity
            # Get average/highest/lowest value
            self.ave_temp = helper.running_average(temperature, self.average_temp_filter)
            self.ave_hum = helper.running_average(humidity, self.average_hum_filter)
            if temperature > self.high_temp:
                self.high_temp = temperature
            elif temperature < self.low_temp:
                self.low_temp = temperature
            if humidity > self.high_hum:
                self.high_hum = humidity
            elif humidity < self.low_hum:
                self.low_hum = humidity
            self.old_temp = temperature
            self.old_hum = humidity
            self.status = 'Success'

            # Store data into the database
            helper.tinydb_write([seconds_since_midnight, temperature, humidity])

            # Display data on the QT interface
            self.current_temperature_text.setPlainText(str("{:.2f}".format(self.current_temp*var1[self.temp_unit]+var2[self.temp_unit])))
            self.current_humidity_text.setPlainText(str("{:.1f}".format(self.current_hum)))
            self.ave_temp_text.setPlainText(str("{:.2f}".format(self.ave_temp*var1[self.temp_unit]+var2[self.temp_unit])))
            self.ave_hum_text.setPlainText(str("{:.1f}".format(self.ave_hum)))
            self.high_temp_text.setPlainText(str("{:.2f}".format(self.high_temp*var1[self.temp_unit]+var2[self.temp_unit])))
            self.high_hum_text.setPlainText(str("{:.1f}".format(self.high_hum)))
            self.low_temp_text.setPlainText(str("{:.2f}".format(self.low_temp*var1[self.temp_unit]+var2[self.temp_unit])))
            self.low_hum_text.setPlainText(str("{:.1f}".format(self.low_hum)))

            # Publishing data to the cloud
            self.aws_client.publish(json.dumps({'time_stamp': seconds_since_midnight,
                                                'current_temperature': self.current_temp, 'average_temperature': self.ave_temp,
                                                'high_temperature': self.high_temp, 'low_temperature': self.low_temp,
                                                'current_humidity': self.current_hum, 'average_humidity': self.ave_hum,
                                                'high_humidity': self.high_hum, 'low_humidity': self.low_hum}))

        # Update data timestamp
        now = datetime.datetime.today()
        self.request_stamp_text.setPlainText('Last Update at ' + str(now)+ ': ' + self.status)
        # Start the timer again
        QtCore.QTimer.singleShot(5000, self.Update)