person_1 = {
    'first_name': 'Stewart',
    'last_name': 'Doe',
    'age': 25,
    'city': 'Philly'}

person_2 = {
    'first_name': 'Alex',
    'last_name': 'Smith',
    'age': 25,
    'city': 'D.C'}

person_3 = {
    'first_name': 'Marcus',
    'last_name': 'Johnson',
    'age': 35,
    'city': 'Baltimore'}

# Storing all three dictionaries in a list
people = [person_1, person_2, person_3]

# Looping through the list and printing information about each person
for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")
