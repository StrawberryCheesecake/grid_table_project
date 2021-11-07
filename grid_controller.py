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
    a.fill(v.max_z/3)
    grid = []
    for i in range(0,y):
        grid.append(a)
    return np.array(grid)

def check_depth(grid, r_x, r_y):
    if v.max_z >= grid[r_x][r_y] >= 0:
        return True
    return False

def dig(grid, r_x, r_y):
    if check_depth(grid, r_x, r_y):
        grid[r_x][r_y] = grid[r_x][r_y] - 1
    return grid

def build(grid, r_x, r_y):
    if check_depth(grid, r_x, r_y):
        grid[r_x][r_y] = grid[r_x][r_y] + 1
    return grid

def big_build(grid, r_x, r_y):
    if check_depth(grid, r_x, r_y):
        grid[r_x][r_y] = grid[r_x][r_y] + 3
    return grid

def build_house(grid, r_x, r_y):
    for i in range(-2, 2):
        for j in range(-2, 2):
            test_x = r_x - i
            test_y = r_y - j
            if -2 < i < 1 and -2 < j < 1:
                continue
            if i == 1 and j ==0:
                continue
            if (len(grid[0]) > test_x > -1) and (len(grid) > test_y > -1) and check_depth(grid, test_x, test_y):
                #print (r_x - i, ', ', r_y - j)
                grid[r_x - i][r_y - j] = grid[r_x - i][r_y - j] + 3
    return grid

def create_river(grid, r_x, r_y):
    if check_depth(grid, r_x, r_y):
        grid[r_x][r_y] = grid[r_x][r_y] - 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            test_x = r_x - i
            test_y = r_y - j
            if (len(grid[0]) > test_x > -1) and (len(grid) > test_y > -1) and check_depth(grid, test_x, test_y):
                print (r_x - i, ', ', r_y - j)
                grid[r_x - i][r_y - j] = grid[r_x - i][r_y - j] - 1
    return grid
