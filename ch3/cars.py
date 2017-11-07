# pylint: disable=invalid-name
"""
Working with lists
"""

cars = ['bmw', 'audi', 'ford', 'volvo']
print(cars)
print(cars[0])
print(sorted(cars))
cars.sort()
print(cars)
popped_car = cars.pop()
print("Popped car: " + popped_car)
print(cars)
