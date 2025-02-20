import time
import matplotlib.pyplot as plt
import pandas as pd

# Fibonacci Calculation using Matrix Exponentiation (O(log n)) - Very fast for large values of n.
# Time Complexity: O(log n) (Logarithmic time complexity)
# Space Complexity: O(log n) (Recursive depth for matrix exponentiation)
def nth_fibonacci_matrix(n):
    def multiply(A, B):
        return [[A[0][0] * B[0][0] + A[0][1] * B[1][0],
                 A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                [A[1][0] * B[0][0] + A[1][1] * B[1][0],
                 A[1][0] * B[0][1] + A[1][1] * B[1][1]]]

    def power(F, n):
        if n == 0 or n == 1:
            return F
        M = [[1, 1], [1, 0]]
        if n % 2 == 0:
            return power(multiply(F, F), n // 2)
        else:
            return multiply(F, power(multiply(F, F), (n - 1) // 2))

    if n == 0:
        return 0
    return power([[1, 1], [1, 0]], n - 1)[0][0]


def measure_performance_matrix():
    test_numbers = [1, 20, 40, 70, 100, 200, 300, 500, 1000, 5000, 10000]
    execution_times = []

    for n in test_numbers:
        start_time = time.perf_counter()
        nth_fibonacci_matrix(n)
        end_time = time.perf_counter()
        execution_times.append((end_time - start_time) * 1000)
    
    # Convert execution times into a Pandas DataFrame for formatted output
    df = pd.DataFrame([execution_times], columns=test_numbers)

    # Print execution times as a table
    print("\nExecution Times using Matrix Exponentiation (O(log n))")
    print(df.to_string(index=False))

    # Plot the performance graph
    plt.figure(figsize=(10, 6))
    plt.plot(test_numbers, execution_times, marker="o",
             color="m", label="Matrix Exponentiation (O(log n))")
    plt.xlabel("n (Fibonacci Index)")
    plt.ylabel("Execution Time (ms)")
    plt.title("Fibonacci Calculation Performance (Matrix Exponentiation)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    measure_performance_matrix()
