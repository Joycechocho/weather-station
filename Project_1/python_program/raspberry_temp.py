import datetime
import csv
import threading
import Adafruit_DHT

TEMP_SENSOR = 22
TEMP_PIN = 4

global old_temp
global old_hum
old_temp = 0
old_hum = 0
def temp_update(data):
    csv_file = open('temperature_history_log/temp.csv','w+', newline='')
    writer = csv.writer(csv_file, delimiter = ',')
    writer.writerow(data)
    csv_file.close()

def temp_log(data):
    locked = True
    year = datetime.date.today().timetuple().tm_year
    month = datetime.date.today().timetuple().tm_mon
    day = datetime.date.today().timetuple().tm_mday
    date = str(month)+str(day)+str(year)
    #with open('temperature_history_log/'+ date + '.csv', "a", newline='') as csv_file:
    while locked:
        csv_file = open('temperature_history_log/'+date+'.csv', "a", newline='') 
        if csv_file:
            locked = False
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(data)
    csv_file.close()

def task():
    global old_temp
    global old_hum
    humidity, temperature = Adafruit_DHT.read(TEMP_SENSOR, TEMP_PIN)
    if humidity is not None and temperature is not None:
        if abs(old_temp - temperature)<5 and abs(old_hum - humidity)<5:
            old_temp = temperature
            old_hum = humidity
            midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            seconds_since_midnight = (datetime.datetime.now() - midnight).seconds
            temperature = float("{:.2f}".format(temperature))
            humidity = float("{:.1f}".format(humidity))
            data = [seconds_since_midnight,temperature,humidity]
            temp_update([temperature, humidity])
            temp_log(data)
            print('running')
    threading.Timer(5,task).start()

while True:
    humidity, temperature = Adafruit_DHT.read(TEMP_SENSOR, TEMP_PIN)
    if humidity is not None and temperature is not None:
        old_temp = temperature
        old_hum = humidity
        threading.Timer(5, task).start()
        input()
