def make_car(manufacturer, model, **features):
    """Build a dictionary containing information about a car."""
   
    car_info = {'manufacturer': manufacturer,'model': model, }
   
    for key, value in features.items():
        car_info[key] = value
    return car_info


car = make_car('Truck', 'Mcclaren', color='blue', tow_package=True)

print(car)
