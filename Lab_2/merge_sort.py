import random


class MergeSort:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0  # Not really swaps in MergeSort, but tracking data movements

    def merge_sort(self, arr):
        """ Main function to sort the array using MergeSort """
        self.merge_sort_recursive(arr, 0, len(arr) - 1)
        return arr

    def merge_sort_recursive(self, arr, left, right):
        """ Recursive MergeSort function """
        if left < right:
            mid = (left + right) // 2
            self.merge_sort_recursive(arr, left, mid)
            self.merge_sort_recursive(arr, mid + 1, right)
            self.merge(arr, left, mid, right)

    def merge(self, arr, left, mid, right):
        """ Merge two sorted halves in-place """
        n1 = mid - left + 1
        n2 = right - mid

        # Create temp arrays
        L = [arr[left + i] for i in range(n1)]
        R = [arr[mid + 1 + j] for j in range(n2)]

        i = j = 0
        k = left

        while i < n1 and j < n2:
            self.comparisons += 1
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def merge_sort_optimized(self, arr):
        """ Optimized MergeSort with Insertion Sort for small partitions """
        INSERTION_SORT_THRESHOLD = 16
        self.merge_sort_recursive_optimized(
            arr, 0, len(arr) - 1, INSERTION_SORT_THRESHOLD)
        return arr

    def merge_sort_recursive_optimized(self, arr, left, right, threshold):
        """ MergeSort that switches to Insertion Sort for small partitions """
        if right - left + 1 <= threshold:
            self.insertion_sort(arr, left, right)
            return

        mid = (left + right) // 2
        self.merge_sort_recursive_optimized(arr, left, mid, threshold)
        self.merge_sort_recursive_optimized(arr, mid + 1, right, threshold)
        self.merge(arr, left, mid, right)

    def insertion_sort(self, arr, left, right):
        """ Insertion Sort for small partitions """
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
                self.comparisons += 1
                self.swaps += 1
            arr[j + 1] = key

    def merge_sort_generator(self, arr, use_improved=False):
        """ Generator-based MergeSort for visualization with option to use Improved MergeSort """
        if use_improved:
            yield from self.merge_sort_recursive_generator_optimized(arr, 0, len(arr) - 1)
        else:
            yield from self.merge_sort_recursive_generator(arr, 0, len(arr) - 1)

        yield arr  # Ensure the final sorted array is yielded

    def merge_sort_recursive_generator(self, arr, left, right):
        """ Recursive MergeSort generator for visualization (Standard) """
        if left < right:
            mid = (left + right) // 2
            yield from self.merge_sort_recursive_generator(arr, left, mid)
            yield from self.merge_sort_recursive_generator(arr, mid + 1, right)
            self.merge(arr, left, mid, right)
            yield arr[:]  # Yield array after merging

    def merge_sort_recursive_generator_optimized(self, arr, left, right):
        """ Recursive MergeSort generator for visualization (Optimized with Insertion Sort) """
        INSERTION_SORT_THRESHOLD = 16

        if right - left + 1 <= INSERTION_SORT_THRESHOLD:
            self.insertion_sort(arr, left, right)
            yield arr[:]
            return

        mid = (left + right) // 2
        yield from self.merge_sort_recursive_generator_optimized(arr, left, mid)
        yield from self.merge_sort_recursive_generator_optimized(arr, mid + 1, right)
        self.merge(arr, left, mid, right)
        yield arr[:]  # Yield array after merging
