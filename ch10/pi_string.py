# pylint: disable=invalid-name
"""
Reading files
"""

filename = './ch10/pi_30_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first 30 digits of pi!")
else:
    print("Your birthday does not appear in the first 30 digits of pi.")
