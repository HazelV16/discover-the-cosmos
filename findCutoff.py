# image_220405.jpg
import time
import numpy as np
import glob
from PIL import Image


def get_file():
    for file in glob.glob("*.jpg"):
        print(file)


def get_array(filename):
    img = Image.open(filename)
    array = np.array(img)
    return array


def find_best_cutoff(filename, starNo):
    img = Image.open(filename)
    array = np.array(img)

    rgb_star = 255

    # # get the cut-off number of stars
    count_list = []
    # rgb range from 0 to 255
    # reverse range is implemented to compare the execution time between 2 search strategies (linear search can perform on disordered array but binary search only perform on sorted ascending array)
    for z in reversed(range(0, rgb_star+1)):
        count = 0
        for i in array:
            for j in i:
                if j[0] > z and j[1] > z and j[2] > z:
                    count += 1

        count_list.append(count)

    starNo = min(count_list, key=lambda x: abs(x-starNo))

    def linear_search(list, starNo):
        index = list.index(starNo)
        return index

    def binary_search(list, starNo):
        first = 0
        last = len(list)-1
        index = -1
        while (first <= last) and (index == -1):
            mid = (first+last)//2
            if list[mid] == starNo:
                index = mid
            else:
                if starNo < list[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
        return index
    # https: // pynative.com/python-get-execution-time-of-program/
    # https: // stackoverflow.com/questions/12141150/from-list-of-integers-get-number-closest-to-a-given-value

    print("\n\n-----------Linear search strategy-----------\n")
    # get the start time
    st = time.time()
    print(
        f"The best cut-off value for {starNo} is: {rgb_star - linear_search(count_list, starNo)}")
    # get the end time
    et = time.time()

    # get the execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

    print("\n\n-----------Binary search strategy-----------\n")
    # get the start time
    st = time.time()
    print(
        f"The best cut-off value for {starNo} is: {rgb_star - binary_search(count_list, starNo)}")

    # get the end time
    et = time.time()

    # get the execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

    # 0.00012803077
    # 0.00009012222
    # 0.00004696846
