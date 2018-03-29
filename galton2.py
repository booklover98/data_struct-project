import random

board_size = 7

def get_ball_bucket():
    return [random.choice("LR") for _ in range(board_size)].count("R")

n = int(input("Enter number of balls: "))

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

simulation = [get_ball_bucket() for _ in range(n)]

def animate(i):
    x = range(0, board_size + 1)
    sim = simulation[0:i]
    arranged = {x: sim.count(x) for x in sorted(set(sim))}
    y = [0] * (board_size + 1)
    for k,v in arranged.items():
        y[k] = v
    return plt.bar (x, y)



ani = animation.FuncAnimation(fig, animate, n,
                              interval=25, blit=False)

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=60, metadata=dict(artist='Me'), bitrate=1800)

ani.save(str(n) + '_balls.mp4', writer=writer)