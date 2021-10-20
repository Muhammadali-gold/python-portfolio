import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.array([[0, 0, 255], [255, 255, 0], [0, 255, 0]])
plt.imshow(x, interpolation='nearest')
plt.show()

def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0, 0, 255],
    [255, 0, 255],
    [0, 255, 255]])
    grid[i:i+3, j:j+3] = glider
N=3
grid = np.zeros(N*N).reshape(N, N)
addGlider(1, 1, grid)