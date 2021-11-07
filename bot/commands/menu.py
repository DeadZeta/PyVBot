from protocol.api import group

def handle(system, body_message, client_info, args):
    group.send_message_keyboard(body_message['peer_id'], 'Привет!', {
        'inline': True,
        'buttons': [
            [{
                'action': {
                    'type': 'open_link',
                    'link': 'https://vk.com/anideadjp',
                    'label': 'Автор',
                }
            }]
        ]
    })
    pass