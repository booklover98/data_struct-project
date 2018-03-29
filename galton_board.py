import random

while execute:

    b_length = 20
    num_balls = n

    def ball():
        path = ""
        for a in length:
            direction = random.choice("LR")
            path += direction
        return path

    def location(str):
        x = [0]*(length + 1)
        A = str.count("L")
        B = str.count("R")
        if (A - B > 0):
                total = A - B
                x[int(length/2+total/2)] += 1
            elif (B - A > 0):
                total = B - A
                x[int(length/2+total/2)] += 1
            else:
                x[int(length/2)] += 1
            return x

    n = int(input("Enter number of balls: "))
    for num_balls:
            ##print evolving 2d array
            ##loop with an exit case
            ##while running the program, or the trial is done, 
            ##update, print, update condition, have a break
            placement = location(ball())

    if input("Calculate another board? [y/n]") == "n":
        execute = False