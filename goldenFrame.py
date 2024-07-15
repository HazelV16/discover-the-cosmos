# 3.1.4
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import re
from matplotlib.ticker import (MultipleLocator)
import os


def frame(filename, num, f=10):
    img = Image.open(filename)
    x = re.search('\d{6}', filename)
    array = np.array(img)
    count = 0
    with open(f'image_{x.group()}_stars_{num}.txt', 'a') as a:
        for i in array:
            for j in i:
                if j[0] > num:
                    if j[1] > num:
                        if j[2] > num:
                            count += 1
                            index_pos = np.where((array[:, :, 0] == j[0]) & (
                                array[:, :, 1] == j[1]) & (array[:, :, 2] == j[2]))
                            asString = np.vectorize(str)
                            arr = asString(index_pos)
                            arr_1 = arr.T
                            # print(arr_1)
                            np.savetxt(a, arr_1, fmt='%s', delimiter=',')
    a.close()

    # get rid of duplicated line in text file
    lines_seen = set()  # holds lines already seen

    with open(f"image_{x.group()}_stars_{num}.txt", "r+") as a:
        d = a.readlines()
        a.seek(0)
        # print the total star count in the first line
        a.write(f"{count}\n")
        for i in d:
            if i not in lines_seen:
                a.write(i)
                lines_seen.add(i)
        a.truncate()
    a.close()
    Y, X = np.loadtxt(f"image_{x.group()}_stars_{num}.txt",
                      delimiter=",", skiprows=1, unpack=True)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, array.shape[1])
    ax.set_ylim(0, array.shape[0])
    ax.xaxis.set_major_locator(MultipleLocator(f))
    ax.yaxis.set_major_locator(MultipleLocator(f))
    plt.scatter(X, Y, color="blue")
    plt.gca().invert_yaxis()
    ax.grid(which='major', color='#CCCCCC', linestyle='--')
    plt.tight_layout()
    os.remove(f"image_{x.group()}_stars_{num}.txt")
    plt.show()


# frame("image_200122.jpg", 210, 100)
