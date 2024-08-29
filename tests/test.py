import sorting_algorithms.sorting_algorithms as sorting_algorithms
import test_data_creation.list_creator as list_creator
import numpy as np

class Testing:
    @classmethod
    def checking_importing_data(cls, test_data = None, raw_data = None):
        try:
            assert raw_data == test_data, "raw data does not match test data"

        except AssertionError as e:
            print(f"Test failed, {e}")
            exit()
        
        print("Data imported")

    @classmethod
    def check_if_sorted(cls, sorted_list: list[int], algorithm_sorted_list: list[int], algorithm: str):
        try:
            assert sorted_list == algorithm_sorted_list , f"list not sorted after algorithm ran {algorithm}"

        except AssertionError as e:
            print(f"Test failed, {e}")
            exit()

        print(f"{algorithm} is sorted and works")

    @classmethod
    def check_short_sort(cls, lst: list[int], type: str):
        try:
            assert len(lst) == 100, "Size of array of arrays is not 100(short)"

        except AssertionError as e:
            exit(f'Error for SHORT: {e}')

        for case in lst:
            try:
                assert len(case) == 2500, "Incorrect size for short lst"

            except AssertionError as e:
                exit(f'Error for SHORT: {e}')

            try:
                assert type == 'rev' or type == 'reg' or type == 'srt', ":Invalid type for short"

            except AssertionError as e:
                exit(f'Error for SHORT: {e}')

            if type == "srt":
                try:
                    assert case == sorted(case), "Sorted short NOT SORTTED"

                except AssertionError as e:
                    exit(f'Error for SHORT: {e}')

            if type == "rev":
                try:
                    assert list(reversed(case)) == sorted(case), "Reversed short NOT REVERSED SORTED"

                except AssertionError as e:
                    exit(f'Error for SHORT: {e}')

        print(f"Short list test data loaded")

    @classmethod
    def check_middle_sort(cls, lst: list[int], type: str):
        try:
            assert len(lst) == 100, "Size of array of arrays is not 100(middle)"

        except AssertionError as e:
            exit(f'Error for MIDDLE: {e}')

        for case in lst:
            try:
                assert len(case) == 5000, "Incorrect size for middle lst"

            except AssertionError as e:
                exit(f'Error for MIDDLE: {e}')

            try:
                assert type == 'rev' or type == 'reg' or type == 'srt', ":Invalid type for middle"

            except AssertionError as e:
                exit(f'Error for MIDDLE: {e}')

            if type == "srt":
                try:
                    assert case == sorted(case), "Sorted middle NOT SORTTED"

                except AssertionError as e:
                    exit(f'Error for MIDDLE: {e}')

            if type == "rev":
                try:
                    assert list(reversed(case)) == sorted(case), "Reversed middle NOT REVERSED SORTED"

                except AssertionError as e:
                    exit(f'Error for MIDDLE: {e}')

        print(f"Middle list test data loaded")

    @classmethod
    def check_long_sort(cls, lst: list[int], type: str):
        try:
            assert len(lst) == 100, "Size of array of arrays is not 100(long)"

        except AssertionError as e:
            exit(f'Error for LONG: {e}')

        for case in lst:
            try:
                assert len(case) == 10000, "Incorrect size for long lst"

            except AssertionError as e:
                exit(f'Error for LONG: {e}')

            try:
                assert type == 'rev' or type == 'reg' or type == 'srt', ":Invalid type for long"

            except AssertionError as e:
                exit(f'Error for LONG: {e}')

            if type == "srt":
                try:
                    assert case == sorted(case), "Sorted long NOT SORTTED"

                except AssertionError as e:
                    exit(f'Error for LONG: {e}')

            if type == "rev":
                try:
                    assert list(reversed(case)) == sorted(case), "Reversed long NOT REVERSED SORTED"

                except AssertionError as e:
                    exit(f'Error for LONG: {e}')

        
        print(f"Long list test data loaded")

    @classmethod
    def check_times(cls, times: list[list]):
        try:
            assert len(times) != 0, "Empty times list"

        except AssertionError as e:
            print(f"Time Error: {e}")
            exit()

        for time in times:
            try:
                assert len(time) != 0 and time != None, "Invalid time in times list"

            except AssertionError as e:
                print(f"Time error: {e}")
                exit()
            for i in time:
                try:
                    assert i != None and i >= 0, "Invalid time in list"
                
                except AssertionError as e:
                    print(f"Time error: {e}")
                    exit()

        

