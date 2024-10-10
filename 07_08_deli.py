sandwich_orders = ['Cheese', 'Peppernoi', 'Steak', 'Veggie', 'Fish']
finished_sandwiches = []


for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)


print("\nAll sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich} sandwich")
