from Pyewacket import choice

from monsters.monster import Monster
from monsters.utilities import Printable


def random_monster_name():
    element = ['Flaming', 'Storm', 'Lightning', 'Stone']
    types = ['Dragon', 'Giant', 'Spirit']
    return f"{choice(element)} {choice(types)}"


class Dungeon(Printable):

    def __init__(self, level):
        raw_monsters = set()
        while len(raw_monsters) < 12:
            raw_monsters.add(Monster(level, random_monster_name()))

        print(raw_monsters)

        self.__dict__ = {
            f"Room {room_number}": f"\n{Monster(level, random_monster_name())}\n"
            for room_number in range(1, 13)
        }


if __name__ == '__main__':

    d = Dungeon(12)
    print(d)

