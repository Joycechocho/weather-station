import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import helper

from mainwindow import MainWindow

UPDATE_REQUEST = 0
AVE_TEMP_REQUEST = 1
HIGH_TEMP_REQUEST = 2
LOW_TEMP_REQUEST = 3
AVE_HUM_REQUEST = 4
HIGH_HUM_REQUEST = 5
LOW_HUM_REQUEST = 6
REFRESH = 7

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print('new connection')

    def on_message(self, message):
        print('message received:  %s' % message)
        # Handling message
        if message == str(UPDATE_REQUEST):
            #MainWindow.update()
            packet = {'current_temperature':MainWindow.current_temp, 'current_humidity': MainWindow.current_hum}
            self.write_message(packet)
        elif message == str(AVE_TEMP_REQUEST):
            packet = {'average_temperature':MainWindow.ave_temp}
            self.write_message(packet)
        elif message == str(HIGH_TEMP_REQUEST):
            packet = {'high_temperature': MainWindow.high_temp}
            self.write_message(packet)
        elif message == str(LOW_TEMP_REQUEST):
            packet = {'low_temperature': MainWindow.low_temp}
            self.write_message(packet)
        elif message == str(AVE_HUM_REQUEST):
            packet = {'average_humidity': MainWindow.ave_hum}
            self.write_message(packet)
        elif message == str(HIGH_HUM_REQUEST):
            packet = {'high_humidity': MainWindow.high_hum}
            self.write_message(packet)
        elif message == str(LOW_HUM_REQUEST):
            packet = {'low_humidity': MainWindow.low_hum}
            self.write_message(packet)
        elif message == str(REFRESH):
            packet =helper.extract_historydata()
            self.write_message(packet)
        else:
            self.write_message('unknown')

    def on_close(self):
        print('connection closed')

    def check_origin(self, origin):
        return True


application = tornado.web.Application([(r'/ws', WSHandler)])


def start_server():
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    # my_ip = socket.gethostbyname(socket.gethostname())
    # print('*** Websocket Server Started at %s***' % my_ip)
    #main.w.plainTextEdit_Server.setPlainText('RUNNING')
    tornado.ioloop.IOLoop.instance().start()
