import random 

class Die:
    def __init__(self, sides=6):
        """Initialize the die with a default number of sides (6)."""
        self.sides = sides
    
    def roll_die(self):
        """Simulate rolling the die and print a random number between 1 and sides."""
        roll = random.randint(1, self.sides)
        print(f"Rolled: {roll}")

die = Die()

for _ in range(10):
    die.roll_die()
