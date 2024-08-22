import numpy as np
import bubble_sort_gif
import butcher_odd_even_sort_gif
import counting_sort_gif
import inserion_sort_gif
import merge_sort_gif
import quick_sort_naive_gif
import radix_sort_gif
import selection_sort_gif

def main():
    lst = np.random.randint(0, 100, 20)
    bubble_sort_gif.run(lst.copy())
    butcher_odd_even_sort_gif.run(lst.copy())
    counting_sort_gif.run(lst.copy())
    inserion_sort_gif.run(lst.copy())
    merge_sort_gif.run(lst.copy())
    quick_sort_naive_gif.run(lst.copy())
    radix_sort_gif.run(lst.copy())
    selection_sort_gif.run(lst.copy())

if __name__ == "__main__":
    main()