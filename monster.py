"""
Monsters by Broken Ltd.

Aug 8, 2020
"""
from Pyewacket import choice, randint
from dice import dice


class Monster:
    element = ['Flaming', 'Storm', 'Lightning', 'Stone']
    types = ['Dragon', 'Giant', 'Spirit']
    armor_lookup = {
        val: int(round(val / 10 + 10, 0)) for val in range(1, 101)
    }

    def __init__(self, level):
        self.name = f"{choice(self.element)} {choice(self.types)}"
        self.level = level
        self.health = dice(self.level, 8)
        self.offense = randint(-3, 3)
        self.defense = randint(-3, 3)
        self.armor = self.armor_lookup[self.level]

    def damage(self):
        return dice(self.level, 6)

    def __str__(self):
        return '\n'.join(f"{k.title()}: {v}" for k, v in self.__dict__.items())


if __name__ == '__main__':

    print(Monster(level=12))
