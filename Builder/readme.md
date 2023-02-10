###Need to implement a Builder pattern to form code snippets.
-------------------------------------------
Example of an API you need to support:
```
cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
print(cb)
```
Expected output of the example:
```
class Person:
  def __init__(self):
    self.name = ""
    self.age = 0
```
*Don't forget to consider spaces and indents.*

An example with an empty class:
```
cb = CodeBuilder('Foo')
print(cb)
```
Expected output of the example:
```
class Foo:
  pass
```