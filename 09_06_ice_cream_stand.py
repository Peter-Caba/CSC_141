class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value of number_served

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def display_flavors(self):
        print(f"Available ice cream flavors at {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")


ice_cream_stand = IceCreamStand("Sweet Treats", "Dessert")

ice_cream_stand.add_flavor("Vanilla")
ice_cream_stand.add_flavor("Chocolate")
ice_cream_stand.add_flavor("Strawberry")
ice_cream_stand.add_flavor("Mint Chocolate Chip")


ice_cream_stand.display_flavors()
