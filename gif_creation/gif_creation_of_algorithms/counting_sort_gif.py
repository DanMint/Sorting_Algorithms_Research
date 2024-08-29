import matplotlib.pyplot as plt
import numpy as np
import imageio
import os

global gif_path
gif_path = 'gifs/counting_sort_animation.gif'

class SortingVisualizer:
    def __init__(self, data):
        self.__counting_data = data[:]  

    def __counting_sort__(self, k, x, frame_dir, filenames, frame_count):
        C = [0] * (k + 1)  

        for j in range(len(self.__counting_data)):
            C[self.__counting_data[j]] += 1

            plt.bar(x, self.__counting_data)
            filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
            plt.savefig(filename)
            filenames.append(filename)
            plt.clf()
            frame_count += 1

        for i in range(1, k + 1):
            C[i] += C[i - 1]

        B = [0] * len(self.__counting_data)
        for j in range(len(self.__counting_data) - 1, -1, -1):
            B[C[self.__counting_data[j]] - 1] = self.__counting_data[j]
            C[self.__counting_data[j]] -= 1

            plt.bar(x, B)
            filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
            plt.savefig(filename)
            filenames.append(filename)
            plt.clf()
            frame_count += 1

        self.__counting_data = B

    def counting_sort_gif(self, k, gif_name=gif_path, duration=0.5):  
        x = np.arange(0, len(self.__counting_data), 1)

        gif_dir = os.getcwd()

        frame_dir = os.path.join(gif_dir, 'frames')
        if not os.path.exists(frame_dir):
            os.makedirs(frame_dir)

        filenames = []
        frame_count = 0

        self.__counting_sort__(k, x, frame_dir, filenames, frame_count)

        plt.bar(x, self.__counting_data)
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
    k = max(lst) 
    visualizer = SortingVisualizer(lst)
    visualizer.counting_sort_gif(k, duration=10)
