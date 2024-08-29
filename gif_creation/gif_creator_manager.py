import numpy as np
import gif_creation_of_algorithms.bubble_sort_gif as bubble_sort_gif
import gif_creation_of_algorithms.butcher_odd_even_sort_gif as butcher_odd_even_sort_gif
import gif_creation_of_algorithms.counting_sort_gif as counting_sort_gif
import gif_creation_of_algorithms.inserion_sort_gif as inserion_sort_gif
import gif_creation_of_algorithms.merge_sort_gif as merge_sort_gif
import gif_creation_of_algorithms.quick_sort_naive_gif as quick_sort_naive_gif
import gif_creation_of_algorithms.quick_sort_impr_1_gif as quick_sort_impr_1_gif
import gif_creation_of_algorithms.quick_sort_impr_2_gif as quick_sort_impr_2_gif
import gif_creation_of_algorithms.radix_sort_gif as radix_sort_gif
import gif_creation_of_algorithms.selection_sort_gif as selection_sort_gif
import gif_creation_of_algorithms.heap_sort_gif as heap_sort_gif

def main():
    lst = np.random.randint(0, 100, 20)
    bubble_sort_gif.run(lst.copy())
    butcher_odd_even_sort_gif.run(lst.copy())
    counting_sort_gif.run(lst.copy())
    inserion_sort_gif.run(lst.copy())
    merge_sort_gif.run(lst.copy())
    quick_sort_naive_gif.run(lst.copy())
    quick_sort_impr_1_gif.run(lst.copy())
    quick_sort_impr_2_gif.run(lst.copy())
    radix_sort_gif.run(lst.copy())
    selection_sort_gif.run(lst.copy())
    heap_sort_gif.run(lst.copy())

if __name__ == "__main__":
    main()