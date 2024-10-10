favorite_places = {
    'Deandre': ['Texas', 'New York', 'Tokyo'],
    'Cahelie': ['Paris', 'Mexico'],
    'Peter': ['Tokyo', 'Barcelona', 'Russain'],}

# Looping through the dictionary and printing each person's favorite places
for name, places in favorite_places.items():
    print(f"{name}'s favorite places are:")
    for place in places:
        print(f"- {place}")
    print()  # Blank line for separation
