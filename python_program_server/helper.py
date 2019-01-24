
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from tinydb import TinyDB, Query
import datetime

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

def tinydb_create_db(name):
    db = TinyDB(name)
    return db

def tinydb_write(data):
    month, day, year = getdate()
    db = TinyDB('databases/'+str(month)+str(day)+str(year)+'.json')
    return db.insert({'time':data[0],'temperature':data[1],'humidity':data[2]})

def extract_historydata():
    packet={}
    month, day, year = getdate()
    db = TinyDB('databases/' + str(month) + str(day) + str(year) + '.json')
    temp = Query()
    current_time = datetime.datetime.now().hour
    for i in range(1, current_time+1):
        temperature = db.search(i*3600-20<temp.time<i*3600+20)
        packet[str(i)] = temperature[0]
    print(packet)
    return packet


def getdate():
    today = datetime.date.today()
    year = str(today.timetuple().tm_year)
    month = str(today.timetuple().tm_mon)
    day = str(today.timetuple().tm_mday)
    return [month, day, year]


def running_average(new_data, filter):
    filter.pop(0)
    filter.append(new_data)
    return sum(filter)/len(filter)