import virtual_display_controller as outD
import numpy as np
#main running code
if __name__ == '__main__':
    a = [(1, 1, 1, 1, 1, 1)]
    for i in range(2, 15):
        a.append((i, i, i, i, i, i))
    grid = np.array(a)
    outD.showTableState(grid)