import time
import matplotlib.pyplot as plt
from fibonacci_recursive import nth_fibonacci_recursive
from fibonacci_memoization import nth_fibonacci_memoization
from fibonacci_bottom_up import nth_fibonacci_bottom_up
from fibonacci_space_optimized import nth_fibonacci_space_optimized
from fibonacci_matrix import nth_fibonacci_matrix
from fibonacci_binet import nth_fibonacci_binet
from fibonacci_fast_doubling import nth_fibonacci_fast

# Benchmark function
def benchmark_fibonacci(func, test_numbers):
    execution_times = []
    
    for n in test_numbers:
        start_time = time.perf_counter()
        func(n)
        end_time = time.perf_counter()
        execution_times.append((end_time - start_time) * 1000)  # Convert to ms
    
    return execution_times

if __name__ == "__main__":
    # Define test cases
    test_numbers = [1, 20, 40, 70, 100, 200, 500, 1000, 5000, 10000, 50000]
    test_numbers_small = [1, 5, 10, 15, 20, 25, 30]
    test_numbers_binet = [1, 5, 10, 15, 20, 30, 40, 50, 60, 70]  # Limited for Binet

    # Collect execution times for each Fibonacci method
    times_recursive = benchmark_fibonacci(nth_fibonacci_recursive, test_numbers_small)
    times_memoization = benchmark_fibonacci(nth_fibonacci_memoization, test_numbers)
    times_bottom_up = benchmark_fibonacci(nth_fibonacci_bottom_up, test_numbers)
    times_space_optimized = benchmark_fibonacci(nth_fibonacci_space_optimized, test_numbers)
    times_matrix = benchmark_fibonacci(nth_fibonacci_matrix, test_numbers)
    times_binet = benchmark_fibonacci(nth_fibonacci_binet, test_numbers_binet)
    times_fast_doubling = benchmark_fibonacci(nth_fibonacci_fast, test_numbers)

    # Plot all performance results in one graph
    plt.figure(figsize=(12, 7))

    plt.plot(test_numbers_small, times_recursive, 'r-o', label="Recursive (O(2ⁿ))")
    plt.plot(test_numbers, times_memoization, 'b-o', label="Memoization (O(n))")
    plt.plot(test_numbers, times_bottom_up, 'g-o', label="Bottom-Up DP (O(n))")
    plt.plot(test_numbers, times_space_optimized, 'c-o', label="Space-Optimized (O(n))")
    plt.plot(test_numbers, times_matrix, 'm-o', label="Matrix Exponentiation (O(log n))")
    plt.plot(test_numbers_binet, times_binet, 'y-o', label="Binet Formula (O(1))")
    plt.plot(test_numbers, times_fast_doubling, 'k-o', label="Fast Doubling (O(log n))")

    plt.xlabel("n (Fibonacci Index)")
    plt.ylabel("Execution Time (ms)")
    plt.title("Fibonacci Algorithm Performance Comparison")
    plt.legend()
    plt.yscale("log")  # Log scale for better visualization
    plt.grid(True)

    # Show all implementations in one plot
    plt.show()
