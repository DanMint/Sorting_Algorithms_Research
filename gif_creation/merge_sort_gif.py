import matplotlib.pyplot as plt
import numpy as np
import imageio
import os

def merge_sort_gif(lst, gif_path, duration=0.1):
    x = np.arange(0, len(lst), 1)

    gif_dir = os.path.dirname(gif_path)
    if not os.path.exists(gif_dir):
        os.makedirs(gif_dir)

    frame_dir = os.path.join(gif_dir, 'frames')
    if not os.path.exists(frame_dir):
        os.makedirs(frame_dir)

    filenames = []
    frame_count = 0

    def merge(p, q, r):
        nonlocal frame_count
        n1 = q - p + 1
        n2 = r - q

        L = lst[p:q + 1]
        R = lst[q + 1:r + 1]

        i = 0
        j = 0
        k = p

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1

            plt.bar(x, lst)
            filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
            plt.savefig(filename)
            filenames.append(filename)
            plt.clf()
            frame_count += 1

        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1

            plt.bar(x, lst)
            filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
            plt.savefig(filename)
            filenames.append(filename)
            plt.clf()
            frame_count += 1

        while j < len(R):
            lst[k] = R[j]
            j += 1
            k += 1

            plt.bar(x, lst)
            filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
            plt.savefig(filename)
            filenames.append(filename)
            plt.clf()
            frame_count += 1

    def merge_sort(p, r):
        if p < r:
            q = (p + r) // 2
            merge_sort(p, q)
            merge_sort(q + 1, r)
            merge(p, q, r)

    merge_sort(0, len(lst) - 1)

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


gif_path = 'Algorithm_Project/gifs/merge_sort_animation.gif'

def run(lst):
    merge_sort_gif(lst, gif_path)

