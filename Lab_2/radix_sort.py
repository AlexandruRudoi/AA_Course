import random


class RadixSort:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0  # Not really swaps, but tracking data movements

    def counting_sort(self, arr, exp):
        """ Helper function for Radix Sort: Performs Counting Sort based on a specific digit """
        n = len(arr)
        output = [0] * n
        count = [0] * 10  # Because decimal numbers (0-9)

        # Store count of occurrences
        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1

        # Update count[i] to contain actual position of this digit in output[]
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array
        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1

        # Copy the output array back to arr
        for i in range(n):
            arr[i] = output[i]

    def radix_sort(self, arr):
        """ Standard Radix Sort (Least Significant Digit First) """
        arr = arr[:]  # Work on a copy to avoid modifying the original list
        max_val = max(arr)

        exp = 1
        while max_val // exp > 0:
            self.counting_sort(arr, exp)
            exp *= 10  # Move to next digit

        return arr

    def radix_sort_improved(self, arr):
        """ Optimized Radix Sort (Uses Bucket-based counting sort) """
        arr = arr[:]  # Work on a copy to avoid modifying the original list
        max_val = max(arr)

        exp = 1
        while max_val // exp > 0:
            self.counting_sort_optimized(arr, exp)
            exp *= 10  # Move to next digit

        return arr

    def counting_sort_optimized(self, arr, exp):
        """ Optimized Counting Sort for Radix Sort (Using direct bucket sorting) """
        n = len(arr)
        output = [0] * n
        # Using buckets instead of a counting array
        buckets = [[] for _ in range(10)]

        # Place elements in buckets
        for num in arr:
            digit = (num // exp) % 10
            buckets[digit].append(num)

        # Flatten buckets back into arr
        index = 0
        for bucket in buckets:
            for num in bucket:
                output[index] = num
                index += 1

        for i in range(n):
            arr[i] = output[i]

    def radix_sort_generator(self, arr, use_improved=False):
        """ Generator-based Radix Sort for visualization """
        arr = arr[:]
        max_val = max(arr)
        exp = 1

        while max_val // exp > 0:
            if use_improved:
                self.counting_sort_optimized(arr, exp)
            else:
                self.counting_sort(arr, exp)

            exp *= 10
            yield arr[:]  # Yield after sorting each digit place

        yield arr  # Ensure the final sorted array is yielded
