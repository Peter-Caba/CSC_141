# Creating the dictionary of rivers and their countries
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

# Loop to print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# Loop to print the name of each river
print("\nRivers:")
for river in rivers.keys():
    print(river.title())

# Loop to print the name of each country
print("\nCountries:")
for country in rivers.values():
    print(country.title())
