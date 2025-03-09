import time
import matplotlib.pyplot as plt
import pandas as pd

# Fast Doubling Method: F(2n) = F(n) * (2 * F(n + 1) - F(n)), F(2n + 1) = F(n + 1)^2 + F(n)^2
# Best for massive Fibonacci numbers (e.g., n = 10⁶).
# Time Complexity: O(log n) - Logarithmic Time Complexity
# Space Complexity: O(log n) - (Recursive depth)
def nth_fibonacci_fast_doubling(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = nth_fibonacci_fast_doubling(n // 2)
        c = a * ((b << 1) - a)
        d = a * a + b * b
        return (c, d) if n % 2 == 0 else (d, c + d)


def nth_fibonacci_fast(n):
    return nth_fibonacci_fast_doubling(n)[0]


def measure_performance_fast_doubling():
    test_numbers = [1, 20, 40, 70, 100, 200, 500, 1000, 5000, 10000, 50000]
    execution_times = []

    for n in test_numbers:
        start_time = time.perf_counter()
        nth_fibonacci_fast(n)
        end_time = time.perf_counter()
        execution_times.append((end_time - start_time) * 1000)

    # Convert execution times into a Pandas DataFrame for formatted output
    df = pd.DataFrame([execution_times], columns=test_numbers)

    # Print execution times as a table
    print("\nExecution Times for Fast Doubling (O(log n)):\n")
    print(df.to_string(index=False))

    # Plot the performance graph
    plt.figure(figsize=(10, 6))
    plt.plot(test_numbers, execution_times, marker="o",
             color="k", label="Fast Doubling (O(log n))")
    plt.xlabel("n (Fibonacci Index)")
    plt.ylabel("Execution Time (ms)")
    plt.title("Fibonacci Calculation Performance (Fast Doubling)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    measure_performance_fast_doubling()
