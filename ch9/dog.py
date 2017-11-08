# pylint: disable=invalid-name
"""
Using classes
"""

class Dog():
    """A simple attempt to model a dog"""
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate sit"""
        print(self.name.title() + ' is now sitting')

    def roll_over(self):
        """Simulate roll over"""
        print(self.name.title() + ' rolled over')
