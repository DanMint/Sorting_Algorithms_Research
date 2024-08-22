import matplotlib.pyplot as plt
import numpy as np
import imageio
import os

def counting_sort_gif(lst, gif_path, duration=0.5):
    max_value = max(lst)
    C = [0] * (max_value + 1)
    B = [0] * len(lst)  
    x = np.arange(0, len(lst), 1)

    gif_dir = os.path.dirname(gif_path)
    if not os.path.exists(gif_dir):
        os.makedirs(gif_dir)

    frame_dir = os.path.join(gif_dir, 'frames')
    if not os.path.exists(frame_dir):
        os.makedirs(frame_dir)

    filenames = []
    frame_count = 0

    for j in range(len(lst)):
        C[lst[j]] += 1

        plt.bar(x, lst)
        plt.ylim(0, max(lst) + 10)  
        filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
        plt.savefig(filename)
        filenames.append(filename)
        plt.clf()
        frame_count += 1

    for i in range(1, len(C)):
        C[i] += C[i - 1]

        plt.bar(x, lst, color='green')
        plt.ylim(0, max(lst) + 10)  
        filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
        plt.savefig(filename)
        filenames.append(filename)
        plt.clf()
        frame_count += 1

    for j in range(len(lst) - 1, -1, -1):
        B[C[lst[j]] - 1] = lst[j]
        C[lst[j]] -= 1

        plt.bar(x, B, color='orange')
        plt.ylim(0, max(lst) + 10)  
        filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
        plt.savefig(filename)
        filenames.append(filename)
        plt.clf()
        frame_count += 1

    for i in range(len(lst)):
        lst[i] = B[i]

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


gif_path = 'Algorithm_Project/gifs/counting_sort_animation.gif'

def run(lst): 
    counting_sort_gif(lst, gif_path)
