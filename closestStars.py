# 3.1.3
# closestStars.py
from ast import Num
from PIL import Image
import numpy as np
import math
import glob


def get_file():
    for file in glob.glob("*.txt"):
        print(file)


def close_Star(pixel_r, pixel_c, fname):
    with open(fname, 'r') as p:
        lines = p.readlines()[1:]  # skipping first line
        coor_1 = np.array([pixel_r, pixel_c])
        list_distance = []
        for line in lines:
            data = line.rstrip()
            split_x_y = data.split(",")
            loc1 = [int(loc) for loc in coor_1]
            loc2 = [int(loc) for loc in split_x_y]
            euclidian_distance = math.sqrt(
                (loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)
            list_ed = [euclidian_distance]
            list_coor = [loc2]
            list_merge = list_ed + list_coor
            list_distance.append(list_merge)
            list_distance = sorted(list_distance)

        # print(list_distance[:2])

        for i in list_distance:
            print(
                f"The distances between {coor_1} and {i[1]}: {i[0]}")
