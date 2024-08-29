import matplotlib.pyplot as plt
import numpy as np
import imageio
import os

class SortingVisualizer:
    def __init__(self, data):
        self.__heap_data = data[:]  # Copy of the data for heap sort

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def __max_heapify__(self, i, heap_size, x, frame_dir, filenames, frame_count):
        l = self.left(i)
        r = self.right(i)
        largest = i

        if l < heap_size and self.__heap_data[l] > self.__heap_data[i]:
            largest = l
        if r < heap_size and self.__heap_data[r] > self.__heap_data[largest]:
            largest = r
        if largest != i:
            self.__heap_data[i], self.__heap_data[largest] = self.__heap_data[largest], self.__heap_data[i]
            
            # Capture frame for GIF
            plt.bar(x, self.__heap_data)
            filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
            plt.savefig(filename)
            filenames.append(filename)
            plt.clf()
            frame_count += 1

            self.__max_heapify__(largest, heap_size, x, frame_dir, filenames, frame_count)

    def __build_max_heap__(self, x, frame_dir, filenames, frame_count):
        heap_size = len(self.__heap_data)
        for i in range(len(self.__heap_data) // 2 - 1, -1, -1):
            self.__max_heapify__(i, heap_size, x, frame_dir, filenames, frame_count)

    def __heapsort__(self, x, frame_dir, filenames, frame_count):
        self.__build_max_heap__(x, frame_dir, filenames, frame_count)
        heap_size = len(self.__heap_data)
        for i in range(len(self.__heap_data) - 1, 0, -1):
            self.__heap_data[0], self.__heap_data[i] = self.__heap_data[i], self.__heap_data[0]
            heap_size -= 1
            
            # Capture frame for GIF
            plt.bar(x, self.__heap_data)
            filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
            plt.savefig(filename)
            filenames.append(filename)
            plt.clf()
            frame_count += 1

            self.__max_heapify__(0, heap_size, x, frame_dir, filenames, frame_count)

        return frame_count

    def heap_sort_gif(self, gif_name="heap_sort_animation.gif", duration=0.5):  # Control the speed with duration
        x = np.arange(0, len(self.__heap_data), 1)

        # Set the current directory
        gif_dir = os.getcwd()

        frame_dir = os.path.join(gif_dir, 'frames')
        if not os.path.exists(frame_dir):
            os.makedirs(frame_dir)

        filenames = []
        frame_count = 0

        # Run the heap sort algorithm and capture frames
        frame_count = self.__heapsort__(x, frame_dir, filenames, frame_count)

        # Final frame after sorting is complete
        plt.bar(x, self.__heap_data)
        filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
        plt.savefig(filename)
        filenames.append(filename)

        # Save the GIF in the current directory
        gif_path = os.path.join(gif_dir, gif_name)
        with imageio.get_writer(gif_path, mode='I', duration=duration) as writer:
            for filename in filenames:
                image = imageio.v2.imread(filename)
                writer.append_data(image)

        # Clean up frames
        for filename in filenames:
            os.remove(filename)
        os.rmdir(frame_dir)

        print(f"GIF saved as {gif_path}")

# Example usage

def run(lst):
    visualizer = SortingVisualizer(lst)
    visualizer.heap_sort_gif(duration=0.5)  # Increase duration to make it slower

# Example data
lst = [10, 7, 8, 9, 1, 5]
run(lst)
