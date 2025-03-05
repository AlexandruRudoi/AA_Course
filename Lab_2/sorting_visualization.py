import matplotlib.pyplot as plt
import matplotlib.animation as animation
from quick_sort import QuickSort
import random


def live_visualize_sorting(sort_func, arr):
    """ Live sorting visualization using Matplotlib animation """
    sorter = QuickSort()
    generator = sort_func(sorter, arr)

    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    ax.set_ylim(0, max(arr) * 1.1)

    def update(frame):
        for rect, val in zip(bar_rects, frame):
            rect.set_height(val)
        return bar_rects

    ani = animation.FuncAnimation(
        fig, update, frames=generator, interval=100, repeat=False, save_count=1000)
    plt.show()
