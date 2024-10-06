favorite_languages = {
    'alice': 'python',
    'brian': 'java',
    'charlie': 'ruby',}

people_to_poll = ['alice', 'david', 'emily', 'frank', 'charlie']

# Loop through the list and check if they have taken the poll
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding.")
    else:
        print(f"Hi {person.title()}, please take our poll!")
