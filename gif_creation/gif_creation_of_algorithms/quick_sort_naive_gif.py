import matplotlib.pyplot as plt
import numpy as np
import imageio
import os

global gif_path
gif_path = 'gifs/quick_sort_naive_animation.gif'

class SortingVisualizer:
    def __init__(self, data):
        self.__quick__naive_data = data[:]  

    def __partition_naive__(self, p, r, x, frame_dir, filenames, frame_count):
        pivot = self.__quick__naive_data[r]
        i = p - 1
        for j in range(p, r):
            if self.__quick__naive_data[j] <= pivot:
                i += 1
                self.__quick__naive_data[i], self.__quick__naive_data[j] = self.__quick__naive_data[j], self.__quick__naive_data[i]
                
                plt.bar(x, self.__quick__naive_data)
                filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
                plt.savefig(filename)
                filenames.append(filename)
                plt.clf()
                frame_count += 1

        self.__quick__naive_data[i + 1], self.__quick__naive_data[r] = self.__quick__naive_data[r], self.__quick__naive_data[i + 1]
        
        plt.bar(x, self.__quick__naive_data)
        filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
        plt.savefig(filename)
        filenames.append(filename)
        plt.clf()
        frame_count += 1

        return i + 1, frame_count

    def __quick_sort_naive__(self, p, r, x, frame_dir, filenames, frame_count):
        if p < r:
            q, frame_count = self.__partition_naive__(p, r, x, frame_dir, filenames, frame_count)
            frame_count = self.__quick_sort_naive__(p, q - 1, x, frame_dir, filenames, frame_count)
            frame_count = self.__quick_sort_naive__(q + 1, r, x, frame_dir, filenames, frame_count)
        return frame_count

    def quick_sort_naive_gif(self, gif_name=gif_path, duration=0.5):  
        x = np.arange(0, len(self.__quick__naive_data), 1)

        gif_dir = os.getcwd()

        frame_dir = os.path.join(gif_dir, 'frames')
        if not os.path.exists(frame_dir):
            os.makedirs(frame_dir)

        filenames = []
        frame_count = 0

        frame_count = self.__quick_sort_naive__(0, len(self.__quick__naive_data) - 1, x, frame_dir, filenames, frame_count)

        plt.bar(x, self.__quick__naive_data)
        filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
        plt.savefig(filename)
        filenames.append(filename)

        gif_path = os.path.join(gif_dir, gif_name)
        with imageio.get_writer(gif_path, mode='I', duration=duration) as writer:
            for filename in filenames:
                image = imageio.v2.imread(filename)
                writer.append_data(image)

        for filename in filenames:
            os.remove(filename)
        os.rmdir(frame_dir)

def run(lst):
    visualizer = SortingVisualizer(lst)
    visualizer.quick_sort_naive_gif(duration=0.5)  
