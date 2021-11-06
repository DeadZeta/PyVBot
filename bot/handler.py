from bot.commands import stop, post

def text_parse(message):
    return message.split(' ')

def handle(system, action_type, message, client_info):
        if action_type == 'message_new':
            args = text_parse(message['text'])
            command = args[0]

            if command == '/stop':
                stop.handle(system, message, client_info, args)

            if command == '/post':
                post.handle(system, message, client_info, args)

        pass