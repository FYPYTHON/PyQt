"""
Time    : 2019/8/1 09:35
Author  : wangguoqiang@kedacom.com
"""
import json
import os
import subprocess
from threading import Timer
import psutil


TOPHD = '/opt/data/hd'
TOPREGION = '/opt/data/region/platformData'
TIMEOUT = 30
CONFIGJSON = '/opt/data/kdfs/config.json'


def psutil_shell(arg, timeout):

    child = psutil.Popen(arg, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    timer = Timer(timeout, lambda process: process.kill(), [child])
    try:
        timer.start()
        stdout, stderr = child.communicate()
        return_code = child.returncode

        if 0 != return_code:
            return return_code, stderr.decode('utf-8')
        else:
            return return_code, stdout.decode('utf-8')
    finally:
        timer.cancel()


def load_config_pool():
    if not os.path.exists(CONFIGJSON):
        return None
    with open(CONFIGJSON, 'r') as load_f:
        config_json = json.load(load_f)
    pool_list = config_json['pool']
    if pool_list:
        pool_list = sorted(pool_list)
        return pool_list
    else:
        return None


def get_disk_usage_shell(disk, timeout):
    """
    df /dev/sdc1 or df /opt/data/hd/hd2
    size:Kb
    :param disk: disk_name or mountpoint
    :return:
    """
    code, result = psutil_shell('df %s | awk \'END {print $1,$2,$3,$4,$5,$6}\'' % disk, timeout)
    if code != 0:
        return None
    # print(disk, "used:", result)
    disk_dict = dict()
    result = result.split(" ")
    disk_dict["device_name"] = result[0]
    disk_dict["device_size"] = result[1]
    disk_dict["used_size"] = result[2]
    disk_dict["available_size"] = result[3]
    disk_dict["used_percent"] = result[4]
    return result[3], result[4]

def get_disk_usage(disk):
    """
    df /dev/sdc1 or df /opt/data/hd/hd2
    size:Kb
    :param disk: disk_name or mountpoint
    :return:
    """
    used = psutil.disk_usage(disk)
    # print("used", used)
    ava_size = used.free
    ava_pert = used.percent
    return ava_size, ava_pert


def check_space_available(pool_list):
    pool_list = sorted(pool_list)
    for hd in pool_list:
        hd_mount = os.path.join(TOPREGION, hd)
        if os.path.exists(hd_mount):
            ava_size, ava_pert = get_disk_usage_shell(hd_mount, 60)
            # print("ava:", ava_size, hd_mount, hd)
            if int(ava_size) > 1*1024 and int(ava_pert) < 100:
                return hd
        else:
            return None
    else:
        return None


if __name__ == "__main__":
    pool_list = load_config_pool()
    if pool_list:
        hd = check_space_available(pool_list)
        if hd is not None:
            print(hd)
        else:
            print('None')
    else:
        print('None')


