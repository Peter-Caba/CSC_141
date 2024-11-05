def make_sandwich(*toppings):
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
    print("Your sandwich is ready!\n")

make_sandwich("lettuce", "tomato", "turkey","cheese", "ketchup")
make_sandwich("ham", "turkey")
make_sandwich("peanut butter", "jelly")
