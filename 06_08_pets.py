pet_1 = {
    'animal_type': 'Goat',
    'owner_name': 'Joyce'}

pet_2 = {
    'animal_type': 'Bird',
    'owner_name': 'Steve'}

pet_3 = {
    'animal_type': 'Dog',
    'owner_name': 'Tyler'}

pet_4 = {
    'animal_type': 'Gold Fish',
    'owner_name': 'Peter'}

# Storing all pet dictionaries in a list
pets = [pet_1, pet_2, pet_3, pet_4]

# Looping through the list and printing information about each pet
for pet in pets:
    print(f"Animal Type: {pet['animal_type']}")
    print(f"Owner Name: {pet['owner_name']}\n")
