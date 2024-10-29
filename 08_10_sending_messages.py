def show_messages(messages):
    """Prints each message from the list."""
    for message in messages:
        print(message)

def send_messages(messages):
    """Prints each message and moves it to sent_messages."""
    sent_messages = []
    while messages:
        current_message = messages.pop(0)  # Get and remove the first message
        print(current_message)               # Print the message
        sent_messages.append(current_message)  # Move it to sent_messages
    return sent_messages

def main():
    # List of short text messages
    messages = [
        "Hello, how are you?",
        "Don't forget our meeting at 3 PM.",
        "Have a great day!",
        "Remember to bring your laptop.",
        "Looking forward to our chat!"
    ]

    # Call the function to send messages
    sent_messages = send_messages(messages)

    # Print both lists to verify
    print("\nOriginal Messages List (should be empty):", messages)
    print("Sent Messages List:", sent_messages)

if __name__ == "__main__":
    main()
