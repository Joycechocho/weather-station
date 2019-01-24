from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from ui_logindialog import Ui_LoginDialog
from authorize import Auth

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class LoginDialog(QDialog, Ui_LoginDialog):
    Success,Failed,Rejected = range(0,3)
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.onAccept)
        self.buttonBox.rejected.connect(self.onReject)

    def onAccept(self):

        auth = Auth()
        if auth.doLogin(self.usernameLineEdit.text(), self.passwordLineEdit.text()):
            self.setResult(self.Success)
        else:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle(_translate("LoginDialog", "Pythonthusiast", None))
            msgBox.setText(_translate("LoginDialog", "Either incorrect username and/or password. Try again!", None))
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            self.setResult(self.Failed)

    def onReject(self):
        self.setResult(self.Rejected)
