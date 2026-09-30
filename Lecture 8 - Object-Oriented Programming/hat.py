import random

class Hat:
    houses = ['gryffindor', 'slytherin', 'ravenclaw', 'hufflepuff']

    @classmethod
    def sort(cls, name):
        print(f'{name} is in {random.choice(cls.houses)}')

Hat.sort('harry')