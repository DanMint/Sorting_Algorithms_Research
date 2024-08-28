import time
import numpy as np

class QuickSortNaive:
    def __init__(self, data):
        self.__quick__naive_data = data

    def sort(self):
        # Start time
        start_time = time.time()

        # Call the recursive quick sort
        self.__quick_sort_naive__(0, len(self.__quick__naive_data) - 1)

        # End time
        end_time = time.time()
        print(f"QuickSort took {end_time - start_time:.6f} seconds")

    def __quick_sort_naive__(self, p, r):
        if p < r:
            q = self.__partition_naive__(p, r)
            self.__quick_sort_naive__(p, q - 1)
            self.__quick_sort_naive__(q + 1, r)

    def __partition_naive__(self, p, r):
        x = self.__quick__naive_data[r]
        i = p - 1
        for j in range(p, r):
            if self.__quick__naive_data[j] <= x:
                i += 1
                self.__quick__naive_data[i], self.__quick__naive_data[j] = self.__quick__naive_data[j], self.__quick__naive_data[i]

        self.__quick__naive_data[i + 1], self.__quick__naive_data[r] = self.__quick__naive_data[r], self.__quick__naive_data[i + 1]
        return i + 1
    
    @property
    def getter(self):
        return self.__quick__naive_data

# Example usage:
lst = np.random.randint(0, 1000000, 1000000)
lst = list(int(i) for i in lst)
sorter = QuickSortNaive(lst)
sorter.sort()
print(sorter.getter)
