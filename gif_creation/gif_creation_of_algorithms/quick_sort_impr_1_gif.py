import matplotlib.pyplot as plt
import numpy as np
import imageio
import os

global gif_path
gif_path = 'gifs/quick_sort_impr_1_animation.gif'

class SortingVisualizer:
    def __init__(self, data):
        self.__quick_impr_1_data = data[:]  

    def __partion_improved_1__(self, p, r, x, frame_dir, filenames, frame_count):
        pivot = self.__quick_impr_1_data[r]  
        left = p
        right = r - 1
        while True:
            while left <= right and self.__quick_impr_1_data[left] < pivot:
                left += 1
            while right >= left and self.__quick_impr_1_data[right] > pivot:
                right -= 1
            if left >= right:
                break
            else:
                self.__quick_impr_1_data[left], self.__quick_impr_1_data[right] = self.__quick_impr_1_data[right], self.__quick_impr_1_data[left]
                
                plt.bar(x, self.__quick_impr_1_data)
                filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
                plt.savefig(filename)
                filenames.append(filename)
                plt.clf()
                frame_count += 1

                left += 1
                right -= 1
        
        self.__quick_impr_1_data[left], self.__quick_impr_1_data[r] = self.__quick_impr_1_data[r], self.__quick_impr_1_data[left]

        plt.bar(x, self.__quick_impr_1_data)
        filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
        plt.savefig(filename)
        filenames.append(filename)
        plt.clf()
        frame_count += 1

        return left, frame_count

    def __quick_sort_improved_1__(self, p, r, x, frame_dir, filenames, frame_count):
        if p < r:
            q, frame_count = self.__partion_improved_1__(p, r, x, frame_dir, filenames, frame_count)
            frame_count = self.__quick_sort_improved_1__(p, q - 1, x, frame_dir, filenames, frame_count)
            frame_count = self.__quick_sort_improved_1__(q + 1, r, x, frame_dir, filenames, frame_count)
        return frame_count

    def quick_sort_improved_1_gif(self, gif_name=gif_path, duration=0.5):  
        x = np.arange(0, len(self.__quick_impr_1_data), 1)

        gif_dir = os.getcwd()

        frame_dir = os.path.join(gif_dir, 'frames')
        if not os.path.exists(frame_dir):
            os.makedirs(frame_dir)

        filenames = []
        frame_count = 0

        frame_count = self.__quick_sort_improved_1__(0, len(self.__quick_impr_1_data) - 1, x, frame_dir, filenames, frame_count)

        plt.bar(x, self.__quick_impr_1_data)
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
    visualizer.quick_sort_improved_1_gif(duration=0.5)  
