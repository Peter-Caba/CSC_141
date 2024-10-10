favorite_numbers = {
    'Steve': [5, 7, 22],
    'Tyler': [19, 34, 98],
    'Cythina': [7, 20, 33],}

# Looping through the dictionary and printing each person's favorite numbers
for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are: {', '.join(map(str, numbers))}\n")
