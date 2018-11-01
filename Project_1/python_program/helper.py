
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import numpy as np

def dbConnect():
    db = QSqlDatabase.addDatabase("QSQLITE")
    filename = "project1.db"
    database =  QFile(filename)
    if not database.exists():
        qDebug("Database not found. Creating and opening")
        db.setDatabaseName(filename)
        db.open()
        query = QSqlQuery()
        query.exec_("create table qtapp_users "
                    "(id integer primary key autoincrement, "
                    "username varchar(30), "
                    "password varchar(255))")
        query.prepare("insert into qtapp_users(username, password) values(:username, :password)")
        query.bindValue(":username", "eko")
        query.bindValue(":password", computeHash("password"))
        query.exec_()
    else:
        qDebug("Database found. Opening")
        db.setDatabaseName(filename)
        db.open()
    return db.isOpen()
 
def computeHash(original):
    return QCryptographicHash.hash(original.encode('utf-8'), QCryptographicHash.Md5).toHex()


def getTemp():
    # Get new temp data
    data = np.genfromtxt('temperature_history_log/temp.csv',delimiter=",")

    return data