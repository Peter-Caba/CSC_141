
while True:
    topping = input("Enter you're pizza topping or quit ")
    
    # Check if the user wants to quit
    if topping.lower() == 'quit':
        break
    
    # Add the topping to the list
    topping.append(topping)
    print(f"I'll add {topping} to your pizza!")
