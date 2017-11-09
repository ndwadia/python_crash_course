# pylint: disable=invalid-name
"""
Working with JSON
"""

import json

filename = './ch10/numbers.json'
with open(filename) as file_object:
    numbers = json.load(file_object)

print(numbers)
