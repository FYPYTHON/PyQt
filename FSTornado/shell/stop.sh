#!/bin/bash

ps -ef | grep "main_app.py" | grep -v grep | awk '{print $2}' | xargs kill -9


