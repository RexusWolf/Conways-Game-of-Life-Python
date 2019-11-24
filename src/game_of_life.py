import grid as g
import os
from time import sleep

class GameOfLife:
    state: g.Grid

    def __init__(self, rows, cols):
        self.state = g.Grid(rows, cols)

    
    def next_generation(self):
        self.state.recursive_update_grid()
        os.system('clear')
    
    def show(self):
        self.state.recursive_print()
        
if(__name__ == '__main__'):
    gameOfLife = GameOfLife(20, 20) 
    while 1:
        gameOfLife.show()
        sleep(0.5)
        gameOfLife.next_generation()