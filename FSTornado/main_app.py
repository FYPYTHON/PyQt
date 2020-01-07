# coding=utf-8
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.escape
from settings import urls
import tornado.options
import logging.config
from settings.logConfig import logConfig
import warnings
warnings.filterwarnings("ignore")
from tornado.options import define, options

define("port", default=9016, help="run on the given port", type=int)
logging.config.dictConfig(logConfig)
MAX_STREAMED_SIZE = 1024 * 1024 * 1024

def check_path_exist():
    if not os.path.exists("/opt/data"):
        os.makedirs('/opt/data')


class Application(tornado.web.Application):
    def __init__(self):

        settings = dict(
            template_path=(os.path.join(os.path.dirname(__file__), "templates")),
            static_path=(os.path.join(os.path.dirname(__file__), "static")),
            cookie_secret="f6d4f6de102f29b5cd37cd5eQtsdfsfdsdJ5/xJ89E=",
            session_secret="12f29b5c61c118ccd37cd5eQtsdfsfdsdJ5/xJ89E=",
            session_timeout=600,
            upload_path=os.path.join("/opt/data", "public"),
            top_path="/opt/data",
            login_url="/login",
            debug=False,
            # autoescape=None,
        )

        handlers = urls.url
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    # tornado.options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app, max_buffer_size=4 * MAX_STREAMED_SIZE)
    http_server.listen(options.port)
    # app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()



