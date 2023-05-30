from enum import Enum

class Command:
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, action, amount):
        self.action = action
        self.amount = amount
        self.success = False
        
class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def process(self, command):
        # todo
        if command.action == command.Action.DEPOSIT:
            self.balance += command.amount
            command.success = True
        elif command.action == command.Action.WITHDRAW:
            if command.amount <= self.balance:
                self.balance -= command.amount
                command.success = True
            elif command.amount > self.balance:
                command.success = False