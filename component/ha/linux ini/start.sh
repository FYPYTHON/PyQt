#!/bin/bash
mkdir -p /var/lib/haproxy
/opt/apps/ha/sbin/haproxy -f /opt/apps/ha/shell/haproxy.cfg >>/opt/apps/ha/shell/ha.log
echo $?
