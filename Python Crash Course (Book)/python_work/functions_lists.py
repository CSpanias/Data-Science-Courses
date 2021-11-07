# 8.9
short_messages = ['Hello!', 'Goodbye!', 'Greetings!', 'Au revoir!', 'Adieu!']

def show_messages(message_list):
    for message in message_list:
        print(message)

show_messages(short_messages)

# 8.10
message_list = ['Hello!', 'Goodbye!', 'Greetings!', 'Au revoir!', 'Adieu!']
sent_messages = []

def send_messages(message_list, sent_messages):
    """
    Prints each text message from message_list.
    Moves each text message to sent_messages.
    """
    while message_list:
        current_message = message_list.pop()
        print(f'Now sending the following message: {current_message}.')
        sent_messages.append(current_message)


send_messages(message_list, sent_messages)

print(message_list)
print(sent_messages)

# 8.11
message_list = ['Hello!', 'Goodbye!', 'Greetings!', 'Au revoir!', 'Adieu!']
sent_messages = []

send_messages(message_list[:], sent_messages)

print(message_list)
print(sent_messages)