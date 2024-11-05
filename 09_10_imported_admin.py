# restaurant.py

class Restaurant:
    def __init__(self, name, cuisine_type):
        """Initialize the restaurant's attributes."""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a description of the restaurant."""
        return f"{self.name} serves {self.cuisine_type} cuisine."

    def open_restaurant(self):
        """Simulate the restaurant opening."""
        return f"{self.name} is now open!"
