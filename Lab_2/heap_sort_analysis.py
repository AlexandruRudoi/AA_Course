import matplotlib.pyplot as plt
from heap_sort import HeapSort
from sorting_benchmark import benchmark_sorting
from sorting_visualization import live_visualize_sorting
import random


def main():
    sizes = [10, 100, 300, 1000, 5000, 10_000,
             50_000, 100_000, 500_000, 1_000_000]
    sorter = HeapSort()

    print("\n--- HeapSort Performance Analysis ---")
    print(f"{'Size':<15} {'Standard Time (s)':<25} {'Improved Time (s)':<25}")
    print("-" * 70)

    standard_times = benchmark_sorting(sorter.heap_sort, sizes)
    improved_times = benchmark_sorting(sorter.heap_sort_improved, sizes)

    for i in range(len(sizes)):
        print(
            f"{sizes[i]:<15} {standard_times[i]:<25.6f} {improved_times[i]:<25.6f}")

    print("\n--- Time Complexity Analysis ---")
    print("Standard HeapSort:  O(n log n) in all cases")
    print("Improved HeapSort (Floyd's Heap Construction): O(n log n), optimized for fewer swaps")

    print("\n--- Space Complexity Analysis ---")
    print("Standard HeapSort: O(1) (in-place sorting)")
    print("Improved HeapSort: O(1), but uses optimized heap building for cache efficiency")

    plt.figure(figsize=(10, 5))
    plt.plot(sizes, standard_times, marker="o",
             label="Standard HeapSort", linestyle="--", color="red")
    plt.plot(sizes, improved_times, marker="s",
             label="Improved HeapSort", linestyle="-", color="blue")
    plt.xlabel("Array Size")
    plt.ylabel("Time (seconds)")
    plt.title("HeapSort vs Improved HeapSort Performance on Small & Large Inputs")
    plt.legend()
    plt.grid(True)
    plt.xscale("log")
    plt.yscale("log")
    plt.show()

    # Live Visualization
    arr = [random.randint(1, 100) for _ in range(50)]
    print("\nVisualizing Standard HeapSort...")
    live_visualize_sorting(lambda s, a: s.heap_sort_generator(
        a, use_improved=False), arr, HeapSort())


if __name__ == "__main__":
    main()
