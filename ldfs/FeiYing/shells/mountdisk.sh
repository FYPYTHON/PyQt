#!/bin/bash
:<<!
Time  : 2019/11/20 15:51
Author: 1823218990@qq.com
arg1: dev_names
arg2: hd_names
eg:./mountdisk.sh "/dev/sdb1,/dev/sdc1" "hd1,hd2" "public,private,extra"
!
OLD_IFS="$IFS"
IFS=","
dev_names=($1)
hd_names=($2)
regions=($3)
IFS="$OLD_IFS"
cur_dir=$(dirname "$0")


#echo "${dev_names[@]}"
#echo "${hd_names[@]}"
for i in "${!dev_names[@]}";
do 

    if [ ! -d "/opt/data/hd/${hd_names[$i]}" ];then
	mkdir -p /opt/data/hd/${hd_names[$i]}
    fi
    mount -o prjquota ${dev_names[$i]} /opt/data/hd/${hd_names[$i]}/
    echo "mount:${dev_names[$i]} /opt/data/hd/${hd_names[$i]}/"
done
echo "mount region..."
for hdname in "${hd_names[@]}";
do
    for j in "${!regions[@]}";
    do
        mt=`mount -l | grep /opt/data/region/${regions[$j]}/$hdname`
        if [ -n "$mt" ];then
           echo "/opt/data/region/${regions[$j]}/$hdname is mount"
        else
           echo "is not mount"
           mkdir -p /opt/data/hd/$hdname/${regions[$j]}
           mkdir -p /opt/data/region/${regions[$j]}/$hdname
           mount --bind /opt/data/hd/$hdname/${regions[$j]}/ /opt/data/region/${regions[$j]}/$hdname/
           echo "mount --bind /opt/data/hd/$hdname/${regions[$j]}/ /opt/data/region/${regions[$j]}/$hdname/"
        fi
    done
done

echo $?

