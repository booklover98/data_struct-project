import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import random

BOARD_SIZE = 7
VIDEO_LENGTH = 10  # seconds
FPS = 30


def get_ball_bucket():
    return [random.choice("LR") for _ in range(BOARD_SIZE)].count("R")


def galton_animate(num_balls):
    fig, ax = plt.subplots()

    x = range(0, BOARD_SIZE + 1)
    simulation = [0] * (BOARD_SIZE + 1)
    plot = plt.bar(x, simulation)
    ball_counter = 0
    frames = VIDEO_LENGTH * FPS

    balls_per_frame = max(num_balls // frames, 1)
    ax.annotate("balls: " + str(num_balls), xy=(0.75, 0.9), xycoords='axes fraction', fontsize=10,
                bbox=dict(facecolor='white', alpha=0.8),
                horizontalalignment='left', verticalalignment='bottom')
    def animate(i):
        nonlocal ball_counter
        if ball_counter < num_balls:
            for _ in range(balls_per_frame):
                if ball_counter >= num_balls:
                    return
                simulation[get_ball_bucket()] += 1  # drop a random ball
                ball_counter += 1
        for bar, y in zip(plot, simulation):
            bar.set_height(y)
        ax.relim()
        ax.autoscale_view(True, True, True)

    ani = animation.FuncAnimation(fig, animate, frames + FPS,
                                  interval=1/FPS, blit=False, repeat=False)
    # Set up formatting for the movie files
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=FPS, metadata=dict(artist='Me'), bitrate=1800)

    ani.save(str(num_balls) + '_balls.mp4', writer=writer)
    print("Done simulation for " + str(num_balls) + " balls!")


if __name__ == "__main__":
    for n in [100, 1000, 10000, 50000, 100000, 1000000]:
        galton_animate(n)
