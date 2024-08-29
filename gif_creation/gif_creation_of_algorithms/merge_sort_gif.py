import matplotlib.pyplot as plt
import numpy as np
import imageio
import os
import sys

global gif_path
gif_path = 'gifs/merge_sort_animation.gif'

class SortingVisualizer:
    def __init__(self, data):
        self.__merge_data = data[:]  

    def __merge_sort__(self, p, r, x, frame_dir, filenames, frame_count):
        if p >= r:
            return
        
        q = int((p + r) / 2)
        self.__merge_sort__(p, q, x, frame_dir, filenames, frame_count)
        self.__merge_sort__(q + 1, r, x, frame_dir, filenames, frame_count)
        self.__merge__(p, q, r, x, frame_dir, filenames, frame_count)

    def __merge__(self, p, q, r, x, frame_dir, filenames, frame_count):
        n1 = q - p + 1
        n2 = r - q
        L = []
        R = []
        for val in range(n1):
            L.append(self.__merge_data[p + val])

        for val in range(n2):
            R.append(self.__merge_data[q + 1 + val])
        
        L.append(sys.maxsize)
        R.append(sys.maxsize)

        i = 0
        j = 0

        for k in range(p, r + 1):
            if L[i] <= R[j]:
                self.__merge_data[k] = L[i]
                i += 1
            else:
                self.__merge_data[k] = R[j]
                j += 1

            plt.bar(x, self.__merge_data)
            filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
            plt.savefig(filename)
            filenames.append(filename)
            plt.clf()
            frame_count += 1

    def merge_sort_gif(self, gif_name=gif_path, duration=0.5):  
        x = np.arange(0, len(self.__merge_data), 1)

        gif_dir = os.getcwd()

        frame_dir = os.path.join(gif_dir, 'frames')
        if not os.path.exists(frame_dir):
            os.makedirs(frame_dir)

        filenames = []
        frame_count = 0

        self.__merge_sort__(0, len(self.__merge_data) - 1, x, frame_dir, filenames, frame_count)

        plt.bar(x, self.__merge_data)
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
    visualizer.merge_sort_gif(duration=10)
