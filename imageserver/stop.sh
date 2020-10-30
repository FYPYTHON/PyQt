#!/bin/bash

ps -ef | grep "imageserver" | grep -v grep | awk '{print $2}' | xargs kill -9


