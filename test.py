import random
import numpy as np
import torch


"""
create a random grid with 0 and 1
"""

def make2DArray(cols, rows):
  return torch.randint(1, (rows, cols))  

if __name__ == '__main__':
  rows, cols = 10, 10
  grid = make2DArray(cols, rows) 
  #print(grid)
  grid[5][5] = 1
  print(grid)
  next_grid = make2DArray(cols, rows)
  for i in range(cols):
    for j in range(rows):
      state = grid[i][j]
      if state == 1:
        below = grid[i][j+1]
        if below == 0:
          next_grid[i][j] = 0
          next_grid[i][j+1] = 1

  grid = next_grid
  print(grid)
