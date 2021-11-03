import virtual_display_controller as outD
import numpy as np
import grid_controller as gc
#main running code
if __name__ == '__main__':
    grid = gc.create_flat_grid()
#    grid = gc.create_grid_from_array([1,2,3,7,2,5,6,1,2], 3, 3)
    print (grid)
    outD.showTableState(grid)