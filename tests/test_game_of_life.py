import unittest
from src.game_of_life import GameOfLife


class TestGameOfLife(unittest.TestCase):

    def test_next_generation(self):
        universe = GameOfLife(10, 10)
        self.assertEqual(universe.next_generation(), 'foo')
        


if __name__ == '__main__':
    unittest.main()