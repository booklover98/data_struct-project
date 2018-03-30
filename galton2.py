import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import random

board_size = 7

def get_ball_bucket():
    return [random.choice("LR") for _ in range(board_size)].count("R")

def galton_animate(n):
    fig, ax = plt.subplots()

    # simulation = [get_ball_bucket() for _ in range(n)]
    x = range(0, board_size + 1)
    simulation = [0] * (board_size + 1)
    plot = plt.bar (x, simulation)

    def animate(i):
        if i % 1000 == 0:
            print(i/n)
        if i < n:
            simulation[get_ball_bucket()] += 1 # drop a random ball
        for bar, y in zip(plot, simulation):
            bar.set_height(y)
        ax.relim()
        ax.autoscale_view(True,True,True)


    ani = animation.FuncAnimation(fig, animate, n + 10,
                                interval=500/n, blit=False, repeat=False)
    # Set up formatting for the movie files
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=30, metadata=dict(artist='Me'), bitrate=1800)

    ani.save(str(n) + '_balls.mp4', writer=writer)
    print("Done simulation for " + str(n) + " balls!")

if __name__ == "__main__":
    for n in [100, 1000, 10000, 50000, 100000, 1000000]:
        galton_animate(n)