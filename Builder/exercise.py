class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.fields = []

    def add_field(self, type="", name=""):
        self.type = type
        self.name = name
        if self.type:
            self.fields.append(f'self.{self.type} = {self.name}')
        return self

    def __str__(self):
        class_name = f' class {self.root_name}:'
        init = '\n  def __init__(self):'
        field_str = ''
        for f in self.fields:
            field_str += f'\n    {f}'
        if len(field_str) > 0:
            return class_name + init+ field_str
        else:
            return class_name + '\n  pass'
    
cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
print(cb)
cb = CodeBuilder('Foo')
print(cb)