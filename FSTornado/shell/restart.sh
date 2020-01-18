#!/bin/bash

./shell/stop.sh
./shell/start.sh

ps -ef | grep "python3.5"
