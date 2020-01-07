# coding=utf-8
logConfig = {

    'version': 1,
    'loggers': {
      'root': {
        'level': 'DEBUG',
        'handlers': ['console']
      },
      'tornado': {
        'level': 'DEBUG',
        'handlers': ['console', 'log'],
        'propagate': 'no'
      },
      'tornado.access': {
        'level': 'DEBUG',
        'handlers': ['access'],
        'propagate': 'no'
      },
      'log': {
        'level': 'INFO',
        'handlers': ['log'],
        'propagate': 'no'
      }
    },
    'formatters': {
      'simple': {
        # 'format': '[%(levelname)s] %(name)s %(funcName)s %(asctime)s %(filename)s %(lineno)s:%(message)s'
        'format': '[%(levelname)s] %(asctime)s %(filename)s %(lineno)s:%(message)s'
      },
      'timedRotating': {
        'format': '[%(levelname)s] %(asctime)s %(filename)-12s %(message)s'
      }
    },
    'handlers': {
      'console': {
        'class': 'logging.StreamHandler',
        'level': 'DEBUG',
        'formatter': 'simple',
        },
      'access': {
        'class': 'logging.handlers.TimedRotatingFileHandler',  # time
        'level': 'INFO',
        'formatter': 'simple',
        'filename': '.access.log',
        'when': 'midnight',
        'interval': 1,
        'backupCount': 0,    # u"备份数"
        'encoding': 'utf8'
        },
      'log': {
        'class': 'logging.handlers.RotatingFileHandler',    # size
        'level': 'INFO',
        'formatter': 'timedRotating',
        'filename': './log.log',
        # 'when': 'midnight',
        # 'interval': 1,
        'backupCount': 0,    # 日志文件的保留个数
        'maxBytes': 50 * 1024 * 1024,  # 文件最大50M
        'encoding': 'gbk'
        }
    }
}