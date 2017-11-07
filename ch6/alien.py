# pylint: disable=invalid-name
"""
Working with dictionaries
"""

alien_o = {'color': 'green', 'points': 5}
print(alien_o)
print(alien_o['color'])
alien_o['x_coordinate'] = 0
alien_o['y_coordinate'] = 25
print(alien_o)
del alien_o['points']
print(alien_o)
