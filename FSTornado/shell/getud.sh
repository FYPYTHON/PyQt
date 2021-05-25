#!/bin/bash

mkdir -p /opt/log/fs/ud
curdate=`date +"%m%d_%Y"`


PYTHONPATH=/opt/midware/FSTornado/python3_fs/lib/python3.5/site-packages /opt/midware/python3.5/bin/python3 /opt/midware/FSTornado/get_updown.py $1>> /opt/log/fs/ud.${curdate}.log 2>&1


nudfile=$(ls /opt/log/fs/ud.* | tr ":" "\n" | wc -l)
if [ $nudfile -gt 1 ];then
   filename=$(ls /opt/log/fs/ud.* |xargs |awk '{print $1}')
   echo "mv $filename to ud/"
   mv $filename /opt/log/fs/ud
fi


