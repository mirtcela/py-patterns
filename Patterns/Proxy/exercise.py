class Person:
  def __init__(self, age):
    self.age = age

  def drink(self):
    return 'drinking'

  def drive(self):
    return 'driving'

  def drink_and_drive(self):
    return 'driving while drunk'

class ResponsiblePerson:
  def __init__(self, person):
    self.person = person

#   Solution:  
#   @property
#   def age(self):
#     return self.person.age

#   @age.setter
#   def age(self, value):
#     self.person.age = value

  def drink(self):
    if self.person.age >= 18:
      return self.person.drink()
    return 'too young'

  def drive(self):
    if self.person.age >= 16:
      return self.person.drive()
    return 'too young'
          
  def drink_and_drive(self):
    return 'dead'

def main():
  p = ResponsiblePerson(Person(10))
  print(p.drive())

main()