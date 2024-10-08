import sys
import timer.timer as timer
import numpy as np

class SortingAlgorithms:
    def __init__(self, data: list[int] = None) -> None:
        self.__original_data = data[:]
        self.__sorted_data = data[:].sort
        self.__insertion_data = data[:]
        self.__merge_data = data[:]
        self.__selection_data = data[:]         
        self.__bubble_data = data[:]
        self.__heap_data = data[:] 
        self.__quick__naive_data = data[:]
        self.__quick_impr_1_data = data[:]
        self.__quick_impr_2_data = data[:]
        self.__counting_data = data[:]
        self.__radix_naive_data = data[:]
        self.__radix_impr_data = data[:]
        self.__butcher_odd_even_merge_data = data[:]
        self.__stalin_data = data[:]

    @property
    def raw_data(self):
        return self.__original_data

    @property
    def sorted_data(self):
        return self.__sorted_data

    def __insertion_sort__(self):
        for i in range(len(self.__insertion_data)):
            key = self.__insertion_data[i]
            j = i - 1

            while j > -1 and self.__insertion_data[j] > key:
                self.__insertion_data[j + 1] = self.__insertion_data[j]
                j -= 1

            self.__insertion_data[j + 1] = key

    @property
    def insertion_sort(self):
        timex = timer.Timer()
        timex.start_time
        self.__insertion_sort__()
        timex.end_time
        return self.__insertion_data, timex.get_time

    def __merge_sort__(self, p, r):
        # start time
        if p >= r:
            return
        
        q = int((p + r) / 2)
        self.__merge_sort__(p, q)
        self.__merge_sort__(q + 1, r)
        self.__merge__(p, q, r)
        # end time

    def __merge__(self, p, q, r):
        n1 = q - p + 1
        n2 = r - q
        L = []
        R = []
        for val in range(n1):
            L.append(self.__merge_data[p + val])

        for val in range(n2):
            R.append(self.__merge_data[q + 1 + val])
        
        L.append(sys.maxsize)
        R.append(sys.maxsize)

        i = 0
        j = 0

        for k in range(p, r + 1):
            if L[i] <= R[j]:
                self.__merge_data[k] = L[i]
                i += 1
            else:
                self.__merge_data[k] = R[j]
                j += 1


    @property
    def merge_sort(self):
        timex = timer.Timer()
        timex.start_time
        self.__merge_sort__(0, len(self.__original_data) - 1)
        timex.end_time
        return self.__merge_data, timex.get_time

    def __selection_sort__(self):
        # start time
        for i in range(len(self.__selection_data)):
            lowest = i
            for j in range(i, len(self.__selection_data)):
                if self.__selection_data[lowest] > self.__selection_data[j]:
                    lowest = j
                    
            self.__selection_data[i], self.__selection_data[lowest] = self.__selection_data[lowest], self.__selection_data[i]
        # end time

    @property
    def selection_sort(self):
        timex = timer.Timer()
        timex.start_time
        self.__selection_sort__()
        timex.end_time
        return self.__selection_data, timex.get_time

    def __bubble_sort__(self):
        # start time
        n = len(self.__bubble_data)
        for i in range(n):
            for j in range(0, n - 1 - i):
                if self.__bubble_data[j] > self.__bubble_data[j + 1]:
                    self.__bubble_data[j], self.__bubble_data[j + 1] = self.__bubble_data[j + 1], self.__bubble_data[j]
        # end time

    @property
    def bubble_sort(self):
        timex = timer.Timer()
        timex.start_time
        self.__bubble_sort__()
        timex.end_time
        return self.__bubble_data, timex.get_time

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def __max_heapify__(self, i, heap_size):
        l = self.left(i)
        r = self.right(i)
        largest = i
        
        if l < heap_size and self.__heap_data[l] > self.__heap_data[i]:
            largest = l
        if r < heap_size and self.__heap_data[r] > self.__heap_data[largest]:
            largest = r
        if largest != i:
            self.__heap_data[i], self.__heap_data[largest] = self.__heap_data[largest], self.__heap_data[i] 
            self.__max_heapify__(largest, heap_size)

    def __build_max_heap__(self):
        heap_size = len(self.__heap_data)
        for i in range(len(self.__heap_data) // 2 - 1, -1, -1):
            self.__max_heapify__(i, heap_size)

    def __heapsort__(self):
        self.__build_max_heap__()
        heap_size = len(self.__heap_data)
        for i in range(len(self.__heap_data) - 1, 0, -1):
            self.__heap_data[0], self.__heap_data[i] = self.__heap_data[i], self.__heap_data[0]
            heap_size -= 1
            self.__max_heapify__(0, heap_size)

    @property
    def heap_sort(self):
        timex = timer.Timer()
        timex.start_time
        self.__heapsort__()
        timex.end_time
        return self.__heap_data, timex.get_time
    
    @property
    def test_heap_sort(self):
        self.__heapsort__()
        return self.__heap_data
    
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
    def quick_sort_naive(self):
        timex = timer.Timer()
        timex.start_time
        self.__quick_sort_naive__(0, len(self.__original_data) - 1)
        timex.end_time
        return self.__quick__naive_data, timex.get_time

    def __quick_sort_improved_1__(self, p, r):
        if p < r:
            q = self.__partion_improved_1__(p, r)
            self.__quick_sort_improved_1__(p, q - 1)
            self.__quick_sort_improved_1__(q + 1, r)

    def __partion_improved_1__(self, p, r):
        x = self.__quick_impr_1_data[r]  
        left = p
        right = r - 1
        while True:
            while left <= right and self.__quick_impr_1_data[left] < x:
                left += 1
            while right >= left and self.__quick_impr_1_data[right] > x:
                right -= 1
            if left >= right:
                break
            else:
                self.__quick_impr_1_data[left], self.__quick_impr_1_data[right] = self.__quick_impr_1_data[right], self.__quick_impr_1_data[left]
                left += 1
                right -= 1
        
        self.__quick_impr_1_data[left], self.__quick_impr_1_data[r] = self.__quick_impr_1_data[r], self.__quick_impr_1_data[left]
        return left

    
    @property
    def quick_sort_imrproved_1(self):
        timex = timer.Timer()
        timex.start_time
        self.__quick_sort_improved_1__(0, len(self.__original_data) - 1)
        timex.end_time
        return self.__quick_impr_1_data, timex.get_time

    def __quick_sort_improved_2__(self, p, r):
        if p < r:
            q = self.__partion_improved_2__(p, r)
            self.__quick_sort_improved_2__(p, q - 1)
            self.__quick_sort_improved_2__(q + 1, r)

    def __partion_improved_2__(self, p, r):
        mid = (p + r) // 2
        median_of_three = sorted([(self.__quick_impr_2_data[p], p), (self.__quick_impr_2_data[mid], mid), (self.__quick_impr_2_data[r], r)])
        pivot_value, pivot_index = median_of_three[1]

        # Move the pivot to the start
        self.__quick_impr_2_data[pivot_index], self.__quick_impr_2_data[r] = self.__quick_impr_2_data[r], pivot_value
        pivot = self.__quick_impr_2_data[r]

        left = p
        right = r - 1

        while True:
            while left <= right and self.__quick_impr_2_data[left] < pivot:
                left += 1
            while left <= right and self.__quick_impr_2_data[right] > pivot:
                right -= 1
            if left >= right:
                break
            else:
                self.__quick_impr_2_data[left], self.__quick_impr_2_data[right] = self.__quick_impr_2_data[right], self.__quick_impr_2_data[left]
                left += 1
                right -= 1

        self.__quick_impr_2_data[left], self.__quick_impr_2_data[r] = self.__quick_impr_2_data[r], self.__quick_impr_2_data[left]

        return left


    @property
    def quick_sort_improved_2(self):
        timex = timer.Timer()
        timex.start_time
        self.__quick_sort_improved_2__(0, len(self.__original_data) - 1)
        timex.end_time
        return self.__quick_impr_2_data, timex.get_time
    
    def __counting_sort__(self, k):
        C = [0] * (k + 1)  

        for j in range(len(self.__counting_data)):
            C[self.__counting_data[j]] += 1

        for i in range(1, k + 1):
            C[i] += C[i - 1]

        B = [0] * len(self.__counting_data)
        for j in range(len(self.__counting_data) - 1, -1, -1):
            B[C[self.__counting_data[j]] - 1] = self.__counting_data[j]
            C[self.__counting_data[j]] -= 1

        self.__counting_data = B
    
    @property
    def counting_sort(self):
        timex = timer.Timer()
        timex.start_time
        self.__counting_sort__(max(self.__counting_data))
        timex.end_time
        return self.__counting_data, timex.get_time
    
    @property
    def test_counting(self):
        self.__counting_sort__(max(self.__counting_data))
        return self.__counting_data

    # does not sort neagtive numbers
    def __radix_naive_sort__(self):
        n = len(self.__radix_naive_data)
        max_val = max(self.__radix_naive_data)

        pos = 1
        while max_val // pos > 0:
            self.__count_sort__(n, pos)
            pos *= 10


    def __count_sort__(self, n, pos):
        output = [0] * len(self.__radix_naive_data)
        count = [0] * 10

        for i in range(n):
            count[(self.__radix_naive_data[i] // pos) % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            output[count[(self.__radix_naive_data[i] // pos) % 10] - 1] = self.__radix_naive_data[i]
            count[(self.__radix_naive_data[i] // pos) % 10] -= 1

        for i in range(n):
            self.__radix_naive_data[i] = output[i]
        
    # sorts negative numbers
    def __radix_improved_sort__(self):
        neg = [-x for x in self.__radix_impr_data if x < 0] 
        pos = [x for x in self.__radix_impr_data if x >= 0]

        if neg:
            self.__radix_sort_pos__(neg)
        if pos:
            self.__radix_sort_pos__(pos)

        self.__radix_impr_data[:] = [-x for x in reversed(neg)] + pos

    def __radix_sort_pos__(self, arr):
        n = len(arr)
        max_val = max(arr)

        pos = 1
        while max_val // pos > 0:
            self.__count_sort_impr__(arr, n, pos)
            pos *= 10

    def __count_sort_impr__(self, arr, n, pos):
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            count[(arr[i] // pos) % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            output[count[(arr[i] // pos) % 10] - 1] = arr[i]
            count[(arr[i] // pos) % 10] -= 1

        for i in range(n):
            arr[i] = output[i]


    @property
    def radix_sort(self):
        timex = timer.Timer()
        timex.start_time
        self.__radix_improved_sort__()
        timex.end_time
        return self.__radix_impr_data, timex.get_time
        
    def __butcher_odd_even_merge_sort__(self):
        n = len(self.__butcher_odd_even_merge_data)
        
        p = 1
        while p < n:
            k = p
            while k >= 1:
                for j in range(k % p, n - k, 2 * k):
                    for i in range(min(k, n - j - k)):
                        if (i + j) // (2 * p) == (i + j + k) // (2 * p):
                            if self.__butcher_odd_even_merge_data[i + j] > self.__butcher_odd_even_merge_data[i + j + k]:
                                self.__butcher_odd_even_merge_data[i + j], self.__butcher_odd_even_merge_data[i + j + k] = self.__butcher_odd_even_merge_data[i + j + k], self.__butcher_odd_even_merge_data[i + j]
                k //= 2
            p *= 2

    @property
    def butcher_odd_even_merge_sort(self):
        timex = timer.Timer()
        timex.start_time
        self.__butcher_odd_even_merge_sort__()
        timex.end_time
        return self.__butcher_odd_even_merge_data, timex.get_time

    def __stalin_sort__(self):
        max = -123456789
        for value in self.__stalin_data:
            if max > value:
                self.__stalin_data.remove(value)
            else:
                max = value

    @property
    def test_qsn(self):
        self.__quick_sort_naive__(0, len(self.__quick__naive_data) - 1)
        return self.__quick__naive_data

    @property
    def get_times_main_test(self):
        insertion_sort_data = self.insertion_sort
        merge_sort_data = self.merge_sort
        selection_sort_data = self.selection_sort
        bubble_sort_data = self.bubble_sort
        heap_sort_data = self.heap_sort
        quick_sort_impr2_data = self.quick_sort_improved_2
        countin_sort_data = self.counting_sort
        radix_sort_data = self.radix_sort
        butcher_odd_even_merge_sort_data = self.butcher_odd_even_merge_sort

        return [insertion_sort_data[1], merge_sort_data[1], selection_sort_data[1], 
                bubble_sort_data[1], heap_sort_data[1], quick_sort_impr2_data[1], 
                countin_sort_data[1], radix_sort_data[1], butcher_odd_even_merge_sort_data[1]]

def main():
    # debugging 
    lst = np.random.randint(0, 10, 10)
    lst = list(int(j) for j in lst)
    print(f"Pre sorted list: {lst}")
    srt = SortingAlgorithms(lst)
    print(f"Sorted list: {srt.test_counting}")


if __name__ == "__main__":
    main()