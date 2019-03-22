#!/bin/bash
:<<!
Time  : 2019/3/21 13:51
Author: wangguoqaing@kedacom.com
arg1: dev_names
arg2: hd_names
eg:./mount.sh "/dev/sdb1,/dev/sdc1" "/opt/data/hd/hd1,/opt/data/hd/hd2"
!
186.75£º
mount -t cifs -o username=wangguoqiang,vers=2.1 //172.16.83.87/kdfs /mnt/Wgq/kdfs
186.133£º
mount -t cifs -o username=wangguoqiang,vers=2.1 //172.16.83.87/stsps  /home/wgq/project/stsps/
mount -t cifs -o username=wangguoqiang,vers=2.1 //172.16.83.87/stsps  /mnt/Wgq/stsps/
umount -l /mnt/sss   #Ç¿ÖÆ½â³ı¹ÒÔØ
