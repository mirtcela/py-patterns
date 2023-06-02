from copy import deepcopy

class Token:
    def __init__(self, value=0):
        self.value = value


class Memento(list):
    pass


class TokenMachine:
    def __init__(self):
        self.tokens = []

    def add_token_value(self, value):
        return self.add_token(Token(value))

    def add_token(self, token):
        # todo
        self.tokens.append(token)
        # deepcopy because Token change from outside
        return Memento(deepcopy(self.tokens))

    def revert(self, memento):
        self.tokens = [Token(x.value) for x in memento]
            