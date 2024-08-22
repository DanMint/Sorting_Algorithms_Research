import matplotlib.pyplot as plt
import numpy as np
import imageio
import os

def radix_improved_sort_gif(lst, gif_path, duration=0.1):
    def radix_sort_pos(arr):
        n = len(arr)
        max_val = max(arr)
        pos = 1

        while max_val // pos > 0:
            count_sort(arr, n, pos)
            pos *= 10

    def count_sort(arr, n, pos):
        nonlocal frame_count
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = (arr[i] // pos) % 10
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            index = (arr[i] // pos) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1

        for i in range(n):
            arr[i] = output[i]
            plt.bar(x, lst)
            plt.ylim(0, max(lst) + 10)  
            filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
            plt.savefig(filename)
            filenames.append(filename)
            plt.clf()
            frame_count += 1

    neg = [-x for x in lst if x < 0]
    pos = [x for x in lst if x >= 0]

    gif_dir = os.path.dirname(gif_path)
    if not os.path.exists(gif_dir):
        os.makedirs(gif_dir)

    frame_dir = os.path.join(gif_dir, 'frames')
    if not os.path.exists(frame_dir):
        os.makedirs(frame_dir)

    filenames = []
    frame_count = 0
    x = np.arange(0, len(lst), 1)

    if neg:
        radix_sort_pos(neg)

    if pos:
        radix_sort_pos(pos)

    sorted_lst = [-x for x in reversed(neg)] + pos

    for i in range(len(lst)):
        lst[i] = sorted_lst[i]

    plt.bar(x, lst)
    plt.ylim(0, max(lst) + 10)  
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


gif_path = 'Algorithm_Project/gifs/radix_sort_improved_animation.gif'

def run(lst):
    radix_improved_sort_gif(lst, gif_path)