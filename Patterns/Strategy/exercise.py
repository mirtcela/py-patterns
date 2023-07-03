from abc import ABC
import math
from cmath import sqrt


class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        # todo
        disc = b**2 - 4*a*c 
        return disc


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        # todo
        disc = b**2 - 4*a*c 
        if disc < 0:
            return float('nan')
        else:
            return disc


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """ Returns a pair of complex (!) values """
        # todo
        disc = self.strategy.calculate_discriminant(a, b, c)
        root = complex(sqrt(disc), 0)
        x1 = ((-b + root) / (2 * a))
        x2 = ((-b - root) / (2 * a))
        return x1, x2