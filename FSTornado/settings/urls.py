# coding=utf-8
from handlers.adminhd import verifyCode, AppVersionHandler, UserinfoHandler, StatusHandler, DecodeSelfHandler
from handlers.author import hd_login, hd_main, hd_manage, hd_mail
from handlers.author.hd_manage import AppCodeHandler, CodeAddHandler
from handlers.show import hd_show, hd_play, hd_history, hd_dbinfo
from handlers.action import hd_fileload, hd_rename, hd_move, hd_create, hd_delete, hd_avator
from handlers.study import hd_poetry, hd_alticle, hd_word
from handlers.study.hd_word import WordActionHandler
from handlers.view import hd_jijin as hd_jijin, hd_image, hd_jsum, hd_sma
# from handlers.view import hd_predict
from tornado.web import StaticFileHandler
path_regex = r"(?P<path>(?:(?:/[^/]+)+|/?))"
url = [                            #
        # vue.js get resource
        # (r'^home/js/(?P<filename>.*\.js)$', myjs, name='myjs'),  # 与html中引入的href src一致
        # (r'^home/css/(?P<filename>.*\.css)$', mycss, name='mycss'),
        #
        (r'/status', StatusHandler),
        (r'/decode', DecodeSelfHandler),
        (r'/decode/([0-9]+)', DecodeSelfHandler),
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
        (r'/delete', hd_delete.FsDeleteHandler),
        (r'/createdir', hd_create.FsCreateHandler),
        (r'/restart', hd_manage.RestartHandler),
        (r'/user/([0-9]+)', hd_manage.UserInfoHandler),
        (r'/user/delete/([0-9]+)', hd_manage.ManageHandler),
        (r'/avator', hd_avator.FsAvatorHandler),
        (r'/history', hd_history.HistoryHandler),
        (r'/sendmail', hd_mail.EmainHandler),
        (r'/image', hd_image.ShowImageHandler),

        # view
        (r'/view', hd_jijin.JiJinHandler),
        (r'/sum', hd_jsum.SumShowHandler),
        (r'/study', hd_poetry.PoetryHandler),
        (r'/poem', hd_poetry.PoemHandler),
        (r'/alticles', hd_alticle.AlticlesHandler),
        (r'/alticle', hd_alticle.AlticleHandler),
        (r'/poemlike', hd_poetry.PoemLikeHandler),
        (r'/word', hd_word.WordHandler),
        (r'/sma', hd_sma.SMAHandler),
        # (r'/notebook%s' % path_regex, hd_notebook.NoteBookHandler),

        # -------- APP -------
        (r'/app/dbinfo', hd_dbinfo.DbinfoHandler),
        (r'/app/createdir', hd_create.AppFsCreateHandler),
        (r'/app/delete', hd_delete.AppFsDeleteHandler),
        (r'/app/fsmain', hd_main.AppFSMainHandler),
        (r'/app/upload', hd_fileload.AppUploadHandler),
        (r'/app/rename', hd_rename.AppFsRenameHandler),
        (r'/app/view', hd_jijin.AppJiJinHandler),
        # (r'/app/predict', hd_predict.AppJijinPredict),
        (r'/app/play/(?P<filename>.*)', hd_play.AppPlayHandler),
        (r'/appversion', AppVersionHandler),
        (r'/appuserinfo', UserinfoHandler),

        (r'/app/word', WordActionHandler),
        (r'/app/code', AppCodeHandler),   # put encode, post decode
        (r'/app/addcode', CodeAddHandler),

        (r'/app/image', hd_image.AppImageHandler),
        (r'/app/sum', hd_jsum.JSumHandler),
        (r'/app/sma', hd_image.SmaMatHandler),

        (r'/tesseract', hd_word.PyTesseractHandler),


]
