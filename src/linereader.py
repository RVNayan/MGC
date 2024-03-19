def decoder(line_data): #takes numpy data  
    #return param
    gcode = []
    X = []
    Y = []
    Z = []
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
        