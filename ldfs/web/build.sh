#!/bin/bash -x
# ln -s /opt/midware/ldfs/web/node-v12.12.0-linux-x64/bin/node  /usr/bin/node
# config/index.js build assetsPublicPath: './',
PS4='$(date "+%s.%N ($LINENO) + ")'
cp -a ../build/node_modules.tar ./
cp -a ../build/node-v12.12.0-linux-x64.tar.xz ./
rm -rf node_modules
rm -rf node-v12.12.0-linux-x64
tar -xf node-v12.12.0-linux-x64.tar.xz
tar -xf node_modules.tar

cpath=$(pwd)
ln -s $cpath/node-v12.12.0-linux-x64/bin/node  /usr/bin/node
./node-v12.12.0-linux-x64/bin/npm install
./node-v12.12.0-linux-x64/bin/npm run build:test
#./node-v12.12.0-linux-x64/bin/npm install -g http-server

rm -rf node_modules*
rm -rf node-v12.12.0-linux-x64*
rm -f /usr/bin/node
cd -

