import pyautogui as pag
import os
import time
import convert_to_pdf as ctp
import glob

page_count = int(input("page count: "))

# page coordinates
x1 = 660
y1 = 0
x2 = 1900
y2 = 1600

# region
leftCord = x1
topCord = y1
width = x2 - x1
height = y2 - y1

image_files = []

time.sleep(5)

# take screenshots
page_delay = 3
for page in range(1, page_count + 1):
    im = pag.screenshot(region=(leftCord, topCord, width, height))
    file_name = f"page{page}.png"
    im.save(os.path.join("pages", file_name))
    image_files.append(file_name)
    pag.press("right")
    time.sleep(page_delay)

# convert images to pdf
ctp.convert_to_pdf(image_files)

# clear pages folder
files = glob.glob('pages/*')
for f in files:
    os.remove(f)