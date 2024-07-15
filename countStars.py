# 3.1.2
import numpy as np
from PIL import Image
import re
import glob


def star_count(num):
    # count = 0
    # get all of the file with jpg extension
    for i in glob.glob("*.jpg"):
        # search for the date format
        x = re.search('\d{6}', i)
        img = Image.open(i)
        array = np.array(img)
        count = 0
        with open(f'image_{x.group()}_star_{num}.txt', 'a') as f:
            for i in array:
                for j in i:
                    if j[0] > num:
                        if j[1] > num:
                            if j[2] > num:
                                # count the total number of star for given cutoff value
                                count += 1
                                # find the star position
                                index_pos = np.where((array[:, :, 0] == j[0]) & (
                                    array[:, :, 1] == j[1]) & (array[:, :, 2] == j[2]))
                                asString = np.vectorize(str)
                                arr = asString(index_pos)
                                arr_1 = arr.T
                                np.savetxt(f, arr_1, fmt='%s', delimiter=',')
        f.close()

        # get rid of duplicated line in text file
        lines_seen = set()  # holds lines already seen

        with open(f"image_{x.group()}_star_{num}.txt", "r+") as f:
            d = f.readlines()
            f.seek(0)
            # print the total star count in the first line
            f.write(f"{count}\n")
            for i in d:
                if i not in lines_seen:
                    f.write(i)
                    lines_seen.add(i)
            f.truncate()
        f.close()
