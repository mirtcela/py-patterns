from abc import ABC
from collections.abc import Iterable


class Summable(Iterable, ABC):
    @property
    def sum(self):
        result = 0
        for s in self:
            for v in s:
                result += v
        return result

                
class SingleValue(Summable):
    def __init__(self, value):
        self.value = value
        
    def __iter__(self):
        yield self.value

    def __str__(self):
        return f'{self.value}'

class ManyValues(list, Summable):
    def __init__(self):
        self.value = self


def main():
    single_value = SingleValue(11)
    other_values = ManyValues()
    other_values.append(22)
    other_values.append(33)

    all_values = ManyValues()
    all_values.append(single_value)
    all_values.append(other_values)
    print(all_values.sum)

main()