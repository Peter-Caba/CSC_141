car = 'jeep'
favorite_cars = [ 'jeep', 'bmw', 'honda', 'bus', ]

age = 18
height = 160


# String equality and inequality tests
print("Is car == 'jeep'? I predict True.")
print(car == 'jeep')  # True

print("\nIs car != 'bmw'? I predict True.")
print(car != 'bmw')    # True

# Tests using the lower() method
print("\nIs car.lower() == 'honda'? I predict True.")
print(car.lower() == 'honda')  # True

print("\nIs car.lower() == 'Bus'? I predict False.")
print(car.lower() == 'Bus')  # False

# Numerical tests
print("\nIs age == 18? I predict True.")
print(age == 18)  # True

print("\nIs height < == 18? I predict True.")
print(height < 160)  # True

print("\nIs age >= 18? I predict False.")
print(age >= 18)  # False

print("\nIs height <= 160? I predict True.")
print(height <= 160)  # True

# Tests using the and keyword
print("\nIs car == 'jeep' and age < 18? I predict True.")
print(car == 'jeep' and age < 18)  # True

print("\nIs car == 'honda' and height > 160? I predict False.")
print(car == 'honda' and height > 160)  # False

# Tests using the or keyword
print("\nIs car == 'bus' or car == 'audi'? I predict True.")
print(car == 'bus' or car == 'audi')  # True

print("\nIs car == 'honda' or height < 160? I predict False.")
print(car == 'honda' or height < 160)  # False

# Test whether an item is in a list
print("\nIs 'jeep' in favorite_cars? I predict True.")
print('jeep' in favorite_cars)  # True

print("\nIs 'bus' in favorite_cars? I predict False.")
print('bus' in favorite_cars)  # False

# Test whether an item is not in a list
print("\nIs 'bwm' not in favorite_cars? I predict False.")
print('bmw' not in favorite_cars)  # False

print("\nIs 'honda' not in favorite_cars? I predict True.")
print('honda' not in favorite_cars)  # True
