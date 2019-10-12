#!/bin/bash
umount -lA /dev/sdb1
mount /dev/sdb1 /opt/gfs
cd /opt/gfs/
rm -rf *
mkdir -p bk1 bk2 bk3
setfattr -x trusted.glusterfs.volume-id bk1
setfattr -x trusted.glusterfs.volume-id bk2
setfattr -x trusted.glusterfs.volume-id bk3
