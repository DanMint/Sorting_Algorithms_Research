import matplotlib.pyplot as plt
import numpy as np
import imageio
import os

def selection_sort_gif(lst, gif_path, duration=0.1):
    x = np.arange(0, len(lst), 1)

    gif_dir = os.path.dirname(gif_path)
    if not os.path.exists(gif_dir):
        os.makedirs(gif_dir)

    frame_dir = os.path.join(gif_dir, 'frames')
    if not os.path.exists(frame_dir):
        os.makedirs(frame_dir)

    filenames = []
    frame_count = 0

    for i in range(len(lst)):
        lowest = i
        for j in range(i + 1, len(lst)):
            if lst[lowest] > lst[j]:
                lowest = j

        lst[i], lst[lowest] = lst[lowest], lst[i]

        plt.bar(x, lst)
        filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
        plt.savefig(filename)
        filenames.append(filename)
        plt.clf()
        frame_count += 1

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


gif_path = 'gifs/selection_sort_animation.gif'

def run(lst):
    selection_sort_gif(lst, gif_path)