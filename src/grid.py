import numpy as np
import copy

class Grid:
    gridMatrix: np.array
    def __init__(self, rows, cols):
        self.gridMatrix = np.random.randint(0, 2, (rows, cols))

    def copy(self):
        return copy.deepcopy(self)
    
    def set(self, row, col, value):
        self.gridMatrix[row, col] = value

    def get(self, row, col):
        return self.gridMatrix[row, col]
    
    def getGrid(self):
        return self.gridMatrix.shape

    def recursive_print(self):
        def aux_recursive_print(self, row, col):
            if(row == self.getGrid()[0]):
                return
            char = '.'
            if self.get(row, col):
                char = '*'
            print(char, end=" ")
            col = (col + 1 ) % self.getGrid()[1]
            if col == 0:
                row = (row + 1)
                print("")
            aux_recursive_print(self, row, col)
        aux_recursive_print(self, 0, 0)
 

    def get_alive_neighbours(self, row, col):
        result = 0
        if row > 0:
            if col > 0:
                result += self.get(row-1, col-1)
            
            result += self.get(row-1, col)
            
            if col + 1 < self.getGrid()[1]:
                result += self.get(row-1, col+1)
        
        if col > 0:
            result += self.get(row, col-1)
        if col + 1 < self.getGrid()[1]:
            result += self.get(row, col+1)
        
        if row + 1 < self.getGrid()[0]:
            if col > 0:
                result += self.get(row+1, col-1)
            
            result += self.get(row+1, col)
            
            if col + 1 < self.getGrid()[1]:
                result += self.get(row+1, col+1)
        
        return result

    def is_alive(self, row, col):
        if self.get(row, col) == 1:
            return (self.get_alive_neighbours(row, col) in (2, 3))
        
        return (self.get_alive_neighbours(row, col) == 2)
    
    def recursive_update_grid(self):
        def aux_recursive_update_grid(self, row, col, old_grid):
            if(row == self.getGrid()[0]):
                return

            self.set(row, col, 0)
            if  old_grid.is_alive(row, col):
                self.set(row, col, 1)

            col = (col + 1 ) % self.getGrid()[1]
            if col == 0:
                row = (row + 1)
            aux_recursive_update_grid(self, row, col, old_grid)

        old_grid = self.copy()
        aux_recursive_update_grid(self, 0, 0, old_grid)