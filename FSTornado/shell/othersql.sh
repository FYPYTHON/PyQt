#!/bin/bash

dbs="/opt/midware/FSTornado/wfs.db"

echo "select count("jid"),jid from tbl_sum group by jid;" | sqlite3 $dbs -cmd ""

if [ ! "$1"x == ""x ];then
    echo "select jdate,jper from tbl_sum where jid="$1" order by jdate desc limit 10;" | sqlite3 $dbs -cmd ""
fi

