﻿# Sorting Algorithms Research

## <ins>Inspiration<ins>
In this repository, I wanted to conduct reserach into sorting algorithms and their respective time complexities. Namely, I wanted to see and test if their given time complexities are true, why do these time complexities matter and visualise these sorting algorithms. An obesrvation that I had through out my learning is that we always learn the theory part of algorithms, namely we look at the psuedo code, break down the time complexities and sometimes as students we implement the algorithms just to finish the homewrok assingment. However, as a student, I found out that actualy visualising the algorithm almost always hooked me and made me understand the algorihtm/s much better. In this research project my aim is to inspect the sorting algorithms, visualise them, see how they compare to one another and see improvements to the algorithms to make them more efficent. This research project was inspired by my masters at *Northeastern University* and the class that I have took at Northeasern EECE 7205 and in addition to my many calsses from my Bachelors degree at *Moscow Insitute of Physics and Tecnology* and *Brandeis Univeristy*.

## <ins>Algorithms Used<ins>

### <ins>Insertion Sort<ins>

![Insertion Sort demo](gifs/insertion_sort_animation.gif)

### <ins>Merge Sort<ins>

![>Merge Sort demo](gifs/merge_sort_animation.gif)

### <ins>Selection Sort<ins>

![Selection Sort demo](gifs/selection_sort_animation.gif)

### <ins>Bubble sort<ins>

![Bubble Sort demo](gifs/bubble_sort_animation.gif)

### <ins>Heap sort<ins>

![Heap Sort demo](gifs/heap_sort_animation.gif)

### <ins>Quick Sort (naive)<ins>

![Quick Sort (naive) demo](gifs/quick_sort_naive_animation.gif)

### <ins>Quick Sort (improvment 1)<ins>

![Quick Sort (improvment 1) demo](gifs/quick_sort_impr_1_animation.gif)

### <ins>Quick Sort (improvment 2)<ins>

![Quick Sort (improvment 2) demo](gifs/quick_sort_impr_2_animation.gif)

### <ins>Counting Sort<ins>

![Counting Sort demo](gifs/counting_sort_animation.gif)

### <ins>Radix Sort (naive)<ins>

![Radix Sort (naive) demo](gifs/radix_sort_improved_animation.gif)

### <ins>Radix Sort (improved)<ins>

![Radix Sort (improved demo](gifs/radix_sort_improved_animation.gif)

### <ins>Butcher Odd Even Merge Sort<ins>

![Butcher Odd Even Merge Sort demo](gifs/butcher_odd_even_merge_sort_animation.gif)

## <ins>Interesting Insight<ins>

It is very interesting how diffrent algorithms act with diffrent inputs. Eventhough, the diffrence between the sorting algorithms is always evidenet the diffrence becomes much clearer with larger inputs. An interesting fact that I have observed is that, similar execution algorithms typicaly have the same plot in the graph. This proves the correctness of their time complexity. Below we can see three exampels. The first example consists of unsorted arrays of the size of 5000 values. The second exmaple consists of unsorted arrays of 10000 values and the last example consists of unsorted arrays of 50000 values.

![small regular data soring](plots/plots_of_algo_comparisons/small%20regular.png)
![middle regular data soring](plots/plots_of_algo_comparisons/middle%20regular.png)
![large regular data soring](plots/plots_of_algo_comparisons/long%20regular.png)

The diffrence is very evident between the algorithms. Moreover, some tendencies are also shown. For one its evident that algorithms with similar time complexity cluster together on the graphs. However, even within these clustering there exists a hierarchy of better performing algorithms. Apart from that its interesting to see the diffrence in the algorithm perfromance with the inputs being sorted, regulary deistbuted and reverse sorted. The next example shows just that with array inputs of 5000 values.

![small sorted data soring](plots/plots_of_algo_comparisons/small%20sorted.png)
![small regular data soring](plots/plots_of_algo_comparisons/long%20regular.png)
![small reverse sorted data soring](plots/plots_of_algo_comparisons/small%20revrse%20sorted.png)






