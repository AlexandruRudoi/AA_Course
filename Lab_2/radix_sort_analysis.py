import matplotlib.pyplot as plt
from radix_sort import RadixSort
from sorting_benchmark import benchmark_sorting
from sorting_visualization import live_visualize_sorting
import random


def main():
    sizes = [10, 100, 300, 1000, 5000, 10_000,
             50_000, 100_000, 500_000, 1_000_000]
    sorter = RadixSort()

    print("\n--- Radix Sort Performance Analysis ---")
    print(f"{'Size':<15} {'Standard Time (s)':<25} {'Optimized Time (s)':<25}")
    print("-" * 70)

    standard_times = benchmark_sorting(sorter.radix_sort, sizes)
    optimized_times = benchmark_sorting(sorter.radix_sort_improved, sizes)

    for i in range(len(sizes)):
        print(
            f"{sizes[i]:<15} {standard_times[i]:<25.6f} {optimized_times[i]:<25.6f}")

    print("\n--- Time Complexity Analysis ---")
    print("Standard Radix Sort:  Best: O(nk), Worst: O(nk), Avg: O(nk)")
    print("Optimized Radix Sort (Bucket-based Counting Sort): Best: O(nk), Worst: O(nk), Avg: O(nk)")

    print("\n--- Space Complexity Analysis ---")
    print("Standard Radix Sort: O(n) (Requires additional storage)")
    print("Optimized Radix Sort: O(n) but reduces redundant comparisons")

    plt.figure(figsize=(10, 5))
    plt.plot(sizes, standard_times, marker="o",
             label="Standard Radix Sort", linestyle="--", color="red")
    plt.plot(sizes, optimized_times, marker="s",
             label="Optimized Radix Sort", linestyle="-", color="blue")
    plt.xlabel("Array Size")
    plt.ylabel("Time (seconds)")
    plt.title(
        "Radix Sort vs Optimized Radix Sort Performance on Small & Large Inputs")
    plt.legend()
    plt.grid(True)
    plt.xscale("log")
    plt.yscale("log")
    plt.show()

    # Live Visualization
    arr = [random.randint(1, 100) for _ in range(50)]
    print("\nVisualizing Standard Radix Sort...")
    live_visualize_sorting(lambda s, a: s.radix_sort_generator(
        a, use_improved=False), arr, RadixSort(), delay=400)


if __name__ == "__main__":
    main()
