import time
import random

def benchmark_sorting(sort_func, sizes):
    """ Benchmark a sorting function execution time for different input sizes """
    times = []
    for size in sizes:
        arr = [random.randint(1, 10000) for _ in range(size)]
        start_time = time.perf_counter()
        sort_func(arr.copy())  # Use a copy to prevent modifying original array
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return times

def time_sorting_function(sort_func, arr):
    """ Time a sorting function on a given array """
    start_time = time.time()
    sort_func(arr)
    return time.time() - start_time
