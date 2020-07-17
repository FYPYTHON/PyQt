#!/bin/bash

find /opt/midware/FSTornado/python3_fs  -type d -name __pycache__ | xargs rm -rf

PYTHONPATH=/opt/midware/FSTornado/python3_fs/lib/python3.5/site-packages /opt/midware/python3.5/bin/python3 /opt/midware/FSTornado/main_app.py & > /dev/null 2>&1
