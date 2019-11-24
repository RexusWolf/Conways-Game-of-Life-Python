import unittest
from src.grid import *


class TestGrid(unittest.TestCase):
    def test_grid_init(self):
        grid = Grid(10, 10)
        self.assertEqual((10,10),grid.getGrid())

    def test_grid_setter_getter(self):
        grid = Grid(10,10)
        grid.set(5, 5, 0)
        self.assertEqual(grid.get(5, 5), 0)
    def test_grid_get_alive_neighbours(self):
        grid = Grid(3,3)
        grid.set(0, 0, 1)
        grid.set(0, 1, 1)
        grid.set(0, 2, 1)
        grid.set(1, 0, 1)
        grid.set(1, 1, 0)
        grid.set(1, 2, 1)
        grid.set(2, 0, 1)
        grid.set(2, 1, 1)
        grid.set(2, 2, 1)

        self.assertEqual(grid.get_alive_neighbours(1, 1), 8)
    
    def test_grid_get_neighbors(self):
        grid = Grid(3,3)
        grid.set(0, 0, 0)
        grid.set(0, 1, 1)
        grid.set(0, 2, 0)
        grid.set(1, 0, 0)
        grid.set(1, 1, 1)
        grid.set(1, 2, 0)
        grid.set(2, 0, 0)
        grid.set(2, 1, 1)
        grid.set(2, 2, 0)
        self.assertEqual(grid.get_alive_neighbours(1, 1), 2)

    def test_grid_update(self):
        grid = Grid(4,4)
        grid.set(0, 0, 0)
        grid.set(0, 1, 1)
        grid.set(0, 2, 0)
        grid.set(0, 3, 0)
        grid.set(1, 0, 1)
        grid.set(1, 1, 0)
        grid.set(1, 2, 1)
        grid.set(1, 3, 0)
        grid.set(2, 0, 0)
        grid.set(2, 1, 0)
        grid.set(2, 2, 1)
        grid.set(2, 3, 1)
        grid.set(3, 0, 1)
        grid.set(3, 1, 1)
        grid.set(3, 2, 0)
        grid.set(3, 3, 1)
        self.assertEqual(grid.get_alive_neighbours(0, 0), 2)
        grid.recursive_update_grid()
        self.assertEqual(grid.get_alive_neighbours(1, 3), 3)