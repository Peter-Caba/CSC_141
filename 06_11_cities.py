# Creating a dictionary of cities
cities = {
    'Philly': {
        'country': 'USA',
        'population': 1533828,
        'fact': 'Philly is known for their cheese steaks.' },
    
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'Tokyo is the most populous metropolitan area in the world.' },
   
    'Mexico': {
        'country': 'USA',
        'population': 128000000,
        'fact': 'Mexico is populated with more people every year.' },
}

# Looping through the dictionary and printing information about each city
for city, info in cities.items():
    print(f"{city}:")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}\n")
