import sorting_algorithms
import numpy as np

class Testing:
    def __init__(self, test_data: list[int], sorted_data: list[int]) -> None:
        self.test_data = test_data
        self.sorted_data = sorted_data

    def check_if_sorted(self, recived_list: list[int]):
        try:
            assert recived_list == self.sorted_data , "list is not sorted"

        except AssertionError as e:
            print("Test failed: ", e)

    def check_short_sort(self, lst: list[int], type: str):
        try:
            assert len(lst) == 100, "Incorrect size for short lst"

        except AssertionError as e:
            print(f'Error for SHORT: {e}')

        try:
            assert type == 'rev' or type == 'reg' or type == 'srt', ":Invalid type for short"

        except AssertionError as e:
            print(f'Error for SHORT: {e}')

        if type == "srt":
            try:
                assert lst == sorted(lst), "Sorted short NOT SORTTED"

            except AssertionError as e:
                print(f'Error for SHORT: {e}')

        if type == "rev":
            try:
                assert list(reversed(lst)) == sorted(lst), "Reversed short NOT REVERSED SORTED"

            except AssertionError as e:
                print(f'Error for SHORT: {e}')


    def check_middle_sort(self, lst: list[int], type: str):
        pass

    def check_long_sort(self, lst: list[int], type: str):
        pass



def main():
    lst = np.random.randint(0, 100, 20)
    lst = list(int(i) for i in lst)
    algorithms = sorting_algorithms.SortingAlgorithms(lst)
    algorithms.run()

    test = Testing(algorithms.raw_data, algorithms.sorted_data)
    print(algorithms.sorted_data)
    print(algorithms.insertion_sort)
    test.check_if_sorted(algorithms.insertion_sort)


if __name__ == "__main__":
    main()
