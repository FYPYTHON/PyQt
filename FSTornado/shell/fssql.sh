#!/bin/bash
# ./fssql.sh 2021-06-03 161725  
sdate="2021-05-25"
dbs="/opt/midware/FSTornado/wfs.db"

cur_dir=$(dirname "$0")
echo "$cur_dir"
echo ".table" | sqlite3 $dbs -cmd ""

echo "select jid,jper from tbl_sum where jdate='$sdate' order by jid;" | sqlite3 $dbs -cmd ""


jid=$2
if [ x"$jid" != x"" ];then
    echo -e "\n\n"
    echo "$jid --->"
    echo "select jdate,jvalue from tbl_jijin where jid='$jid' order by jdate desc limit 14;" | sqlite3 $dbs -cmd ""
fi


