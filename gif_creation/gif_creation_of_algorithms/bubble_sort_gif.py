import matplotlib.pyplot as plt
import numpy as np
import imageio
import os

global gif_path
gif_path = 'gifs/bubble_sort_animation.gif'

class SortingVisualizer:
    def __init__(self, data):
        self.__bubble_data = data[:]  

    def __bubble_sort__(self, x, frame_dir, filenames, frame_count):
        n = len(self.__bubble_data)
        for i in range(n):
            for j in range(0, n - 1 - i):
                if self.__bubble_data[j] > self.__bubble_data[j + 1]:
                    self.__bubble_data[j], self.__bubble_data[j + 1] = self.__bubble_data[j + 1], self.__bubble_data[j]

                plt.bar(x, self.__bubble_data)
                filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
                plt.savefig(filename)
                filenames.append(filename)
                plt.clf()
                frame_count += 1

    def bubble_sort_gif(self, gif_name=gif_path, duration=0.5):  
        x = np.arange(0, len(self.__bubble_data), 1)

        gif_dir = os.getcwd()

        frame_dir = os.path.join(gif_dir, 'frames')
        if not os.path.exists(frame_dir):
            os.makedirs(frame_dir)

        filenames = []
        frame_count = 0

        self.__bubble_sort__(x, frame_dir, filenames, frame_count)

        plt.bar(x, self.__bubble_data)
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
    visualizer.bubble_sort_gif(duration=10)
