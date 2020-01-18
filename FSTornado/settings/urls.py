# coding=utf-8
from handlers.adminhd import verifyCode
from handlers.author import hd_login, hd_main
from handlers.show import hd_show, hd_play
from handlers.action import hd_fileload, hd_rename, hd_move, hd_create
from tornado.web import StaticFileHandler
url = [                            #
        # (r'/', signin_handler.SigninHandler),
        (r'/login', hd_login.LoginHandler),
        (r'/logout', hd_login.LogoutHandler),
        (r'/fsmain', hd_main.FSMainHandler),
        # (r'/home', home_handler.HomeHandler),
        (r'/admin/verifyCode', verifyCode),
        # (r'/sendEmail/stmp',email_smtp_handler.SendEmailHandler),
        # (r'/sendEmail/exchange',email_exchange_handler.SendEmailHandler),
        (r'/show/(?P<filename>.*)', hd_show.FsShowHandler),
        (r'/play/(?P<filename>.*)', hd_play.FsPlayHandler),
        (r'/opt/data/(.*?)$', StaticFileHandler, {"path": "/opt/data"}),
        (r'/upload', hd_fileload.UploadHandler),
        (r'/download', hd_fileload.DownloadHandler),
        (r'/rename', hd_rename.FsRenameHandler),
        (r'/move', hd_move.FsMoveHandler),
        (r'/createdir', hd_create.FsCreateHandler),
]
