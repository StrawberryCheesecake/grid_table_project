import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
import shared_vars as v

def normalize(values):
    average = np.mean(values)
    stdv = np.std(values)
    return (values-average)/stdv

def rescale(values):
    y = np.reshape(values, [-1, 1])
    min_max_scaler = preprocessing.MinMaxScaler()
    x = min_max_scaler.fit_transform(y)
    out = np.reshape(x, [-1, 1])
    return out

def scalemax10(values):
    return values/10

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
#    colorvals = rescale(z[0])
    colorvals = scalemax10(z[0])
#    colorvals = z[0]
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
    ax.set_xlim3d(0, v.max_x)
    ax.set_ylim3d(0, v.max_y)
    ax.set_zlim3d(0, v.max_z)
    plt.show()
    plt.clf()
