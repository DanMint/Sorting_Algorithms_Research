import matplotlib.pyplot as plt
import numpy as np
import imageio
import os

global gif_path
gif_path = 'gifs/radix_sort_improved_animation.gif'

class SortingVisualizer:
    def __init__(self, data):
        self.__radix_impr_data = data[:]  

    def __radix_improved_sort__(self, x, frame_dir, filenames, frame_count):
        neg = [-x for x in self.__radix_impr_data if x < 0] 
        pos = [x for x in self.__radix_impr_data if x >= 0]

        if neg:
            self.__radix_sort_pos__(neg, x, frame_dir, filenames, frame_count)
        if pos:
            self.__radix_sort_pos__(pos, x, frame_dir, filenames, frame_count)

        self.__radix_impr_data[:] = [-x for x in reversed(neg)] + pos

        plt.bar(x, self.__radix_impr_data)
        filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
        plt.savefig(filename)
        filenames.append(filename)
        plt.clf()
        frame_count += 1

    def __radix_sort_pos__(self, arr, x, frame_dir, filenames, frame_count):
        n = len(arr)
        max_val = max(arr)

        pos = 1
        while max_val // pos > 0:
            self.__count_sort_impr__(arr, n, pos)
            pos *= 10

            plt.bar(x, self.__radix_impr_data)
            filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
            plt.savefig(filename)
            filenames.append(filename)
            plt.clf()
            frame_count += 1

    def __count_sort_impr__(self, arr, n, pos):
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            count[(arr[i] // pos) % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            output[count[(arr[i] // pos) % 10] - 1] = arr[i]
            count[(arr[i] // pos) % 10] -= 1

        for i in range(n):
            arr[i] = output[i]

    def radix_sort_improved_gif(self, gif_name=gif_path, duration=0.5):  
        x = np.arange(0, len(self.__radix_impr_data), 1)

        gif_dir = os.getcwd()

        frame_dir = os.path.join(gif_dir, 'frames')
        if not os.path.exists(frame_dir):
            os.makedirs(frame_dir)

        filenames = []
        frame_count = 0

        self.__radix_improved_sort__(x, frame_dir, filenames, frame_count)

        plt.bar(x, self.__radix_impr_data)
        filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
        plt.savefig(filename)
        filenames.append(filename)

        gif_path = os.path.join(gif_dir, gif_name)
        with imageio.get_writer(gif_path, mode='I', duration=duration) as writer:
            for filename in filenames:
                if os.path.exists(filename):
                    image = imageio.v2.imread(filename)
                    writer.append_data(image)

        for filename in filenames:
            if os.path.exists(filename):
                os.remove(filename)
        if os.path.exists(frame_dir):
            os.rmdir(frame_dir)

def run(lst):
    visualizer = SortingVisualizer(lst)
    visualizer.radix_sort_improved_gif(duration=10)
