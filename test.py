import sorting_algorithms
import numpy as np

class Testing:
    def __init__(self, test_data: list[int], sorted_data: list[int]) -> None:
        self.test_data = test_data
        self.sorted_data = sorted_data

    def check_if_sorted(self, recived_list):
        try:
            assert recived_list == self.sorted_data , "list is not sorted"

        except AssertionError as e:
            print("Test failed: ", e)


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
