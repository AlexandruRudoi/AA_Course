import matplotlib.pyplot as plt
from merge_sort import MergeSort
from sorting_benchmark import benchmark_sorting
from sorting_visualization import live_visualize_sorting
import random


def main():
    sizes = [10, 100, 300, 1000, 5000, 10_000,
             50_000, 100_000, 500_000, 1_000_000]
    sorter = MergeSort()

    print("\n--- MergeSort Performance Analysis ---")
    print(f"{'Size':<15} {'Standard Time (s)':<25} {'Optimized Time (s)':<25}")
    print("-" * 70)

    standard_times = benchmark_sorting(sorter.merge_sort, sizes)
    optimized_times = benchmark_sorting(sorter.merge_sort_optimized, sizes)

    for i in range(len(sizes)):
        print(
            f"{sizes[i]:<15} {standard_times[i]:<25.6f} {optimized_times[i]:<25.6f}")

    print("\n--- Time Complexity Analysis ---")
    print("Standard MergeSort:  O(n log n) in all cases")
    print("Optimized MergeSort (Insertion Sort for Small Partitions): O(n log n) but faster for small inputs")

    print("\n--- Space Complexity Analysis ---")
    print("Standard MergeSort: O(n) extra space for merging")
    print("Optimized MergeSort: O(n), but fewer recursive calls make it more cache-efficient")

    plt.figure(figsize=(10, 5))
    plt.plot(sizes, standard_times, marker="o",
             label="Standard MergeSort", linestyle="--", color="red")
    plt.plot(sizes, optimized_times, marker="s",
             label="Optimized MergeSort", linestyle="-", color="blue")
    plt.xlabel("Array Size")
    plt.ylabel("Time (seconds)")
    plt.title("MergeSort vs Optimized MergeSort Performance on Small & Large Inputs")
    plt.legend()
    plt.grid(True)
    plt.xscale("log")
    plt.yscale("log")
    plt.show()

    # Live Visualization
    arr = [random.randint(1, 100) for _ in range(50)]
    arr2 = arr.copy()
    print("\nVisualizing Standard MergeSort...")
    live_visualize_sorting(lambda s, a: s.merge_sort_generator(a, use_improved=False), arr, MergeSort())

    # Live Visualization of Optimized MergeSort
    print("\nVisualizing Optimized MergeSort...")
    live_visualize_sorting(lambda s, a: s.merge_sort_generator(a, use_improved=True), arr2, MergeSort())


if __name__ == "__main__":
    main()
