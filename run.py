import test
import list_creator 
import sorting_algorithms
import sys
sys.setrecursionlimit(10000)  # Increase as needed


def times(lsts, name):
    time = []
    print(f"Running: {name}")
    for lst in lsts:
        srt_alg = sorting_algorithms.SortingAlgorithms(lst)
        time.append(srt_alg.get_times_main_test)

    return time

def test_times(times, names):
    time_test = test.Testing
    for time, name in times, names:
        print(f"Testing validity of {name} times list")
        time_test.check_times(time)

    print("Passed all time tests")


def main():
    if test.main() == False:
        exit("ALL TESTS NOT PASSED")

    print("---------------------------------------------------------------------------------------------------------")
    print("ALL PRE PROCESSING TESTS PASSED")
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

    print("----------------------------------------Starting the time calcualtions----------------------------------------")

    print("Getting small sorted list times")
    ss_times = times(ss, "small sorted")
    print("Getting small regular list times")
    sr_times = times(sr, "small regular")
    print("Getting small reverse sorted list times")
    su_times = times(su, "small revrse sorted")
    print("Getting middle sorted list times")
    ms_times = times(ms, "middle sorted")
    print("Getting middle regular list times")
    mr_times = times(mr, "middle regular") 
    print("Getting middle reverse sorted list times")
    mu_times = times(mu, "middle reverse sorted")
    print("Getting large sorted list times")
    ls_times = times(ls, "long sorted")
    print("Getting large regular list times")
    lr_times = times(lr, "long regular") 
    print("Getting large reverse sorted list times")
    lu_times = times(lu, "long unosrted") 

    all_times = [ss_times, sr_times, su_times, ms_times, mr_times, 
                 mu_times, ls_times, lr_times, lu_times]
    
    all_times_names = ["small sorted", "small regular", 
                       "small revrse sorted", "middle sorted", 
                       "middle regular", "middle reverse sorted", "long sorted", "long regular", 
                       "long unosrted"]
    
    test_times(all_times, all_times_names)


if __name__ == "__main__":
    main()