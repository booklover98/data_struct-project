import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim 
import numpy as np
import time

execute = True

while execute:
    
    start_time = time.time()
    n = int(input("Enter number of balls: "))
    length = 6
    num_balls = n
    output = [0] * (length+1)

    def ball():
        path = ""
        for a in range(0, length):
            direction = random.choice("LR")
            path += direction
        return path

    def location(str):
        x = [0]*(length + 1)
        A = str.count("L")
        B = str.count("R")
        if ((A - B) > 0):
                total = A - B
                x[int(length/2 - total/2)] += 1
        elif ((B - A) > 0):
                total = B - A
                x[int(length/2 + total/2)] += 1
        else:
                x[int(length/2)] += 1
        return x

    while num_balls > 0:
            placement = location(ball())
            output = [x + y for x, y in zip(output, location(ball()))]
            num_balls -= 1
            plt.hist()
            ## NOT WORKING PROPERLY!!!!

    print(output)
    end_time = time.time()
    print(str(end_time - start_time))
            

    if input("Calculate another board? [y/n]") == "n":
        execute = False