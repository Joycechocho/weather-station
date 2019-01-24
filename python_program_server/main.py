"""main.py: This is the main file for the interface program.

On the python command line, you could type
>>> import main
>>> help(main)
and it would print out this docstring.
"""

import sys
from PyQt5.QtWidgets import QApplication
import argparse
import websocket
import coap.py
import threading

from logindialog import LoginDialog
from mainwindow import MainWindow
from aws_helper import AWSIoTHandler
import helper


# Read in command-line parameters
parser = argparse.ArgumentParser()
parser.add_argument("-e", "--endpoint", action="store", required=True,
                    dest="host", help="Your AWS IoT custom endpoint")
parser.add_argument("-r", "--rootCA", action="store", required=True,
                    dest="rootCAPath", help="Root CA file path")
parser.add_argument("-c", "--cert", action="store", dest="certificatePath",
                    help="Certificate file path")
parser.add_argument("-k", "--key", action="store", dest="privateKeyPath",
                    help="Private key file path")
parser.add_argument("-w", "--websocket", action="store_true", dest="useWebsocket",
                    default=False, help="Use MQTT over WebSocket")
parser.add_argument("-id", "--clientId", action="store", dest="clientId",
                    default="basicPubSub", help="Targeted client id")
parser.add_argument("-t", "--topic", action="store", dest="topic",
                    default="sdk/test/Python", help="Targeted topic")


def protocol_test():
    coap.start_coap_test()
    websocket.start_websocket_test()


if __name__ == "__main__":
    a = QApplication(sys.argv)
    helper.dbConnect()
    
    loginDialog = LoginDialog()
    
    isAuth = False
    result = -1
    while not isAuth:
        result = loginDialog.exec_()
        if result == LoginDialog.Success or result == LoginDialog.Rejected:
            isAuth = True
        else:
            isAuth = False
    if result == LoginDialog.Success:
        ralphie = AWSIoTHandler(parser.parse_args())
        w = MainWindow(ralphie)
        w.show()
        w.Update()
        t = threading.Thread(target=protocol_test)
        t.start()
        a.exec_()
    sys.exit(-1)
