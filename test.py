import sorting_algorithms
import list_creator
import numpy as np

class Testing:
    def __init__(self, test_data: list[int] = None, sorted_data: list[int] = None) -> None:
        self.test_data = test_data
        self.sorted_data = sorted_data

    def check_if_sorted(self, recived_list: list[int]):
        try:
            assert recived_list == self.sorted_data , f"list is not sorted: {recived_list}. Sorted list is: "

        except AssertionError as e:
            print("Test failed: ", e)

    def check_short_sort(self, lst: list[int], type: str):
        try:
            assert len(lst) == 100, "Size of array of arrays is not 100(short)"

        except AssertionError as e:
            print(f'Error for SHORT: {e}')

        for case in lst:
            try:
                assert len(case) == 100, "Incorrect size for short lst"

            except AssertionError as e:
                print(f'Error for SHORT: {e}')

            try:
                assert type == 'rev' or type == 'reg' or type == 'srt', ":Invalid type for short"

            except AssertionError as e:
                print(f'Error for SHORT: {e}')

            if type == "srt":
                try:
                    assert case == sorted(case), "Sorted short NOT SORTTED"

                except AssertionError as e:
                    print(f'Error for SHORT: {e}')

            if type == "rev":
                try:
                    assert list(reversed(case)) == sorted(case), "Reversed short NOT REVERSED SORTED"

                except AssertionError as e:
                    print(f'Error for SHORT: {e}')


    def check_middle_sort(self, lst: list[int], type: str):
        try:
            assert len(lst) == 100, "Size of array of arrays is not 100(middle)"

        except AssertionError as e:
            print(f'Error for MIDDLE: {e}')

        for case in lst:
            try:
                assert len(case) == 1000, "Incorrect size for middle lst"

            except AssertionError as e:
                print(f'Error for MIDDLE: {e}')

            try:
                assert type == 'rev' or type == 'reg' or type == 'srt', ":Invalid type for middle"

            except AssertionError as e:
                print(f'Error for MIDDLE: {e}')

            if type == "srt":
                try:
                    assert case == sorted(case), "Sorted middle NOT SORTTED"

                except AssertionError as e:
                    print(f'Error for MIDDLE: {e}')

            if type == "rev":
                try:
                    assert list(reversed(case)) == sorted(case), "Reversed middle NOT REVERSED SORTED"

                except AssertionError as e:
                    print(f'Error for MIDDLE: {e}')

    def check_long_sort(self, lst: list[int], type: str):
        try:
            assert len(lst) == 100, "Size of array of arrays is not 100(long)"

        except AssertionError as e:
            print(f'Error for LONG: {e}')

        for case in lst:
            try:
                assert len(case) == 1000, "Incorrect size for long lst"

            except AssertionError as e:
                print(f'Error for LONG: {e}')

            try:
                assert type == 'rev' or type == 'reg' or type == 'srt', ":Invalid type for long"

            except AssertionError as e:
                print(f'Error for LONG: {e}')

            if type == "srt":
                try:
                    assert case == sorted(case), "Sorted long NOT SORTTED"

                except AssertionError as e:
                    print(f'Error for LONG: {e}')

            if type == "rev":
                try:
                    assert list(reversed(case)) == sorted(case), "Reversed long NOT REVERSED SORTED"

                except AssertionError as e:
                    print(f'Error for LONG: {e}')



def main():
    # checking algorithms in sorting_algorithms.py
    # lst = np.random.randint(0, 100, 20)
    # lst = list(int(i) for i in lst)
    # algorithms = sorting_algorithms.SortingAlgorithms(lst)
    # algorithms.run()

    # test = Testing(algorithms.raw_data, algorithms.sorted_data)
    # print(algorithms.sorted_data)
    # print(algorithms.insertion_sort)
    # test.check_if_sorted(algorithms.insertion_sort)

    # checking validity of list_creator.py
    lists = list_creator.GenerateLists()

    ss = lists.get_short_sorted
    sr = lists.get_short_regular
    su = lists.get_short_rsorted

    ms = lists.get_middle_sorted
    mr = lists.get_middle_regular
    mu = lists.get_middle_rsorted

    test = Testing()
    # testing short lists
    test.check_short_sort(ss, "srt")
    test.check_short_sort(sr, "reg")
    test.check_short_sort(su, "rev")

    # testing middle lists
    test.check_middle_sort(ms, "srt")
    test.check_middle_sort(mr, "reg")
    test.check_middle_sort(mu, "rev")

if __name__ == "__main__":
    main()
