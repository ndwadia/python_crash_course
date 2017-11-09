# pylint: disable=invalid-name
"""
Reading files
"""

filename = './ch10/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
