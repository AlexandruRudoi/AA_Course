import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


def live_visualize_sorting(sort_func, arr, sorter, delay=0):
    """ Live sorting visualization using Matplotlib animation """
    generator = sort_func(sorter, arr)

    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    ax.set_ylim(0, max(arr) * 1.1)

    def update(frame):
        for rect, val in zip(bar_rects, frame):
            rect.set_height(val)

        time.sleep(delay / 1000)  # Slow down sorting by adding a delay
        return bar_rects

    ani = animation.FuncAnimation(
        fig, update, frames=generator, interval=100, repeat=False, save_count=1000)
    plt.show()
