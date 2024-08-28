import test
import list_creator 
import sorting_algorithms
import sys
sys.setrecursionlimit(2000)  # Increase as needed



def times(lsts):
    for lst in lsts:
        srt_alg = sorting_algorithms.SortingAlgorithms(lst)
        srt_alg.test_qsn


def main():
    if test.main() == False:
        exit("ALL TESTS NOT PASSED")

    print("---------------------------------------------------------------------------------------------------------")
    print("ALL TESTS PASSED")
    print("---------------------------------------------------------------------------------------------------------")

    # strting the time extractions
    lists = test.lists
    
    ss = lists.get_short_sorted
    sr = lists.get_short_regular
    su = lists.get_short_rsorted

    ms = lists.get_middle_sorted
    mr = lists.get_middle_regular
    mu = lists.get_middle_rsorted

    ls = lists.get_long_sorted
    lr = lists.get_long_regular
    lu = lists.get_long_rsorted

    # times(ss)

    for lst in sr:
        srt_alg = sorting_algorithms.SortingAlgorithms(lst)
        insertion = srt_alg.insertion_sort
        print(insertion[1])
        merge = srt_alg.merge_sort
        print(merge[1])
        bub = srt_alg.bubble_sort
        print(bub[1])
        quick = srt_alg.quick_sort_naive
        print(quick[1])




if __name__ == "__main__":
    main()