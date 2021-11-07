import numpy as np
import shared_vars as v


def create_grid_from_array(array,x,y):
    if x > v.max_x or y > v.max_y:
        print('max dimensions exceeded')
        exit()
    if x*y != len(array):
        print ('incorrect dimension combination with array error')
        exit()
    grid = []
    for i in range(0,x):
        tempgrid = []
        for j in range(0,y):
            tempgrid.append(array[i*y +j ])
        grid.append(tempgrid)
    return np.array(grid)

def create_flat_grid(x=v.max_x, y=v.max_y):
    if x > v.max_x or y > v.max_y:
        print('max dimensions exceeded')
        exit()
    a = np.empty(x)
    a.fill(v.max_z/2)
    grid = []
    for i in range(0,y):
        grid.append(a)
    return np.array(grid)

def create_river(grid, r_x, r_y):
    grid[r_x][r_y] = grid[r_x][r_y] - 2
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (len(grid[0]) > r_x - i > -1) and (len(grid) > r_y - j > -1):
                print (r_x - i, ', ', r_y - j)
                grid[r_x - i][r_y - j] = grid[r_x - i][r_y - j] - 1
    return grid
