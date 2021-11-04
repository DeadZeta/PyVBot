import requests
from json import loads, dumps
import config
from random import randint

VK_API_URL = "https://api.vk.com/method/"
header = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

def send(method: str, params: dict):
    params['access_token'] = config.access_token,
    params['v'] = config.version,

    response = requests.post(VK_API_URL + method, data = params, headers=header)

    if response.status_code != 200:
        print("Error: status code is not 200")
        exit()

    if loads(response.text).get('error') is not None:
        print("Error:", loads(response.text).get('error')['error_msg'])
        exit()

    return loads(response.text)

def send_server(server: str, key: str, ts: int):
    act = 'a_check',
    wait = 25

    response = requests.get(server, params={'act': act, 'wait': wait, 'key': key, 'ts': ts}, headers=header)

    if response.status_code != 200:
        print("Error: status code is not 200")
        exit()

    if response.text == '':
        print("Warning: Server return Empty text")
        return {}

    if loads(response.text).get('failed') == 2:
        print("Warning: failed request server")
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