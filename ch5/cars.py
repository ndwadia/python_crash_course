# pylint: disable=invalid-name
"""
if statements
"""

cars = ["audi", "bmw", "volvo", "ford"]
for car in cars:
    if car.lower() == "bmw":
        print(car.upper())
    else:
        print(car.title())
