#!/bin/bash

# remote
/opt/midware/mysql/bin/mysql -uroot -p$1 --connect-expired-password -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '$1';flush privileges;"

# repl
/opt/midware/mysql/bin/mysql -uroot -p$1 --connect-expired-password -e "create user repl;GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%.%.%.%' IDENTIFIED BY '$1';flush privileges;"
