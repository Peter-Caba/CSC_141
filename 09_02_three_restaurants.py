class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} Is Now open!")

restaurant1 = Restaurant("Philly CheeseSteaks", "Philadelphia")
restaurant2 = Restaurant("Peter's Pizaa", "Italian")
restaurant3 = Restaurant("Enpanadas's Free For All", "Dominican")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
