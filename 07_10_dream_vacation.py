dream_vacations = []

def poll_users():
    while True:
        response = input("If you could visit one place in the world, where would you go? (type 'quit' to stop) ")
        if response.lower() == 'quit':
            break
        dream_vacations.append(response)

def display_results():
    print("\nDream Vacation Poll Results:")
    if dream_vacations:
        for index, vacation in enumerate(dream_vacations, start=1):
            print(f"{index}. {vacation}")
    else:
        print("No responses received.")


poll_users()


display_results()
