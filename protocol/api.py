import requests
from json import loads, dumps
import config
from random import randint

VK_API_URL = "https://api.vk.com/method/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}

def send(method: str, params: dict):
    params['access_token'] = config.access_token,
    params['v'] = config.version,

    response = requests.post(VK_API_URL + method, data = params, headers=headers)

    if response.status_code != 200:
        print("Error: status code is not 200")
        exit()

    if loads(response.text).get('error') is not None:
        print("Error:", loads(response.text).get('error')['error_msg'])
        exit()

    return loads(response.text)

def send_server(system, longpoll: dict):
    act = 'a_check',
    wait = 5

    response = requests.get(longpoll['server'], params={'act': act, 'wait': wait, 'key': longpoll['key'], 'ts': longpoll['ts']}, headers=headers)

    if response.status_code != 200:
        print("Error: status code is not 200")
        exit()

    if response.text == '' or None:
        print("Warning: Server return Empty text")
        return {}

    if loads(response.text).get('failed') is not None:
        if loads(response.text).get('failed') != 1:
            system['reconnect'] = True

            return {}

    return loads(response.text)

def get_server(group_id: int):
    return send('groups.getLongPollServer', {
        'group_id': group_id
    })

def message_user(user_id: int, message: str):
    return send('messages.send', {
        'peer_id': user_id,
        'message': message,
        'random_id': randint(0, 99999999999)
    })