# pylint: disable=invalid-name
"""
Using classes
"""

from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2015)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2015)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.battery_size = 85
print("Upgraded the battery: ")
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
