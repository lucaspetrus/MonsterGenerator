import unittest

from monsters.dungeon import Dungeon


class DungeonTest(unittest.TestCase):

    def test_monsters(self):
        d = Dungeon("Test Dungeon", 1)
        self.assertEqual(len(d.rooms), 12)
        seen_names = []
        for monster in d.rooms.values():
            seen_names.append(monster.name)
        for _ in range(12):
            name = seen_names.pop(0)
            self.assertNotIn(name, seen_names)
            seen_names.append(name)


if __name__ == '__main__':
    unittest.main()
