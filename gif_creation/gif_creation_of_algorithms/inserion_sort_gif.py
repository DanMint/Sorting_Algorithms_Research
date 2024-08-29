import matplotlib.pyplot as plt
import numpy as np
import imageio
import os

global gif_path
gif_path = 'gifs/insertion_sort_animation.gif'

class SortingVisualizer:
    def __init__(self, data):
        self.__insertion_data = data[:]  

    def __insertion_sort__(self, x, frame_dir, filenames, frame_count):
        for i in range(len(self.__insertion_data)):
            key = self.__insertion_data[i]
            j = i - 1

            while j > -1 and self.__insertion_data[j] > key:
                self.__insertion_data[j + 1] = self.__insertion_data[j]
                j -= 1

            self.__insertion_data[j + 1] = key

            plt.bar(x, self.__insertion_data)
            filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
            plt.savefig(filename)
            filenames.append(filename)
            plt.clf()
            frame_count += 1

    def insertion_sort_gif(self, gif_name=gif_path, duration=0.5):  
        x = np.arange(0, len(self.__insertion_data), 1)

        gif_dir = os.getcwd()

        frame_dir = os.path.join(gif_dir, 'frames')
        if not os.path.exists(frame_dir):
            os.makedirs(frame_dir)

        filenames = []
        frame_count = 0

        self.__insertion_sort__(x, frame_dir, filenames, frame_count)

        plt.bar(x, self.__insertion_data)
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
    visualizer.insertion_sort_gif(duration=10)
