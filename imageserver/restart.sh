#!/bin/bash
cd /opt/midware/imageserver
./stop.sh

./start.sh

ps -ef | grep "imageserver"
