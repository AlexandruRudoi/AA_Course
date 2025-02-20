import time
import matplotlib.pyplot as plt
import pandas as pd

# Naïve Recursive Fibonacci Calculation - This is the slowest method but serves as a baseline to show inefficiency.
# Time Complexity: O(2ⁿ) (Terrible for large n)
# Space Complexity: O(n) (Recursive stack)
def nth_fibonacci_recursive(n):
    if n <= 1:
        return n
    return nth_fibonacci_recursive(n - 1) + nth_fibonacci_recursive(n - 2)


def measure_performance_recursive():
    test_numbers = [1, 5, 10, 15, 20, 25, 30]
    execution_times = []

    for n in test_numbers:
        start_time = time.perf_counter()
        nth_fibonacci_recursive(n)
        end_time = time.perf_counter()
        execution_times.append((end_time - start_time) * 1000)
    
    # Convert execution times into a Pandas DataFrame for formatted output
    df = pd.DataFrame([execution_times], columns=test_numbers)

    # Print execution times as a table
    print("\nExecution Times using Naïve Recursion (O(2ⁿ))")
    print(df.to_string(index=False))

    # Plot the performance graph
    plt.figure(figsize=(10, 6))
    plt.plot(test_numbers, execution_times, marker="o",
             color="r", label="Recursive (O(2ⁿ))")
    plt.xlabel("n (Fibonacci Index)")
    plt.ylabel("Execution Time (ms)")
    plt.title("Fibonacci Calculation Performance (Naïve Recursion)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    measure_performance_recursive()
