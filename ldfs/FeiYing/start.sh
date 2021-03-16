#!/usr/bin/env bash


mkdir -p /var/run/ldfs
mkdir -p /opt/log/ldfs
mkdir -p /opt/data/ldfs

find /opt/midware/ldfs  -type d -name __pycache__ | xargs rm -rf

python3 /opt/midware/ldfs/mountdisk.py >> /opt/log/ldfs/init.log 2>&1

uwsgi3 -i ./uwsgi.ini

cd - >/dev/null 2>&1
