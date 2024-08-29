import matplotlib.pyplot as plt
import numpy as np
import imageio
import os

global gif_path
gif_path = 'gifs/butcher_odd_even_merge_sort_animation.gif'

class SortingVisualizer:
    def __init__(self, data):
        self.__butcher_odd_even_merge_data = data[:]  

    def __butcher_odd_even_merge_sort__(self, x, frame_dir, filenames, frame_count):
        n = len(self.__butcher_odd_even_merge_data)
        
        p = 1
        while p < n:
            k = p
            while k >= 1:
                for j in range(k % p, n - k, 2 * k):
                    for i in range(min(k, n - j - k)):
                        if (i + j) // (2 * p) == (i + j + k) // (2 * p):
                            if self.__butcher_odd_even_merge_data[i + j] > self.__butcher_odd_even_merge_data[i + j + k]:
                                self.__butcher_odd_even_merge_data[i + j], self.__butcher_odd_even_merge_data[i + j + k] = self.__butcher_odd_even_merge_data[i + j + k], self.__butcher_odd_even_merge_data[i + j]

                                plt.bar(x, self.__butcher_odd_even_merge_data)
                                filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
                                plt.savefig(filename)
                                filenames.append(filename)
                                plt.clf()
                                frame_count += 1
                k //= 2
            p *= 2

    def butcher_odd_even_merge_sort_gif(self, gif_name=gif_path, duration=0.5):  
        x = np.arange(0, len(self.__butcher_odd_even_merge_data), 1)

        gif_dir = os.getcwd()

        frame_dir = os.path.join(gif_dir, 'frames')
        if not os.path.exists(frame_dir):
            os.makedirs(frame_dir)

        filenames = []
        frame_count = 0

        self.__butcher_odd_even_merge_sort__(x, frame_dir, filenames, frame_count)

        plt.bar(x, self.__butcher_odd_even_merge_data)
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
    visualizer.butcher_odd_even_merge_sort_gif(duration=10)
