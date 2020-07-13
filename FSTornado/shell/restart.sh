#!/bin/bash

/opt/midware/FSTornado/shell/stop.sh
/opt/midware/FSTornado/shell/start.sh

ps -ef | grep "tornadofs"
