class BasicClass():
    def __init__(self, name):
        self.name = name
        self.fields = []
    
    def __str__(self):
        class_name = f' class {self.name}:'
        init = '\n  def __init__(self):'
        field_str = ''
        for f in self.fields:
            field_str += f'\n    {f}'
        if len(field_str) > 0:
            return class_name + init+ field_str
        else:
            return class_name + '\n  pass'

class Field():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f'self.{self.name} = {self.value}'
    
class CodeBuilder:
    def __init__(self, root_name):
        self.__class = BasicClass(root_name)

    def add_field(self, type, name):
        self.__class.fields.append(Field(type, name))
        return self

    def __str__(self):
        return self.__class.__str__()
    
cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
print(cb)
cb = CodeBuilder('Foo')
print(cb)