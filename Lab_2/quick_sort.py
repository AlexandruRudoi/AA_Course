import random


class QuickSort:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

    def quick_sort(self, arr):
        """ Standard Recursive QuickSort """
        if len(arr) <= 1:
            return arr

        pivot = arr[0]  # Choosing first element as pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        # Each element is compared with the pivot
        self.comparisons += len(arr) - 1
        return self.quick_sort(left) + middle + self.quick_sort(right)

    def median_of_three(self, arr, low, high):
        """ Selects pivot as the median of first, middle, and last elements """
        mid = (low + high) // 2
        a, b, c = arr[low], arr[mid], arr[high]
        if a < b:
            if b < c:
                return mid
            elif a < c:
                return high
            else:
                return low
        else:
            if a < c:
                return low
            elif b < c:
                return high
            else:
                return mid

    def partition(self, arr, low, high):
        """ Partition the array using the last element as pivot """
        pivot = arr[high]
        i = low - 1  # Position for smaller elements

        for j in range(low, high):
            self.comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.swaps += 1

        arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Move pivot to correct position
        self.swaps += 1
        return i + 1  # Return final pivot position


    def quick_sort_improved(self, arr):
        """ Iterative QuickSort with median-of-three and insertion sort for small partitions """
        INSERTION_SORT_THRESHOLD = 16

        def insertion_sort(arr, low, high):
            for i in range(low + 1, high + 1):
                key = arr[i]
                j = i - 1
                while j >= low and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                    self.comparisons += 1
                    self.swaps += 1
                arr[j + 1] = key

        stack = [(0, len(arr) - 1)]

        while stack:
            low, high = stack.pop()
            if high - low <= INSERTION_SORT_THRESHOLD:
                insertion_sort(arr, low, high)
                continue

            pivot_index = self.median_of_three(arr, low, high)
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Swap pivot with last element

            pivot_final_index = self.partition(arr, low, high)

            if pivot_final_index - 1 - low > high - (pivot_final_index + 1):
                stack.append((low, pivot_final_index - 1))
                stack.append((pivot_final_index + 1, high))
            else:
                stack.append((pivot_final_index + 1, high))
                stack.append((low, pivot_final_index - 1))

        return arr

    def quick_sort_generator(self, arr, use_improved=False):
        """ Generator-based QuickSort for visualization with option to use Improved QuickSort """
        INSERTION_SORT_THRESHOLD = 16

        def insertion_sort(arr, low, high):
            for i in range(low + 1, high + 1):
                key = arr[i]
                j = i - 1
                while j >= low and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                    self.comparisons += 1
                    self.swaps += 1
                    yield arr[:]
                arr[j + 1] = key
                yield arr[:]

        if use_improved:
            stack = [(0, len(arr) - 1)]

            while stack:
                low, high = stack.pop()
                if high - low <= INSERTION_SORT_THRESHOLD:
                    yield from insertion_sort(arr, low, high)
                    continue

                pivot_index = self.median_of_three(arr, low, high)
                arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
                yield arr[:]

                pivot_final_index = self.partition(arr, low, high)
                yield arr[:]

                if pivot_final_index - 1 - low > high - (pivot_final_index + 1):
                    stack.append((low, pivot_final_index - 1))
                    stack.append((pivot_final_index + 1, high))
                else:
                    stack.append((pivot_final_index + 1, high))
                    stack.append((low, pivot_final_index - 1))
        else:
            def recursive_quick_sort(arr, low, high):
                if low < high:
                    pivot_index = self.partition(arr, low, high)
                    yield arr[:]
                    yield from recursive_quick_sort(arr, low, pivot_index - 1)
                    yield from recursive_quick_sort(arr, pivot_index + 1, high)

            yield from recursive_quick_sort(arr, 0, len(arr) - 1)
