from enum import Enum
import re

class ExpressionProcessor:
    def __init__(self):
        self.variables = {}
        
    class Operation(Enum):
        ADDITION = '+'
        SUBTRACTION = '-'
        
    def calculate(self, expression):
        print(expression)
        result = 0
        reg_vars = re.findall('[^\W\d]+', expression)
        for var in reg_vars:
            if len(var) > 2:
                return 0
                
        numbers = re.findall('\w+', expression)
        for i in range(len(numbers)):
            if numbers[i] in self.variables:
                numbers[i] = self.variables[numbers[i]]
            elif len(numbers[i]) > 1:
                return 0

        # find all operations in expression    
        operations = re.findall('\W', expression)
        if 0 < len(operations) < 2:
            idx_num = len(numbers)-1
            op = operations[0]
            
            if op == self.Operation.ADDITION.value:
                result += int(numbers[idx_num-1]) + int(numbers[idx_num])
                return result
            elif op == self.Operation.SUBTRACTION.value:
                result += int(numbers[idx_num-1]) - int(numbers[idx_num])
                return result
            else:
                return 0
        elif len(operations) <= 0:
            if len(numbers) > 0:
                return int(numbers[0])
            else:
                return 0
                