import matplotlib.pyplot as plt
from quick_sort import QuickSort
from sorting_benchmark import benchmark_sorting
from sorting_visualization import live_visualize_sorting
import random

def main():
    sizes = [10, 100, 300, 1000, 5000, 10_000, 50_000, 100_000, 500_000, 1_000_000]
    sorter = QuickSort()

    # Benchmark standard and improved QuickSort
    print("\n--- QuickSort Performance Analysis ---")
    print(f"{'Size':<15} {'Standard Time (s)':<25} {'Improved Time (s)':<25}")
    print("-" * 70)
    
    standard_times = benchmark_sorting(sorter.quick_sort, sizes)
    optimized_times = benchmark_sorting(sorter.quick_sort_improved, sizes)

    for i in range(len(sizes)):
        print(f"{sizes[i]:<15} {standard_times[i]:<25.6f} {optimized_times[i]:<25.6f}")

    print("\n--- Time Complexity Analysis ---")
    print("Standard QuickSort:  Best: O(n log n), Worst: O(n²), Avg: O(n log n)")
    print("Improved QuickSort (Median-of-Three): Best: O(n log n), Worst: O(n log n), Avg: O(n log n)")
    
    print("\n--- Space Complexity Analysis ---")
    print("Standard QuickSort: O(n) for recursion in worst case, O(log n) expected")
    print("Improved QuickSort: O(log n) (reduces stack depth using better pivot selection)")

    # Graph Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, standard_times, marker="o", label="Standard QuickSort", linestyle="--", color="red")
    plt.plot(sizes, optimized_times, marker="s", label="Improved QuickSort", linestyle="-", color="blue")
    plt.xlabel("Array Size")
    plt.ylabel("Time (seconds)")
    plt.title("QuickSort vs Improved QuickSort Performance")
    plt.legend()
    plt.grid(True)
    plt.xscale("log")
    plt.yscale("log")
    plt.show()

    # Live Visualization (Standard QuickSort)
    arr = [random.randint(1, 100) for _ in range(50)]
    print("\nVisualizing Standard QuickSort...")
    live_visualize_sorting(lambda s, a: s.quick_sort_generator(a, use_improved=False), arr)

if __name__ == "__main__":
    main()
