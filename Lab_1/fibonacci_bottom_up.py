import time
import matplotlib.pyplot as plt
import pandas as pd

# Bottom-Up Dynamic Programming Fibonacci Calculation - Faster than recursion but uses extra memory.
# Time Complexity: O(n) (Linear time complexity)
# Space Complexity: O(n) (DP table) (Array stores results)
def nth_fibonacci_bottom_up(n):
    if n <= 1:
        return n
    fib = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

def measure_performance_bottom_up():
    test_numbers = [1, 20, 40, 70, 100, 130, 200, 250, 400, 500]
    execution_times = []

    for n in test_numbers:
        start_time = time.perf_counter()
        nth_fibonacci_bottom_up(n)
        end_time = time.perf_counter()
        execution_times.append((end_time - start_time) * 1000)
    
    # Convert execution times into a Pandas DataFrame for formatted output
    df = pd.DataFrame([execution_times], columns=test_numbers)

    # Print execution times as a table
    print("\nExecution Times for Bottom-Up DP (O(n)):\n")
    print(df.to_string(index=False))
    
    # Plot the performance graph
    plt.figure(figsize=(10, 6))
    plt.plot(test_numbers, execution_times, marker="o", color="g", label="Bottom-Up DP (O(n))")
    plt.xlabel("n (Fibonacci Index)")
    plt.ylabel("Execution Time (ms)")
    plt.title("Fibonacci Calculation Performance (Bottom-Up DP)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    measure_performance_bottom_up()
