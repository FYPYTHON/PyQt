import tornado.web

from handlers.notify import NotifyHandler
from function.function import config
from utils.utils import log

import pika
from pika.adapters import tornado_connection

HANDLERS = [(r'/notify', NotifyHandler)]

class PikaClient():
    def __init__(self, io_loop):
        self.io_loop = io_loop
        self.connected = False
        self.connecting = False
        self.connection = None
        self.channel = None
        self.message_count = 9


    def connect(self):
        if self.connecting:
            return
        self.connecting = True
        cred = pika.PlainCredentials('guest', 'guest')
        param = pika.ConnectionParameters(host="10.xxx.xxx.75", credentials=cred)
        self.connection = tornado_connection.TornadoConnection(param, custom_ioloop = self.io_loop, on_open_callback = self.on_connected)
        self.connection.add_on_open_error_callback(self.err)
        self.connection.add_on_close_callback(self.on_closed)


    def err(self, conn):
        log('socket error', conn)
        pass


    def on_connected(self, conn):
        log('connected')
        self.connected = True
        self.connection = conn
        self.connection.channel(channel_number = 1, on_open_callback = self.on_channel_open)


    def on_message(self, channel, method, properties, body):
        log(body)
        print('body : ', body)
        pass


    def on_channel_open(self, channel):
        self.channel = channel
        channel.basic_consume(on_message_callback = self.on_message, queue='hello', auto_ack=True)
        return


    def on_closed(self, conn, c):
        log('pika close!')
        self.io_loop.stop()
        pass


def main():
    port = 3002
    is_debug = config('sys', 'debug')
    print('DEBUG', is_debug)
    app = tornado.web.Application(
            HANDLERS,
            debug = is_debug,
            )
    io_loop = tornado.ioloop.IOLoop.instance()
    app.pc = PikaClient(io_loop)
    app.pc.connect()
    http_server = tornado.httpserver.HTTPServer(app)
    app.listen(port)
    io_loop.start()
    print('listen {}'.format(port))


if __name__ == '__main__':
    main()