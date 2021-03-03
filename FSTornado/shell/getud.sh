#!/bin/bash

mkdir -p /opt/log/fs
PYTHONPATH=/opt/midware/FSTornado/python3_fs/lib/python3.5/site-packages /opt/midware/python3.5/bin/python3 /opt/midware/FSTornado/get_updown.py $1>> /opt/log/fs/ud.log 2>&1
