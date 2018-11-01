"""main.py: This is the main file for the interface program.

On the python command line, you could type
>>> import main
>>> help(main)
and it would print out this docstring.
"""

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
import threading

from logindialog import LoginDialog
from mainwindow import MainWindow
import helper
import server

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
        w = MainWindow()
        w.show()
        w.Update()
        threading.Timer(1, server.start_server).start()
        a.exec_()

    sys.exit(-1)
