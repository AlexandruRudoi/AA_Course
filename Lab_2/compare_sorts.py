import matplotlib.pyplot as plt
from sorting_benchmark import benchmark_sorting
from heap_sort import HeapSort
from merge_sort import MergeSort
from quick_sort import QuickSort
from radix_sort import RadixSort


def main():
    sizes = [10, 100, 300, 1000, 5000, 10_000,
             50_000, 100_000, 500_000, 1_000_000]

    heap_sorter = HeapSort()
    merge_sorter = MergeSort()
    quick_sorter = QuickSort()
    radix_sorter = RadixSort()

    print("\n--- Sorting Algorithms Performance Analysis ---")
    print(f"{'Size':<15} {'HeapSort (s)':<20} {'HeapSort Opt (s)':<20} "
          f"{'MergeSort (s)':<20} {'MergeSort Opt (s)':<20} "
          f"{'QuickSort (s)':<20} {'QuickSort Opt (s)':<20} "
          f"{'RadixSort (s)':<20} {'RadixSort Opt (s)':<20}")
    print("-" * 160)

    heap_times = benchmark_sorting(heap_sorter.heap_sort, sizes)
    heap_opt_times = benchmark_sorting(heap_sorter.heap_sort_improved, sizes)
    merge_times = benchmark_sorting(merge_sorter.merge_sort, sizes)
    merge_opt_times = benchmark_sorting(
        merge_sorter.merge_sort_optimized, sizes)
    quick_times = benchmark_sorting(quick_sorter.quick_sort, sizes)
    quick_opt_times = benchmark_sorting(
        quick_sorter.quick_sort_improved, sizes)
    radix_times = benchmark_sorting(radix_sorter.radix_sort, sizes)
    radix_opt_times = benchmark_sorting(
        radix_sorter.radix_sort_improved, sizes)

    for i in range(len(sizes)):
        print(f"{sizes[i]:<15} {heap_times[i]:<20.6f} {heap_opt_times[i]:<20.6f} "
              f"{merge_times[i]:<20.6f} {merge_opt_times[i]:<20.6f} "
              f"{quick_times[i]:<20.6f} {quick_opt_times[i]:<20.6f} "
              f"{radix_times[i]:<20.6f} {radix_opt_times[i]:<20.6f}")

    # Plot results
    plt.figure(figsize=(12, 7))

    plt.plot(sizes, heap_times, marker="o",
             label="HeapSort", linestyle="--", color="blue")
    plt.plot(sizes, heap_opt_times, marker="o",
             label="HeapSort Opt", linestyle="-", color="cyan")

    plt.plot(sizes, merge_times, marker="s",
             label="MergeSort", linestyle="--", color="red")
    plt.plot(sizes, merge_opt_times, marker="s",
             label="MergeSort Opt", linestyle="-", color="orange")

    plt.plot(sizes, quick_times, marker="d",
             label="QuickSort", linestyle="--", color="green")
    plt.plot(sizes, quick_opt_times, marker="d",
             label="QuickSort Opt", linestyle="-", color="lime")

    plt.plot(sizes, radix_times, marker="^",
             label="RadixSort", linestyle="--", color="purple")
    plt.plot(sizes, radix_opt_times, marker="^",
             label="RadixSort Opt", linestyle="-", color="magenta")

    plt.xlabel("Array Size")
    plt.ylabel("Time (seconds)")
    plt.title("Sorting Algorithms Performance Comparison")
    plt.legend()
    plt.grid(True)
    plt.xscale("log")
    plt.yscale("log")
    plt.show()


if __name__ == "__main__":
    main()
