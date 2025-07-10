import math
import time


GRID_ROWS = 25
GRID_COLS = 25
GRID_CELLS = (GRID_ROWS * GRID_COLS)
ALIVE = '*'
DEAD = '.'


def cell_to_index(x, y):
    if x < 0:
        x = -x % GRID_ROWS
        x = GRID_COLS - x
    if y < 0:
        y = -y % GRID_COLS
        y = GRID_COLS - y
    if x >= GRID_ROWS:
        x = x % GRID_ROWS
    if y >= GRID_COLS:
        y = x % GRID_COLS

    return x*GRID_ROWS+y

def set_cell(grid, x, y, state):
    grid[cell_to_index(x, y)] = state

def get_cell(grid, x, y):
    return grid[cell_to_index(x, y)]

def set_grid(grid, state):
    for x in range(GRID_ROWS):
        for y in range(GRID_COLS):
            set_cell(grid, x, y, state)

def print_grid(grid):
    print("\x1b[3J\x1b[H\x1b[2J") #clear screen
    for x in range(GRID_ROWS):
        for y in range(GRID_COLS):
            print(get_cell(grid, x, y), end='', flush=True)
        print()

def update_grid(old, new):
    for x in range(GRID_ROWS):
        for y in range(GRID_COLS):
            if get_cell(old, x, y) == ALIVE:
                set_cell(old, x, y, DEAD)
                set_cell(new, x+1, y, ALIVE)

def main():
    old_grid = [DEAD] * GRID_CELLS
    new_grid = [DEAD] * GRID_CELLS

    set_grid(old_grid, DEAD)

    set_cell(old_grid, 0, 10, ALIVE)
    set_cell(old_grid, 0, 9, ALIVE)
    set_cell(old_grid, 0, 8, ALIVE)
    set_cell(old_grid, 0, 11, ALIVE)
    set_cell(old_grid, 0, 12, ALIVE)
    set_cell(old_grid, 0, 14, ALIVE)
    set_cell(old_grid, 0, 15, ALIVE)
    set_cell(old_grid, 1, 17, ALIVE)
    set_cell(old_grid, 1, 15, ALIVE)
    set_cell(old_grid, 2, 10, ALIVE)
    set_cell(old_grid, 2, 15, ALIVE)
    set_cell(old_grid, 1, 2, ALIVE)
    set_cell(old_grid, 1, 4, ALIVE)
    set_cell(old_grid, 1, 5, ALIVE)
    print_grid(old_grid)

    while True:
        update_grid(old_grid, new_grid)
        print_grid(new_grid)
        time.sleep(0.2)
        update_grid(new_grid, old_grid)
        print_grid(old_grid)
        time.sleep(0.2)


if __name__ == "__main__":
    main()
