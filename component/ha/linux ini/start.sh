#!/bin/bash
/opt/apps/ha/sbin/haproxy -f /opt/apps/ha/shell/haproxy.cfg >>/opt/apps/ha/shell/ha.log
echo $?
