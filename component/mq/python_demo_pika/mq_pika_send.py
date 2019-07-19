# coding=utf-8
from amqplib import client_0_8 as amqp
HOST = '172.16.83.226'
USER = 'root'
PAWD = 'feiying'


def main():
    server = {'host': HOST, 'userid': USER, 'password': PAWD, 'ssl': False}
    x_name = 'message'

    conn = amqp.Connection(server['host'],
                           userid=server['userid'],
                           password=server['password'],
                           ssl=server['ssl'])
    ch = conn.channel()
    ch.access_request('/data', active=True, write=True)
    ch.exchange_declare(exchange=x_name, type='topic', durable=True, auto_delete=False)
    retry = True
    while retry:
        msg_body = input('>')
        msg = amqp.Message(msg_body, content_encoding='UTF-8')
        msg.properties['delivery_mode'] = 2
        ch.basic_publish(msg, x_name)

        if msg_body == 'quit':
            retry = False

    ch.close()
    conn.close()


if __name__ == '__main__':
    main()