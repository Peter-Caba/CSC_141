def send_messages(messages):
    sent_messages = []
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)
    return sent_messages


messages = ["Hello, how are you?","Don't forget our meeting tomorrow.","Happy birthday!", "Let's grab lunch sometime."]

messages_to_send = messages.copy()


sent = send_messages(messages_to_send)


print("\nOriginal messages:", messages)
print("Sent messages:", sent)
