#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 9:52
# @Author  : 1823218990@qq.com
# @File    : main_task.py
# @Software: PyCharm
#     # gene_jijin_data()
#     # gene_jijin_current()
import sys
import logging.config
sys.path.append("/opt/midware/FSTornado/")
from timedtask.getjijindata import gene_jijin_data
from timedtask.getcurrentjj import gene_jijin_current
from settings.logConfig import logConfig
logging.config.dictConfig(logConfig)

if __name__ == '__main__':
    try:
        import setproctitle
        setproctitle.setproctitle("tornadofs-task")     # set process name in linux environment
    except:
        pass
    gene_jijin_data()
    gene_jijin_current()
