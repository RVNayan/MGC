import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

def cos_angle(v1 ,v2):
    temp1 = (np.sum(v1 ** 2)) ** 0.5
    temp2 = (np.sum(v2 ** 2)) ** 0.5
    return (np.dot(v1, v2)) / (temp1 * temp2) 

# print(cos_angle(np.array([1, 1, 0]),np.array([1, 0,0])))

def points_generator(ai, A):
    T = 2   #nno of datapoints (default)
    a = np.linspace(ai, A, T)
    return a


def linear_motion(xi, yi, zi, X, Y, Z, feed):
    V = np.concatenate((X, Y, Z),axis = 0)
    xaxis = np.array([1,0,0])
    yaxis = np.array([0,1,0])

    cos_theta = cos_angle(V, yaxis)
    sin_theta = (1 - cos_theta ** 2) ** 0.5

    cos_phi = cos_angle(np.array([V[0],V[1],0]), xaxis)
    sin_phi = (1 - cos_phi ** 2) ** 0.5

    v_x = np.array(feed[0] * sin_theta * cos_phi)
    v_y = np.array(feed[0] * cos_theta)
    v_z = np.array(feed[0] * sin_theta * sin_phi)

    x = points_generator(xi[0], X[0])
    y = points_generator(yi[0], Y[0])
    z = points_generator(zi[0], Z[0])

    return [x, y, z, v_x, v_y, v_z]


# Generating Data Points and testing

# xi = [1]
# yi = [2]
# zi = [3]

# X = [1]
# Y = [4]
# Z = [3]
# speed = [0.5]
# print(linear_motion(xi, yi, zi, X, Y, Z, speed))

# dataSet = np.array(linear_motion(xi, yi, zi, X, Y, Z, speed))
# # t = np.linspace(0, (X[0] - xi[0]) / speed[0], 10)  # Time array, must be replaced

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# line_ani = animation.FuncAnimation(fig, animate_func, interval=100, frames=len(dataSet[0]))
# plt.show()
