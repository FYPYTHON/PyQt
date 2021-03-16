#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 14:41
# @Author  : 1823218990@qq.com
# @File    : mountdisk.py.py
# @Software: PyCharm
import os
import json
CONFIG_JSON = "/opt/data/ldfs/config.json"
CONTENT = ['public', 'private', 'extra']


def load_config():

    with open(CONFIG_JSON, 'r') as load_f:
        config_json = json.load(load_f)
    return config_json


def init():
    config_json = load_config()
    pool = config_json['pool']
    hds = []
    devs = []
    for key,disk in config_json['disks'].items():
        print(key, disk)
        if disk['hd_name'] in pool:
            hds.append(disk['hd_name'])
            devs.append(key + "1")

    res = os.system("/opt/midware/ldfs/shells/mountdisk.sh {} {} {}".format(",".join(devs), ",".join(hds), ",".join(CONTENT)))
    print(res)



if __name__ == '__main__':
    init()


