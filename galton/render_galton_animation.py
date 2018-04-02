import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import random

BOARD_SIZE = 7 # how many pegs on the bottom-most row of the board
VIDEO_LENGTH = 10  # desired video length in seconds
FPS = 30 # frames per second for the video


def get_ball_bucket():
    # simulate a ball falling down a galton board.
    # a ball may fall left or right at any given peg with 50% chance.
    # this function makes BOARD_SIZE many choices and counts the number of right choices,
    # thus determining which bucket it would fall into at the bottom.
    return [random.choice("LR") for _ in range(BOARD_SIZE)].count("R")


def galton_animate(num_balls):
    fig, ax = plt.subplots() # get axes from matplotlib to plot

    x = range(0, BOARD_SIZE + 1) # a board with n pegs on the bottom row has n+1 spaces for balls to fall into
    simulation = [0] * (BOARD_SIZE + 1) # create an empty array to keep track of fallen balls
    plot = plt.bar(x, simulation) # create an empty bar plot, to be updated later
    ball_counter = 0 # since we want to simulate more than one ball per video frame, keep track of how many balls we've dropped so far
    frames = VIDEO_LENGTH * FPS # calculate the total number of frames

    balls_per_frame = max(num_balls // frames, 1) # drop at least one ball per frame
    ax.annotate("balls: " + str(num_balls), xy=(0.75, 0.9), xycoords='axes fraction', fontsize=10,
                bbox=dict(facecolor='white', alpha=0.8),
                horizontalalignment='left', verticalalignment='bottom') # draw an indicator for how many balls this video is simulating

    def animate(i):
        # this function is run once per iteration of the simulation
        nonlocal ball_counter
        if ball_counter < num_balls: # make sure we don't drop too many balls
            for _ in range(balls_per_frame):
                if ball_counter >= num_balls:
                    return
                simulation[get_ball_bucket()] += 1  # drop a random ball
                ball_counter += 1
        for bar, y in zip(plot, simulation):
            bar.set_height(y) # update each bar on the bar plot
        ax.relim() # rescale the numbers on the axes
        ax.autoscale_view(True, True, True) # rescale the view to the axes and data.

    ani = animation.FuncAnimation(fig, animate, frames + FPS,
                                  interval=1/FPS, blit=False, repeat=False) # add one second of animation to see the finished board
    
    # Set up formatting for the movie files
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=FPS, metadata=dict(artist='Me'), bitrate=1800)

    # Render the animation to disk
    ani.save(str(num_balls) + '_balls.mp4', writer=writer)
    print("Done simulation for " + str(num_balls) + " balls!")


if __name__ == "__main__":
    # create animations for each given number of balls
    for n in [100, 1000, 10000, 50000, 100000, 1000000]:
        galton_animate(n)
