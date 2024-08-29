import matplotlib.pyplot as plt
import numpy as np
import imageio
import os

def butcher_odd_even_merge_sort_gif(lst, gif_path, duration=0.1):
    def butcher_odd_even_merge_sort(arr):
        nonlocal frame_count
        p = 1
        while p < len(arr):
            k = p
            while k >= 1:
                for j in range(k % p, len(arr) - 1 - k, 2 * k):
                    for i in range(0, min(k - 1, len(arr) - j - k - 1) + 1): 
                        if int((i + j) / (p * 2)) == int((i + j + k) / (p * 2)):
                            if arr[i + j] > arr[i + j + k]:
                                arr[i + j], arr[i + j + k] = arr[i + j + k], arr[i + j]

                                plt.bar(x, lst)
                                plt.ylim(0, max(lst) + 10)  
                                filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
                                plt.savefig(filename)
                                filenames.append(filename)
                                plt.clf()
                                frame_count += 1
                k = k // 2
            p = p * 2

    gif_dir = os.path.dirname(gif_path)
    if not os.path.exists(gif_dir):
        os.makedirs(gif_dir)

    frame_dir = os.path.join(gif_dir, 'frames')
    if not os.path.exists(frame_dir):
        os.makedirs(frame_dir)

    filenames = []
    frame_count = 0
    x = np.arange(0, len(lst), 1)

    butcher_odd_even_merge_sort(lst)

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


gif_path = 'gifs/butcher_odd_even_merge_sort_animation.gif'

def run(lst):
    butcher_odd_even_merge_sort_gif(lst, gif_path)
