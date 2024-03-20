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
        

def func_decoder(xi, yi, zi, gcode, mcode, X, Y, Z, F, S):
    
    for idx, data in enumerate(gcode):
        if (data == 0):
            custom_vel = 10
            # call the animation function which moves the cutter to the desired X,Y,Z location 
            datapoints = np.array(linear_motion(xi, yi, zi, X, Y, Z, custom_vel))

        
        if (data == 1):
            # call the animation function which moves the cutter to the desired X,Y,Z location 
            linear_motion(xi, yi, zi, X, Y, Z, feed)

    