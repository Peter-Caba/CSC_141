car = 'Jeep'


car = 'jeep'

# Test 1
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  # This should return True

# Test 2
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')    # This should return False

# Test 3
print("\nIs car.lower() == 'jeep'? I predict True.")
print(car.lower() == 'jeep')  # This should return True

# Test 4
print("\nIs car != 'toyota'? I predict True.")
print(car != 'toyota')  # This should return True

# Test 5
print("\nIs 'subaru' in car? I predict False.")
print('subaru' in car)  # This should return True, but check with another string

# Test 6
print("\nIs car == 'jeep'? I predict False.")
print(car == 'jeep')  # This should return False due to case sensitivity
