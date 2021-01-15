#!/bin/bash

/opt/midware/mysql/bin/mysql -uroot -p$1 --connect-expired-password -e "set password=password('fy123456');"



