
import pandas as pd
import numpy as np
from linereader import decoder
from linereader import func_decoder

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

text_file_path = "../code/acode.txt"
df = pd.read_csv(text_file_path, sep=" ", header=None)
df = df.dropna(how='all')


arrays_collection = df.apply(lambda row: row.str.rstrip(';')).values.tolist()
lines_data = []
for lines in arrays_collection:
    line_data = [[str(item)] for item in lines]
    lines_data.append(line_data)

x,y,z = [0],[0],[0] #manual setup
mcode = [99]
F = [1]
S = [1]
path = []
for i in range(len(lines_data)):
    gcode, X, Y, Z = decoder(lines_data[i])
    func_decoder(path, x, y, z, gcode, mcode, X, Y, Z, F,S)
    x = X
    y = Y
    z = Z
print(path) #generated points and currosponding velocities