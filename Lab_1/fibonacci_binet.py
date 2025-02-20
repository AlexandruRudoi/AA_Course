import time
import matplotlib.pyplot as plt
import decimal
import pandas as pd

# Binet's Formula: F(n) = (phi^n - (-phi)^(-n)) / sqrt(5) - Best for small Fibonacci numbers but inaccurate for n > 70.
# Time Complexity: O(1) - Constant Time Complexity
# Space Complexity: O(1) - Constant Space Complexity
def nth_fibonacci_binet(n):
    if n > 70:  # Prevent floating-point precision errors
        return None
    decimal.getcontext().prec = 100
    phi = decimal.Decimal(1 + decimal.Decimal(5).sqrt()) / 2
    return round(phi**n / decimal.Decimal(5).sqrt())


def measure_performance_binet():
    test_numbers = [1, 5, 10, 15, 20, 30, 40, 50, 60, 70]  # Limited to n <= 70
    execution_times = []

    for n in test_numbers:
        start_time = time.perf_counter()
        nth_fibonacci_binet(n)
        end_time = time.perf_counter()
        execution_times.append((end_time - start_time) * 1000)
    
    # Convert execution times into a Pandas DataFrame for better formatting
    df = pd.DataFrame([execution_times], columns=test_numbers)

    # Print table format
    print("\nExecution Times for Binet's Formula (O(1)):\n")
    print(df.to_string(index=False))
    
    # Plot the performance graph
    plt.figure(figsize=(10, 6))
    plt.plot(test_numbers, execution_times, marker="o",
             color="y", label="Binet Formula (O(1))")
    plt.xlabel("n (Fibonacci Index)")
    plt.ylabel("Execution Time (ms)")
    plt.title("Fibonacci Calculation Performance (Binet’s Formula)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    measure_performance_binet()
