
current_users = ['Joyce', 'bob', 'john', 'charlie', 'dave']

new_users = ['John', 'Eve', 'bob', 'Zoe', 'Joyce']


lowercase_current_users = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in lowercase_current_users:
        print(f"The username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")
