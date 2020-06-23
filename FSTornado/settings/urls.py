# coding=utf-8
from handlers.adminhd import verifyCode
from handlers.author import hd_login, hd_main, hd_manage
from handlers.show import hd_show, hd_play
from handlers.action import hd_fileload, hd_rename, hd_move, hd_create
from handlers.view import jijinhd as hd_jijin
from handlers.view import hd_predict
from tornado.web import StaticFileHandler
url = [                            #
        # (r'/', signin_handler.SigninHandler),
        (r'/login', hd_login.LoginHandler),
        (r'/logout', hd_login.LogoutHandler),
        (r'/manage', hd_manage.ManageHandler),
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
        (r'/restart', hd_manage.RestartHandler),

        # view
        (r'/view', hd_jijin.JiJinHandler),

        # -------- APP -------
        (r'/app/fsmain', hd_main.AppFSMainHandler),
        (r'/app/upload', hd_fileload.AppUploadHandler),
        (r'/app/rename', hd_rename.AppFsRenameHandler),
        (r'/app/view', hd_jijin.AppJiJinHandler),
        (r'/app/predict', hd_predict.AppJijinPredict),
]
