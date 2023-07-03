from abc import ABC

class Creature:
    def __init__(self, attack, health):
        self.health = health
        self.attack = attack

class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    # return -1 if both creatures alive or both dead after combat
    # otherwise, return the _index_ of winning creature
    def combat(self, c1_index, c2_index):
        # todo
        c1 = self.creatures[c1_index]
        c2 = self.creatures[c2_index]
        self.hit(c1, c2)
        self.hit(c2, c1)
        c1_alive = c1.health > 0 
        c2_alive = c2.health > 0 
        if c1_alive == c2_alive: return -1
        return c1_index if c1.health > 0 else c2_index

    def hit(self, attacker, defender):
        pass  # implement this in derived classes


class TemporaryDamageCardGame(CardGame):
    # todo
    def hit(self, attacker, defender):
        old_health = defender.health
        defender.health -= attacker.attack
        if defender.health > 0:
            defender.health = old_health


class PermanentDamageCardGame(CardGame):
    # todo
    def hit(self, attacker, defender):
        defender.health -= attacker.attack