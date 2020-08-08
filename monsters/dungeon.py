from Pyewacket import choice
from monsters.monster import Monster
from monsters.utilities import Printable, mean


def random_monster_name():
    element = ['Flaming', 'Storm', 'Lightning', 'Stone']
    types = ['Dragon', 'Giant', 'Spirit']
    raw_monsters = set()
    while len(raw_monsters) < 12:
        raw_monsters.add(f"{choice(element)} {choice(types)}")
    return raw_monsters


class Dungeon(Printable):

    def __init__(self, name, level):
        self.name = name
        self.rooms = {
            f"Room {room_number+1}": Monster(level, name)
            for room_number, name in enumerate(random_monster_name())
        }

    def __str__(self):
        output = (
            f"Name: {self.name}\n",
            "\n".join(f"{room}: \n{monster}\n" for room, monster in self.rooms.items()),
        )
        return '\n'.join(output)

    def summary(self):
        defenses = []
        offenses = []
        healths = []
        for monster in self.rooms.values():
            defenses.append(monster.defense)
            offenses.append(monster.offense)
            healths.append(monster.health)
        output = (
            f"{self.name} Summary",
            f"Offense: {mean(offenses):.2f}",
            f"Defense: {mean(defenses):.2f}",
            f"Health: {mean(healths):.2f}",
        )
        return "\n".join(output)


if __name__ == '__main__':

    print(Dungeon("Starter Dungeon", 100).summary())
