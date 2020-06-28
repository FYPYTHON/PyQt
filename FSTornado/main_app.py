# coding=utf-8
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.escape
from settings import urls
import tornado.options
import logging.config
from tornado.log import app_log as weblog
from settings.logConfig import logConfig
import warnings

from timedtask.timedget import clear_history

warnings.filterwarnings("ignore")
from tornado.options import define, options

define("port", default=9080, help="run on the given port", type=int)
logging.config.dictConfig(logConfig)
MAX_STREAMED_SIZE = 1024 * 1024 * 1024

def check_path_exist():
    if not os.path.exists("/opt/data"):
        os.makedirs('/opt/data')
    if not os.path.exists('/opt/log/fs'):
        os.makedirs('/opt/log/fs')


class Application(tornado.web.Application):
    def __init__(self):

        settings = dict(
            template_path=(os.path.join(os.path.dirname(__file__), "templates")),
            static_path=(os.path.join(os.path.dirname(__file__), "static")),
            cookie_secret="f6d4f6de102f29b5cd37cd5eQtsdfsfdsdJ5/xJ89E=",
            session_secret="12f29b5c61c118ccd37cd5eQtsdfsfdsdJ5/xJ89E=",
            session_timeout=300,   # seconds
            token_timeout=10,   # minutes
            days_clear=7,
            upload_path=os.path.join("/opt/data", "public"),
            top_path="/opt/data",
            login_url="/login",
            debug=False,
            autoescape=None,
            xheaders=True,
        )

        handlers = urls.url
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    import setproctitle
    try:
        setproctitle.setproctitle("tornadofs")     # set process name in linux environment
    except:
        pass
    check_path_exist()
    # tornado.options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app, max_buffer_size=4 * MAX_STREAMED_SIZE)
    http_server.listen(options.port)
    try:
        http_server.start(2)    # linux use mutli process
    except:
        pass
    # app.listen(options.port)
    # from timedtask.timedget import printLineFileFunc
    tornado.ioloop.PeriodicCallback(lambda: clear_history(app.settings.get("days_clear")), 1000 * 60 * 60).start()    # ms
    weblog.info("-- tornadofs server start .... pid:{} ".format(os.getpid()))
    tornado.ioloop.IOLoop.instance().start()



