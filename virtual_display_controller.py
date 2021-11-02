import matplotlib.pyplot as plt
import numpy as np

def normalize(values):
    average = np.mean(values)
    stdv = np.std(values)
    return (values-average)/stdv

def rescale(values):
    min = np.min(values)
    max = np.max(values)
    return (values-min)/(max-min)


def showTableState(grid):
    xlen = len(grid[0])
    ylen = len(grid)

    xVal = np.arange(0, xlen)
    yVal = np.arange(0, ylen)

    _xx, _yy = np.meshgrid(xVal, yVal)
    x, y = _xx.ravel(), _yy.ravel()
    z = np.reshape(grid, [1, xlen*ylen])
    bottom = np.zeros_like(z)
    width = length = np.ones_like(z)
    colorvals = rescale(z[0])
    colors = plt.cm.terrain(colorvals)

    #print (bottom)
    #print (width)
    #print (x)
    #print (y)
    #print (z)
    #print (colorvals)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.bar3d(x, y, bottom[0], width[0], length[0], z[0], shade=True, color=colors)

    plt.show()
    plt.clf()
