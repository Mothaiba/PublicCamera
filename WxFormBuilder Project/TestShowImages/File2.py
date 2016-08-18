import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import random
import sys


def drawChart(x = range(0, 30), y = np.random.randint(1, 10, 30), npoints = 30):

    fig, ax = plt.subplots()
    ax.scatter(x, y, color = 'cyan', lw=5)

    # ax.plot(x, y, 'cs', lw = 5)
    ax.plot(x, y, 'c', lw = 1)
    ax.set_ylim(0, 10, 10)
    ax.set_xlim(0, npoints, 5)
    ax.fill_between(x, 0, y, alpha = .2, color = 'cyan')
    ax.set(xlim = (0, len(x) - 1), ylim = (0, None))


    plt.grid()
    plt.xlabel('Time')
    plt.ylabel('Crowd Index')

    plt.show()

