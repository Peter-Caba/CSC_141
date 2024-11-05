def show_messages(messages):
    """Prints each message from the list."""
    for message in messages:
        print(message)

def main():

    messages = [ "Hello, how are you?","Don't forget our meeting at 3 PM.","Have a great day!",
                "Remember to bring your laptop.","Looking forward to our chat!" ]

 
    show_messages(messages)

if __name__ == "__main__":
    main()
