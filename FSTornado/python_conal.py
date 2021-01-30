#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/24 10:38
# @Author  : 1823218990@qq.com
# @File    : python_conal
# @Software: Pycharm

import time

from canal.client import Client
from canal.protocol import EntryProtocol_pb2
from canal.protocol import CanalProtocol_pb2

# host = '172.16.83.226'
host = '192.168.0.223'
client = Client()
client.connect(host=host, port=11111)
client.check_valid(username=b'', password=b'')
client.subscribe(client_id=b'10011', destination=b'example', filter=b'.*\\..*')

while True:
    message = client.get(100)
    entries = message['entries']
    for entry in entries:
        entry_type = entry.entryType
        if entry_type in [EntryProtocol_pb2.EntryType.TRANSACTIONBEGIN, EntryProtocol_pb2.EntryType.TRANSACTIONEND]:
            continue
        row_change = EntryProtocol_pb2.RowChange()
        row_change.MergeFromString(entry.storeValue)
        event_type = row_change.eventType
        header = entry.header
        database = header.schemaName
        table = header.tableName
        event_type = header.eventType
        for row in row_change.rowDatas:
            # print("insert:", row)
            format_data = dict()
            if event_type == EntryProtocol_pb2.EventType.DELETE:
                for column in row.beforeColumns:
                    format_data = {
                        column.name: column.value
                    }
            elif event_type == EntryProtocol_pb2.EventType.INSERT:
                for column in row.afterColumns:
                    # format_data = {
                    #     column.name: column.value
                    # }
                    # print(column)
                    format_data[column.name] = column.value
            else:
                format_data['before'] = format_data['after'] = dict()
                for column in row.beforeColumns:
                    format_data['before'][column.name] = column.value
                for column in row.afterColumns:
                    format_data['after'][column.name] = column.value
            data = dict(
                db=database,
                table=table,
                event_type=event_type,
                data=format_data,
            )
            print(data)
    time.sleep(1)

client.disconnect()