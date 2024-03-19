#Dont use semicolons at the end of a command


import pandas as pd
import numpy as np
from linereader import decoder

text_file_path = "../code/acode.txt"
df = pd.read_csv(text_file_path, sep=" ", header=None)
df = df.dropna(how='all')


arrays_collection = df.apply(lambda row: row.str.rstrip(';')).values.tolist()

lines_data = [[str(item)] for sublist in arrays_collection for item in sublist]
print(decoder(lines_data))
print(lines_data)           # Extra zero in the middle (?)
