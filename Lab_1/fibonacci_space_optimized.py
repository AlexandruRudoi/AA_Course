import time
import matplotlib.pyplot as plt
import pandas as pd

# Space-Optimized Iterative Fibonacci Calculation - Best for iterative solutions.
# Time Complexity: O(n) (Linear time complexity)
# Space Complexity: O(1) (Constant space complexity)
def nth_fibonacci_space_optimized(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def measure_performance_space_optimized():
    test_numbers = [1, 20, 40, 70, 100, 130, 200, 250, 400, 500]
    execution_times = []

    for n in test_numbers:
        start_time = time.perf_counter()
        nth_fibonacci_space_optimized(n)
        end_time = time.perf_counter()
        execution_times.append((end_time - start_time) * 1000)
    
     # Convert execution times into a Pandas DataFrame for formatted output
    df = pd.DataFrame([execution_times], columns=test_numbers)

    # Print execution times as a table
    print("\nExecution Times using Space-Optimized Iterative Fibonacci Calculation (O(n)):")
    print(df.to_string(index=False))

    # Plot the performance graph
    plt.figure(figsize=(10, 6))
    plt.plot(test_numbers, execution_times, marker="o",
             color="c", label="Space-Optimized (O(n))")
    plt.xlabel("n (Fibonacci Index)")
    plt.ylabel("Execution Time (ms)")
    plt.title("Fibonacci Calculation Performance (Space-Optimized Iterative)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    measure_performance_space_optimized()
