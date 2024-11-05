
class Battery:
    def __init__(self, battery_size=50):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def upgrade_battery(self):
        """Upgrade the battery to 65 kWh if it isn't already."""
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh.")
        else:
            print("Battery is already 65 kWh.")

    def get_range(self):
        """Return the range of the car based on the battery size."""
        if self.battery_size == 50:
            range = 150  
        elif self.battery_size == 65:
            range = 225  
        else:
            range = 0  
        return range

