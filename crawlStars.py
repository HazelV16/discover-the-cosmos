# 3.1.1
# import all libraries
import re
import urllib.request


def url_input(url):
    # url = "https://apod.nasa.gov/apod/archivepix.html"

    page = urllib.request.urlopen(url)

    for line in page:
        line = line.decode("utf-8", "ignore").strip()
        # find the img in required date range
        if re.findall('2023\s(?:May|June|July|August|September|October|November|December)\s(?:3[01]|[12][0-9]|0[1-9])|2024\s(?:January|February|March|April|May)\s(?:3[01]|[12][0-9]|0[1-9])', line) and re.search('Star Cluster', line):
            # find the .html link
            x = re.search('ap\d{6}.html', line)
            # find the date formate on the web
            z = re.search("\d{6}", line)
            if x:
                # get the individual image url with description
                image_url = f"https://apod.nasa.gov/apod/{x.group()}"
                page_1 = urllib.request.urlopen(image_url)
                for line_1 in page_1:
                    line_1 = line_1.decode().strip()
                    # get the image url with image only
                    if re.search(
                            '^<IMG[^<>]+SRC=["\']([^"\'<>]+\.(?:gif|png|jpe?g))["\']', line_1):
                        y = re.search(
                            'image([^"\'<>]+\.(?:gif|png|jpe?g))', line_1)
                        save_image_url = f'https://apod.nasa.gov/apod/{y.group()}'
                        urllib.request.urlretrieve(
                            save_image_url, f"image_{z.group()}.jpg")

# https://stackoverflow.com/questions/6076979/regular-expression-to-match-a-valid-day-in-a-date
