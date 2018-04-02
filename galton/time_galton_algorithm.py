import timeit
import random

def get_ball_bucket():
    return [random.choice("LR") for _ in range(7)].count("R")

def run_sim(n):
    simulation = [0] * (8)

    for _ in range(n):
        simulation[get_ball_bucket()] += 1

for n in [100, 1000, 10000, 50000, 100000, 1000000]:
    results = timeit.timeit('run_sim(%d)' % n, setup="from __main__ import run_sim", number=10) / 10
    print('for %d balls, it took an average of %s seconds.' % (n, str(results)))