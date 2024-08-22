import matplotlib.pyplot as plt
import numpy as np
import imageio
import os

def quick_sort_naive_gif(lst, gif_path, duration=0.1):
    x = np.arange(0, len(lst), 1)

    gif_dir = os.path.dirname(gif_path)
    if not os.path.exists(gif_dir):
        os.makedirs(gif_dir)

    frame_dir = os.path.join(gif_dir, 'frames')
    if not os.path.exists(frame_dir):
        os.makedirs(frame_dir)

    filenames = []
    frame_count = 0

    def partition_naive(p, r):
        nonlocal frame_count
        x = lst[r]
        i = p - 1
        for j in range(p, r):
            if lst[j] <= x:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
                
                plt.bar(x, lst)
                filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
                plt.savefig(filename)
                filenames.append(filename)
                plt.clf()
                frame_count += 1

        lst[i + 1], lst[r] = lst[r], lst[i + 1]
        
        plt.bar(x, lst)
        filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
        plt.savefig(filename)
        filenames.append(filename)
        plt.clf()
        frame_count += 1

        return i + 1

    def quick_sort_naive(p, r):
        if p < r:
            q = partition_naive(p, r)
            quick_sort_naive(p, q - 1)
            quick_sort_naive(q + 1, r)

    quick_sort_naive(0, len(lst) - 1)

    plt.bar(x, lst)
    filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
    plt.savefig(filename)
    filenames.append(filename)

    with imageio.get_writer(gif_path, mode='I', duration=duration) as writer:
        for filename in filenames:
            image = imageio.v2.imread(filename)
            writer.append_data(image)

    for filename in filenames:
        os.remove(filename)
    os.rmdir(frame_dir)


gif_path = 'Algorithm_Project/gifs/quick_sort_naive_animation.gif'

def run(lst):
    quick_sort_naive_gif(lst, gif_path)