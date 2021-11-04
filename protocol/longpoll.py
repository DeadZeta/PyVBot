from .api import get_server, send_server, message_user
import config
import time

longpoll = {
    'key': '',
    'server': '',
    'ts': 0
}

milli = 0

def init():
    print(get_server(config.group_id))
    server = get_server(config.group_id)

    longpoll['key'] = server['response'].get('key')
    longpoll['server'] = server['response'].get('server')
    longpoll['ts'] = int(server['response'].get('ts'))

    listen()

def listen():
    while True:
        server = send_server(longpoll.get('server'), longpoll.get('key'), longpoll.get('ts'))

        if server.get('updates') is None:
            continue

        if len(server.get('updates')) == 0:
            longpoll['ts'] += 1
            continue

        message_user(server.get('updates')[0]['object']['message']['peer_id'], server.get('updates')[0]['object']['message']['text'])
        longpoll['ts'] += 1

        continue