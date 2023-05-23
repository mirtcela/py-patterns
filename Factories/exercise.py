# todo: Create PersonFactory with non-static method create_person()
# that takes a person's name and returns an instance of the Person class with that name and id. The id field must start with zero. 
# So the factory will return the first instance with id = 0, the second with id = 1, and so on.

# One Solution
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return f'PersonId = {self.id}, PersonName = {self.name}'

class PersonFactory:
    _person_idx = -1
    
    def count_person(self):
        self._person_idx += 1
        return self._person_idx
    
    def create_person(self, name):
        self.id = self.count_person(self)
        return Person(self.id, name)

    
# Second Solution
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return f'PersonId = {self.id}, PersonName = {self.name}'
    
class PersonFactory:
    id = 0

    def create_person(self, name):
        p = Person(PersonFactory.id, name)
        PersonFactory.id += 1
        return p

if __name__ == '__main__':
    p1 = PersonFactory.create_person(PersonFactory, 'A')
    p2 = PersonFactory.create_person(PersonFactory, 'B')

    print(p1, p2)