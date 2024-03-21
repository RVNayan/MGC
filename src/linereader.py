import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

from func import linear_motion

def decoder(line_data): #takes numpy data  
    #return param
    gcode = []
    mcode = []
    X = []
    Y = []
    Z = []
    F = []
    S = []

    linelen = len(line_data)
    for idx, data in enumerate(line_data):
        type = data[0]
        if (type[0] == 'G'):
            gcode.append(float(type[1:]))
    
        elif (type[0] == 'X'):
            X.append(float(type[1:]))

        elif (type[0] == 'Y'):
            Y.append(float(type[1:]))

        elif (type[0] == 'Z'):
            Z.append(float(type[1:]))

    return gcode,X,Y,Z
        
def animate_func(num, ax, dataSet):
    ax.clear()  
    ax.plot3D(dataSet[0, :num+1], dataSet[1, :num+1], 
              dataSet[2, :num+1], c='blue')
    ax.scatter(dataSet[0, num], dataSet[1, num], dataSet[2, num], 
               c='blue', marker='o')
    ax.plot3D(dataSet[0, 0], dataSet[1, 0], dataSet[2, 0],     
               c='black', marker='o')
    ax.set_xlim3d([-10, 10])
    ax.set_ylim3d([-10, 10])
    ax.set_zlim3d([0, 10])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

#change the way the animations are triggeredd, compute the trajectory and give the entire datapoints as inputs: [X,Y,Z,time or speed]
def func_decoder(fig,xi, yi, zi, gcode, mcode, X, Y, Z, F, S):
    ax = plt.axes(projection='3d')  # Define ax here

    for idx, data in enumerate(gcode):
        if (data == 0):
            custom_vel = 10
            datapoints = np.array(linear_motion(xi, yi, zi, X, Y, Z, custom_vel))
            line_ani = animation.FuncAnimation(fig, animate_func, interval=100, frames=len(datapoints[0]),
                                               fargs=(ax, datapoints))

        elif (data == 1):
            feed = F
            datapoints = np.array(linear_motion(xi, yi, zi, X, Y, Z, feed))
            line_ani = animation.FuncAnimation(fig, animate_func, interval=100, frames=len(datapoints[0]),
                                               fargs=(ax, datapoints))

    plt.show()


