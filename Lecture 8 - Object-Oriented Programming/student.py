class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f'{self.name} in {self.house}'

    # getter
    @property
    def name(self):
        return self._name

    # setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError('Missing name')
        self._name = name

    # getter
    @property
    def house(self):
        return self._house

    # setter
    @house.setter
    def house(self, house):
        if house not in ['gryffindor', 'slytherin', 'ravenclaw', 'hufflepuff']:
            raise ValueError('Invalid house')
        self._house = house

    @classmethod
    def get(cls):
        return cls(input('name: '), input('house: '))

def main():
    student = Student.get()
    print(student)

if __name__ == '__main__':
    main()
