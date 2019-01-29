# EN5053-002 Embedded Interface Design
Developed by: ShuTing Guo, Joyce Cho

date: 12/10/2017

# Content
- Project Description and System Diagram
- Project Features
- File Organization
- Setup
- User Guide
- Reference Sources

# Project Description
With the goal in mind to get ourselves familiarized with communication on different protocols and continue to develop the QT interface, we have developed a demo that consists of two python programs, a server and a client. The server periodically interacts with the DHT22 sensors and handles temperature/humidity data acquisition as well as storage. It has a QT interface that display temperature/humidity data. When starting the connection with AWS, the server send the temperature and humidity readings to AWS IoT via MQTT every 5 seconds. In AWS, a Lambda function is created to receive the incoming temperature and humidity message and perform data processing before putting the data on a FIFO queue using the Simple Queue Service (SQS) eventually. On the other hand, the client retrieves messages from the SQS Queue and running a webpage that allows users to access the temperature/humidity data remotely. Moreover, after getting messages from Amazon Web Services, client would set up four protocols and communicate with sever back and forth. We provide a web interface to present the analysis between below 4 message protocols:

- MQTT
- COAP
- WebSocket 
- AMQP

Below is the system diagram:
![Image 3](https://github.com/Joycechocho/weather-station/blob/master/pictures/system_diagram.png)

# Project Features
#### 1. MQTT/AWS Lambda function Implementation - Server
#### 2. AWS SDK for Javascript on SQS Queue - Client
Amazon Simple Queue Service (SQS) is a fast, reliable, scalable, fully managed message queuing service. Before retrieving the messages in the queue, few more steps are implemented such as "Configure the SDK for JavaScript" and "Getting the URL for a Queue" in Javascript. AWS also provdes SDK for Javacript that can deal with the receive_message. We are using sqs.deleteMessages API to delete the messages that have been read to prevent the redundant message reading. 

#### 3. A Server-Client Websocket Implementation
#### 4. A Server-Client MQTT Implementation
#### 5. A Server-Client CAOP Implementation
#### 6. A Server-Client AMQP Implementation
#### 7. A Continuous Graph of Temperature/Humidity data with multiple lines
An open souce chart project is implemented to display the graph of the temperature/humidity data after the websocket connection is initiallized.

![Image 3](https://github.com/Joycechocho/weather-station/blob/master/pictures/line%20chart.png)

#### 8. A Bar Chart support multiple data input

![Image 3](https://github.com/Joycechocho/weather-station/blob/master/pictures/bar%20chart.png)

#### 9. Flask framework Implementation (***)
Flask is a micro web framework written in Python and based on the Werkzeug toolkit and Jinja2 template engine. It is implemented in this project in order to call python backend from Javascript frontend. 

#### 10. Beautiful and Intuitive User Interface 
Bootstrap is used in this project. It includes a powerful mobile-first flexbox grid system for building layouts of all shapes and sizes. It is a front-end web framework that was originally created by developers at Twitter to provide consistency across their internal tools. Today, it’s available to everyone through GitHub as a free and open-source collection of tools containing HTML and CSS-based design templates and JavaScript (JS) extensions.


#### 11. Logging Interface Easy for Debugging (***)

![Image 3](https://github.com/Joycechocho/weather-station/blob/master/pictures/log.png)

In the server side UI, HTML5 is integrated in the module stylesheet to facilitate the development and enhance the beauty of its presentation.

# Setup
Hardware:
* The setup tutorial of the Raspberry Pi can be found [here][s2]
* The wiring of DHT22 sensor to Raspberry Pi can be found [here][s1]

The server-side software requires the installation of the packages listed below:

| Packages | Source |
| ------ | ------ |
| Python 3.6 | https://liftcodeplay.com/2017/06/30/how-to-install-python-3-6-on-raspbian-linux-for-raspberry-pi/
| sip 4.19.4+ | https://riverbankcomputing.com/software/sip/download
| PyQt5 | https://riverbankcomputing.com/software/pyqt/download5
| AWSIoTPythonSDK | https://pypi.python.org/pypi/AWSIoTPythonSDK/1.0.0
| paho-mqtt | https://www.eclipse.org/paho/clients/python/docs/
| tornado | http://www.tornadoweb.org/en/stable/
| aiocoap | http://aiocoap.readthedocs.io/en/latest/index.html
| pika | https://pika.readthedocs.io/en/0.10.0/
| rabbitmq | http://blog.abarbanell.de/raspberry/2015/06/06/making-of-benchmarking-rabbitmq-on-raspberry/
| mosquitto | http://www.switchdoc.com/2016/02/tutorial-installing-and-testing-mosquitto-mqtt-on-raspberry-pi/

Note:
1. In order to install the rabbitmq, below should be done first:
add the following line in /etc/apt/sources.list/:
deb http://archive.raspbian.org/raspbian jessie main contrib non-free rpi

2. config files for rabbitmq and mosquitto files can be found in: /etc/rabbitmq/ and /etc/mosquitto
3. Stop both mosquitto and rabbitmq-server running as background service by default:
sudo /etc/init.d/rabbitmq-server stop
sudo /etc/init.d/mosquitto stop

# User Guide
### Server Side
The execution of the server program requires some additional authentication files for AWS connection and interaction. Multiple command lines are needed to run the program. Thus a script is developed to smooth the process:
```sh
$ cd python_program_server/
$ ./start.sh
```
![Image 3](https://github.com/Joycechocho/weather-station/blob/master/Project_2/pictures/server_interface.png)
### Client Side
##### After setting up the hardware, go to [python_program_client/] and execute the client program,
```sh
$ cd python_program_client/
$ python web.py
```
##### The data for temperature/humidity and result for protocols would be shown on the main page. 
![Image 3](https://github.com/Joycechocho/weather-station/blob/master/pictures/data%20display.png)
![Image 3](https://github.com/Joycechocho/weather-station/blob/master/pictures/protocol%20test.png)

Reference Sources
* [Chart js: Open source HTML5 Charts for your website][rs1]
* [Amazon Simple Queue Service (SQS)][rs2]
* [Class: AWS.SQS — AWS SDK for JavaScript][rs3]
* [Flask Web Framework][rs4]


[rs1]:https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwiysbWF5oTXAhUG5YMKHUQWBlkQFggnMAA&url=http%3A%2F%2Fwww.chartjs.org%2F&usg=AOvVaw2iuT1ijbo1ACXx1QYv3q-r
[rs2]:https://aws.amazon.com/tw/sqs/
[rs3]:http://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/SQS.html
[rs4]:http://flask.pocoo.org/
[t1]:http://www.tornadoweb.org/en/stable/
[python_program_client/]:https://github.com/Embedded-Phelps/ECEN5053_002/tree/master/Projects/Project_2/python_program_client
[python_program_server/]:https://github.com/Embedded-Phelps/ECEN5053_002/tree/master/Projects/Project_2/python_program_server
[database_login/]:https://github.com/Embedded-Phelps/ECEN5053_002/tree/master/Projects/Project_2/database_login
[s1]:https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/software-install-updated
[s2]:https://www.raspberrypi.org/help/
