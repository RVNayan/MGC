
import pandas as pd
import numpy as np
from linereader import decoder
from linereader import func_decoder

text_file_path = "../code/acode.txt"
df = pd.read_csv(text_file_path, sep=" ", header=None)
df = df.dropna(how='all')


arrays_collection = df.apply(lambda row: row.str.rstrip(';')).values.tolist()

lines_data = [[str(item)] for sublist in arrays_collection for item in sublist]

x,y,z = [0],[0],[0]
mcode = [99]
F = [1]
S = [1]
gcode, X, Y, Z = decoder(lines_data)
func_decoder(x,y,z, gcode, mcode, X,Y,Z,F,S)

#add functional for additional lines 