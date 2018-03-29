import random

execute = True

while execute:

    b_length = 20
    num_balls = n
    output = [0] * (b_length + 1)

    def ball():
        path = ""
        for a in range(0, b_length):
            direction = random.choice("LR")
            path += direction
        return path

    def location(str):
        x = [0]*(b_length + 1)
        A = str.count("L")
        B = str.count("R")
        if ((A - B) > 0):
                total = A - B
                x[int(b_length/2+total/2)] += 1
        elif ((B - A) > 0):
                total = B - A
                x[int(b_length/2+total/2)] += 1
        else:
                x[int(b_length/2)] += 1
        return x

    n = int(input("Enter number of balls: "))
    while num_balls > 0:
            ##print evolving 2d array
            ##loop with an exit case
            ##while running the program, or the trial is done, 
            ##update, print, update condition, have a break
            placement = location(ball())
            output = [x + y for x, y in zip(output, location(ball()))]
            num_balls -= 1

    if input("Calculate another board? [y/n]") == "n":
        execute = False