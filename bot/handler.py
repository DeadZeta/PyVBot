from bot.commands import stop

def text_parse(message):
    return message.split(' ')

def handle(system, action_type, message, client_info):
    if action_type == 'message_new':
        command = text_parse(message['text'])[0]

        if command == '/стоп' or '/завершить' or '/остановка':
            stop.handle(system, message, client_info)