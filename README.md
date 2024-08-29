# Sorting Algorithms Research

## <ins>Inspiration<ins>
In this repository I wanted to conduct reserach into sorting algorithms and thier respective time complexities. Namely, I wanted to see and test if thier given time complexities are true and why do these time complexities matter (We always learn the theory side and the break down of time complexities however I wanted to see it for my self). This research project was inspired by my masters class at Northeastern EECE 7205 and many years of algorithms practice.

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

![Heap Sort demo]()

### <ins>Quick Sort (naive)<ins>

![Quick Sort (naive) demo]()

### <ins>Quick Sort (improvment 1)<ins>

![Quick Sort (improvment 1) demo]()

### <ins>Quick Sort (improvment 2)<ins>

![Quick Sort (improvment 2) demo]()

### <ins>Counting Sort<ins>

![Counting Sort demo](gifs/counting_sort_animation.gif)

### <ins>Radix Sort (naive)<ins>

![Radix Sort (naive) demo](gifs/radix_sort_improved_animation.gif)

### <ins>Radix Sort (improved)<ins>

![Radix Sort (improved demo](gifs/radix_sort_improved_animation.gif)

### <ins>Butcher Odd Even Merge Sort<ins>

![Butcher Odd Even Merge Sort demo](gifs/butcher_odd_even_merge_sort_animation.gif)

## <ins>Interesting Insight<ins>

It is very interesting how diffrent algorithms act with diffrent inputs. Eventhough, the diffrence between the sorting algorithms is always evidenet the diffrence becomes much clearer with larger inputs. An interesting fact that I have observed is that, similar execution algorithms typicaly have the same plot in the graph. This proves the correctness of thier time complexity. Below I have listed two exampels:

![Small Regular Data Sorting](plots/plots_of_algo_comparisons/small%20regular.png)

In this exmaple its fairly clear that sorting algorithms like: *Radix Sort*, *Quick Sort(improved 2)*, *Merge Sort*, *Heap sort* and *Butcher odd even merge sort* execute quicker then the other algorithms. Its also evident that these algorithms clump together on the plot. Eventhough, this graph shows that the *Butcher odd even merge sort* performs the worst of of the five best ones its less evident when we look on a larger input.

![Large Regular Data Sorting](plots/plots_of_algo_comparisons/long%20regular.png)




