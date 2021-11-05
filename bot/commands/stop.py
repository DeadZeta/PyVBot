import protocol.api as api

def handle(system, message, client_info):
    api.message_user(message['peer_id'], 'Завершение работы...')
    system['stop'] = True