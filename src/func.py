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

def animate_func(num):
    ax.clear()  
    ax.plot3D(dataSet[0, :num+1], dataSet[1, :num+1], 
              dataSet[2, :num+1], c='blue')
    ax.scatter(dataSet[0, num], dataSet[1, num], dataSet[2, num], 
               c='blue', marker='o')
    ax.plot3D(dataSet[0, 0], dataSet[1, 0], dataSet[2, 0],     
               c='black', marker='o')
    ax.set_xlim3d([-1, 1])
    ax.set_ylim3d([-1, 1])
    ax.set_zlim3d([0, 100])
    ax.set_title('Trajectory \nTime = ' + str(np.round(t[num],    
                 decimals=2)) + ' sec')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

# Generating Data Points
xi = [1]
yi = [2]
zi = [3]
X = [1]
Y = [4]
Z = [3]
speed = [0.5]
dataSet = np.array(linear_motion(xi, yi, zi, X, Y, Z, speed))
t = np.linspace(0, (X[0] - xi[0]) / speed[0], 10)  # Time array, must be replaced

fig = plt.figure()
ax = plt.axes(projection='3d')
line_ani = animation.FuncAnimation(fig, animate_func, interval=100, frames=len(dataSet[0]))
plt.show()
