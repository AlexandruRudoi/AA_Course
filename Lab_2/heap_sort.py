import random


class HeapSort:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

    def heap_sort(self, arr):
        """ Standard HeapSort using bottom-up heap construction """
        arr = arr[:]  # Work on a copy to avoid modifying the original list
        n = len(arr)

        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # Extract elements one by one
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Swap max element to end
            self.swaps += 1
            self.heapify(arr, i, 0)

        return arr

    def heapify(self, arr, n, i):
        """ Heapify a subtree rooted at index i (Standard Version) """
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
            self.comparisons += 1

        if right < n and arr[right] > arr[largest]:
            largest = right
            self.comparisons += 1

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.swaps += 1
            self.heapify(arr, n, largest)

    def heap_sort_improved(self, arr):
        """ Improved HeapSort using Floyd’s Heap Construction Algorithm """
        arr = arr[:]  # Work on a copy to avoid modifying the original list
        n = len(arr)

        # Floyd's heap construction (faster than standard method)
        for i in range(n // 2 - 1, -1, -1):
            self.floyd_heapify(arr, n, i)

        # Extract elements one by one
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Move max element to end
            self.swaps += 1
            self.floyd_heapify(arr, i, 0)

        return arr

    def floyd_heapify(self, arr, n, i):
        """ Optimized Heapify using Floyd's Algorithm """
        root = arr[i]  # Store the root value
        largest = i

        while True:
            left = 2 * largest + 1
            right = 2 * largest + 2
            max_child = largest

            if left < n and arr[left] > arr[max_child]:
                max_child = left

            if right < n and arr[right] > arr[max_child]:
                max_child = right

            if max_child == largest:
                arr[largest] = root
                break

            arr[largest] = arr[max_child]
            largest = max_child
            self.swaps += 1

    def heap_sort_generator(self, arr, use_improved=False):
        """ Generator-based HeapSort for visualization (Standard & Improved) """
        arr = arr[:]
        n = len(arr)

        if use_improved:
            # Improved HeapSort using Floyd's Algorithm
            for i in range(n // 2 - 1, -1, -1):
                self.floyd_heapify(arr, n, i)
                yield arr[:]  # Yield after every heapify step

            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]  # Move max element to end
                self.swaps += 1
                yield arr[:]  # Yield after swapping root with last element

                # Ensure yielding after every heap restructuring step
                for j in range(i // 2 - 1, -1, -1):  
                    self.floyd_heapify(arr, i, j)
                    yield arr[:]

        else:
            # Standard HeapSort
            for i in range(n // 2 - 1, -1, -1):
                self.heapify(arr, n, i)
                yield arr[:]

            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                self.swaps += 1
                yield arr[:]
                self.heapify(arr, i, 0)
                yield arr[:]

        yield arr

