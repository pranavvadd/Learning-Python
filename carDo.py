from car_model import Car

car1 = Car("Toyota Camry", 2020, "Blue", True)
print(car1.model)  # Output: Toyota Camry
car2 = Car("Lamborghini", 2012, "Yellow", False)

car1.drive()  # Output: You drive the Toyota Camry
car2.describe()  # Output: 2012 Yellow Lamborghini - Not For Sale