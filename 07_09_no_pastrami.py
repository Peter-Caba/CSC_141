sandwich_orders = ['Peppernoi', 'Pepper', 'pastrami', 'Steak', 'Turkey', 'Club', 'Cheese', 'Fish']

finished_sandwiches = []

print("The deli has run out of pastrami.")


while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")

    finished_sandwiches.append(sandwich)

print("\nAll sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich} sandwich")

