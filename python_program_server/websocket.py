import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import mqtt
import time

global n
n = 0

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print('new connection')

    def on_message(self, message):
        global n
        n += 1
        print('message received:  %s' % message)
        self.write_message(message)
        if n == 3:
            n = 0
            time.sleep(1)
            tornado.ioloop.IOLoop.instance().stop()
            # print('Websocket connection closed')
            # mqtt.start_mqtt_test()


    def on_close(self):
        print('connection closed')

    def check_origin(self, origin):
        return True


application = tornado.web.Application([(r'/ws', WSHandler)])


def start_websocket_test():
    print('start websocket test')
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    # my_ip = socket.gethostbyname(socket.gethostname())
    # print('*** Websocket Server Started at %s***' % my_ip)
    tornado.ioloop.IOLoop.instance().start()
    http_server.stop()
    print('Websocket connection closed')
    mqtt.start_mqtt_test()
