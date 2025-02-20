import time
import matplotlib.pyplot as plt
import pandas as pd

# Define a safe recursion depth limit
SAFE_RECURSION_LIMIT = 999  # Adjust based on testing

# Memoization is a technique used to store the results of expensive function calls and return the cached result when the same inputs occur again.
# Time Complexity: O(n) (Linear time complexity)
# Space Complexity: O(n) (Memoization table) (Due to recursion + dictionary)
def nth_fibonacci_util(n, memo):
    if n <= 1:
        return n
    if memo[n] != -1:
        return memo[n]
    memo[n] = nth_fibonacci_util(n - 1, memo) + nth_fibonacci_util(n - 2, memo)
    return memo[n]

def nth_fibonacci_memoization(n):
    if n > SAFE_RECURSION_LIMIT:
        print(f"Skipping n={n} as it exceeds the safe recursion limit ({SAFE_RECURSION_LIMIT})")
        return None
    
    memo = [-1] * (n + 1)
    return nth_fibonacci_util(n, memo)

def measure_performance_memoization():
    test_numbers = [1, 20, 40, 70, 100, 130, 200, 250, 400, 500]
    execution_times = []

    for n in test_numbers:
        start_time = time.perf_counter()
        nth_fibonacci_memoization(n)
        end_time = time.perf_counter()
        execution_times.append((end_time - start_time) * 1000)
    
    # Convert execution times into a Pandas DataFrame for formatted output
    df = pd.DataFrame([execution_times], columns=test_numbers)

    # Print execution times as a table
    print("\nExecution Times using Memoization (O(n))")
    print(df.to_string(index=False))

    # Plot the performance graph
    plt.figure(figsize=(10, 6))
    plt.plot(test_numbers, execution_times, marker="o", color="b", label="Memoization (O(n))")
    plt.xlabel("n (Fibonacci Index)")
    plt.ylabel("Execution Time (ms)")
    plt.title("Fibonacci Calculation Performance (Memoization)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    measure_performance_memoization()
