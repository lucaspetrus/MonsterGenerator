"""
Monsters by Broken Ltd.

Aug 8, 2020
"""
from Pyewacket import choice, randint
from monsters.dice import dice
from monsters.utilities import Printable


class Monster(Printable):
    armor_lookup = {
        val: int(round(val / 10 + 10, 0)) for val in range(1, 101)
    }

    def __init__(self, level, name):
        self.name = name
        self.level = level
        self.health = dice(self.level, 8)
        self.offense = randint(-3, 3)
        self.defense = randint(-3, 3)
        self.armor = self.armor_lookup[self.level]

    def damage(self):
        return dice(self.level, 6)


if __name__ == '__main__':

    print(Monster(name="Joe the Monster", level=12))
