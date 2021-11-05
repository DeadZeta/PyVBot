import protocol.api as api
import config
from bot.handler import handle
import time
from threading import Thread

longpoll = {
    'key': '',
    'server': '',
    'ts': 0
}

system = {
    'reconnect': False,
    'stop': False
}

def init():
    server = api.get_server(config.group_id)

    longpoll['key'] = server['response'].get('key')
    longpoll['server'] = server['response'].get('server')
    longpoll['ts'] = int(server['response'].get('ts'))

    listen()

def listen():
    while True:
        if system.get('reconnect') == True:
            server = api.get_server(config.group_id)

            longpoll['key'] = server['response'].get('key')
            longpoll['server'] = server['response'].get('server')
            longpoll['ts'] = server['response'].get('ts')
            system['reconnect'] = False

        if system.get('stop') == True:
            system['stop'] = False
            exit()
            break

        server = api.send_server(system, longpoll)

        if server.get('updates') is None:
            continue

        if len(server.get('updates')) == 0:
            longpoll['ts'] += 1
            continue

        thread = Thread(target=handle, args=(system, server.get('updates')[0]['type'],
                                     server.get('updates')[0]['object']['message'],
                                     server.get('updates')[0]['object']['client_info']))
        thread.start()

        longpoll['ts'] += 1

        continue