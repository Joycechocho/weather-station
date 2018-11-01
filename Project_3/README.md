# ECEN5053-002 PROJECT_3 README
Developed by: ShuTing Guo, Joyce Cho

date: 11/12/2017

# Content
- Project Description and System Diagram
- Project Features
- File Organization
- Setup
- User Guide
- Reference Sources

# Project Description
With the goal in mind to get ourselves familiarized with websocket communication, building interface using HTML and continue to develop the QT interface on top of that in Project 2, we have developed a demo that consists of two python programs, a server and a client. The server periodically interacts with the DHT22 sensors and handles temperature/humidity data acquisition as well as storage. It has a QT interface that display temperature/humidity data. When starting the connection with AWS, the server send the temperature and humidity readings to AWS IoT via MQTT every 5 seconds. In AWS, a Lambda function is created to receive the incoming temperature and humidity message and perform data processing before putting the data on a FIFO queue using the Simple Queue Service (SQS) eventually. On the other hand, the client retrieves messages from the SQS Queue and is a webpage that allow users to access the temperature/humidity data remotely. It requests the data from the server via a websocket developed using [Tornado][t1]. Below is the system diagram:
![Image 3](https://github.com/Embedded-Phelps/ECEN5053_002/blob/master/Projects/Project_3/pictures/system_diagram.png)

# Project Features
##### 1. MQTT/AWS Lambda function Implementation - Server

##### 2. AWS SDK for Javascript on SQS Queue - Client
Amazon Simple Queue Service (SQS) is a fast, reliable, scalable, fully managed message queuing service. Before retrieving the messages in the queue, few more steps are implemented such as "Configure the SDK for JavaScript" and "Getting the URL for a Queue" in Javascript. AWS also provdes SDK for Javacript that can deal with the receive_message. We are using sqs.deleteMessages API to delete the messages that have been read to prevent the redundant message reading. 


##### 3. A Server-Client Websocket Implementation

The python program that directly interacts with the sensor serves as a server running on raspberry pi, constantly reading temperature/humidity values periodically (every 5 seconds) and storing the data. On the other hand, another computer that acts as a client, used to send the request to the server to retrieve temperature/humidity data for display.

##### 4. A Client Login Interface with Cookie Authentication.

Cookies were designed to be a reliable mechanism for websites to remember stateful information or to record the user's browsing activity. Authentication cookies are the most common method used by web servers to know whether the user is logged in or not, and which account they are logged in with. Here, we implemented cookie authentication to check if user's credential is valid or not. If the user visit /index page without login or cookie stored before, he/she will be redirected to /login page to sign in with the username and password. On the contray, if the user have the cookie stored on the browser before, he/she will visit the main page without needing to login again.

##### 5. A Continuous Graph of Temperature/Humidity data with multiple lines

An open souce HTML5 chart project is implemented to display the graph of the temperature/humidity data since the websocket connection to the server is opened.

##### 6. Robust Error Handling (***)

A run-time error takes place during the execution of a program and usually happens because of adverse system parameters or invalid input data. We have implemented the Exception Handling(Try Catch) in our client webpage. The try block contains set of statements where an exception can occur, while a catch block is where you handle the exceptions. For example, if there's no data in the queue and users are attempting to request data, there will be an alert popping out.

Considering the nature of FIFO, in the lambda function, it checks for the current available number of messages in the Queue. If the number reaches 15, it will delete one oldest message in the queue before writing a new message to it. This way it keeps the number of messages in the queue to be 15 and thus make sure that when the client pulls data from the queue, it always gets the most recent data.

##### 7. Beautiful and Intuitive User Interface (***)

Bootstrap is used in our porject because it includes a powerful mobile-first flexbox grid system for building layouts of all shapes and sizes. It is a front-end web framework that was originally created by developers at Twitter to provide consistency across their internal tools. Today, it’s available to everyone through GitHub as a free and open-source collection of tools containing HTML- and CSS-based design templates and JavaScript (JS) extensions.

In the Server side UI, HTML5 is integrated in the module stylesheet to facilitate the development and enhance the beauty of its presentation.

# Files Organization
* [python_program_client/] - client side python program
* [python_program_server/] - server side python program

# Setup
Hardware:
* The setup tutorial of the Raspberry Pi can be found [here][s2]
* The wiring of the DHT22 sensor to Raspberry Pi can be found [here][s1]

The server-side software requires the installation of the packages listed below:

| Packages | Source |
| ------ | ------ |
| Python 3.6 | https://liftcodeplay.com/2017/06/30/how-to-install-python-3-6-on-raspbian-linux-for-raspberry-pi/
| sip 4.19.4+ | https://riverbankcomputing.com/software/sip/download
| PyQt5 | https://riverbankcomputing.com/software/pyqt/download5
| AWSIoTPythonSDK | https://pypi.python.org/pypi/AWSIoTPythonSDK/1.0.0
| Tinydb | http://tinydb.readthedocs.io |

# User Guide
### Server Side
The execution of the server program requires some additional authentification files for AWS connection and interaction, and multiple long command lines are needed to run the program. Thus a script is developed to smooth the process:
```sh
$ cd python_program_server/
$ ./start.sh
```
![Image 3](https://github.com/Embedded-Phelps/ECEN5053_002/blob/master/Projects/Project_2/pictures/server_interface.png)
### Client Side
##### After setting up the hardware, go to [python_program_client/] and execute the client program,
```sh
$ cd python_program_client/
$ python client.py
```


##### Visit localhost:9888/index

![Image 3](https://github.com/Embedded-Phelps/ECEN5053_002/blob/master/Projects/Project_3/pictures/main_page.png)

Detailed features on the graphical display:
![Image 3](https://github.com/Embedded-Phelps/ECEN5053_002/blob/master/Projects/Project_3/pictures/point_display.png)

If it is your first time to visit the main page, you will be redirected to localhost:9888/login for asking the username and password. Once your are signed in with a the correct credential, the cookie will be stored and reused in next time when you visit.

![Image 3](https://github.com/Embedded-Phelps/ECEN5053_002/blob/master/Projects/Project_2/pictures/login_page.png)

Error handling when the number of messages in the queue is sufficient:

![Image 3](https://github.com/Embedded-Phelps/ECEN5053_002/blob/master/Projects/Project_3/pictures/error_handle.png)

 Reference Sources
* [Chart js: Open source HTML5 Charts for your website][rs1]
* [Amazon Simple Queue Service (SQS)][rs2]
* [Class: AWS.SQS — AWS SDK for JavaScript][rs3]


[rs1]:https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwiysbWF5oTXAhUG5YMKHUQWBlkQFggnMAA&url=http%3A%2F%2Fwww.chartjs.org%2F&usg=AOvVaw2iuT1ijbo1ACXx1QYv3q-r
[rs2]:https://aws.amazon.com/tw/sqs/
[rs3]:http://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/SQS.html
[t1]:http://www.tornadoweb.org/en/stable/
[python_program_client/]:https://github.com/Embedded-Phelps/ECEN5053_002/tree/master/Projects/Project_2/python_program_client
[python_program_server/]:https://github.com/Embedded-Phelps/ECEN5053_002/tree/master/Projects/Project_2/python_program_server
[database_login/]:https://github.com/Embedded-Phelps/ECEN5053_002/tree/master/Projects/Project_2/database_login
[s1]:https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/software-install-updated
[s2]:https://www.raspberrypi.org/help/
