#!/bin/bash
:<<!
Time   :2019/4/30 10:39
Autohor:1823218990@qq.com
arg1: raid name (/dev/md0)
eg:./raid_delete.sh /dev/md0
!
umount -lA $1
mdadm -S $1
rm -rf $1

