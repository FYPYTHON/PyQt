#!/bin/bash

nohup /opt/midware/seaweedfs/weed master -mdir=/opt/data/seaweedfs -port=9333 -defaultReplication=001 -ip=172.16.83.227 >>/opt/log/seaweedfs/master.log  &

nohup /opt/midware/seaweedfs/weed volume -dir=/opt/data/hd/hd0 -mserver=172.16.83.227:9333 -port 8081 -ip=172.16.83.227 >>/opt/log/seaweedfs/vol1.log &

nohup /opt/midware/seaweedfs/weed volume -dir=/opt/data/hd/hd1 -mserver=172.16.83.227:9333 -port 8082 -ip=172.16.83.227 >>/opt/log/seaweedfs/vol2.log &

nohup /opt/midware/seaweedfs/weed filer -master=172.16.83.227:9333 -ip=172.16.83.227 -defaultReplicaPlacement=001 &
