toppings_count = [0]
max_toppings = [5]

while True:
    topping = input("your toppings are: ")
    
    # Check if the user wants to quit
    if topping.lower() == 'quit':
        break
    
    # Add the topping to the list
    toppings_count.append(topping)
    print(f"I'll add {topping} to your pizza!")
    
    toppings_count += 1

