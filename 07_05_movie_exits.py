while True:
    age_input = input("Please enter your age (or type 'quit' to exit): ")

    if age_input.lower() == 'quit':
        print("Thank you for using the ticket pricing system!")
        break
    try:
        age = int(age_input)

        if age < 3:
            ticket_price = "free"
        elif 3 <= age <= 12:
            ticket_price = 10
        else:
            ticket_price = 15

        print(f"The cost of your movie ticket is: ${ticket_price}")

    except ValueError:
        print("Please enter a valid age or type 'quit' to exit.")