def main():
    # checking algorithms in sorting_algorithms.py
    lst = np.random.randint(0, 100, 20)
    lst = list(int(i) for i in lst)
    sorted_lst = sorted(lst)
    algorithms = sorting_algorithms.SortingAlgorithms(lst)

    insertion_sort_data = algorithms.insertion_sort
    merge_sort_data = algorithms.merge_sort
    selection_sort_data = algorithms.selection_sort
    bubble_sort_data = algorithms.bubble_sort
    heap_sort_data = []
    quick_sort_naive_data = algorithms.quick_sort_naive
    quick_sort_impr1_data = algorithms.quick_sort_imrproved_1
    quick_sort_impr2_data = algorithms.quick_sort_improved_2
    radix_sort_data = algorithms.radix_sort
    butcher_odd_even_merge_sort_data = algorithms.butcher_odd_even_merge_sort

    insertion_sort = insertion_sort_data[0]
    merge_sort = merge_sort_data[0]
    selection_sort = selection_sort_data[0]
    bubble_sort = bubble_sort_data[0]
    heap_sort = []
    quick_sort_naive = quick_sort_naive_data[0]
    quick_sort_impr1 = quick_sort_impr1_data[0]
    quick_sort_impr2 = quick_sort_impr2_data[0]
    radix_sort = radix_sort_data[0]
    butcher_odd_even_merge_sort = butcher_odd_even_merge_sort_data[0]

    print(f"Sorted            : {sorted_lst}")
    print(f"After butcher sort: {butcher_odd_even_merge_sort}")

    Testing.checking_importing_data(lst, algorithms.raw_data)
    Testing.check_if_sorted(sorted_lst, insertion_sort, "Insertion Sort")
    Testing.check_if_sorted(sorted_lst, merge_sort, "Merge Sort")
    Testing.check_if_sorted(sorted_lst, selection_sort, "Selection Sort")
    Testing.check_if_sorted(sorted_lst, bubble_sort, "Bubble Sort")
    # Testing.check_if_sorted(sorted_lst, heap_sort, "Heap Sort")
    Testing.check_if_sorted(sorted_lst, quick_sort_naive, "Quick Sort Naive")
    Testing.check_if_sorted(sorted_lst, quick_sort_impr1, "Quick Sort Impr1")
    Testing.check_if_sorted(sorted_lst, quick_sort_impr2, "Quick Sort Impr2")
    Testing.check_if_sorted(sorted_lst, radix_sort, "Radix Sort")
    Testing.check_if_sorted(sorted_lst, butcher_odd_even_merge_sort, "Butcher odd even merge Sort")


    # checking validity of list_creator.py
    global lists
    lists = list_creator.GenerateLists()

    ss = lists.get_short_sorted
    sr = lists.get_short_regular
    su = lists.get_short_rsorted

    ms = lists.get_middle_sorted
    mr = lists.get_middle_regular
    mu = lists.get_middle_rsorted

    ls = lists.get_long_sorted
    lr = lists.get_long_regular
    lu = lists.get_long_rsorted

    # testing short lists
    Testing.check_short_sort(ss, "srt")
    Testing.check_short_sort(sr, "reg")
    Testing.check_short_sort(su, "rev")

    # testing middle lists
    Testing.check_middle_sort(ms, "srt")
    Testing.check_middle_sort(mr, "reg")
    Testing.check_middle_sort(mu, "rev")
    
    # testing long lists
    Testing.check_long_sort(ls, "srt")
    Testing.check_long_sort(lr, "reg")
    Testing.check_long_sort(lu, "rev")

    return True

if __name__ == "__main__":
    main()
