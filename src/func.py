import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

def points_generator(ai, A, speed):
    T = (A - ai) / speed  
    t = np.linspace(0, T, 10)
    a = ai + speed * t
    return a

def linear_motion(xi, yi, zi, X, Y, Z, speed):
    x = points_generator(xi[0], X[0], speed[0])
    y = points_generator(yi[0], Y[0], speed[0])
    z = points_generator(zi[0], Z[0], speed[0])
    return x, y, z


# Generating Data Points and testing

# xi = [1]
# yi = [2]
# zi = [3]

# X = [1]th
# Y = [4]
# Z = [3]
# speed = [0.5]

# dataSet = np.array(linear_motion(xi, yi, zi, X, Y, Z, speed))
# # t = np.linspace(0, (X[0] - xi[0]) / speed[0], 10)  # Time array, must be replaced

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# line_ani = animation.FuncAnimation(fig, animate_func, interval=100, frames=len(dataSet[0]))
# plt.show()
