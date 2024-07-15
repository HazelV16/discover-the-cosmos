import crawlStars
import countStars
import closestStars
import findCutoff
import goldenFrame

def main():
    # # 3.1.1: crawling the images as detailed in the specification
    print("~~~~~~~~~Task 3.1.1~~~~~~~~~\n")
    url = "https://apod.nasa.gov/apod/archivepix.html"
    crawlStars.url_input(url)

    # # 3.1.2: reading the image files, counting and storing the number
    # #       of "stars" in them as detailed in the specification
    print("\n\n~~~~~~~~~Task 3.1.2~~~~~~~~~\n")
    cutoff = int(input(
        "Insert an integer between 0 and 255 to distingush the stars: "))
    pass
    countStars.star_count(cutoff)

    # # 3.1.3: printing the k closest stars to a given pixel
    print("\n\n~~~~~~~~~Task 3.1.3~~~~~~~~~\n")
    print("---------List of available given cut-off value image file ---------")
    closestStars.get_file()
    fName = input(
        "Enter the name of the image file: ")
    pixel_r = int(input(
        "Enter the row number of your pixel: "))
    pixel_c = int(input(
        "Enter the column number of your pixel: "))
    closestStars.close_Star(pixel_r, pixel_c, fName)

    # 3.1.4: visualising the golden frame in an image
    print("\n\n~~~~~~~~~Task 3.1.4~~~~~~~~~\n")
    print("---------List of available image file---------")
    findCutoff.get_file()
    fName = input("Enter the name of the image file: ")
    f = input(
        "Enter the number of frames (press enter if you have no specific number in mind): ")
    newC = input("Do you want to choose a new cut-off value? (y or n)")
    if newC == "y":
        cutoff = int(input(
            "Insert an integer between 0 and 255 to distingush the stars: "))

    goldenFrame.frame(fName, cutoff, 100)
    # # 3.1.5: printing the best cut-off value for a given number of stars
    # print("\n\n~~~~~~~~~Task 3.1.5~~~~~~~~~\n")
    # print("---------List of available image file---------")
    # findCutoff.get_file()
    # fName = input("Enter the name of the image file: ")
    # while True:
    #     starNo = int(input("Enter the number of stars: "))
    #     if starNo < 0:
    #         print("An image cannot have negative number of stars")
    #         continue
    #     if starNo > findCutoff.get_array(fName).shape[0]*findCutoff.get_array(fName).shape[1]:
    #         print("An image cannot have more than row x column pixels")
    #         continue
    #     else:
    #         break
    # findCutoff.find_best_cutoff(fName, starNo)


if __name__ == "__main__":
    main()
