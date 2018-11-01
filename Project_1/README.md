# ECEN5053-002 PROJECT_1 README
Developed by: ShuTing Guo
date: 10/02/2017
# Content
- Project Description and System Diagram
- Project Features
- File Organization
- Setup
- User Guide
- Reference Sources

# Project Description
With the goal in mind to get myself familiarized with Qt5 and Python 3.x on Raspberry Pi, I have developed a demo that consists of two python programs. One periodically interacts with the DHT22 sensors and handles temperature/humidity data acquisition as well as storage (The tutorial of using Python on Raspberry Pi to work with DHT22 sensor is available [here on Adafruit][s1]). The other is built based on PyQt5 that provides users with an intuitive interface to see the current temperature and humidity data, temperature history and to request a new sensor read. The system is as the below diagram shows:

![Image 2](https://github.com/Embedded-Phelps/ECEN5053_002/blob/master/Projects/Project_1/pictures/System_diagram.png?raw=true)

# Project Features
##### 1. A Server-Client Architecture
The python program that directly interacts with the sensor serves as a server running in the background, constantly reading temperature/humidity values periodically (every 10 seconds) and storing the data. The interface program acts as a client, whenever started, would pull all the temperature data from the current date and plot them in a graph against time; It would also acquire the most recent temperature/humidity data for display, every 10 seconds or whenever requested by users. Such an architecture saves power (only runs the interface when needed) while maintains a complete data record.

##### 2. A Login interface for User Authentication Using Database Support
A very frequent scenario used in an application is that: before entering the main window, users must first authenticate themselves. This is implemented in this demo with database support, in this case, the postgreSQL. A database storing user's’ credentials is created using postgreSQL. Whenever a user want to access the main window, the credential s(he) enters will be compared with that in the database and s(he) will be granted access only when they match.

##### 3. A Real-time Graph of Temperature Over Time
A graph of the temperature record since the start of the current date is displayed on the interface when the program is run, and the graph will update in real time.

##### 4. Robust Error Handling
The DHT22 sensor is slow and the every reading requires a interval of at least two seconds. The program takes into account when the periodic action of reading data collides with the user’s request for reading update to avoid reading bad data or causing program crash: It will pop out a warning window reminding the sensor is not ready.

##### 5. Unittest Framework for Functionality Testing
A unit test program is also developed for the testing of some of the key utility functionalities of the program including: connecting to database, encryption, user credential authentication and sensor reading. 

# Files Organization
* [python_program/] - two python programs and a unittest program
* [Qt_Creator_Project_1] - Files created by the QT Creator
* [database/] - the postgreSQL database for user credentail authentication

# Setup
Hardware:
* The setup tutorial of the Raspberry Pi can be found [here][s2]
* The wiring of the DHT22 sensor to Raspberry Pi can be found [here][s1]

The software requires the installation of the packages listed below:

| Packages | Source |
| ------ | ------ |
| Python 3.6 | https://liftcodeplay.com/2017/06/30/how-to-install-python-3-6-on-raspbian-linux-for-raspberry-pi/
| sip 4.19.4+ | https://riverbankcomputing.com/software/sip/download
| PyQt5 | https://riverbankcomputing.com/software/pyqt/download5
| pyqtgraph | www.pyqtgraph.org
| Numpy | https://sourceforge.net/projects/numpy/files/ |

# User Guide
After setting up the hardware, go to [python_program/] and execute the server program first,
```sh
$ cd python_program/
$ python3.6 raspberry_temp.py
```
This runs the server program to start sampling the DHT sensor in the background. Then do,
```sh
$ python3.6 main.py
```
This will start the client program. But before the main window interface can show up, you need to login first with this credential:
>Username : eko
>Password : password

The login window looks like the pircture below. With the wrong credential, an error message would show up to ask you to try again:

![Image 2](https://github.com/Embedded-Phelps/ECEN5053_002/blob/master/Projects/Project_1/pictures/login.png?raw=true)

![Image 2](https://github.com/Embedded-Phelps/ECEN5053_002/blob/master/Projects/Project_1/pictures/login_error.png?raw=true)

After successful login, the main window would show up with the updated temperature and humidity value along with a temperature history graph:

![Image 3](https://github.com/Embedded-Phelps/ECEN5053_002/blob/master/Projects/Project_1/pictures/mainwindow.png?raw=true)

You can request a sensor read by clicked the **Refresh** button. But you should note that since the sensor is very slow and every reading requires a 2s interval at least, if you request too frequent, the program would pop up an warning for you to try again a bit later:

![Image 3](https://github.com/Embedded-Phelps/ECEN5053_002/blob/master/Projects/Project_1/pictures/request_error.png?raw=true)

If the temperature goes up above 35 degree C, the interface would look like this:

![Image 4](https://github.com/Embedded-Phelps/ECEN5053_002/blob/master/Projects/Project_1/pictures/hot_day_window.png?raw=true)

# Reference Sources
* [PyQt5 Reference Guide][rs1]
* [DHT Humidity Sensing on Raspberry Pi or Beaglebone Black with GDocs Logging][s1]
* [Raspberry Pi Documentation][s2]
* [Pyqtgraph Documentation][rs2]
* [Developing Cross Platform Application using Qt, PyQt and PySide][rs3]
* [Live Data in PyQt4 with PlotWidget][rs4]

[s1]:https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/software-install-updated
[s2]:https://www.raspberrypi.org/help/
[python_program/]:https://github.com/Embedded-Phelps/ECEN5053_002/tree/master/Projects/Project_1/python_program 
[database/]:https://github.com/Embedded-Phelps/ECEN5053_002/tree/master/Projects/Project_1/database/project1_database
[Qt_Creator_Project_1]:https://github.com/Embedded-Phelps/ECEN5053_002/tree/master/Projects/Project_1/Qt_Creator_Project_1
[rs1]:http://pyqt.sourceforge.net/Docs/PyQt5/
[rs2]:http://www.pyqtgraph.org/documentation/
[rs3]:http://pythonthusiast.pythonblogs.com/230_pythonthusiast/categories/426_qt_pyqt_and_pyside_tutorial.html
[rs4]:https://www.swharden.com/wp/2016-07-31-live-data-in-pyqt4-with-plotwidget/